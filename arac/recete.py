#!/usr/bin/env python3
"""Reçete / Recipe — "bu kod hangi adlandırılmış sonuçları, hangi sırayla birleştiriyor" tek belgede.
TR: Öteki araçların çıktılarını sabit başlıklar altında birleştirir; kendi cümlesi yoktur.
EN: Stitches the other tools' outputs under fixed headings; adds no sentences of its own.
Kullanım: recete.py --kok durum --dok durum/dok.jsonl.gz --dil tr --kok-onerme UpperTheory.EveryCharacter --cikti RECETE_tr.md
"""
import argparse
import os
import subprocess
import sys
import tempfile

B = {"tr": ["# İspatın reçetesi: {kok}", "## 1. Varılan sonuç", "## 2. Adımlar ve ağırlıkları", "## 3. Birleşim: hangi önerme hangilerinden çıkıyor",
            "## 4. Malzemeler: kodun \"yayımlanmış sonuç\" diye etiketlediği önermeler",
            "Ad, kodun verdiği addır; cümle, kodun yazdığı önermedir. İkisinin literatürdeki teoremle örtüşüp örtüşmediğine bu belge hüküm vermez.",
            "## 5. Sayılar"],
     "en": ["# The recipe of the proof: {kok}", "## 1. The result reached", "## 2. Steps and their weights", "## 3. Assembly: which statement follows from which",
            "## 4. Ingredients: statements the code labels as \"published results\"",
            "The name is the code's name; the sentence is the statement the code writes. This document does not judge whether they match the theorem in the literature.",
            "## 5. Numbers"]}


def bolum(L, bas, son=None):
    i = next(k for k, x in enumerate(L) if x.startswith(bas)) + 1
    j = next((k for k in range(i, len(L)) if son and L[k].startswith(son)), len(L))
    return L[i:j]


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--kok", default="durum")
    a.add_argument("--dok", required=True)
    a.add_argument("--dil", default="tr")
    a.add_argument("--kok-onerme", required=True)
    a.add_argument("--cikti", required=True)
    A = a.parse_args()
    H, T = os.path.dirname(os.path.abspath(__file__)), tempfile.mkdtemp()

    def kos(betik, *arg):
        subprocess.run([sys.executable, f"{H}/{betik}", "--kok", A.kok, "--dok", A.dok, "--dil", A.dil, *arg], check=True, stdout=subprocess.DEVNULL)

    kos("belge.py", "--adim", "8", "--cikti", f"{T}/c.md")
    kos("mantik.py", "--kok-onerme", A.kok_onerme, "--en-cok", "60", "--cikti", f"{T}/m.md")
    kos("varsayim.py", "--etiketli", "--cikti", f"{T}/v.md")
    C, Mm, V = (open(f"{T}/{x}.md", encoding="utf-8").read().split("\n") for x in "cmv")
    b = B[A.dil]
    L = [b[0].format(kok=C[0].split(": ", 1)[1] if ": " in C[0] else ""), "", C[2], "", b[1], ""]
    L += [x for x in bolum(C, "## 1.", "## 2.") if x.strip()]
    L += ["", b[2], ""] + [x for x in bolum(C, "## 2.", "**") if x.startswith("|")]
    L += ["", b[3], ""] + Mm[2:]
    L += ["", b[4], "", b[5], "", V[4], ""] + V[6:]
    L += ["", b[6], ""] + [x for x in bolum(C, "## 4.", "## 5.") if x.startswith("|")]
    open(A.cikti, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(len(" ".join(L).split()), "kelime")


if __name__ == "__main__":
    main()
