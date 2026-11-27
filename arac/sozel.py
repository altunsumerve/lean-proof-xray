#!/usr/bin/env python3
"""Sözel çevirici / Verbaliser — Lean çekirdek terimlerini kurallarla matematik cümlesine çevirir.

TR: Girdi kitapcik/Dok.lean dökümüdür (çekirdek terimi ağaç olarak; hiçbir argüman gizli değildir). Çeviri tümüyle
    kurallıdır: yapay zekâ ya da rastgelelik yoktur; aynı girdi her zaman aynı çıktıyı verir. Hangi argümanın
    gösterileceği, sabitin Lean'deki bağlayıcı türlerinden (açık / örtük / tip sınıfı) okunur. Üslerde üs türü
    (doğal / tam / gerçel) terimden okunup yazılır. Tanınmayan her sabit genel biçimde `Ad(a, b)` yazılır.
EN: Rule-based rendering of Lean kernel terms (from kitapcik/Dok.lean) as mathematical sentences. Fully
    deterministic: no model, no randomness. Explicit/implicit/instance arguments are decided from the binder
    kinds recorded by Lean; exponent kinds are read from the term.

Kullanım / usage:
  sozel.py --dok dok.jsonl.gz --ad UpperTheory.EveryCharacter [--ad ...]      # seçilen bildirimler
  sozel.py --dok dok.jsonl.gz --liste adlar.txt --cikti cikti.jsonl            # toplu
"""
import argparse
import gzip
import json
import re
import sys

TIP_AD = {"Real": "ℝ", "Nat": "ℕ", "Int": "ℤ", "Complex": "ℂ", "Rat": "ℚ", "NNReal": "ℝ≥0", "ENNReal": "ℝ≥0∞",
          "EReal": "[-∞,∞]", "PadicInt": "ℤ_p", "Padic": "ℚ_p", "Bool": "Bool", "Unit": "Unit"}
# (sembol, öncelik, sol-sağ birleşme) — açık argümanların son ikisi üzerinde
IKILI = {"Eq": ("=", 50), "Ne": ("≠", 50), "LT.lt": ("<", 50), "LE.le": ("≤", 50), "GT.gt": (">", 50), "GE.ge": ("≥", 50),
         "HEq": ("≍", 50), "Iff": ("↔", 20), "And": ("∧", 35), "Or": ("∨", 30),
         "HAdd.hAdd": ("+", 65), "HSub.hSub": ("−", 65), "HMul.hMul": ("·", 70), "HDiv.hDiv": ("/", 70),
         "HSMul.hSMul": ("•", 73), "HVAdd.hVAdd": ("+ᵥ", 65), "HasSubset.Subset": ("⊆", 50), "HasSSubset.SSubset": ("⊂", 50),
         "Union.union": ("∪", 65), "Inter.inter": ("∩", 70), "SDiff.sdiff": ("∖", 70), "Function.comp": ("∘", 90),
         "Dvd.dvd": ("∣", 50), "HMod.hMod": ("mod", 70), "Max.max": ("⊔", 68), "Min.min": ("⊓", 69),
         "Prod": ("×", 35), "Sum": ("⊕", 30), "Equiv": ("≃", 25), "RingHom": ("→+*", 25), "MonoidHom": ("→*", 25),
         "AddMonoidHom": ("→+", 25), "LinearMap": ("→ₗ", 25)}
TEKLI = {"Not": "¬", "Neg.neg": "−", "Nat.cast": "↑", "Int.cast": "↑", "Rat.cast": "↑", "NNReal.toReal": "↑",
         "Complex.ofReal": "↑", "Subtype.val": "↑", "Units.val": "↑", "SetLike.coe": "↑", "Finset.coe": "↑",
         "NumberField.RingOfIntegers.val": "↑", "Subfield.subtype": "↑", "algebraMap": "↑"}
OZEL = {"Complex.re": "Re", "Complex.im": "Im", "Real.log": "log", "Real.exp": "exp", "Real.sqrt": "√", "Complex.exp": "exp",
        "Complex.log": "log", "Complex.abs": "abs", "Nat.Prime": "Prime", "DirichletCharacter.LFunction": "L",
        "riemannZeta": "ζ", "Set.ncard": "ncard", "Nat.card": "card", "Finset.card": "card", "Fintype.card": "card",
        "Module.finrank": "finrank", "Real.pi": "π"}
