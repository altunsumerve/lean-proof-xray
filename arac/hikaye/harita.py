#!/usr/bin/env python3
"""harita — haritada bir adımı aç / open a step of the map. No AI; reads taslar_ust.tsv only.
Usage: harita.py <result folder> --top N            the N heaviest steps of the proof
       harita.py <result folder> --search TEXT      names containing TEXT
       harita.py <result folder> NAME [NAME ...]    share, the step it exists only for, heaviest parts directly under it
"Share" = the part of the proof that exists only for that step (subtree weight in the dominator tree). Not importance."""
import sys


def agac(klasor):
    T, bas = {}, None
    for l in open(f"{klasor}/taslar_ust.tsv", encoding="utf-8"):
        f = l.rstrip("\n").split("\t")
        if bas is None:
            bas = f
            continue
        T[f[0]] = dict(zip(bas, f))
    top = max((int(d["alt_agirlik"]) for d in T.values()), default=1) or 1
    return T, top


def coz(T, a, son=None):
    """Tam ad ya da tek anlamlı son bileşen."""
    if a in T:
        return a
    if son is None:
        son = {}
        for n in T:
            son.setdefault(n.split(".")[-1], []).append(n)
    c = son.get(a, [])
    return c[0] if len(c) == 1 else None


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    T, top = agac(sys.argv[1])
    args = sys.argv[2:]
    pay = lambda n: f"{100 * int(T[n]['alt_agirlik']) / top:.1f}%"
    cocuk = {}
    for n, d in T.items():
        cocuk.setdefault(d["baskin"], []).append(n)
    if args[0] == "--top":
        for n in sorted(T, key=lambda n: (-int(T[n]["alt_agirlik"]), n))[:int(args[1]) if len(args) > 1 else 30]:
            print(f"{pay(n):>7}  {n}   (kind {T[n]['tur']}; exists only for: {T[n]['baskin']})")
        return 0
    if args[0] == "--search":
        r = sorted((n for n in T if args[1].lower() in n.lower()), key=lambda n: (-int(T[n]["alt_agirlik"]), n))
        for n in r[:40]:
            print(f"{pay(n):>7}  {n}")
        print(f"({len(r)} names among the heaviest steps contain '{args[1]}')")
        return 0
    son = {}
    for n in T:
        son.setdefault(n.split(".")[-1], []).append(n)
    for a in args:
        n = coz(T, a, son)
        if n is None:
            c = son.get(a, [])
            print(f"## {a}\n" + (f"AMBIGUOUS: {len(c)} steps end in this name: {', '.join(c[:6])}" if c else "NOT among the heaviest steps of this proof (a definition, a small step, or not in the proof).") + "\n")
            continue
        print(f"## {n}\nshare of the proof: {pay(n)}   exists only for: {T[n]['baskin']}   declarations under it: {T[n]['alt_sayi']}")
        cs = sorted(cocuk.get(n, []), key=lambda c: (-int(T[c]["alt_agirlik"]), c))
        if cs:
            print("heaviest parts directly under it:")
            for c in cs[:10]:
                print(f"  {pay(c):>7}  {c}  ({T[c]['tur']})")
            if len(cs) > 10:
                print(f"  ... and {len(cs) - 10} smaller ones among the heaviest steps")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
