#!/usr/bin/env python3
"""İçe aktarma taraması / Import scan — "A klasörü B klasöründen hiçbir şey kullanmıyor" iddiasını dosya düzeyinde denetler.

TR: Lean'de bir dosya başka bir dosyadaki bildirimi ancak onu (doğrudan ya da dolaylı) içe aktarırsa kullanabilir.
    Bu araç kaynak ağacındaki bütün `import` satırlarından modül grafiğini kurar ve A.* modüllerinden B.* modüllerine
    giden (dolaylı dahil) bir yol olup olmadığına bakar. Yol yoksa iddia kesin doğrudur. Lean gerekmez.
EN: Builds the module graph from `import` lines and reports whether any A.* module reaches a B.* module (transitively).
Kullanım / usage: import_tara.py <kaynak_kökü> A B [cikti.txt]
"""
import os
import re
import sys

IMP = re.compile(r"^\s*(?:(?:public|private|meta)\s+)*import\s+(?:all\s+)?([A-Za-z_][\w.«»']*)")


def main():
    kok, A, B = sys.argv[1], sys.argv[2], sys.argv[3]
    G = {}
    for d, _, fs in sorted(os.walk(kok)):
        for f in sorted(fs):
            if f.endswith(".lean"):
                yol = os.path.join(d, f)
                mod = os.path.relpath(yol, kok)[:-5].replace(os.sep, ".")
                G[mod] = sorted({m.group(1) for l in open(yol, encoding="utf-8", errors="replace") for m in [IMP.match(l)] if m})

    def icinde(m, X):
        return m == X or m.startswith(X + ".")

    As = [m for m in G if icinde(m, A)]
    Bs = [m for m in G if icinde(m, B)]
    # A modüllerinden erişilen her modül; B'ye ilk varan yol saklanır
    once, yigin, bulunan = {m: None for m in As}, list(As), []
    while yigin:
        u = yigin.pop()
        for v in G.get(u, []):
            if v not in once:
                once[v] = u
                if icinde(v, B):
                    bulunan.append(v)
                yigin.append(v)
    s = [f"kaynak: {len(G)} dosya; {A}.*: {len(As)} modül; {B}.*: {len(Bs)} modül",
         f"{A}.* modüllerinin doğrudan içe aktardıkları, ilk bileşene göre: "
         + ", ".join(f"{k} {n}" for k, n in sorted(__import__('collections').Counter(v.split('.')[0] for m in As for v in G[m]).items()))]
    if bulunan:
        s.append(f"SONUÇ: {A} -> {B} yolu VAR ({len(bulunan)} {B} modülüne erişiliyor). Örnek zincir:")
        z, u = [], sorted(bulunan)[0]
        while u is not None:
            z.append(u)
            u = once[u]
        s.append("  " + " <- ".join(z))
    else:
        s.append(f"SONUÇ: {A} -> {B} yolu YOK: hiçbir {A}.* modülü, doğrudan ya da dolaylı, bir {B}.* modülünü içe aktarmıyor.")
    t = "\n".join(s) + "\n"
    sys.stdout.write(t)
    if len(sys.argv) > 4:
        open(sys.argv[4], "w", encoding="utf-8").write(t)


if __name__ == "__main__":
    main()