US_TURU = {"Nat": "ℕ", "Int": "ℤ", "Real": "ℝ", "Complex": "ℂ", "Rat": "ℚ"}


def temiz(ad):
    """Bağlayıcı adından Lean'in hijyen eklerini atar."""
    ad = ad.split("._@")[0]
    return ad


class Cevirici:
    def __init__(self, baglayici, tam_ad=False, katla=None):
        self.bag = baglayici
        self.katla = katla or {}   # json(gövde) -> parametresiz tanımın adı
        self.katlanan = {}
        self.tam_ad = tam_ad
        self.kullanilan = {}   # kısa ad -> tam ad (proje sabitleri)
        self.kirpik = False    # bütçe yüzünden kesilmiş alt terim görüldü mü

    # ---- yardımcılar
    def kisa(self, ad):
        if ad in TIP_AD:
            return TIP_AD[ad]
        if ad in OZEL:
            return OZEL[ad]
        p = ad.split(".")
        k = p[-1]
        if k in ("mk", "val", "toFun", "coe", "carrier") and len(p) > 1:
            k = p[-2] + "." + k
        if self.kullanilan.get(k, ad) != ad:
            k = ".".join(p[-2:]) if len(p) > 1 else k
        self.kullanilan.setdefault(k, ad)
        return k

    def acik(self, bas, args):
        """Sabitin açık argümanları (bağlayıcı tablosuna göre); tablo kısa kalırsa kalanlar açık sayılır."""
        b = self.bag.get(bas, "")
        return [a for i, a in enumerate(args) if (b[i] if i < len(b) else "e") == "e"]

    def kullanir(self, e, k=0):
        """Terim de Bruijn k'yi kullanıyor mu?"""
        if not isinstance(e, list):
            return False
        t = e[0]
        if t == "b":
            return e[1] == k
        if t in ("l", "p"):
            return self.kullanir(e[3], k) or self.kullanir(e[4], k + 1)
        if t == "z":
            return self.kullanir(e[2], k) or self.kullanir(e[3], k) or self.kullanir(e[4], k + 1)
        if t == "a":
            return any(self.kullanir(x, k) for x in e[1:])
        if t == "j":
            return self.kullanir(e[3], k)
        return False

    def yeni_ad(self, ad, ortam, tip=None):
        ad = temiz(ad)
        if tip == "ornek":
            ad = "_i"
        elif ad in ("", "a", "inst", "x✝", "_") or ad.startswith("inst") or "✝" in ad:
            ad = "h" if tip == "onerme" else "x"
        taban, i = ad, 1
        while ad in ortam:
            i += 1
            ad = f"{taban}{i}"
        return ad

    def sayi(self, e):
        """OfNat.ofNat α n inst -> (n, α) ; değilse None"""
        if isinstance(e, list) and e[0] == "a" and e[1] == ["c", "OfNat.ofNat"] and len(e) >= 4 and isinstance(e[3], list) and e[3][0] == "n":
            return e[3][1], e[2]
        if isinstance(e, list) and e[0] == "n":
            return e[1], ["c", "Nat"]
        return None

    # ---- terim
    def t(self, e, ortam, onc=0):
        """Terimi yazar. onc: çevrenin önceliği; daha düşük öncelikli ifadeler paranteze alınır."""
        if not isinstance(e, list):
            self.kirpik = True
            return "…"
        k = e[0]
        if self.katla and k in ("a", "p") :
            anahtar = katla_anahtari(e)
            if anahtar in self.katla and self.katla[anahtar] != getattr(self, "_kendi", None):
                self.katlanan[self.katla[anahtar]] = True
                return self.kisa(self.katla[anahtar])
        if k == "b":
            i = e[1]
            return ortam[-1 - i] if i < len(ortam) else f"#{i}"
        if k == "c":
            return self.kisa(e[1])
        if k == "s":
            return e[1]
        if k == "n":
            return str(e[1])
        if k == "t":
            return json.dumps(e[1], ensure_ascii=False)
        if k == "j":
            return self.par(f"{self.t(e[3], ortam, 100)}.{e[2] + 1}", 100, onc)
        if k == "z":
            ad = self.yeni_ad(e[1], ortam)
            return self.par(f"let {ad} := {self.t(e[3], ortam)}; {self.t(e[4], ortam + [ad])}", 5, onc)
        if k == "l":
            adlar, govde, o2 = [], e, list(ortam)
            while isinstance(govde, list) and govde[0] == "l":
                ad = self.yeni_ad(govde[1], o2, "ornek" if govde[2] == "c" else None)
                if govde[2] == "c":
                    adlar.append(f"[{self.t(govde[3], o2)}]")
                else:
                    adlar.append(f"({ad} : {self.t(govde[3], o2)})")
                o2.append(ad)
                govde = govde[4]
            return self.par(f"{' '.join(adlar)} ↦ {self.t(govde, o2, 10)}", 10, onc)
        if k == "p":
            return self.pi(e, ortam, onc)
        if k == "a":
            return self.uygula(e, ortam, onc)
        return "?"

    def par(self, s, kendi, cevre):
        return f"({s})" if kendi < cevre else s

    def pi(self, e, ortam, onc):
        ad0, tur, tip, govde = e[1], e[2], e[3], e[4]
        if not self.kullanir(govde, 0):
            sol = self.t(tip, ortam, 26)
            sag = self.t(govde, ortam + ["_"], 25)
            if tur == "c":
                return self.par(f"[{self.t(tip, ortam)}] → {sag}", 25, onc)
            return self.par(f"{sol} → {sag}", 25, onc)
        # bağımlı: ∀ ; aynı tipli ardışık bağlayıcıları birleştir
        parcalar, o2, g = [], list(ortam), e
        while isinstance(g, list) and g[0] == "p" and self.kullanir(g[4], 0):
            ad = self.yeni_ad(g[1], o2, "ornek" if g[2] == "c" else None)
            tp = self.t(g[3], o2)
            if g[2] == "c":
                parcalar.append(f"[{tp}]")
            elif parcalar and parcalar[-1][1] == tp and parcalar[-1][0] == "v":
                parcalar[-1] = ("v", tp, parcalar[-1][2] + [ad])
            else:
                parcalar.append(("v", tp, [ad]))
            o2.append(ad)
            g = g[4]
        bas = " ".join(p if isinstance(p, str) else f"({' '.join(p[2])} : {p[1]})" for p in parcalar)
        return self.par(f"∀ {bas}, {self.t(g, o2, 0)}", 10, onc)

    def uygula(self, e, ortam, onc):
        bas, args = e[1], e[2:]
        if not (isinstance(bas, list) and bas[0] == "c"):
            f = self.t(bas, ortam, 100)
            gor = [x for x in (self.t(a, ortam) for a in args) if not re.fullmatch(r"_i\d*", x)]   # tip sınıfı değişkenleri gizlenir
            return self.par(f"{f}({', '.join(gor)})" if gor else f, 95, onc)
        ad = bas[1]
        ac = self.acik(ad, args)
        s = self.sayi(e)
        if s is not None:
            return str(s[0])
        if ad == "Exists" and len(args) == 2 and isinstance(args[1], list) and args[1][0] == "l":
            adlar, g, o2 = [], e, list(ortam)
            while isinstance(g, list) and g[0] == "a" and g[1] == ["c", "Exists"] and len(g) == 4 and isinstance(g[3], list) and g[3][0] == "l":
                lam = g[3]
                v = self.yeni_ad(lam[1], o2)
                adlar.append(f"({v} : {self.t(lam[3], o2)})")
                o2.append(v)
                g = lam[4]
            return self.par(f"∃ {' '.join(adlar)}, {self.t(g, o2, 0)}", 10, onc)
        if ad in ("setOf", "Set.ofPred") and ac and isinstance(ac[-1], list) and ac[-1][0] == "l":
            lam = ac[-1]
            v = self.yeni_ad(lam[1], ortam)
            return f"{{{v} : {self.t(lam[3], ortam)} | {self.t(lam[4], ortam + [v])}}}"
        if ad == "HPow.hPow" and len(args) == 6:
            taban, us = args[4], args[5]
            ut = args[1][1] if isinstance(args[1], list) and args[1][0] == "c" else None
            ust = self.t(us, ortam, 76)
            if self.sayi(us) is not None and ut in US_TURU:
                ust = f"({self.sayi(us)[0]} : {US_TURU[ut]})"
            elif ut in US_TURU and ut != "Nat":
                ust = f"{ust}"
            return self.par(f"{self.t(taban, ortam, 76)} ^ {ust}", 75, onc)
        if ad in ("Membership.mem",) and len(ac) == 2:
            return self.par(f"{self.t(ac[1], ortam, 51)} ∈ {self.t(ac[0], ortam, 51)}", 50, onc)
        if ad in IKILI and len(ac) >= 2:
            sem, p = IKILI[ad]
            a, b = ac[-2], ac[-1]
            if p in (35, 30, 20):   # ∧ ∨ ↔ sağa birleşir
                return self.par(f"{self.t(a, ortam, p + 1)} {sem} {self.t(b, ortam, p)}", p, onc)
            return self.par(f"{self.t(a, ortam, p)} {sem} {self.t(b, ortam, p + 1)}", p, onc)
        if ad in TEKLI and len(ac) >= 1:
            return self.par(f"{TEKLI[ad]}{self.t(ac[-1], ortam, 80)}", 80, onc)
        if ad in ("abs",) and ac:
            return f"|{self.t(ac[-1], ortam)}|"
        if ad in ("Norm.norm",) and ac:
            return f"‖{self.t(ac[-1], ortam)}‖"
        if ad == "Inv.inv" and ac:
            return self.par(f"{self.t(ac[-1], ortam, 100)}⁻¹", 100, onc)
        if ad in ("Prod.mk",) and len(ac) == 2:
            return f"({self.t(ac[0], ortam)}, {self.t(ac[1], ortam)})"
        if ad in ("Prod.fst", "Prod.snd") and ac:
            return self.par(f"{self.t(ac[-1], ortam, 100)}.{1 if ad.endswith('fst') else 2}", 100, onc)
        if ad in ("Set", "Finset", "Multiset", "List", "Option", "Subgroup", "AddSubgroup", "Ideal") and len(ac) == 1:
            return self.par(f"{ad} {self.t(ac[0], ortam, 100)}", 95, onc)
        if ad in ("DFunLike.coe", "FunLike.coe") and len(ac) >= 2:
            return self.par(f"{self.t(ac[0], ortam, 100)}({', '.join(self.t(a, ortam) for a in ac[1:])})", 95, onc)
        if ad in ("DFunLike.coe", "FunLike.coe") and len(ac) == 1:
            return self.t(ac[0], ortam, onc)
        k = self.kisa(ad)
        if not ac:
            return k
        return self.par(f"{k}({', '.join(self.t(a, ortam) for a in ac)})", 95, onc)

    def baglayici_satirlari(self, bas, parcalar, en):
        """'∀ (x : A) (y : B) …,' satırını gerektiğinde böler."""
        L, satir = [], bas
        for p_ in parcalar:
            if len(satir) + len(p_) + 1 > en and satir.strip() not in ("∀", "∃"):
                L.append(satir.rstrip())
                satir = " " * len(bas) + p_ + " "
            else:
                satir += p_ + " "
        L.append(satir.rstrip() + ",")
        return L

    def blok(self, e, ortam, gir=0, en=96):
        """Önermeyi yazar; satır uzunsa ∀ / ∃ / → / ∧ / ∨ yerlerinden böler. Çıktı: satır listesi."""
        b = "  " * gir
        tek = self.t(e, ortam)
        if len(tek) + len(b) <= en or not isinstance(e, list):
            return [b + tek]
        if e[0] == "p":
            if self.kullanir(e[4], 0):
                parcalar, o2, g = [], list(ortam), e
                while isinstance(g, list) and g[0] == "p" and self.kullanir(g[4], 0):
                    ad = self.yeni_ad(g[1], o2, "ornek" if g[2] == "c" else None)
                    tp = self.t(g[3], o2)
                    parcalar.append(f"[{tp}]" if g[2] == "c" else f"({ad} : {tp})")
                    o2.append(ad)
                    g = g[4]
                return self.baglayici_satirlari(b + "∀ ", parcalar, en) + self.blok(g, o2, gir + 1, en)
            sol = self.blok(e[3], ortam, gir, en)
            if isinstance(e[3], list) and e[3][0] == "p":
                sol = [b + "("] + self.blok(e[3], ortam, gir + 1, en) + [b + ")"]
            sol[-1] += " →"
            return sol + self.blok(e[4], ortam + ["_"], gir, en)
        if e[0] == "a" and e[1] == ["c", "Exists"] and len(e) == 4 and isinstance(e[3], list) and e[3][0] == "l":
            adlar, g, o2 = [], e, list(ortam)
            while isinstance(g, list) and g[0] == "a" and g[1] == ["c", "Exists"] and len(g) == 4 and isinstance(g[3], list) and g[3][0] == "l":
                lam = g[3]
                v = self.yeni_ad(lam[1], o2)
                adlar.append(f"({v} : {self.t(lam[3], o2)})")
                o2.append(v)
                g = lam[4]
            return self.baglayici_satirlari(b + "∃ ", adlar, en) + self.blok(g, o2, gir + 1, en)
        if e[0] == "a" and e[1] in (["c", "And"], ["c", "Or"]) and len(e) == 4:
            sem = "∧" if e[1][1] == "And" else "∨"

            def sarili(x):
                # niceleyici ya da → ile başlayan işlenen, kapsamı belli olsun diye paranteze alınır
                acik_uclu = isinstance(x, list) and (x[0] == "p" or (x[0] == "a" and x[1] in (["c", "Exists"], ["c", "Or"] if sem == "∧" else ["c", "Exists"])))
                if acik_uclu:
                    return [b + "("] + self.blok(x, ortam, gir + 1, en) + [b + ")"]
                return self.blok(x, ortam, gir, en)
            sol = sarili(e[2])
            sol[-1] += " " + sem
            sag = e[3]
            # sağ işlenen aynı bağlaçla devam ediyorsa zincir; son işlenen niceleyiciyse parantezsiz bırakılabilir (kapsam sona kadar)
            return sol + (self.blok(sag, ortam, gir, en) if isinstance(sag, list) and sag[0] == "a" and sag[1] == e[1] else self.blok(sag, ortam, gir, en))
        return [b + tek]

    # ---- önerme düzeyi: Let / Assume / Then
    def metin(self, d, dil="en"):
        S = {"en": ("Let", "Assume", "Then", "Statement", "Definition", "of type", "Declaration"),
             "tr": ("Verilsin", "Varsayalım", "O zaman", "Önerme", "Tanım", "tipi", "Bildirim")}[dil]
        self.kullanilan = {}
        self.kirpik = False
        self.katlanan = {}
        self._kendi = d["ad"]

        def degisken(deg):
            return "; ".join(f"[{x[1]}]" if x[0] == "c" else f"{', '.join(x[2])} : {x[1]}" for x in deg)

        satir = []
        if d["tur"] == "teorem":
            ortam, deg, var, sonuc = self.ac(d["tip"], [], teorem=True)
            if deg:
                satir.append(f"{S[0]}: {degisken(deg)}.")
            for v, o in var:
                satir.extend(self.blok_etiketli(f"{S[1]}: ", v, o))
            satir.extend(self.blok_etiketli(f"{S[2]}: " if (deg or var) else f"{S[3]}: ", sonuc, ortam))
        elif d["tur"] == "tanim" and d.get("govde") is not None:
            g, ortam, ps = d["govde"], [], []
            while isinstance(g, list) and g[0] == "l":
                ad = self.yeni_ad(g[1], ortam, "ornek" if g[2] == "c" else None)
                tp = self.t(g[3], ortam)
                ps.append(f"[{tp}]" if g[2] == "c" else f"{ad} : {tp}")
                ortam.append(ad)
                g = g[4]
            if ps:
                satir.append(f"{S[0]}: " + "; ".join(ps) + ".")
            bas = self.kisa(d["ad"])
            ac = [a for a, b in zip(ortam, d.get("b", "")) if b == "e"]
            imza = f"{bas}({', '.join(ac)})" if ac else bas
            # sonuç tipi: tipin kalan kısmı
            tp, o2 = d["tip"], []
            for _ in ortam:
                if isinstance(tp, list) and tp[0] == "p":
                    o2.append(ortam[len(o2)])
                    tp = tp[4]
            sonuc_tipi = self.t(tp, o2)
            if sonuc_tipi == "Prop":
                satir.append(f"{S[4]}: {imza} :⟺")
                satir.extend(self.blok(g, ortam, 1))
            else:
                satir.extend(self.blok_etiketli(f"{S[4]}: {imza} := ", g, ortam))
                satir.append(f"  ({S[5]} {sonuc_tipi})")
        else:
            satir.append(f"{S[6]}: {self.kisa(d['ad'])} : {self.t(d['tip'], [])}")
        return {"ad": d["ad"], "tur": d["tur"], "metin": "\n".join(satir), "sabitler": dict(self.kullanilan), "kesik": self.kirpik,
                "katlanan": sorted(self.katlanan)}

    def blok_etiketli(self, etiket, e, ortam):
        L = self.blok(e, ortam, 0)
        if len(L) == 1:
            return [etiket + L[0]]
        return [etiket.rstrip()] + ["  " + x for x in L]

    def ac(self, tip, ortam0, teorem=False):
        """Baştaki bağlayıcıları ayırır: değişkenler (ve tip sınıfı varsayımları), varsayımlar, sonuç."""
        ortam, deg, var, sonuc = list(ortam0), [], [], tip
        while isinstance(sonuc, list) and sonuc[0] == "p":
            ad0, tur, tp, govde = sonuc[1], sonuc[2], sonuc[3], sonuc[4]
            bagimli = self.kullanir(govde, 0)
            if tur == "c":
                ad = self.yeni_ad(ad0, ortam, "ornek")
                deg.append(("c", self.t(tp, ortam)))
            elif bagimli or tur == "i":
                if var:
                    break   # varsayımdan sonra gelen niceleyici: sırayı korumak için sonuca bırak
                ad = self.yeni_ad(ad0, ortam)
                tps = self.t(tp, ortam)
                if deg and deg[-1][0] == "v" and deg[-1][1] == tps:
                    deg[-1] = ("v", tps, deg[-1][2] + [ad])
                else:
                    deg.append(("v", tps, [ad]))
            else:
                ad = self.yeni_ad(ad0, ortam, "onerme")
                var.append((tp, list(ortam)))
            ortam.append(ad)
            sonuc = govde
        return ortam, deg, var, sonuc


