#!/usr/bin/env python3
"""denetle — bir hikâyeyi haritaya karşı denetler / checks a story against the map. No AI; same input, same output.

Story format: prose with the names of proof steps in `backticks`, then a section "## Claims" with lines of three kinds:
  - STEP `Name`              the proof has a step with this name
  - UNDER `A` `B`            B exists only for A (B is in A's subtree of the dominator tree)
  - SHARE `Name` 55.7        Name carries this percentage of the proof (tolerance: one point)
Reports: names in the prose that are not steps of the proof; each claim confirmed or wrong; and heavy steps
(share >= 10% and not a mere wrapper around one child) that the story never mentions.
What it does NOT check: the mathematical reading in the prose. It checks that the story is about this proof's real
steps, in their real places, with their real weights.
With a questions file (from sorular.py) it also checks that the story has a section "## Answers to the required
questions" with one line "- Qn: ..." for every question, and counts the ones answered NOT FOUND.
Usage: denetle.py <result folder> story.md [questions.md]      (exit code 1 if anything is wrong or missing)"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harita  # noqa: E402


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    T, top = harita.agac(sys.argv[1])
    pay = lambda n: 100 * int(T[n]["alt_agirlik"]) / top
    son = {}
    for n in T:
        son.setdefault(n.split(".")[-1], []).append(n)
    coz = lambda a: harita.coz(T, a, son)
    s = open(sys.argv[2], encoding="utf-8").read()
    govde, _, iddia = s.partition("## Claims")
    adlar = sorted(set(re.findall(r"`([^`\s]+)`", govde.split("## Answers to the required questions")[0] + govde.partition("## Answers to the required questions")[2])))
    yok = [a for a in adlar if not coz(a)]
    ok = yanlis = 0
    satirlar = []
    for l in iddia.splitlines():
        m = re.match(r"\s*-\s*(STEP|UNDER|SHARE)\s+(.*)", l)
        if not m:
            continue
        t, ns = m.group(1), re.findall(r"`([^`]+)`", m.group(2))
        c = [coz(x) for x in ns]
        if not c or any(x is None for x in c) or (t == "UNDER" and len(c) != 2):
            iyi, sonuc = False, "NOT IN MAP"
        elif t == "STEP":
            iyi, sonuc = True, f"ok ({pay(c[0]):.1f}%)"
        elif t == "UNDER":
            x, zincir = c[1], set()
            while x in T and x not in zincir:
                zincir.add(x)
                x = T[x]["baskin"]
            iyi = c[0] in zincir and c[0] != c[1]
            sonuc = "ok" if iyi else f"WRONG (`{ns[1]}` exists only for `{T[c[1]]['baskin']}`)"
        else:
            v = re.search(r"([\d.]+)\s*%?\s*$", m.group(2))
            iyi = bool(v) and abs(float(v.group(1)) - pay(c[0])) <= 1.0
            sonuc = "ok" if iyi else f"WRONG (measured {pay(c[0]):.1f}%)"
        ok += iyi
        yanlis += not iyi
        satirlar.append(f"{sonuc:<44} {l.strip()}")
    cocuk = {}
    for n, d in T.items():
        cocuk.setdefault(d["baskin"], []).append(n)
    anilan = {coz(a) for a in adlar if coz(a)}
    eksik = []
    for n in sorted(T, key=lambda n: (-int(T[n]["alt_agirlik"]), n)):
        if pay(n) < 10:
            break
        enb = max((int(T[c]["alt_agirlik"]) for c in cocuk.get(n, [])), default=0)
        if enb < 0.97 * int(T[n]["alt_agirlik"]) and n not in anilan:
            eksik.append(f"{pay(n):.1f}% {n}")
    cevapsiz, bulunamadi, nq = [], [], 0
    if len(sys.argv) > 3:
        qs = re.findall(r"\*\*Q(\d+)\.\*\*", open(sys.argv[3], encoding="utf-8").read())
        nq = len(qs)
        cv = s.partition("## Answers to the required questions")[2].split("\n## ")[0]
        for q in qs:
            m = re.search(r"^\s*-\s*\**Q" + q + r"\b[.:*\s]*(.*)$", cv, flags=re.M)
            if not m or len(m.group(1).strip()) < 20:
                cevapsiz.append("Q" + q)
            elif "NOT FOUND" in m.group(1):
                bulunamadi.append("Q" + q)
    print(f"names in the story: {len(adlar)}; steps of the proof: {len(adlar) - len(yok)}; NOT steps of the proof: {len(yok)} {yok[:12]}")
    print(f"claims: {ok + yanlis}; confirmed {ok}; wrong {yanlis}")
    for x in satirlar:
        print("  " + x)
    print(f"heavy steps (>=10%, not mere wrappers) the story never mentions: {len(eksik)}")
    for x in eksik[:15]:
        print("  " + x)
    if nq:
        print(f"required questions: {nq}; answered {nq - len(cevapsiz) - len(bulunamadi)}; answered NOT FOUND {len(bulunamadi)} {bulunamadi}; missing {len(cevapsiz)} {cevapsiz}")
    return 1 if (yok or yanlis or eksik or cevapsiz or ok + yanlis == 0) else 0


if __name__ == "__main__":
    sys.exit(main())
