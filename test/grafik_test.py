#!/usr/bin/env python3
"""Grafik araçlarının sınaması / Tests for the graph tools (koni.cpp, agac.cpp, karsila.cpp). Lean gerekmez.

TR: 1) Elle yazılmış küçük bir lean4export kaydı: koni → agac → karsila. Beklenen aksiyom listesi ve "nerede kuruluyor"
       sınıfları elle hesaplanmıştır.
    2) Rastgele bağımlılık grafikleri: agac.cpp'nin baskınlık ağacı ve alt ağaç toplamları, tanımdan kaba kuvvetle
       hesaplananla karşılaştırılır (X, Y'nin baskınıdır <=> X silinince Y köke bağlanamaz).
EN: 1) A hand-written tiny export through koni → agac → karsila, against hand-computed expectations.
    2) Random dependency graphs: agac.cpp's dominator tree and subtree sums against brute force from the definition.

Kullanım / usage: python3 test/grafik_test.py [tekrar=300]
"""
import json
import os
import random
import struct
import subprocess
import sys
import tempfile

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def derle(g, ad):
    x = os.path.join(g, ad)
    subprocess.run(["g++", "-O2", "-o", x, os.path.join(KOK, "arac", ad + ".cpp")], check=True)
    return x


def tsv(yol):
    R = [l.rstrip("\n").split("\t") for l in open(yol, encoding="utf-8")]
    return [dict(zip(R[0], r)) for r in R[1:]]


def kucuk_kayit(g, koni, agac, karsila):
    AD = ["Q", "H", ("H", "mk"), "G", "uses_H", "build", "root", "propext", "projAx", "unusedAx", "via_def", "uses_G", ("H", "rec"), "lonely"]
    no, L = {}, []
    for i, a in enumerate(AD, 1):
        if isinstance(a, tuple):
            L.append({"in": i, "str": {"pre": no[a[0]], "str": a[1]}})
            no[".".join(a)] = i
        else:
            L.append({"in": i, "str": {"pre": 0, "str": a}})
            no[a] = i
    E = []

    def e(d):
        E.append(d)
        return len(E) - 1

    def c(a):
        return e({"const": {"name": no[a], "us": []}})

    def bildir(tur, ad, tip, deger=None):
        nonlocal E
        for d in E[bildir.yazilan:]:
            L.append(dict({"ie": bildir.yazilan}, **d))
            bildir.yazilan += 1
        o = {"name": no[ad], "levelParams": [], "type": tip}
        if deger is not None:
            o["value"] = deger
        L.append({tur: o})
    bildir.yazilan = 0
    prop = e({"sort": 0})
    bildir("axiom", "propext", prop)
    bildir("axiom", "unusedAx", prop)
    bildir("def", "Q", prop, prop)
    q = c("Q")
    bildir("def", "G", prop, q)
    gk = c("G")
    bildir("axiom", "projAx", gk)
    h = c("H")
    for d in E[bildir.yazilan:]:
        L.append(dict({"ie": bildir.yazilan}, **d))
        bildir.yazilan += 1
    L.append({"inductive": {"types": [{"name": no["H"], "levelParams": [], "type": prop, "ctors": [no["H.mk"]]}],
                            "ctors": [{"name": no["H.mk"], "levelParams": [], "type": h}],
                            "recs": [{"name": no["H.rec"], "levelParams": [], "type": prop, "rules": [{"ctor": no["H.mk"], "nfields": 0, "rhs": q}]}]}})
    bildir("thm", "uses_H", e({"forallE": {"name": 0, "type": h, "body": q, "binderInfo": "default"}}), e({"lam": {"name": 0, "type": h, "body": q, "binderInfo": "default"}}))
    bildir("thm", "uses_G", e({"forallE": {"name": 0, "type": gk, "body": q, "binderInfo": "default"}}), e({"lam": {"name": 0, "type": gk, "body": q, "binderInfo": "default"}}))
    bildir("thm", "build", q, e({"app": {"fn": c("uses_H"), "arg": c("H.mk")}}))
    bildir("thm", "via_def", q, e({"app": {"fn": c("uses_G"), "arg": c("projAx")}}))
    bildir("thm", "root", q, e({"app": {"fn": e({"app": {"fn": c("build"), "arg": c("via_def")}}), "arg": c("propext")}}))
    bildir("thm", "lonely", q, c("unusedAx"))
    kayit = os.path.join(g, "kayit.ndjson")
    with open(kayit, "w") as f:
        for d in L:
            f.write(json.dumps(d, separators=(",", ":")) + "\n")
    env = dict(os.environ, KUNYE_KAPASITE="4096")
    k = os.path.join(g, "k")
    os.makedirs(k)
    with open(kayit, "rb") as f:
        subprocess.run([koni, os.path.join(g, "g.bin"), k], stdin=f, env=env, check=True, stderr=subprocess.DEVNULL)
    open(os.path.join(g, "kok.txt"), "w").write("root\n")
    open(os.path.join(g, "kut.txt"), "w").write("propext\n")
    subprocess.run([agac, f"{k}/dugum.tsv", f"{k}/kenar.bin", os.path.join(g, "kok.txt"), os.path.join(g, "kut.txt"), k], check=True, stderr=subprocess.DEVNULL)
    A = {r["ad"]: r for r in tsv(f"{k}/aksiyomlar.tsv")}
    assert set(A) == {"propext", "projAx", "unusedAx"}, A
    assert (A["propext"]["konide"], A["propext"]["kutuphane"]) == ("1", "1"), A
    assert (A["projAx"]["konide"], A["projAx"]["kutuphane"]) == ("1", "0"), A
    assert A["unusedAx"]["konide"] == "0", A
    O = json.load(open(f"{k}/ozet.json"))
    assert O["aksiyom_kayitta"] == 3 and sorted(O["aksiyom_konide"]) == ["projAx", "propext"], O
    open(os.path.join(g, "hedef.txt"), "w").write("H\nG\nOlmayan\n")
    subprocess.run([karsila, f"{k}/dugum.tsv", f"{k}/kenar.bin", os.path.join(g, "hedef.txt"), f"{k}/taslar.tsv", f"{k}/karsila.tsv"], check=True, stderr=subprocess.DEVNULL)
    R = {r["ad"]: r for r in tsv(f"{k}/karsila.tsv")}
    say = lambda r: tuple(int(r[x]) for x in ("kurucu", "tasiyan", "kuran", "kuran_t", "iceride", "kullanan"))
    assert R["H"]["tur"] == "i" and say(R["H"]) == (1, 1, 1, 0, 0, 1) and R["H"]["sonuc"] == "kuruluyor", R["H"]
    assert R["H"]["en_agir_kuran"].startswith("build"), R["H"]
    assert R["G"]["tur"] == "d" and say(R["G"]) == (0, 2, 0, 0, 0, 1) and R["G"]["sonuc"] == "iceride", R["G"]
    assert R["G"]["en_agir_kullanan"].startswith("via_def"), R["G"]
    assert R["Olmayan"]["sonuc"] == "kayitta_yok", R["Olmayan"]
    # rapor: aksiyom bölümü standart dışı aksiyomu işaretlemeli
    subprocess.run([sys.executable, "-I", os.path.join(KOK, "arac", "koni_rapor.py"), "--koni", k, "--md", f"{k}/KONI.md"], check=True, stdout=subprocess.DEVNULL)
    md = open(f"{k}/KONI.md", encoding="utf-8").read()
    bolum = md.split("## 1b. Aksiyomlar")[1].split("## 2.")[0]   # konide olmayan aksiyom bu bölümde listelenmemeli
    assert "| `projAx` | **standart dışı" in bolum and "| `propext` | standart" in bolum and "unusedAx" not in bolum, bolum
    print("küçük kayıt: aksiyom listesi, karşılama sınıfları ve rapor beklenenle aynı")


