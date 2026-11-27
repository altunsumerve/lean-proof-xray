#!/usr/bin/env python3
"""duz.py sınaması: belirsizlik yok mu?
TR: Rastgele mantık iskeletleri üretir (her, vardır, ise, ve, veya, değil, ancak-ve-ancak) ve iki FARKLI iskeletin
    aynı cümleye çevrilmediğini denetler. Aynı cümle = belirsizlik = hata.
EN: Random logical skeletons; checks that two different skeletons never render to the same sentence."""
import json
import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "arac"))
import duz  # noqa: E402

BAG = {"And": "ee", "Or": "ee", "Not": "e", "Iff": "ee", "Exists": "ie", "P": "e", "Q": "ee", "A": "", "B": "", "C": ""}


def atom(r, derinlik):
    if derinlik == 0 or r.random() < 0.4:
        return ["c", r.choice("ABC")]
    if r.random() < 0.5:
        return ["a", ["c", "P"], ["b", r.randrange(derinlik)]]
    return ["a", ["c", "Q"], ["b", r.randrange(derinlik)], ["b", r.randrange(derinlik)]]


def uret(r, n, derinlik):
    """n: kalan düğüm bütçesi; derinlik: bağlı değişken sayısı"""
    if n <= 0:
        return atom(r, derinlik)
    k = r.choice(["her", "ise", "ve", "veya", "degil", "var", "ancak", "atom"])
    if k == "atom":
        return atom(r, derinlik)
    if k == "her":
        g = uret(r, n - 1, derinlik + 1)
        # bağımlı olması için değişkeni kullanan bir atomla birleştir
        return ["p", "x", "e", ["c", "Nat"], ["a", ["c", "And"], ["a", ["c", "P"], ["b", 0]], g]]
    if k == "ise":
        a = uret(r, n // 2, derinlik)
        g = uret(r, n // 2, derinlik + 1)
        return ["p", "h", "e", a, kaydir_kontrol(g)]
    if k in ("ve", "veya", "ancak"):
        return ["a", ["c", {"ve": "And", "veya": "Or", "ancak": "Iff"}[k]], uret(r, n // 2, derinlik), uret(r, n // 2, derinlik)]
    if k == "degil":
        return ["a", ["c", "Not"], uret(r, n - 1, derinlik)]
    g = uret(r, n - 1, derinlik + 1)
    return ["a", ["c", "Exists"], ["c", "Nat"], ["l", "y", "e", ["c", "Nat"], ["a", ["c", "And"], ["a", ["c", "P"], ["b", 0]], g]]]


def kullanir(e, k):
    if e[0] == "b":
        return e[1] == k
    if e[0] in ("l", "p"):
        return kullanir(e[3], k) or kullanir(e[4], k + 1)
    if e[0] == "a":
        return any(kullanir(x, k) for x in e[1:])
    return False


def kaydir_kontrol(g):
    return g


def main():
    r = random.Random(7)
    for dil in ("tr", "en"):
        C = duz.Duz(BAG, dil)
        gorulen, say, atla = {}, 0, 0
        for _ in range(60000):
            e = uret(r, r.randrange(1, 7), 0)
            # "ise" gövdesinde 0 numaralı değişken (varsayımın kendisi) kullanılmamalı; kullanılıyorsa örneği atla
            def gecerli(x):
                if x[0] == "p" and x[1] == "h" and kullanir(x[4], 0):
                    return False
                return all(gecerli(y) for y in x[1:] if isinstance(y, list))
            if not gecerli(e):
                atla += 1
                continue
            s = C.cumle(e)
            k = json.dumps(e)
            if s in gorulen and gorulen[s] != k:
                print("BELİRSİZLİK / AMBIGUITY", dil)
                print(" ", s)
                print(" ", gorulen[s])
                print(" ", k)
                return 1
            gorulen[s] = k
            say += 1
        print(dil, "örnek", say, "farklı cümle", len(gorulen), "atlanan", atla)
    # fonksiyon tipi önerme değildir: "eğer ℕ ise ℕ" yazılmamalı
    import sozel
    B = sozel.Bag(BAG)
    B.onerme = {"And", "Or", "Not", "Iff", "Exists", "P", "Q", "A", "B", "C"}
    C = duz.Duz(B, "en")
    s1 = C.cumle(["p", "x", "e", ["c", "Nat"], ["c", "Nat"]])
    s2 = C.cumle(["p", "h", "e", ["c", "A"], ["c", "B"]])
    s3 = C.cumle(["p", "f", "e", ["p", "x", "e", ["c", "Nat"], ["s", "Prop"]], ["p", "h", "e", ["a", ["b", 0], ["n", 3]], ["c", "A"]]])
    # tipi önerme olmayan bağımsız argüman bir nesnedir: "for every", "if" değil
    s4 = C.cumle(["p", "g", "e", ["c", "Nat"], ["c", "A"]])
    if "if" in s4.lower() or "for every" not in s4.lower():
        print("NESNE ARGÜMANI HATASI", s4)
        return 1
    if "if" in s1 or s2 != "If A then B." or "if f(3) then A" not in s3:
        print("FONKSİYON TİPİ HATASI", s1, "|", s2, "|", s3)
        return 1
    print("TAMAM")
    return 0


if __name__ == "__main__":
    sys.exit(main())
