#!/usr/bin/env python3
"""Alanlar / Fields — kütüphane ad alanlarından matematik alanına sabit tablo ve adım başına ayırt edicilik hesabı.

TR: `alan.cpp` her adımın altında her kütüphane ad alanının kaç kez kullanıldığını sayar. Burada ad alanları sabit bir
    tabloyla matematik alanlarına toplanır ve her adım için "yoğunluk" hesaplanır:
      yoğunluk = (alanın adımdaki payı) / (alanın bütün projedeki payı).
    Yoğunluk 1 ise adım o alanı proje ortalaması kadar kullanıyor; 5 ise beş kat yoğun. Tabloda olmayan ad alanı sayılmaz.
EN: Fixed table from Mathlib namespaces to mathematical fields, and per-step concentration (share in the step's
    subtree divided by share in the whole project). Counting only.
"""
import collections
import gzip

TABLO = {
    "modüler formlar|modular forms": ["CongruenceSubgroup", "CuspForm", "ModularGroup", "SlashAction", "UpperHalfPlane", "ModularForm", "EisensteinSeries", "SlashInvariantForm"],
    "homolojik cebir|homological algebra": ["CochainComplex", "DerivedCategory", "SimplexCategory", "ComplexShape", "HomologicalComplex", "ChainComplex", "HomotopyCategory"],
    "cebirsel geometri|algebraic geometry": ["AlgebraicGeometry", "PrimeSpectrum", "ProjectiveSpectrum"],
    "kategori teorisi|category theory": ["CategoryTheory"],
    "sayı cisimleri|number fields": ["NumberField", "IsDedekindDomain", "ClassGroup", "IsCyclotomicExtension"],
    "eliptik eğriler|elliptic curves": ["WeierstrassCurve", "PeriodPair"],
    "kuvvet serileri|power series": ["PowerSeries", "LaurentSeries", "HahnSeries", "HahnModule"],
    "Young diyagramları ve bileşimler|Young diagrams and compositions": ["YoungDiagram", "Composition"],
    "kuadratik ve kuaterniyon cebirleri|quadratic and quaternion algebras": ["QuadraticAlgebra", "QuaternionAlgebra", "Quaternion", "QuadraticForm"],
    "ölçü ve integral|measure and integration": ["MeasureTheory", "intervalIntegral", "circleIntegral"],
    "diferansiyel formlar|differential forms": ["ContinuousAlternatingMap", "extDeriv"],
    "yerel haritalar ve manifoldlar|local charts and manifolds": ["PartialHomeomorph", "OpenPartialHomeomorph", "PartialEquiv", "ChartedSpace", "ModelWithCorners"],
    "p-adik sayılar|p-adic numbers": ["Padic", "PadicInt", "IsUltrametricDist", "padicValNat", "padicValInt", "padicValRat"],
    "analitik sayı teorisi|analytic number theory": ["DirichletCharacter", "ArithmeticFunction", "LSeries", "riemannZeta", "jacobiSym", "legendreSym"],
    "sonlu cisimler|finite fields": ["GaloisField", "FiniteField"],
    "Galois teorisi|Galois theory": ["krullTopology", "IsGalois", "IntermediateField"],
    "çok doğrusal cebir|multilinear algebra": ["MultilinearMap", "AlternatingMap", "TensorProduct", "ExteriorAlgebra"],
    "karmaşık analiz|complex analysis": ["Complex", "DifferentiableOn", "AnalyticAt", "MeromorphicAt"],
    "temsil teorisi|representation theory": ["Representation", "Action", "Rep", "FDRep", "MonoidAlgebra"],
}


def yukle(yol):
    R, T = collections.defaultdict(dict), {}
    with gzip.open(yol, "rt", encoding="utf-8") as f:
        for l in f:
            h, k, a, b = l.rstrip("\n").split("\t")
            if k == "<toplam>":
                T[h] = int(a)
            else:
                R[h][k] = (int(a), int(b))
    return R, T


def yogunluk(R, T, h, dil="tr", esik=2.0, en_az=300):
    """Adım h için (alan adı, yoğunluk, sayı) listesi; yoğunluk ≥ esik ve sayı ≥ en_az olanlar, yoğunluğa göre."""
    if h not in T or not T[h]:
        return []
    G, L = T["<hepsi>"], []
    for alan, adlar in TABLO.items():
        a = sum(R[h].get(n, (0, 0))[0] for n in adlar)
        b = sum(R["<hepsi>"].get(n, (0, 0))[0] for n in adlar)
        if a >= en_az and b:
            y = (a / T[h]) / (b / G)
            if y >= esik:
                L.append((alan.split("|")[0 if dil == "tr" else 1], y, a))
    L.sort(key=lambda x: (-x[1], x[0]))
    return L