def kaba_kuvvet(n, kom, w):
    def eris(yasak):
        g, y = set(), [0] if yasak != 0 else []
        while y:
            x = y.pop()
            if x in g or x == yasak:
                continue
            g.add(x)
            y.extend(kom[x])
        return g
    koni = eris(-1)
    dom = {y: {y} for y in koni}
    for x in koni:
        for y in koni - eris(x):
            dom[y].add(x)
    idom = {}
    for y in koni:
        if y != 0:
            idom[y] = max(dom[y] - {y}, key=lambda x: len(dom[x]))   # en derindeki baskın
    alt = {x: [0, 0] for x in koni}
    for y in koni:
        for x in dom[y]:
            alt[x][0] += 1
            alt[x][1] += w[y]
    return koni, idom, alt


def rastgele(g, agac, tekrar):
    R = random.Random(20261126)
    for t in range(tekrar):
        n = R.randint(2, 45)
        p = R.choice([0.05, 0.12, 0.3])
        kom = [sorted(j for j in range(n) if j != i and (j > i or R.random() < 0.1) and R.random() < p) for i in range(n)]   # döngüler de olabilir
        w = [R.randint(0, 50) for _ in range(n)]
        with open(f"{g}/dugum.tsv", "w") as f:
            for i in range(n):
                f.write(f"{i}\tt\tn{i}\t{w[i]}\t1\t1\n")
        with open(f"{g}/kenar.bin", "wb") as f:
            f.write(struct.pack("<Q", n))
            for i in range(n):
                nt = R.randint(0, len(kom[i]))
                f.write(struct.pack("<II", nt, len(kom[i]) - nt) + struct.pack(f"<{len(kom[i])}I", *kom[i]))
        open(f"{g}/kok.txt", "w").write("n0\n")
        c = f"{g}/c"
        os.makedirs(c, exist_ok=True)
        subprocess.run([agac, f"{g}/dugum.tsv", f"{g}/kenar.bin", f"{g}/kok.txt", "-", c], check=True, stderr=subprocess.DEVNULL)
        T = {int(r["ad"][1:]): r for r in tsv(f"{c}/taslar.tsv")}
        koni, idom, alt = kaba_kuvvet(n, kom, w)
        assert set(T) == koni, (t, sorted(T), sorted(koni))
        for y in koni:
            bek = "<kok>" if y == 0 else f"n{idom[y]}"
            assert T[y]["baskin"] == bek, (t, y, T[y]["baskin"], bek)
            assert (int(T[y]["alt_sayi"]), int(T[y]["alt_agirlik"])) == tuple(alt[y]), (t, y, T[y], alt[y])
    print(f"rastgele grafik: {tekrar} grafikte baskınlık ağacı ve alt ağaç toplamları kaba kuvvetle aynı")


if __name__ == "__main__":
    tekrar = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    with tempfile.TemporaryDirectory() as g:
        koni, agac, karsila = derle(g, "koni"), derle(g, "agac"), derle(g, "karsila")
        kucuk_kayit(g, koni, agac, karsila)
        rastgele(g, agac, tekrar)
