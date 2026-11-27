#!/usr/bin/env python3
"""kaynak — tek bir bildirimin Lean kodu, açıklama satırları silinmiş / the Lean code of single declarations, comments stripped.
No AI. Comments and docstrings are removed on purpose: a story must come from the code, not from what the code says about itself.
Usage: kaynak.py <source root> NAME [NAME ...]     (full name or last component; at most 220 lines per declaration)"""
import os
import re
import sys

ANAHTAR = (r"(?:(?:private|protected|noncomputable|unsafe|partial|nonrec)\s+)*"
           r"(?:theorem|lemma|def|abbrev|structure|class|inductive|instance|opaque|axiom)")


def temizle(s):
    s = re.sub(r"/-.*?-/", "", s, flags=re.S)
    return [l for l in (re.sub(r"--.*$", "", x).rstrip() for x in s.split("\n")) if l.strip()]


def yukle(kok):
    D = []
    for d, alt, fs in sorted(os.walk(kok)):
        alt[:] = sorted(x for x in alt if x not in (".lake", ".git"))
        for f in sorted(fs):
            if f.endswith(".lean"):
                yol = os.path.join(d, f)
                D.append((os.path.relpath(yol, kok), temizle(open(yol, encoding="utf-8", errors="replace").read())))
    return D


BAS = re.compile(r"^(?:@\[|" + ANAHTAR + r"\s|end\s|namespace\s|section\s|open\s|variable\s)")


def bul(D, ad):
    """Adı (ya da son bileşeni) `ad` olan bildirimler: (dosya, satırlar, kesildi mi)."""
    son = ad.split(".")[-1]
    kal = re.compile(r"^\s*(?:@\[[^\]]*\]\s*)*" + ANAHTAR + r"\s+(?:[\w.']+\.)?" + re.escape(son) + r"(?![\w'.])")
    r = []
    for yol, L in D:
        for i, l in enumerate(L):
            if kal.match(l):
                j = i + 1
                while j < len(L) and j - i < 220 and not BAS.match(L[j]):
                    j += 1
                r.append((yol, L[i:j], j - i >= 220))
    return r


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    D = yukle(sys.argv[1])
    for ad in sys.argv[2:]:
        r = bul(D, ad)
        if not r:
            print(f"## {ad}\nNOT FOUND in the source.\n")
            continue
        for yol, blok, kesik in r[:2]:
            print(f"## {ad}   [{yol}, {len(blok)} lines{', CUT at 220' if kesik else ''}]")
            print("\n".join(blok) + "\n")
        if len(r) > 2:
            print(f"({len(r)} declarations match '{ad}'; showing 2. Use a more specific name.)\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