def katlama_tablosu(D):
    """Parametresiz (sabit) tanımların gövdeleri: aynı terim başka yerde geçerse adıyla yazılabilir."""
    T = {}
    for n, d in D.items():
        g = d.get("govde")
        if d["tur"] == "tanim" and isinstance(g, list) and g[0] in ("a", "p") and d.get("b", "") == "" and d.get("govdeTam", True):
            k = katla_anahtari(g)
            if len(k) > 200:
                T.setdefault(k, n)
    return T


def adsiz(e):
    """Terimin bağlı değişken adları ve bağlayıcı türleri silinmiş hali (α-denklik için)."""
    if isinstance(e, list) and e:
        if e[0] in ("l", "p"):
            return [e[0], "", "", adsiz(e[3]), adsiz(e[4])]
        if e[0] == "z":
            return ["z", "", adsiz(e[2]), adsiz(e[3]), adsiz(e[4])]
        return [e[0]] + [adsiz(x) for x in e[1:]]
    return e


def katla_anahtari(e):
    return json.dumps(adsiz(e), ensure_ascii=False, separators=(",", ":"))


class Bag(dict):
    """Bağlayıcı tablosu; .onerme: tipi sonunda Prop'a varan sabitlerin kümesi (dökümde varsa)."""
    onerme = None


