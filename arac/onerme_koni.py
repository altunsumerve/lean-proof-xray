#!/usr/bin/env python3
"""Önerme konisi / Statement cone — verilen adımların önermelerini okumak için gereken proje bildirimleri.

TR: Tam grafikten (koni.cpp çıktısı) hesaplanır, kayıt yeniden akıtılmaz. Kural kapanis.cpp ile aynıdır: teoremde yalnızca
    önerme (tip kenarları), tanım/yapı/kurucuda her şey izlenir. Kütüphane adları verilirse onlara girilmez.
    Çıktı ayikla.cpp'ye ad listesi olur: böylece adımların cümlelerinde geçen kavramların TANIMLARI da dökülür.
EN: From the full graph, the project declarations needed to read the statements of the given steps (theorems contribute
    their type only, definitions everything; library names are not entered). Used as the name list for the term dump.
Kullanım / usage: onerme_koni.py dugum.tsv kenar.bin kokler.txt kutuphane.txt|- > adlar.txt
"""
import array
import struct
import sys


def main():
    dugum, kenar, kokler, kut = sys.argv[1:5]
    ad, tur = [], []
    for l in open(dugum, encoding="utf-8"):
        p = l.rstrip("\n").split("\t")
        if len(p) >= 3:
            tur.append(p[1])
            ad.append(p[2])
    N = len(ad)
    sira = {}
    for i, n in enumerate(ad):
        sira.setdefault(n, i)
    kutuphane = set()
    if kut != "-":
        kutuphane = {sira[x] for x in (l.rstrip("\n") for l in open(kut, encoding="utf-8")) if x in sira}
    bas, tip_son, K = array.array("Q"), array.array("Q"), array.array("I")
    with open(kenar, "rb") as f:
        assert struct.unpack("<Q", f.read(8))[0] == N, "dugum/kenar sayısı uyuşmuyor"
        for _ in range(N):
            nt, nv = struct.unpack("<II", f.read(8))
            bas.append(len(K))
            tip_son.append(len(K) + nt)
            if nt + nv:
                K.frombytes(f.read(4 * (nt + nv)))
    bas.append(len(K))
    gor, yigin = set(), []
    for l in open(kokler, encoding="utf-8"):
        x = sira.get(l.rstrip("\n"))
        if x is not None and x not in gor:
            gor.add(x)
            yigin.append(x)
    while yigin:
        x = yigin.pop()
        son = tip_son[x] if tur[x] == "t" else bas[x + 1]
        for k in range(bas[x], son):
            z = K[k]
            if z not in gor and z not in kutuphane:
                gor.add(z)
                yigin.append(z)
    sys.stdout.write("".join(ad[i] + "\n" for i in sorted(gor)))
    print(f"önerme konisi: {len(gor)} bildirim", file=sys.stderr)


if __name__ == "__main__":
    main()
