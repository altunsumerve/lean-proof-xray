#!/usr/bin/env python3
"""Koni raporu / Cone report.

TR: arac/agac.cpp çıktısından (ozet.json, taslar.tsv, kullanilmayan.tsv) ve isteğe bağlı olarak parmak izi
    tablosundan (parmak.tsv) ve atlastan okunur bir rapor yazar: kullanılan/kullanılmayan kod, kopya önermeler,
    baskınlık ağacı (makalenin katmanlı iskeleti) ve en büyük kilometre taşları.
    Buradaki bütün sayılar grafikten gelir; yalnızca "yardımcı ad" süzgeci (gösterim için) ad kalıbına bakar.
EN: Writes a readable report from the cone/dominator data: used vs. unused code, duplicate statements,
    the dominator tree (layered skeleton of the article) and the largest milestones.

Kullanım / usage:
  python3 koni_rapor.py --koni KLASOR [--parmak parmak.tsv] [--atlas atlas.jsonl --dosyalar files.json]
                        --md KONI.md [--ust taslar_ust.tsv]
"""
import argparse
import collections
import json
import os
import re

YARDIMCI = re.compile(r"(\._proof_\d+|\.proof_\d+|\.match_\d+|\._sunfold|\._unfold|\.eq_\d+|\.eq_def|"
                      r"\._eq_\d+|\.induct|\.rec$|\.recOn$|\.casesOn$|\.noConfusion|\.below|\.brecOn|"
                      r"\.binductionOn|\.ibelow|\.sizeOf_spec|\._sizeOf|\.mk\.inj|\.injEq|\._cstage|"
                      r"\._closed|\._lambda|_aux_|\._simp_\d+|\.ext_iff$|^_private\.|\.ctorIdx|\.ctorElim|\.toCtorIdx)")
STANDART = {"propext", "Classical.choice", "Quot.sound"}
AKS_NOT = {"sorryAx": "**eksik ispat (`sorry`) / missing proof**",
           "Lean.ofReduceBool": "**standart dışı: derleyiciye güven (`native_decide`) / non-standard: trusts the compiler**",
           "Lean.trustCompiler": "**standart dışı: derleyiciye güven (`native_decide`) / non-standard: trusts the compiler**"}
TUR = {"t": "teorem", "d": "tanım", "a": "aksiyom", "o": "opak", "i": "tip", "c": "kurucu", "r": "özyineleyici"}


def b(n):
    return f"{n:,}".replace(",", ".")


