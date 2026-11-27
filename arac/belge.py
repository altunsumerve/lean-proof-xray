#!/usr/bin/env python3
"""Belge / Document — büyük bir Lean projesinin kısa, düz cümleli çıktısı.

TR: Girdi: baskınlık ağacı (taslar_ust.tsv), bölüm tablosu, sayılar ve terim dökümü. Çıktı: bir–iki sayfalık belge:
    (1) kanıtlanan cümle, (2) ispatın omurgası, (3) adı geçen ara önermeler, (4) sayılar, (5) denetim.
    Bütün cümleler `duz.py` kalıplarıyla, bütün sayılar kayıttan sayılarak üretilir. Yapay zekâ kullanılmaz;
    aynı girdi bayt bayt aynı belgeyi verir.
EN: Short plain-sentence document for a large Lean project. Rule-based and deterministic.

Kullanım / usage:
  belge.py --kok durum --dok durum/taslar/dok_ornek.jsonl.gz --dil tr --adim 6 --cikti durum/makale/CIKTI.md
"""
import argparse
import collections
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import alanlar  # noqa: E402
import duz  # noqa: E402
import sozel  # noqa: E402

M = {
    "tr": {
        "baslik": "Kodun çıktısı: {kok}",
        "kunye": "*Bu belge bir yapay zekâ tarafından yazılmadı. Resmi Lean kaydından, sabit kurallarla üretildi "
                 "(`arac/belge.py`). Aynı kayıtla çalıştıran herkes harfi harfine aynı belgeyi elde eder. "
                 "Köşeli parantez içindeki adlar koddaki adlardır.*",
        "b1": "## 1. Kanıtlanan cümle",
        "ad_verir": "Kodun kanıtladığı teorem `{t}`{yer}. Önermesi tek bir addan ibaret: `{c}`. Bu adın kütüphanedeki tanımı açıldığında cümle şudur:",
        "dogrudan": "Kodun kanıtladığı teorem `{t}`{yer}. Önermesi:",
        "yalniz_ktp": "Bu cümle yalnızca standart kütüphanedeki (Mathlib) {n} kavramla yazılmıştır; projeye özgü hiçbir tanım içermez. "
                      "Yani neyin kanıtlandığını anlamak için proje kodunun hiçbir satırını okumak gerekmez.",
        "proje_var": "Bu cümle projeye özgü {p} tanıma ve kütüphaneden {n} kavrama dayanır.",
        "b2": "## 2. İspatın omurgası",
        "omurga": "İspatın tamamı {n} bildirimdir. Aşağıdaki adımlar bunların içinden kurallı olarak seçildi: her seferinde, altında en çok ispat "
                  "bulunan adım açıldı. Yüzde, ispatın ne kadarının yalnızca o adım için var olduğunu gösterir.",
        "adim": "**Adım {i} — ispatın {y}** [`{ad}`{yer}]",
        "sarmal": "Buraya {k} ara ad üzerinden gelinir; bunlar aynı sonucu yeniden adlandırır: {z}.",
        "sarmal2": "Buraya şu adlar üzerinden gelinir; her birinin ispatının en az %97'si bir sonrakinin altındadır: {z}.",
        "kesik": "[Not: bu önermenin \"…\" ile gösterilen kısımları dökümün boyut sınırı yüzünden kesilmiştir; cümle eksiktir.]",
        "tek": "Önermesi tek bir addan ibaret: **{c}**. Tanımı açıldığında:",
        "yok": "(Bu adımın önermesi bu dökümde yok.)",
        "cok_uzun": "Bu adımın önermesi kısa bir cümleye sığmıyor ({n} karakter); tam hali uzun çıktıdadır.",
        "tablo_bas": "| Adım | Önerme | İspattaki payı | Yoğun kullandığı alanlar |",
        "uzun_kisa": "(uzun; aşağıda)",
        "birlesim2": "İspatı doğrudan şu {n} sonucu birleştirir (parantezde: ispatın o sonucun altındaki payı):",
        "alan": " — yoğun kullandığı alanlar: {z}",
        "alan_not": "\"Yoğun kullandığı alanlar\": o parçanın altında standart kütüphanenin hangi matematik alanı, proje ortalamasına göre kaç kat sık kullanılıyor (sabit tablo: `arac/alanlar.py`).",
        "parca": "Dayandığı parçalar:",
        "parca1": "- {y}: [`{ad}`]{ek}",
        "acildi": " → Adım {i}",
        "kucuk": "- {y}: {n} küçük yardımcı sonuç",
        "b3": "## 3. Adı geçen ara önermeler",
        "ara": "Yukarıdaki cümlelerde tek kelimeyle geçen önermeler projenin kendi tanımlarıdır. Kısa olanların tanımı aynı kurallarla aşağıdadır.",
        "uzun": "- **{k}** [`{ad}`]: tanımı kısa bir cümleye sığmıyor ({n} karakter). Tam hali uzun çıktıdadır.",
        "kisa": "- **{k}** [`{ad}`]: {c}",
        "bildirim": "- **{k}** [`{ad}`]: birkaç koşulun bir arada tutulduğu bir pakettir (Lean yapısı).",
        "b4": "## 4. Sayılar",
        "s": [("Projenin bildirimi", "proje"), ("Bunlardan teorem", "teorem"), ("Ana teoremin kullandığı", "koni"),
              ("Ana teoremin hiç kullanmadığı", "kullanilmayan"), ("Önermesi başka bir teoreminkiyle birebir aynı olan fazladan teorem", "kopya"),
              ("Kaynak dosyalarda olup ispata hiç girmeyen (yaklaşık)", "kaynak")],
        "b5": "## 5. Bu belge nasıl denetlenir",
        "denetim": "1. Kayıt: Lean'in resmi dışa aktarımı (`solution.ndjson.zst`), Lean çekirdeği tarafından doğrulanmış haliyle.\n"
                   "2. Omurga: kayıttaki bağımlılıklardan hesaplanan baskınlık ağacı. \"Yalnızca o adım için var\" ifadesi tanım gereği kesindir.\n"
                   "3. Cümleler: önermenin mantık iskeleti sabit kalıplarla yazılır (her, vardır, eğer–ise, ve, veya, değil); formüller kayıttaki terimden aynen basılır.\n"
                   "4. Yorum yok: belgede kayıtta bulunmayan hiçbir açıklama, niyet ya da değerlendirme yer almaz.",
    },
    "en": {
        "baslik": "What the code proves: {kok}",
        "kunye": "*This document was not written by an AI. It was produced from the official Lean export by fixed rules "
                 "(`arac/belge.py`). Anyone running the same export obtains the same document, character for character. "
                 "Names in brackets are the names used in the code.*",
        "b1": "## 1. The statement proved",
        "ad_verir": "The theorem proved by the code is `{t}`{yer}. Its statement is a single name: `{c}`. Unfolding the library definition of that name gives:",
        "dogrudan": "The theorem proved by the code is `{t}`{yer}. Its statement:",
        "yalniz_ktp": "This sentence is written only with {n} concepts of the standard library (Mathlib); it contains no project-specific definition. "
                      "So understanding what is proved requires reading none of the project's code.",
        "proje_var": "This sentence depends on {p} project-specific definitions and {n} library concepts.",
        "b2": "## 2. The spine of the proof",
        "omurga": "The whole proof consists of {n} declarations. The steps below were selected from them by rule: each time, the step with the most proof "
                  "beneath it was opened. The percentage is the share of the proof that exists only for that step.",
        "adim": "**Step {i} — {y} of the proof** [`{ad}`{yer}]",
        "sarmal": "It is reached through {k} intermediate names that restate the same result: {z}.",
        "sarmal2": "It is reached through these names; at least 97% of the proof of each lies under the next: {z}.",
        "kesik": "[Note: the parts shown as \"…\" were cut by the dump's size limit; the sentence is incomplete.]",
        "tek": "Its statement is a single name: **{c}**. Unfolding the definition:",
        "yok": "(The statement of this step is not in this dump.)",
        "cok_uzun": "The statement of this step does not fit in a short sentence ({n} characters); the full form is in the long output.",
        "tablo_bas": "| Step | Statement | Share of the proof | Fields used most densely |",
        "uzun_kisa": "(long; see below)",
        "birlesim2": "Its proof directly combines these {n} results (in parentheses: share of the proof under that result):",
        "alan": " — fields used most densely: {z}",
        "alan_not": "\"Fields used most densely\": which mathematical areas of the standard library are used under that part, and how many times more often than the project average (fixed table: `arac/alanlar.py`).",
        "parca": "It rests on:",
        "parca1": "- {y}: [`{ad}`]{ek}",
        "acildi": " → Step {i}",
        "kucuk": "- {y}: {n} small auxiliary results",
        "b3": "## 3. Intermediate statements named above",
        "ara": "Statements that appear above as a single word are the project's own definitions. The short ones are given below by the same rules.",
        "uzun": "- **{k}** [`{ad}`]: its definition does not fit in a short sentence ({n} characters). The full form is in the long output.",
        "kisa": "- **{k}** [`{ad}`]: {c}",
        "bildirim": "- **{k}** [`{ad}`]: a bundle of several conditions (a Lean structure).",
        "b4": "## 4. Numbers",
        "s": [("Declarations in the project", "proje"), ("of which theorems", "teorem"), ("Used by the main theorem", "koni"),
              ("Never used by the main theorem", "kullanilmayan"), ("Redundant theorems whose statement is identical to another theorem's", "kopya"),
              ("In the source files but never entering the proof (approximate)", "kaynak")],
        "b5": "## 5. How to check this document",
        "denetim": "1. Record: Lean's official export (`solution.ndjson.zst`), as verified by the Lean kernel.\n"
                   "2. Spine: the dominator tree computed from the dependencies in the record. \"Exists only for that step\" is exact by definition.\n"
                   "3. Sentences: the logical skeleton of each statement is written with fixed templates (for every, exists, if–then, and, or, not); formulas are printed from the recorded term unchanged.\n"
                   "4. No interpretation: the document contains no explanation, intent or judgement that is not in the record.",
    },
}