def yukle(yol):
    D, bag = {}, {}
    ac = gzip.open if yol.endswith(".gz") else open
    with ac(yol, "rt", encoding="utf-8") as f:
        for s in f:
            d = json.loads(s)
            if "baglayici" in d:
                bag = Bag(d["baglayici"])
                if "onerme" in d:
                    bag.onerme = set(d["onerme"])
            else:
                D[d["ad"]] = d
    if getattr(bag, "onerme", None) is not None:
        for n, d in D.items():
            t = d.get("tip")
            while isinstance(t, list) and t and t[0] == "p":
                t = t[4]
            if t == ["s", "Prop"]:
                bag.onerme.add(n)
    return D, bag


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--dok", required=True)
    a.add_argument("--ad", action="append", default=[])
    a.add_argument("--liste")
    a.add_argument("--cikti")
    a.add_argument("--dil", default="en")
    A = a.parse_args()
    D, bag = yukle(A.dok)
    C = Cevirici(bag, katla=katlama_tablosu(D))
    adlar = list(A.ad)
    if A.liste:
        adlar += [l.strip() for l in open(A.liste, encoding="utf-8") if l.strip()]
    o = open(A.cikti, "w", encoding="utf-8") if A.cikti else None
    for n in adlar:
        if n not in D:
            print(f"yok: {n}", file=sys.stderr)
            continue
        r = C.metin(D[n], A.dil)
        if o:
            o.write(json.dumps(r, ensure_ascii=False) + "\n")
        else:
            print(f"## {n}\n{r['metin']}\n")


if __name__ == "__main__":
    main()
