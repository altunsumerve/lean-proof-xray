#!/usr/bin/env python3
"""Blueprint karşılaştırması / Blueprint comparison — aracın çıktısını insan eliyle yazılmış bir blueprint ile ölçer.

TR: Bir Lean projesinin blueprint'i (leanblueprint LaTeX kaynağı) cevap anahtarı olarak kullanılır:
      1. Blueprint'teki `\\lean{...}` adları kodda (kökün ispat konisinde) var mı?
      2. Aracın "kilometre taşı" sıralaması, insanların blueprint'e koyduğu teoremleri ne kadar iyi buluyor?
         (birkaç sıralama ölçütü yan yana denenir)
      3. Blueprint'teki `\\uses{...}` iddiaları kodun bağımlılık grafiğiyle doğrulanıyor mu? Kodda olup
         blueprint'te yazılmamış bağımlılıklar hangileri?
EN: Uses a hand-written blueprint as the answer key: are its `\\lean{}` names in the proof cone, how well do
    the tool's milestone rankings recover the theorems humans chose, and are its `\\uses{}` claims confirmed
    by the dependency graph of the code.

Kullanım / usage:
  python3 blueprint_karsilastir.py --blueprint KLASOR --dugum dugum.tsv --kenar kenar.bin --taslar taslar.tsv --md CIKTI.md
"""
import argparse
import array
import collections
import json
import os
import re
import struct

ORTAM = ("theorem", "lemma", "proposition", "corollary", "definition", "claim", "remark", "example")
YARDIMCI = re.compile(r"(\._proof_\d+|\.proof_\d+|\.match_\d+|\._sunfold|\._unfold|\.eq_\d+|\.eq_def|"
                      r"\._eq_\d+|\.induct|\.rec$|\.recOn$|\.casesOn$|\.noConfusion|\.below|\.brecOn|"
                      r"\.binductionOn|\.ibelow|\.sizeOf_spec|\._sizeOf|\.mk\.inj|\.injEq|\._cstage|"
                      r"\._closed|\._lambda|_aux_|\._simp_\d+|\.ext_iff$|^_private\.|\.ctorIdx|\.ctorElim|\.toCtorIdx)")


def liste(metin, komut):
    r = []
    for m in re.finditer(r"\\" + komut + r"\s*\{([^}]*)\}", metin):
        r += [x.strip() for x in m.group(1).split(",") if x.strip()]
    return r