def b(n, dil):
    return f"{int(n):,}".replace(",", "." if dil == "tr" else ",")


def yz(a, t, dil):
    if 0 < 100 * a / t < 0.05:
        return "<%0,1" if dil == "tr" else "<0.1%"
    s = f"{100 * a / t:.1f}"
    return f"%{s.replace('.', ',')}" if dil == "tr" else f"{s}%"


def tablo(yol):
    bas, L = None, []
    for l in open(yol, encoding="utf-8"):
        p = l.rstrip("\n").split("\t")
        if bas is None:
            bas = p
            continue
        L.append(dict(zip(bas, p + [""] * (len(bas) - len(p)))))
    return L


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--kok", default="durum")
    a.add_argument("--dok", required=True)
    a.add_argument("--dil", default="tr")
    a.add_argument("--adim", type=int, default=6)
    a.add_argument("--esik", type=float, default=2.0)
    a.add_argument("--kisa", type=int, default=260, help="ara önermenin tanımı en çok bu kadar karakterse yazılır")
    a.add_argument("--uzun", type=int, default=400, help="adım önermesi bundan uzunsa kısa belgede yazılmaz")
    a.add_argument("--cikti", required=True)
    A = a.parse_args()
    K, dil, S = A.kok, A.dil, M[A.dil]
    KN = f"{K}/koni" if os.path.exists(f"{K}/koni/ozet.json") else K   # düz klasör düzeni de kabul edilir
    O = json.load(open(f"{KN}/ozet.json", encoding="utf-8"))
    Q = json.load(open(f"{K}/olcum/olcum.json", encoding="utf-8")) if os.path.exists(f"{K}/olcum/olcum.json") else {}
    T = {}
    for d in tablo(f"{KN}/taslar_ust.tsv"):
        for k in ("derinlik", "alt_sayi", "alt_agirlik", "agirlik", "kullanan", "cocuk"):
            d[k] = int(d[k])
        T[d["ad"]] = d
    yer = {}
    if os.path.exists(f"{K}/olcum/bolumler.tsv"):
        for d in tablo(f"{K}/olcum/bolumler.tsv"):
            if d["dosya"]:
                yer[d["ad"]] = f"{d['dosya']}:{d['satir']}"
    AR, AT, DG = {}, {}, collections.defaultdict(list)
    if os.path.exists(f"{K}/alan/adalani.tsv.gz"):
        AR, AT = alanlar.yukle(f"{K}/alan/adalani.tsv.gz")
    if os.path.exists(f"{K}/alan/dogrudan.tsv"):
        for l in open(f"{K}/alan/dogrudan.tsv", encoding="utf-8"):
            h_, td, dep, tur_ = l.rstrip("\n").split("\t")
            if td == "d" and tur_ == "t" and "._proof_" not in dep and dep not in DG[h_]:
                DG[h_].append(dep)

    def alan_sozu(n):
        L = alanlar.yogunluk(AR, AT, n, dil)[:3] if AT else []
        if not L:
            return ""
        return S["alan"].format(z=", ".join(f"{a} ({('%.0f' % y)}×)" for a, y, _ in L))

    D, bag = sozel.yukle(A.dok)
    KT = sozel.katlama_tablosu(D)
    C = duz.Duz(bag, dil, katla=KT)
    cocuk = collections.defaultdict(list)
    for d in T.values():
        cocuk[d["baskin"]].append(d)
    for k in cocuk:
        cocuk[k].sort(key=lambda d: (-d["alt_agirlik"], d["ad"]))
    kokler = cocuk["<kok>"]
    topA = sum(d["alt_agirlik"] for d in kokler) or 1

    def zincir(d):
        z = [d]
        while True:
            c = cocuk.get(z[-1]["ad"], [])
            if c and c[0]["alt_agirlik"] * 100 >= 97 * z[-1]["alt_agirlik"]:
                z.append(c[0])
            else:
                return z

    acik, kuyruk = [], list(kokler)
    while kuyruk and len(acik) < A.adim:
        kuyruk.sort(key=lambda d: (-d["alt_agirlik"], d["ad"]))
        d = kuyruk.pop(0)
        z = zincir(d)
        cs = [c for c in cocuk.get(z[-1]["ad"], []) if c["alt_agirlik"] * 100 >= A.esik * topA]
        acik.append((z, cs))
        kuyruk.extend(cs)
    sira = {z[0]["ad"]: i for i, (z, _) in enumerate(acik, 1)}
    ara = collections.OrderedDict()   # kısa ad -> tam ad

    def cumle(n, ac_tek=False, say=True):
        """Bildirimin önermesi düz cümle olarak; ac_tek: önerme tek sabitse tanımını aç."""
        d = D.get(n)
        if not d:
            return None, None
        e = d["tip"] if d["tur"] == "teorem" else d.get("govde")
        tek = duz.tek_sabit(e)
        if ac_tek and tek and tek in D and D[tek].get("govde") is not None:
            return C.cumle(D[tek]["govde"]), tek
        s = C.cumle(e)
        if C.kirpik:      # dökümün düğüm bütçesi yüzünden terimin bir kısmı yok: açıkça söylenir
            s += " " + S["kesik"]
        if not say or len(s) > 4 * A.uzun:
            return s, None
        for k_, v_ in list(C.kullanilan.items()) + [(C.kisa(x), x) for x in C.katlanan]:
            if v_ in D and D[v_].get("b", "") == "" and D[v_]["tur"] != "teorem" and D[v_].get("tip") == ["s", "Prop"] and re.search(rf"(?<![\w.(]){re.escape(k_)}(?![\w(])", s):
                ara.setdefault(k_, v_)
        return s, None

    y_ = []
    y = y_.append
    kok = kokler[0]
    y("# " + S["baslik"].format(kok=kok["ad"]))
    y("")
    y(S["kunye"])
    y("")
    y(S["b1"])
    y("")
    for d in kokler:
        c, tek = cumle(d["ad"], ac_tek=True)
        y((S["ad_verir"] if tek else S["dogrudan"]).format(t=d["ad"], yer=(" (" + yer[d["ad"]] + ")") if d["ad"] in yer else "", c=tek))
        y("")
        y(f"> {c}")
        y("")
    op, ok = O.get("onerme_konisinde_proje", 0) - len(kokler), O.get("onerme_konisinde_kutuphane", 0)
    y(S["yalniz_ktp"].format(n=b(ok, dil)) if op <= 0 else S["proje_var"].format(p=b(op, dil), n=b(ok, dil)))
    y("")
    y(S["b2"])
    y("")
    y(S["omurga"].format(n=b(O["konide_proje"], dil)))
    y("")
    # özet tablo: adım, kısa önerme, pay, yoğun alanlar
    # alan verisi yoksa (alan.cpp çalıştırılmamışsa) o sütun hiç yazılmaz
    y(S["tablo_bas"] if AT else S["tablo_bas"].rsplit("|", 2)[0] + "|")
    y("|---:|---|---:|---|" if AT else "|---:|---|---:|")
    for i, (z, cs) in enumerate(acik, 1):
        son = z[-1]
        cx = duz.Duz(bag, dil, katla=KT).cumle(D[son["ad"]]["tip"]) if son["ad"] in D else ""
        al = alanlar.yogunluk(AR, AT, son["ad"], dil)[:3] if AT else []
        y(f"| {i} | {cx if len(cx) <= 170 else S['uzun_kisa']} | {yz(z[0]['alt_agirlik'], topA, dil)} |"
          + ((" " + ", ".join(f"{a} ({('%.0f' % yo)}×)" for a, yo, _ in al) + " |") if AT else ""))
    y("")
    for i, (z, cs) in enumerate(acik, 1):
        son = z[-1]
        y(S["adim"].format(i=i, y=yz(z[0]["alt_agirlik"], topA, dil), ad=son["ad"], yer=(", " + yer[son["ad"]]) if son["ad"] in yer else ""))
        y("")
        c, tek = cumle(son["ad"], ac_tek=True)
        if tek:
            y(S["tek"].format(c=C.kisa(tek)))
            y("")
        if c is None:
            y(S["yok"])
        elif len(c) <= A.uzun:
            y(f"> {c}")
        elif len(c) <= 4 * A.uzun and son["ad"] in D:
            # uzun önerme: bölünmüş yazım (verilenler / varsayımlar / sonuç)
            for satir_ in duz.yapili(C, D[son["ad"]]["tip"]):
                y(f"> {satir_}")
                y(">")
            y_.pop()
        else:
            y(S["cok_uzun"].format(n=b(len(c), dil)))
        y("")
        if len(z) > 1:
            # "aynı sonuç" yalnızca önermeler kayıtta birebir aynıysa söylenir
            tipler = [json.dumps(D[x["ad"]]["tip"]) if x["ad"] in D else None for x in z]
            ayni = all(t is not None and t == tipler[-1] for t in tipler)
            y(S["sarmal" if ayni else "sarmal2"].format(k=len(z) - 1, z=" → ".join(f"`{x['ad']}`" for x in z[:-1])))
            y("")
        dg = DG.get(son["ad"], [])
        if 2 <= len(dg) <= 8:
            y(S["birlesim2"].format(n=len(dg)))
            for x in dg:
                pay = f" ({yz(T[x]['alt_agirlik'], topA, dil)})" if x in T else ""
                cx = None
                if x in D:
                    cx = duz.Duz(bag, dil, katla=KT).cumle(D[x]["tip"])
                y(f"- [`{x}`]{pay}" + (f": {cx}" if cx and len(cx) <= A.uzun else ""))
            y("")
        if cs:
            y(S["parca"])
            for c_ in cs:
                y(S["parca1"].format(y=yz(c_["alt_agirlik"], topA, dil), ad=c_["ad"],
                                     ek=(S["acildi"].format(i=sira[c_["ad"]]) if c_["ad"] in sira else "") + alan_sozu(c_["ad"])))
            kalan = son["alt_agirlik"] - son["agirlik"] - sum(c_["alt_agirlik"] for c_ in cs)
            if son["cocuk"] - len(cs) > 0:
                y(S["kucuk"].format(y=yz(kalan, topA, dil), n=b(son["cocuk"] - len(cs), dil)))
            y("")
    if AT:
        y(S["alan_not"])
        y("")
    if ara:
        y(S["b3"])
        y("")
        y(S["ara"])
        y("")
        acilmis, alan_acilan = [], []
        for k_, v_ in list(ara.items()):
            d = D[v_]
            if d.get("govde") is None:
                y(S["bildirim"].format(k=k_, ad=v_))
                # yapının alanları: kurucunun argümanları (bağımsız olanlar), koddaki adlarıyla
                kur = D.get((d.get("kurucular") or [None])[0])
                if kur and len(alan_acilan) < 2:
                    e_, o_, L_ = kur["tip"], [], []
                    C3 = duz.Duz(bag, dil, katla=sozel.katlama_tablosu(D))
                    while isinstance(e_, list) and e_[0] == "p":
                        L_.append((sozel.temiz(e_[1]), C3.c(e_[3], o_)))
                        o_.append(C3.ad(e_[1], o_, e_[3]))
                        e_ = e_[4]
                    if 1 <= len(L_) <= 6 and all(len(x[1]) <= 200 for x in L_):
                        alan_acilan.append(k_)
                        for a_, c_ in L_:
                            y(f"  - `{a_}`: {c_}")
                continue
            C2 = duz.Duz(bag, dil)
            c = C2.cumle(d["govde"])
            g_ = d["govde"]
            bas_ = g_[1][1] if isinstance(g_, list) and g_[0] == "a" and isinstance(g_[1], list) and g_[1][0] == "c" else None
            alt = duz.tanim_cumlesi(duz.Duz(bag, dil), D[bas_]) if bas_ in D and D[bas_]["tur"] == "tanim" else None
            if alt and len(alt) <= 1500 and len(acilmis) < 2:
                # tanım başka bir tanımın uygulanmasıysa (ilk iki ara önerme için) o tanım da tam yazılır
                acilmis.append(k_)
                y(S["kisa"].format(k=k_, ad=v_, c=c))
                y(f"  - {alt}")
                continue
            y((S["kisa"] if len(c) <= A.kisa and "↦" not in c else S["uzun"]).format(k=k_, ad=v_, c=c, n=b(len(c), dil)))
        y("")
    y(S["b4"])
    y("")
    km = open(f"{KN}/KONI.md", encoding="utf-8").read() if os.path.exists(f"{KN}/KONI.md") else ""
    mk = re.search(r"fazladan kopya: \*\*([\d.]+)\*\*", km)
    kq = Q.get("kaynak") or {}
    V = {"proje": b(O["proje"], dil), "teorem": b(O["proje_tur"]["t"][0], dil), "koni": b(O["konide_proje"], dil),
         "kullanilmayan": b(O["proje"] - O["konide_proje"], dil),
         "kopya": (b(int(mk.group(1).replace(".", "")), dil) + f" ({yz(int(mk.group(1).replace('.', '')), O['proje_tur']['t'][0], dil)})") if mk else None,
         "kaynak": f"{b(kq['son_parcasi_da_yok'], dil)} – {b(kq['kayitta_yok'], dil)}" if kq else None}
    y("| | |")
    y("|---|---:|")
    for et, k_ in S["s"]:
        if V.get(k_):
            y(f"| {et} | {V[k_]} |")
    y("")
    y(S["b5"])
    y("")
    y(S["denetim"])
    open(A.cikti, "w", encoding="utf-8").write("\n".join(y_) + "\n")
    print(json.dumps({"adim": len(acik), "ara": len(ara), "satir": len(y_), "kelime": len(" ".join(y_).split())}))


if __name__ == "__main__":
    main()
