#!/usr/bin/env python3
"""sorular — anlatıcının ikinci turda cevaplamak ZORUNDA olduğu sorular / the questions the narrator MUST answer in round 2.

No AI: the questions are derived by fixed rules from the map and from the junction's own statement.
  junction  = the heaviest theorem whose share is below 99% (the first place where the proof stops being one chain)
  parent    = the step the junction exists only for
  quantities= the defined names that occur in the junction's statement
  branches  = the theorems directly under the junction with a share of at least 5%
Why: without required questions a narrator stops at the skeleton. Two independent narrators agreed on the skeleton of
the same proof, but only the one who was asked these questions reached the mechanism.
Usage: sorular.py <result folder> <source root>  > questions.md"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harita  # noqa: E402
import kaynak  # noqa: E402

TANIM = re.compile(r"^\s*(?:@\[[^\]]*\]\s*)*(?:(?:private|protected|noncomputable|unsafe|partial|nonrec)\s+)*(?:def|abbrev|structure|class|inductive)\s")


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    T, top = harita.agac(sys.argv[1])
    D = kaynak.yukle(sys.argv[2])
    pay = lambda n: 100 * int(T[n]["alt_agirlik"]) / top
    sirali = sorted(T, key=lambda n: (-int(T[n]["alt_agirlik"]), n))
    j = next((n for n in sirali if T[n]["tur"] == "t" and pay(n) < 99.0), None)
    if j is None:
        print("No junction found.")
        return 1
    ust = T[j]["baskin"]
    dallar = [n for n in sirali if T[n]["baskin"] == j and T[n]["tur"] == "t" and pay(n) >= 5.0]
    # kavşağın önermesinde geçen, kaynakta tanım olarak bulunan adlar (yazıldıkları sırayla, en çok 8)
    nicelik = []
    b = kaynak.bul(D, j)
    if b:
        imza = " ".join(b[0][1]).split(":=")[0]
        for tok in re.findall(r"[A-Za-z_][\w']*(?:\.[A-Za-z_][\w']*)*", imza):
            ad = tok.split(".")[-1]
            if ad in nicelik or ad == j.split(".")[-1] or len(ad) < 2 and "." not in tok:
                continue
            if any(TANIM.match(blok[0]) for _, blok, _ in kaynak.bul(D, ad)):
                nicelik.append(ad)
    nicelik = nicelik[:8]
    S, k = [], 0

    def soru(t):
        nonlocal k
        k += 1
        S.append(f"- **Q{k}.** {t}")
    for ad in nicelik:
        soru(f"What is {ad} (open its definition)? Which step of the proof produces it or bounds it, and by what mechanism? Follow the code at least two levels below that step.")
    if ust in T:
        soru(f"In `{ust}`, how is `{j}` turned into the conclusion? Which parameters are chosen there, how large is each relative to the main variable, and why does that choice give the bound in the statement of `{ust}`?")
    soru(f"When the parts of `{j}` are combined, what cancels, and what is left?")
    soru("Is anything in the construction repeated a variable number of times (a chain, an iteration, a tower)? If so: what is repeated, how many times, what does each repetition contribute, and why is that number of repetitions the right one?")
    for d in dallar:
        soru(f"Where is `{d}` consumed (which declaration calls it), and what does it contribute to `{j}`?")
    print(f"# Required questions\n\nJunction: `{j}` ({pay(j):.1f}% of the proof). Answer every question from code you read. "
          "If you cannot answer one after looking, write NOT FOUND and say where you looked.\n")
    print("\n".join(S))
    return 0


if __name__ == "__main__":
    sys.exit(main())