def yuzde(a, t):
    return f"%{100 * a / t:.1f}".replace(".", ",") if t else "-"


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--koni", required=True)
    a.add_argument("--parmak")
    a.add_argument("--atlas")
    a.add_argument("--dosyalar")
    a.add_argument("--md", required=True)
    a.add_argument("--ust")
    A = a.parse_args()
    s = []
    y = s.append
    y("# Koni / Cone — ispat konisi ve baskınlık ağacı / proof cone and dominator tree")
    y("")
    op = os.path.join(A.koni, "ozet.json")
    if not os.path.exists(op):
        y("**Kök bulunamadı / root not found.** Aday adlar / candidate names:")
        y("")
        y("```")
        kp = os.path.join(A.koni, "kok_adaylari.txt")
        if os.path.exists(kp):
            s.extend(x.rstrip("\n") for x in list(open(kp, encoding="utf-8"))[:300])
        y("```")
        open(A.md, "w", encoding="utf-8").write("\n".join(s) + "\n")
        return
    O = json.load(open(op, encoding="utf-8"))
    T = []  # ad, tur, baskin, derinlik, alt_sayi, alt_agirlik, agirlik, tip_boyu, deger_boyu, kullanan, cocuk, onermede
    with open(os.path.join(A.koni, "taslar.tsv"), encoding="utf-8") as f:
        next(f)
        for l in f:
            p = l.rstrip("\n").split("\t")
            T.append((p[0], p[1], p[2], int(p[3]), int(p[4]), int(p[5]), int(p[6]), int(p[7]), int(p[8]), int(p[9]), int(p[10]), p[11] == "1"))
    konide = {t[0] for t in T}
    U = []
    with open(os.path.join(A.koni, "kullanilmayan.tsv"), encoding="utf-8") as f:
        for l in f:
            p = l.rstrip("\n").split("\t")
            U.append((p[0], p[1], int(p[2])))
    kokler = [t for t in T if t[2] == "<kok>"]
    topA = sum(t[5] for t in kokler) or 1
    topS = sum(t[4] for t in kokler) or 1

    # atlas: ad -> (dosya, satır, kaynak önermesi)
    atlas = {}
    ilgi = {t[0] for t in T if t[5] * 2000 >= topA or t[3] <= 2}
    if A.atlas and os.path.exists(A.atlas):
        files = json.load(open(A.dosyalar)) if A.dosyalar and os.path.exists(A.dosyalar) else []
        with open(A.atlas, encoding="utf-8") as f:
            for l in f:
                d = json.loads(l)
                if d[1] in ilgi and d[1] not in atlas:
                    atlas[d[1]] = (files[d[2]] if d[2] < len(files) else str(d[2]), d[3], d[11])

    def yer(n):
        return f"`{atlas[n][0]}:{atlas[n][1]}`" if n in atlas else ""

    y(f"Kök / root: {', '.join('`' + k + '`' for k in O['kok'])}")
    y("")
    y("Bu sayfadaki sayılar resmi Lean kaydının (lean4export) bağımlılık grafiğinden hesaplanır; tahmin içermez. "
      "/ All numbers on this page are computed from the dependency graph of the official Lean export.")
    y("")
    if not O["kutuphane_ayrimi"]:
        y("> **Uyarı / warning:** kütüphane (Mathlib) adları okunamadı; aşağıda \"proje\" kayıttaki her şeyi kapsıyor.")
        y("")
    y("## 1. Sayılar / Numbers")
    y("")
    y("| | Bildirim / declarations | İfade ağırlığı / expression weight |")
    y("|---|---:|---:|")
    y(f"| Kayıttaki toplam / total in the export | {b(O['bildirim'])} | {b(O['ifade_agirligi'])} |")
    y(f"| Kütüphane (Mathlib ve altı) / library | {b(O['kutuphane'])} | {b(O['ifade_agirligi'] - O['proje_agirlik'])} |")
    y(f"| Proje / project | {b(O['proje'])} | {b(O['proje_agirlik'])} |")
    y(f"| &nbsp;&nbsp;kökün ispat konisinde / in the root's proof cone | {b(O['konide_proje'])} ({yuzde(O['konide_proje'], O['proje'])}) | {b(O['konide_proje_agirlik'])} ({yuzde(O['konide_proje_agirlik'], O['proje_agirlik'])}) |")
    y(f"| &nbsp;&nbsp;**kullanılmayan / unused by the root** | **{b(O['proje'] - O['konide_proje'])}** ({yuzde(O['proje'] - O['konide_proje'], O['proje'])}) | {b(O['proje_agirlik'] - O['konide_proje_agirlik'])} ({yuzde(O['proje_agirlik'] - O['konide_proje_agirlik'], O['proje_agirlik'])}) |")
    y(f"| Kökün önermesini anlamak için gereken proje bildirimi / project declarations needed to read the root's statement | {b(O['onerme_konisinde_proje'])} | |")
    y(f"| Konideki kütüphane bildirimi / library declarations in the cone | {b(O['konide_kutuphane'])} | |")
    y("")
    y("İfade ağırlığı: bildirimin kayda eklediği yeni ifade düğümü sayısı (ispatın büyüklüğünün ölçüsü). "
      "/ Expression weight: number of new expression nodes the declaration added to the export.")
    y("")
    y("| Tür / kind | Projede / in project | Konide / in cone |")
    y("|---|---:|---:|")
    for k, (x, z) in sorted(O["proje_tur"].items(), key=lambda kv: -kv[1][0]):
        y(f"| {TUR.get(k, k)} | {b(x)} | {b(z)} |")
    y("")

    # 1b. aksiyomlar
    y("## 1b. Aksiyomlar / Axioms")
    y("")
    if "aksiyom_konide" not in O:
        y("Ölçülmedi: bu sonuç aracın aksiyom listesi yazmayan eski sürümüyle üretildi. / Not measured: produced by an older version of the tool.")
        y("")
    else:
        ak = sorted(O["aksiyom_konide"])
        disi = [x for x in ak if x not in STANDART]
        y(f"Kökün ispat konisindeki aksiyom: **{len(ak)}** (kayıttaki toplam aksiyom: {O['aksiyom_kayitta']}; kütüphane dahil, hiçbiri atlanmadı). "
          f"Lean'in üç standart aksiyomu dışında kalan: **{len(disi)}**. "
          f"/ Axioms in the root's proof cone: {len(ak)} (axioms in the export: {O['aksiyom_kayitta']}; library included). Outside Lean's three standard axioms: {len(disi)}.")
        y("")
        if ak:
            y("| Aksiyom / axiom | Not / note |")
            y("|---|---|")
            for x in ak:
                y(f"| `{x}` | {AKS_NOT.get(x, 'standart / standard' if x in STANDART else '**standart dışı / non-standard**')} |")
            y("")
        y("Bu liste kayıttaki `axiom` bildirimlerinden okunur; ispatı yeniden denetlemez (bunu Lean çekirdeği ve bağımsız denetleyiciler yapar). "
          "/ Read from the `axiom` declarations of the export; it does not re-check the proof.")
        y("")

    # 2. kullanılmayan
    y("## 2. Kullanılmayan kod / Unused code")
    y("")
    yard = sum(1 for u in U if YARDIMCI.search(u[0]))
    y(f"Kökün ispatına hiç girmeyen proje bildirimi: **{b(len(U))}** (bunların {b(yard)} tanesi Lean'in otomatik yardımcısı). "
      f"/ Project declarations never used by the root's proof: {b(len(U))} ({b(yard)} of them Lean-generated auxiliaries).")
    y("")
    ns = collections.Counter()
    nsA = collections.Counter()
    for n, _, w in U:
        k = ".".join(n.split(".")[:2])
        ns[k] += 1
        nsA[k] += w
    if ns:
        y("| Ad alanı / namespace | Bildirim | Ağırlık / weight |")
        y("|---|---:|---:|")
        for k, c in ns.most_common(20):
            y(f"| `{k}` | {b(c)} | {b(nsA[k])} |")
        y("")

    # 3. kopyalar
    if A.parmak and os.path.exists(A.parmak):
        proje = konide | {u[0] for u in U}
        G = collections.defaultdict(list)
        with open(A.parmak, encoding="utf-8", errors="replace") as f:
            for l in f:
                p = l.rstrip("\n").split("\t")
                if len(p) >= 3 and p[1] == "thm" and p[0] in proje:
                    G[p[2]].append(p[0])
        cok = [v for v in G.values() if len(v) > 1]
        fazla = sum(len(v) - 1 for v in cok)
        cokG = [[n for n in v if not YARDIMCI.search(n)] for v in cok]
        cokG = [v for v in cokG if len(v) > 1]
        fazlaG = sum(len(v) - 1 for v in cokG)
        nthm = sum(len(v) for v in G.values())
        y("## 3. Kopya önermeler / Duplicate statements")
        y("")
        y(f"Proje teoremi: {b(nthm)}. Önermesi (tipi) başka bir teoreminkiyle yapısal olarak aynı olan gruplar: **{b(len(cok))}**; "
          f"fazladan kopya: **{b(fazla)}** ({yuzde(fazla, nthm)}). Yardımcı adlar hariç: {b(len(cokG))} grup, {b(fazlaG)} fazladan kopya. "
          f"/ Project theorems: {b(nthm)}. Groups whose statement (type) is structurally identical: {b(len(cok))}; "
          f"redundant copies: {b(fazla)}. Excluding auxiliary names: {b(len(cokG))} groups, {b(fazlaG)} redundant copies.")
        y("")
        y("Not: parmak izi 64 bit ve yapısaldır (bağlı değişken adları sayılmaz); evren parametre adları farklıysa kopya sayılmaz. "
          "/ The fingerprint is 64-bit and structural.")
        y("")
        if cokG:
            y("| Kopya sayısı | Konide | Örnek adlar / example names |")
            y("|---:|---:|---|")
            for v in sorted(cokG, key=len, reverse=True)[:15]:
                y(f"| {len(v)} | {sum(1 for n in v if n in konide)} | " + ", ".join(f"`{n}`" for n in v[:3]) + " |")
            y("")

    # 4. baskınlık ağacı
    cocuk = collections.defaultdict(list)
    for t in T:
        cocuk[t[2]].append(t)
    for k in cocuk:
        cocuk[k].sort(key=lambda t: -t[5])
    der = collections.Counter(t[3] for t in T)
    y("## 4. Baskınlık ağacı / Dominator tree")
    y("")
    y("X, Y'nin üstündeyse kökten Y'ye giden her bağımlılık yolu X'ten geçer: Y yalnızca X için vardır. "
      "Bir satırın alt ağacı, makalede o başlığın altına girecek her şeydir. "
      "/ If X is above Y, every dependency path from the root to Y passes through X.")
    y("")
    y(f"Ağaçtaki düğüm: {b(O['agac_dugum'])}; kökün doğrudan çocukları: {b(sum(t[10] for t in kokler))}; "
      f"en derin düzey: {max(der) if der else 0}.")
    y("")
    y("| Alt ağaç büyüklüğü / subtree size | Düğüm / nodes |")
    y("|---|---:|")
    for esik in (10, 100, 1000, 10000, 100000):
        y(f"| ≥ {b(esik)} bildirim | {b(sum(1 for t in T if t[4] >= esik))} |")
    y("")
    y("Aşağıda ağırlığı toplamın en az %0,5'i olan dallar (en çok 5 düzey). Sütunlar: alt ağaçtaki bildirim, ağırlık payı, bu bildirimi doğrudan kullanan sayısı.")
    y("")
    y("```")
    satir = [0]

    def yaz(t, d):
        if satir[0] >= 220:
            return
        satir[0] += 1
        y(f"{'  ' * d}{t[0]}  [{TUR.get(t[1], t[1])}]  alt={b(t[4])}  {yuzde(t[5], topA)}  kullanan={t[9]}")
        if d >= 5:
            return
        kalan = [c for c in cocuk.get(t[0], []) if c[5] * 200 >= topA]
        for c in kalan:
            yaz(c, d + 1)
        diger = len(cocuk.get(t[0], [])) - len(kalan)
        if diger and satir[0] < 220:
            y(f"{'  ' * (d + 1)}… ve {b(diger)} küçük çocuk daha")

    for t in kokler:
        yaz(t, 0)
    y("```")
    y("")

    # 5. kilometre taşları
    y("## 5. En büyük kilometre taşları / Largest milestones")
    y("")
    y("Kök dışındaki, yardımcı olmayan teoremler; alt ağaç ağırlığına göre. Önerme metni projenin kaynağından alınmıştır (atlas verildiyse). "
      "/ Non-auxiliary theorems other than the root, by subtree weight; statement text is from the source when available.")
    y("")
    taslar = sorted((t for t in T if t[1] == "t" and t[2] != "<kok>" and not YARDIMCI.search(t[0])), key=lambda t: -t[5])
    y("| # | Teorem | Alt ağaç | Pay | Üstü / dominator | Kaynak |")
    y("|---:|---|---:|---:|---|---|")
    for i, t in enumerate(taslar[:50], 1):
        y(f"| {i} | `{t[0]}` | {b(t[4])} | {yuzde(t[5], topA)} | `{t[2]}` | {yer(t[0])} |")
    y("")
    onermeli = [t for t in taslar[:50] if t[0] in atlas]
    if onermeli:
        y("### Önermeler / Statements")
        y("")
        for t in onermeli:
            y(f"- `{t[0]}` ({yer(t[0])})")
            y("  ```lean")
            y("  " + atlas[t[0]][2][:500])
            y("  ```")
        y("")
    open(A.md, "w", encoding="utf-8").write("\n".join(s) + "\n")
    if A.ust:
        with open(A.ust, "w", encoding="utf-8") as f:
            f.write("ad\ttur\tbaskin\tderinlik\talt_sayi\talt_agirlik\tagirlik\ttip_boyu\tdeger_boyu\tkullanan\tcocuk\tonermede\n")
            for t in sorted(T, key=lambda t: -t[5])[:3000]:
                f.write("\t".join(str(int(x)) if isinstance(x, bool) else str(x) for x in t) + "\n")
    print(json.dumps({"agac": len(T), "kullanilmayan": len(U), "tas": len(taslar)}))


if __name__ == "__main__":
    main()
