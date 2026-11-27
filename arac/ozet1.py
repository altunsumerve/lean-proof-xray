#!/usr/bin/env python3
"""Tek sayfalık özet / One-page summary — öteki araçların çıktılarından derlenir; kendi cümlesi yoktur.

TR: belge.py (kanıtlanan cümle, adım tablosu, sayılar), varsayim.py (taşınan önermeler) ve sozluk.py (kavram
    derinlikleri) çalıştırılır; çıktılarının ilgili bölümleri sabit başlıklar altında art arda konur.
EN: Stitches sections of the other tools' outputs under fixed headings. Adds no sentences of its own beyond headings.
"""
import argparse
import os
import subprocess
import sys
import tempfile

B = {"tr": ["# Tek sayfalık özet: {kok}", "## A. Kanıtlanan cümle", "## B. İspatın ilk adımları", "## C. Varsayım olarak taşınan önermeler (en ağır 10)",
            "## D. Ana ara önermelerin tanım derinliği", "## E. Sayılar", "## F. Nasıl tekrar üretilir",
            "Resmi Lean dışa aktarımı → `arac/koni.cpp` (bağımlılık grafiği) → `arac/agac.cpp` (baskınlık ağacı) → `kitapcik/Dok.lean` (terim dökümü) → "
            "`arac/belge.py`, `arac/sozluk.py`, `arac/mantik.py`, `arac/varsayim.py`. Hiçbir adımda yapay zekâ çalışmaz; aynı girdi bayt bayt aynı çıktıyı verir. "
            "Ayrıntılı belgeler: `CIKTI`, `KOPRU`, `MANTIK`, `VARSAYIM`, `SOZLUK`."],
     "en": ["# One-page summary: {kok}", "## A. The statement proved", "## B. First steps of the proof", "## C. Statements carried as hypotheses (10 heaviest)",
            "## D. Definition depth of the main intermediate statements", "## E. Numbers", "## F. How to reproduce",
            "Official Lean export → `arac/koni.cpp` (dependency graph) → `arac/agac.cpp` (dominator tree) → `kitapcik/Dok.lean` (term dump) → "
            "`arac/belge.py`, `arac/sozluk.py`, `arac/mantik.py`, `arac/varsayim.py`. No AI runs at any step; the same input gives byte-identical output. "
            "Detailed documents: `CIKTI`, `KOPRU`, `MANTIK`, `VARSAYIM`, `SOZLUK`."]}


def bolum(L, bas, son=None):
    """bas ile başlayan satırdan sonraki, son ile başlayan satıra kadarki satırlar."""
    i = next(k for k, x in enumerate(L) if x.startswith(bas)) + 1
    j = next((k for k in range(i, len(L)) if son and L[k].startswith(son)), len(L))
    return [x for x in L[i:j]]


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--kok", default="durum")
    a.add_argument("--dok", required=True)
    a.add_argument("--dil", default="tr")
    a.add_argument("--ad", action="append", default=[], help="derinliği yazılacak ara önermeler")
    a.add_argument("--cikti", required=True)
    A = a.parse_args()
    H = os.path.dirname(os.path.abspath(__file__))
    T = tempfile.mkdtemp()

    def kos(betik, *arg):
        subprocess.run([sys.executable, f"{H}/{betik}", "--dok", A.dok, "--dil", A.dil, *arg], check=True, stdout=subprocess.DEVNULL)

    kos("belge.py", "--kok", A.kok, "--adim", "4", "--cikti", f"{T}/c.md")
    kos("varsayim.py", "--kok", A.kok, "--en-cok", "10", "--cikti", f"{T}/v.md")
    ads = []
    for n in A.ad:
        ads += ["--ad", n]
    kos("sozluk.py", *ads, "--derin", "0", "--cikti", f"{T}/s.md")
    C = open(f"{T}/c.md", encoding="utf-8").read().split("\n")
    V = open(f"{T}/v.md", encoding="utf-8").read().split("\n")
    S = open(f"{T}/s.md", encoding="utf-8").read().split("\n")
    b = B[A.dil]
    kok = C[0].split(": ", 1)[1] if ": " in C[0] else ""
    L = [b[0].format(kok=kok), "", C[2], "", b[1], ""]
    L += [x for x in bolum(C, "## 1.", "## 2.") if x.strip()]
    L += ["", b[2], ""]
    L += [x for x in bolum(C, "## 2.", "**") if x.startswith("|")]
    L += ["", b[3], "", V[4], ""] + [x for x in V if x.startswith("|")]
    L += ["", b[4], ""] + [x for x in S if x.startswith("|")]
    L += ["", b[5], ""] + [x for x in bolum(C, "## 4.", "## 5.") if x.startswith("|")]
    L += ["", b[6], "", b[7]]
    open(A.cikti, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(len(" ".join(L).split()), "kelime")


if __name__ == "__main__":
    main()
