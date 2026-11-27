#!/usr/bin/env python3
"""Düz / Plain — önermeleri kurallı biçimde düz cümleye çevirir.

TR: `sozel.py` terimleri sembollerle yazar. Bu katman önermenin mantık iskeletini (her, vardır, ise, ve, veya, değil)
    sabit kalıplarla cümleye döker; iskeletin altındaki formüller `sozel.py` ile aynen yazılır. Yapay zekâ yoktur;
    aynı girdi aynı cümleyi verir. Kalıplar aşağıdaki tablolardadır ve belgenin sonunda listelenebilir.
EN: Renders the logical skeleton of a statement (for every, exists, if-then, and, or, not) with fixed sentence
    templates; formulas below the skeleton are printed by `sozel.py` unchanged. Rule-based, deterministic.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sozel  # noqa: E402

KALIP = {
    "tr": {"her": "her {b} için: {g}", "ise": "eğer {v} ise {s}", "ve": " ve ", "veya": " veya ",
           "degil": "{a} doğru değildir", "yok": "hiçbir {b} için {g} doğru olmaz", "var": "öyle bir {b} vardır ki {g}",
           "ancak": "{a} ancak ve ancak {b}", "ayrac": ", ", "ile": "{b} ({k})", "son_ve": " ve "},
    "en": {"her": "for every {b}: {g}", "ise": "if {v} then {s}", "ve": " and ", "veya": " or ",
           "degil": "it is not the case that {a}", "yok": "there is no {b} such that {g}",
           "var": "there exists {b} such that {g}", "ancak": "{a} if and only if {b}", "ayrac": ", ",
           "ile": "{b} ({k})", "son_ve": " and "},
}
# tip başı -> ad öbeği ({0}, {1}: açık argümanlar)
TIP_SOZ = {
    "tr": {"DirichletCharacter": "{1} modülünde {0}-değerli bir Dirichlet karakteri"},
    "en": {"DirichletCharacter": "a {0}-valued Dirichlet character modulo {1}"},
}
# tip sınıfı varsayımı -> koşul
SINIF_SOZ = {"NeZero": "{0} ≠ 0", "Fact": "{0}"}


class Ad(str):
    """Bağlı değişken adı; .p: değişken bir önerme ya da yüklem mi (tipi sonunda Prop'a varıyor mu)."""
    p = False


def sonuc_prop(tip):
    while isinstance(tip, list) and tip and tip[0] == "p":
        tip = tip[4]
    return tip == ["s", "Prop"]


class Duz(sozel.Cevirici):
    def __init__(self, baglayici, dil="tr", katla=None):
        super().__init__(baglayici, katla=katla)
        self.dil = dil
        self.K = KALIP[dil]
        self.onerme = getattr(baglayici, "onerme", None)

    def ad(self, ham, ortam, tip, tur=None):
        a = Ad(self.yeni_ad(ham, ortam, tur) if tur else self.yeni_ad(ham, ortam))
        a.p = sonuc_prop(tip)
        return a

    def onerme_mi(self, e, ortam):
        """e bir önerme mi? Dökümde önerme tablosu yoksa bilinemez: True (eski davranış)."""
        if self.onerme is None:
            return True
        o = list(ortam)
        while isinstance(e, list) and e and e[0] == "p":
            a = Ad("_")
            a.p = sonuc_prop(e[3])
            o.append(a)
            e = e[4]
        if not isinstance(e, list) or not e:
            return False
        bas = e[1] if e[0] == "a" else e
        if isinstance(bas, list) and bas and bas[0] == "c":
            return bas[1] in self.onerme
        if isinstance(bas, list) and bas and bas[0] == "b":
            i = bas[1]
            return i < len(o) and getattr(o[-1 - i], "p", False)
        return False

    # ---- yardımcılar
    def bas(self, e):
        if isinstance(e, list) and e[0] == "a" and isinstance(e[1], list) and e[1][0] == "c":
            return e[1][1], self.acik(e[1][1], e[2:])
        if isinstance(e, list) and e[0] == "c":
            return e[1], []
        return None, []

    def bilesik(self, e):
        """Önerme iskeletinde bir bağlaç ya da niceleyici mi?"""
        if isinstance(e, list) and e[0] == "p":
            return "pi"
        ad, ac = self.bas(e)
        if ad in ("And", "Or", "Iff", "Not", "Exists"):
            return ad
        return None

    def sar(self, e, ortam, serbest=()):
        s = self.c(e, ortam)
        b = self.bilesik(e)
        return f"({s})" if b and b not in serbest else s

    def baglayici_sozu(self, ad, tip, ortam):
        ta, ac = self.bas(tip)
        if ta in sozel.US_TURU:
            return f"{ad} ∈ {sozel.US_TURU[ta]}"
        if ta in TIP_SOZ[self.dil]:
            return f"{ad} ({TIP_SOZ[self.dil][ta].format(*[self.t(x, ortam) for x in ac])})"
        return f"{ad} : {self.t(tip, ortam)}"

    def sinif_sozu(self, tip, ortam):
        ta, ac = self.bas(tip)
        if ta in SINIF_SOZ:
            return SINIF_SOZ[ta].format(*[self.t(x, ortam) for x in ac])
        return f"[{self.t(tip, ortam)}]"

    def kosul(self, sinif):
        """Tip sınıfı varsayımları: bağlayıcı listesinin sonunda, ayrı bir öbekte."""
        if not sinif:
            return ""
        return {"tr": " (koşullar: {k})", "en": " (with: {k})"}[self.dil].format(k=", ".join(sinif))

    def birlestir(self, L):
        if len(L) <= 1:
            return "".join(L)
        return self.K["ayrac"].join(L[:-1]) + self.K["son_ve"] + L[-1]

    # ---- cümle
    def c(self, e, ortam):
        K = self.K
        if isinstance(e, list) and e[0] == "p":
            # sonu bir evrene (Prop/Type) varan ∀ bir önerme değil, tip imzasıdır: cümleye çevrilmez
            g = e
            while isinstance(g, list) and g[0] == "p":
                g = g[4]
            if isinstance(g, list) and g[0] == "s":
                return self.t(e, ortam)
            if not self.onerme_mi(e, ortam):
                return self.t(e, ortam)      # fonksiyon tipi: cümle değil
            # baştaki bağlayıcı öbeği: bağımlı olanlar ve tip sınıfı varsayımları
            bag, sinif, o2, g = [], [], list(ortam), e
            # bağlayıcı: bağımlı olanlar, tip sınıfı varsayımları ve tipi önerme OLMAYAN her argüman (bir nesne; varsayım değil)
            while isinstance(g, list) and g[0] == "p" and (g[2] == "c" or self.kullanir(g[4], 0) or not self.onerme_mi(g[3], o2)):
                if g[2] == "c":
                    ad = self.ad(g[1], o2, g[3], "ornek")
                    sinif.append(self.sinif_sozu(g[3], o2))
                else:
                    ad = self.ad(g[1], o2, g[3])
                    bag.append(self.baglayici_sozu(ad, g[3], o2))
                o2.append(ad)
                g = g[4]
            if bag or sinif:
                return K["her"].format(b=self.birlestir(bag) + self.kosul(sinif), g=self.c(g, o2))
            # varsayım zinciri
            var = []
            while isinstance(g, list) and g[0] == "p" and g[2] != "c" and not self.kullanir(g[4], 0):
                var.append(self.sar(g[3], o2))
                o2.append(self.ad(g[1], o2, g[3], "onerme"))
                g = g[4]
            son = self.c(g, o2)
            if isinstance(g, list) and g[0] == "p":
                son = f"({son})"
            return K["ise"].format(v=K["ve"].join(var), s=son)
        ad, ac = self.bas(e)
        if ad == "And" and len(ac) == 2:
            return self.sar(ac[0], ortam) + K["ve"] + self.sar(ac[1], ortam, ("And",))
        if ad == "Or" and len(ac) == 2:
            return self.sar(ac[0], ortam) + K["veya"] + self.sar(ac[1], ortam, ("Or",))
        if ad == "Iff" and len(ac) == 2:
            return K["ancak"].format(a=self.sar(ac[0], ortam), b=self.sar(ac[1], ortam))
        if ad in ("Not", "Exists"):
            ic, olumsuz = e, False
            if ad == "Not" and len(ac) == 1:
                a2, _ = self.bas(ac[0])
                if a2 != "Exists":
                    return K["degil"].format(a=self.sar(ac[0], ortam))
                ic, olumsuz = ac[0], True
            bag, o2, g = [], list(ortam), ic
            while isinstance(g, list) and g[0] == "a" and g[1] == ["c", "Exists"] and len(g) == 4 and isinstance(g[3], list) and g[3][0] == "l":
                lam = g[3]
                v = self.ad(lam[1], o2, lam[3])
                bag.append(self.baglayici_sozu(v, lam[3], o2))
                o2.append(v)
                g = lam[4]
            if bag:
                return K["yok" if olumsuz else "var"].format(b=self.birlestir(bag), g=self.sar(g, o2, ("Not",)))
        return self.t(e, ortam)

    def cumle(self, e):
        self.kullanilan = {}
        self.kirpik = False
        self.katlanan = {}
        s = self.c(e, [])
        return s[0].upper() + s[1:] + "."


YAPI = {"tr": ("Verilsin", "Varsayalım", "O zaman"), "en": ("Given", "Assume", "Then")}


def yapili(C, e):
    """Uzun önerme için bölünmüş yazım: verilenler, numaralı varsayımlar, sonuç. Satır listesi döner.
    Bölme yalnızca baştaki ∀ ve → zincirini ayırır; anlam cümle biçimiyle aynıdır."""
    C.kullanilan, C.kirpik, C.katlanan = {}, False, {}
    V, Va, O = YAPI[C.dil]
    ortam, bag, sinif, g = [], [], [], e
    while isinstance(g, list) and g[0] == "p" and (g[2] == "c" or C.kullanir(g[4], 0) or not C.onerme_mi(g[3], ortam)):
        if g[2] == "c":
            ad = C.ad(g[1], ortam, g[3], "ornek")
            sinif.append(C.sinif_sozu(g[3], ortam))
        else:
            ad = C.ad(g[1], ortam, g[3])
            bag.append(C.baglayici_sozu(ad, g[3], ortam))
        ortam.append(ad)
        g = g[4]
    var = []
    while isinstance(g, list) and g[0] == "p" and g[2] != "c" and not C.kullanir(g[4], 0):
        var.append(C.c(g[3], ortam))
        ortam.append(C.ad(g[1], ortam, g[3], "onerme"))
        g = g[4]
    L = []
    if bag or sinif:
        L.append(f"{V}: {C.birlestir(bag)}{C.kosul(sinif)}.")
    for i, v in enumerate(var, 1):
        L.append(f"{Va} ({i}): {v}.")
    L.append(f"{O}: {C.c(g, ortam)}.")
    return L


def sonuc_tipi(tip):
    while isinstance(tip, list) and tip[0] == "p":
        tip = tip[4]
    return tip


def tanim_cumlesi(C, d):
    """Tanımı cümle olarak yazar. Parametreli önerme tanımı: 'Ad(a, b) şu demektir: …'. Önerme değilse None."""
    g = d.get("govde")
    if g is None or sonuc_tipi(d["tip"]) != ["s", "Prop"]:
        return None
    C.kullanilan, C.kirpik, C.katlanan = {}, False, {}
    ortam, ps = [], []
    while isinstance(g, list) and g[0] == "l":
        ad = C.ad(g[1], ortam, g[3], "ornek" if g[2] == "c" else None)
        if g[2] == "e":
            ps.append(C.baglayici_sozu(ad, g[3], ortam))
        ortam.append(ad)
        g = g[4]
    govde = C.c(g, ortam)
    if not ps:
        return govde[0].upper() + govde[1:] + "."
    acik = [a for a, b in zip(ortam, d.get("b", "")) if b == "e"]
    bas = {"tr": "{ad}({a}) şu demektir ({p} için): {g}.", "en": "{ad}({a}) means (for {p}): {g}."}[C.dil]
    return bas.format(ad=C.kisa(d["ad"]), a=", ".join(acik), p=C.birlestir(ps), g=govde)


def tek_sabit(e):
    """Önerme tek bir sabitten mi ibaret? (öyleyse adı)"""
    return e[1] if isinstance(e, list) and e[0] == "c" else None


def main():
    import argparse
    a = argparse.ArgumentParser()
    a.add_argument("--dok", required=True)
    a.add_argument("--ad", action="append", default=[])
    a.add_argument("--dil", default="tr")
    A = a.parse_args()
    D, bag = sozel.yukle(A.dok)
    C = Duz(bag, A.dil)
    for n in A.ad:
        d = D.get(n)
        if not d:
            print("yok:", n)
            continue
        e = d["tip"] if d["tur"] == "teorem" else d.get("govde")
        print(f"{n}: {C.cumle(e)}")


if __name__ == "__main__":
    main()