def blueprint_oku(kl):
    """[{etiket, tur, lean:[..], uses:[..] (önerme), puses:[..] (ispat)}]"""
    ogeler = []
    for d, _, fs in sorted(os.walk(kl)):
        for f in sorted(fs):
            if not f.endswith(".tex"):
                continue
            t = open(os.path.join(d, f), encoding="utf-8", errors="replace").read()
            t = re.sub(r"(?<!\\)%[^\n]*", "", t)
            son = None
            for m in re.finditer(r"\\begin\{(" + "|".join(ORTAM) + r"|proof)\}(.*?)\\end\{\1\}", t, re.S):
                tur, g = m.group(1), m.group(2)
                if tur == "proof":
                    hedef = son
                    pr = liste(g, "proves")
                    if pr:
                        hedef = next((o for o in ogeler if o["etiket"] == pr[0]), son)
                    if hedef is not None:
                        hedef["puses"] += liste(g, "uses")
                    continue
                et = liste(g, "label")
                son = {"etiket": et[0] if et else None, "tur": tur, "lean": liste(g, "lean"), "uses": liste(g, "uses"), "puses": [], "dosya": f}
                ogeler.append(son)
    return ogeler


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--blueprint", required=True)
    a.add_argument("--dugum", required=True)
    a.add_argument("--kenar", required=True)
    a.add_argument("--taslar", required=True)
    a.add_argument("--md", required=True)
    a.add_argument("--yol", help="yol.cpp çıktısı (ad<TAB>yol_payi); verilirse sıralama ölçütlerine eklenir")
    A = a.parse_args()

    ad, tur = [], []
    for l in open(A.dugum, encoding="utf-8"):
        p = l.rstrip("\n").split("\t")
        ad.append(p[2])
        tur.append(p[1])
    N = len(ad)
    sira = {}
    for i, n in enumerate(ad):
        sira.setdefault(n, i)
    off = array.array("Q", [0])
    K = array.array("I")
    with open(A.kenar, "rb") as f:
        assert struct.unpack("<Q", f.read(8))[0] == N
        for _ in range(N):
            nt, nv = struct.unpack("<II", f.read(8))
            K.frombytes(f.read(4 * (nt + nv)))
            off.append(len(K))
    T = {}
    bas = None
    for l in open(A.taslar, encoding="utf-8"):
        p = l.rstrip("\n").split("\t")
        if bas is None:
            bas = p
            continue
        T[p[0]] = dict(zip(bas, p))

    O = blueprint_oku(A.blueprint)
    leanli = [o for o in O if o["lean"]]
    tum = sorted({n for o in O for n in o["lean"]})
    kayitta = [n for n in tum if n in sira]
    konide = [n for n in tum if n in T]
    s = []
    y = s.append
    y("# Blueprint karşılaştırması / Blueprint comparison")
    y("")
    y("Cevap anahtarı: projenin elle yazılmış blueprint'i. Araç: kayıttan (lean4export) hesaplanan bağımlılık grafiği ve baskınlık ağacı. "
      "/ Answer key: the project's hand-written blueprint. Tool: dependency graph and dominator tree computed from the export.")
    y("")
    y("## 1. Blueprint adları kodda var mı / Are the blueprint's names in the code")
    y("")
    y("| | Sayı / Count |")
    y("|---|---:|")
    y(f"| Blueprint öğesi / items | {len(O)} |")
    y(f"| `\\lean{{}}` taşıyan öğe / items with a Lean name | {len(leanli)} |")
    y(f"| Farklı Lean adı / distinct Lean names | {len(tum)} |")
    y(f"| Kayıtta bulunan / found in the export | {len(kayitta)} |")
    y(f"| Kökün ispat konisinde (proje bildirimi) / in the root's proof cone | {len(konide)} |")
    y("")
    yok = [n for n in tum if n not in sira]
    if yok:
        y(f"Kayıtta olmayan adlar ({len(yok)}; kök bunları kullanmıyor ya da ad değişmiş): " + ", ".join(f"`{n}`" for n in yok[:40]) + (" …" if len(yok) > 40 else ""))
        y("")

    # 2. sıralama ölçütleri
    aday = [n for n, d in T.items() if d["tur"] == "t" and d["baskin"] != "<kok>" and not YARDIMCI.search(n)]
    hedef = {n for n in konide if T[n]["tur"] == "t" and T[n]["baskin"] != "<kok>"}
    y("## 2. Kilometre taşı sıralaması insan seçimini buluyor mu / Do milestone rankings recover the human choice")
    y("")
    y(f"Aday: konideki yardımcı olmayan proje teoremleri ({len(aday)}). Hedef: bunlardan blueprint'te adı geçenler ({len(hedef)}). "
      f"Rastgele seçimde beklenen isabet: {100 * len(hedef) / max(1, len(aday)):.1f}%. "
      "/ Candidates: non-auxiliary project theorems in the cone. Target: those named in the blueprint.")
    y("")
    olcut = {
        "alt ağaç ağırlığı / subtree weight": lambda d: int(d["alt_agirlik"]),
        "alt ağaç bildirim sayısı / subtree count": lambda d: int(d["alt_sayi"]),
        "kendi ispat ağırlığı / own proof weight": lambda d: int(d["agirlik"]),
        "doğrudan kullanan sayısı / direct users": lambda d: int(d["kullanan"]),
        "ağırlık ÷ önerme boyu / weight per statement size": lambda d: int(d["alt_agirlik"]) / (1 + int(d["tip_boyu"])),
        "ağaçta sığlık (köke yakınlık) / shallowness": lambda d: -int(d["derinlik"]),
    }
    if A.yol and os.path.exists(A.yol):
        YP = {}
        for l in open(A.yol, encoding="utf-8"):
            p = l.rstrip("\n").split("\t")
            if len(p) == 2 and p[0] != "ad":
                YP[p[0]] = float(p[1])
        olcut["yol payı (köke giden yolların geçen kesri) / path share"] = lambda d: YP.get(d["ad"], 0.0)
        # birleşik: iki sıralamadaki yerin iyisi (ağırlık ya da yol payı)
        sa = {n: i for i, n in enumerate(sorted(aday, key=lambda n: -int(T[n]["alt_agirlik"])))}
        sy = {n: i for i, n in enumerate(sorted(aday, key=lambda n: -YP.get(n, 0.0)))}
        olcut["ağırlık ile yol payının iyisi / better of weight and path share"] = lambda d: -min(sa.get(d["ad"], 1 << 30), sy.get(d["ad"], 1 << 30))
    y("| Ölçüt / criterion | İlk k'da isabet (k = hedef sayısı) / hits in top k | İlk 2k'da / in top 2k | Hedeflerin ortanca sırası / median rank of targets |")
    y("|---|---:|---:|---:|")
    k = len(hedef)
    for isim, fn in olcut.items():
        sirali = sorted(aday, key=lambda n: -fn(T[n]))
        yer = {n: i for i, n in enumerate(sirali)}
        h1 = sum(1 for n in sirali[:k] if n in hedef)
        h2 = sum(1 for n in sirali[:2 * k] if n in hedef)
        rs = sorted(yer[n] for n in hedef)
        ort = rs[len(rs) // 2] + 1 if rs else 0
        y(f"| {isim} | {h1} / {k} ({100 * h1 / max(1, k):.0f}%) | {h2} / {k} ({100 * h2 / max(1, k):.0f}%) | {ort} / {len(aday)} |")
    # zincir: baskınlık ağacında tek çocuğu olan bir adayın o çocuğu da adaysa ikisi aynı adımdır (sarmalayıcı: x, x', x_aux ...).
    # Eşik yok: yalnız "ağaçta tam bir çocuk" koşulu. Zincir, üyelerinden biri blueprint'teyse isabet sayılır; k = hedef zincir sayısı.
    aday_k = set(aday)
    tek = {}                                         # üst -> tek çocuğu (ikisi de aday)
    cs = collections.defaultdict(list)
    for n, d in T.items():
        cs[d["baskin"]].append(n)
    for u, c in cs.items():
        if u in aday_k and len(c) == 1 and c[0] in aday_k:
            tek[u] = c[0]
    alt_uye = set(tek.values())
    zincir = []
    for n in sorted(aday, key=lambda n: (-int(T[n]["alt_agirlik"]), n)):
        if n in alt_uye:
            continue                                 # zincirin başı değil
        z = [n]
        while z[-1] in tek:
            z.append(tek[z[-1]])
        zincir.append(z)
    hz = [z for z in zincir if any(n in hedef for n in z)]
    kz = len(hz)
    h1z = sum(1 for z in zincir[:kz] if any(n in hedef for n in z))
    h2z = sum(1 for z in zincir[:2 * kz] if any(n in hedef for n in z))
    rz = sorted(i for i, z in enumerate(zincir) if any(n in hedef for n in z))
    y(f"| alt ağaç ağırlığı, zincirler tek adım / subtree weight, chains as one step | {h1z} / {kz} ({100 * h1z / max(1, kz):.0f}%) | {h2z} / {kz} ({100 * h2z / max(1, kz):.0f}%) | {(rz[len(rz) // 2] + 1) if rz else 0} / {len(zincir)} |")
    y("")
    y(f"Son satır: baskınlık ağacında tek çocuğu olan bir adım ile o çocuk tek adım sayılır ({len(aday)} aday {len(zincir)} zincir eder; rastgele beklenen {100 * kz / max(1, len(zincir)):.1f}%). "
      "/ Last row: a step with exactly one child in the dominator tree is merged with that child.")
    y("")

    # 2b. küme olarak seçim kuralları (eşik ayarı yok, yapısal)
    topA = max((int(d["alt_agirlik"]) for d in T.values()), default=1) or 1
    ic_dugum = {d["baskin"] for n, d in T.items() if not YARDIMCI.search(n)}
    kural = {
        "ağaçta çocuğu olan / has children in the tree": lambda d: int(d["cocuk"]) > 0,
        "yardımcı olmayan çocuğu olan / has a non-auxiliary child": lambda d: d["ad"] in ic_dugum,
        "en az 2 yerde kullanılan / used in at least 2 places": lambda d: int(d["kullanan"]) >= 2,
        "çocuğu olan VEYA ≥2 yerde kullanılan / children or ≥2 users": lambda d: d["ad"] in ic_dugum or int(d["kullanan"]) >= 2,
        "alt ağaç ağırlığı ≥ %0,5 / subtree weight ≥ 0.5%": lambda d: int(d["alt_agirlik"]) * 200 >= topA,
        "ağırlık ≥ %0,5 VEYA ≥2 yerde kullanılan / weight ≥ 0.5% or ≥2 users": lambda d: int(d["alt_agirlik"]) * 200 >= topA or int(d["kullanan"]) >= 2,
        "hepsi (her aday) / everything": lambda d: True,
    }
    y("Yapısal seçim kuralları: kuralın seçtiği adaylardan kaçı blueprint'te (kesinlik), blueprint teoremlerinin kaçı seçildi (kapsama). "
      "/ Structural selection rules: precision = selected candidates that are in the blueprint, recall = blueprint theorems selected.")
    y("")
    y("| Kural / rule | Seçilen / selected | Kesinlik / precision | Kapsama / recall |")
    y("|---|---:|---:|---:|")
    for isim, fn in kural.items():
        sec = [n for n in aday if fn(T[n])]
        ist = sum(1 for n in sec if n in hedef)
        y(f"| {isim} | {len(sec)} | {100 * ist / max(1, len(sec)):.0f}% | {100 * ist / max(1, len(hedef)):.0f}% |")
    y("")
    sirali = sorted(aday, key=lambda n: -int(T[n]["alt_agirlik"]))
    yer = {n: i + 1 for i, n in enumerate(sirali)}
    y("Ağırlık sıralamasının en geride bıraktığı blueprint teoremleri / blueprint theorems ranked lowest by weight:")
    y("")
    for n in sorted(hedef, key=lambda n: -yer[n])[:20]:
        d = T[n]
        y(f"- `{n}` — sıra {yer[n]}, alt={d['alt_sayi']}, kullanan={d['kullanan']}, önerme boyu={d['tip_boyu']}, ispat ağırlığı={d['agirlik']}")
    y("")
    y("Ağırlık sıralamasında en üstte olup blueprint'te olmayan teoremler / top-ranked theorems not in the blueprint:")
    y("")
    for n in [n for n in sirali if n not in hedef][:20]:
        d = T[n]
        y(f"- `{n}` — sıra {yer[n]}, alt={d['alt_sayi']}, kullanan={d['kullanan']}, üstü=`{d['baskin']}`")
    y("")

    # 3. \uses iddiaları
    def idler(adlar):
        return [sira[n] for n in adlar if n in sira]

    etiket = {o["etiket"]: o for o in O if o["etiket"]}
    bp = set()
    for o in leanli:
        bp.update(idler(o["lean"]))
    sahip = collections.defaultdict(set)  # bildirim -> blueprint etiketleri
    for o in leanli:
        for i in idler(o["lean"]):
            sahip[i].add(o["etiket"])

    def gez(kokler, dur):
        """kokler'den ulaşılanlar; dur=True ise başka bir blueprint düğümüne varınca orada durur."""
        g = set(kokler)
        yg = list(kokler)
        varilan = set()
        while yg:
            x = yg.pop()
            for z in K[off[x]:off[x + 1]]:
                if z in g:
                    continue
                g.add(z)
                if z in bp:
                    varilan.add(z)
                    if dur:
                        continue
                yg.append(z)
        return g, varilan

    dogru = yanlis = olculemez = 0
    yanlislar, eksikler = [], []
    eksikS = bildirilenS = gercekS = 0
    for o in leanli:
        A_ = idler(o["lean"])
        if not A_:
            continue
        tumu, _ = gez(A_, False)
        _, dogrudan = gez(A_, True)
        dogrudan -= set(A_)
        bildirilen = set()
        for u in set(o["uses"] + o["puses"]):
            h = etiket.get(u)
            if h is None or not idler(h["lean"]):
                olculemez += 1
                continue
            B_ = idler(h["lean"])
            bildirilen.update(B_)
            if any(b in tumu for b in B_):
                dogru += 1
            else:
                yanlis += 1
                yanlislar.append((o["etiket"], o["lean"][0], u, h["lean"][0]))
        gercekS += len(dogrudan)
        bildirilenS += len(bildirilen)
        e = [b for b in dogrudan if b not in bildirilen and not (sahip[b] & {o["etiket"]})]
        eksikS += len(e)
        for b in e[:3]:
            eksikler.append((o["etiket"], o["lean"][0], ad[b]))
    y("## 3. `\\uses` iddiaları kodla doğrulanıyor mu / Are the `\\uses` claims confirmed by the code")
    y("")
    y("Blueprint \"A, B'yi kullanır\" diyorsa, kodda A'nın bildirimi B'nin bildirimine (doğrudan ya da dolaylı) dayanmalı. "
      "/ If the blueprint says A uses B, A's declaration must depend on B's in the code.")
    y("")
    y("| | Sayı / Count |")
    y("|---|---:|")
    y(f"| Doğrulanan `\\uses` / confirmed | {dogru} |")
    y(f"| **Kodda karşılığı olmayan `\\uses` / not backed by the code** | **{yanlis}** |")
    y(f"| Ölçülemeyen (iki uçtan biri Lean adı taşımıyor) / not measurable | {olculemez} |")
    y(f"| Kodda olan blueprint düzeyi doğrudan bağımlılık / blueprint-level direct dependencies in the code | {gercekS} |")
    y(f"| &nbsp;&nbsp;blueprint'te yazılmamış olanlar / of which missing from the blueprint | {eksikS} |")
    y("")
    if yanlislar:
        y("Kodda karşılığı olmayan iddialar (ilk 30) / claims not backed by the code:")
        y("")
        for e1, n1, e2, n2 in yanlislar[:30]:
            y(f"- `{e1}` (`{n1}`) → `{e2}` (`{n2}`)")
        y("")
    if eksikler:
        y("Kodda olup blueprint'te yazılmamış bağımlılık örnekleri (ilk 30) / dependencies in the code missing from the blueprint:")
        y("")
        for e1, n1, b in eksikler[:30]:
            y(f"- `{e1}` (`{n1}`) → `{b}`")
        y("")
    open(A.md, "w", encoding="utf-8").write("\n".join(s) + "\n")
    print(json.dumps({"oge": len(O), "lean": len(tum), "konide": len(konide), "hedef": len(hedef), "aday": len(aday),
                      "uses_dogru": dogru, "uses_yanlis": yanlis, "eksik": eksikS}))


if __name__ == "__main__":
    main()
