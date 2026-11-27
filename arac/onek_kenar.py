#!/usr/bin/env python3
"""Önek kenarı — adı A önekiyle başlayan bildirimlerden adı B önekiyle başlayanlara giden bağımlılık kenarlarını sayar.
TR: "A kısmı B kısmından hiçbir şey kullanmıyor" türü iddiaları kayıttan denetlemek için. Yalnızca sayar.
EN: Counts dependency edges from declarations named A.* to declarations named B.*; checks claims like "A uses nothing from B".
Kullanım: onek_kenar.py dugum.tsv kenar.bin A. B. [cikti.txt]
"""
import struct
import sys


def main():
    dugum, kenar, A, B = sys.argv[1:5]
    ad = [l.split("\t")[2] for l in open(dugum, encoding="utf-8")]
    a = [n.startswith(A) for n in ad]
    b = [n.startswith(B) for n in ad]
    say, ornek, na, nb = 0, [], sum(a), sum(b)
    with open(kenar, "rb") as f:
        (n,) = struct.unpack("<Q", f.read(8))
        for i in range(n):
            nt, nv = struct.unpack("<II", f.read(8))
            ks = struct.unpack(f"<{nt + nv}I", f.read(4 * (nt + nv))) if nt + nv else ()
            if a[i]:
                for k in ks:
                    if b[k]:
                        say += 1
                        if len(ornek) < 10:
                            ornek.append(f"{ad[i]} -> {ad[k]}")
    L = [f"{A}* bildirimi: {na}", f"{B}* bildirimi: {nb}", f"{A}* -> {B}* kenarı: {say}"] + ornek
    print("\n".join(L))
    if len(sys.argv) > 5:
        open(sys.argv[5], "w", encoding="utf-8").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
