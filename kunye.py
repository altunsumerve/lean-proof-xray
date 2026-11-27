"""Proof passport / İspat künyesi.

EN: A short report on what a Lean theorem claims and relies on: the declarations needed to understand
    its statement, the axioms used, and fingerprints to compare exports. Report language: --dil en|tr.
TR: Bir Lean teoreminin neyi iddia ettiğini ve neye dayandığını gösteren kısa rapor.

Kullanım (derlenmiş bir Lake projesinin klasöründe):
  python3 kunye.py --proje . --modul Mathlib.NumberTheory.SumFourSquares --teorem Nat.sum_four_squares
  python3 kunye.py --kayit hazir.ndjson --teorem riemannHypothesis     # hazır lean4export kaydından

Rapor:
  * tam ispat zincirindeki bildirim sayısı (ispatın dayandığı her şey)
  * önermeyi anlamak için gereken bildirimler (ispatlar izlenmez; tanımlar tümüyle izlenir)
  * kullanılan aksiyomlar
  * teoremin ve tanımların parmak izi (aynı kod iki ayrı kayıtta aynı izi verir)
"""
import argparse
import collections
import json
import os
import re
import subprocess
import sys
import tempfile

BURASI = os.path.dirname(os.path.abspath(__file__))
STANDART = {"propext", "Classical.choice", "Quot.sound"}
# Lean'in kendiliğinden ürettiği yardımcı adlar: okuyucuya gösterilmez (sayıma dahildir)
YARDIMCI = re.compile(r"(\._|\.match_\d|\.proof_\d|\.eq_\d|\.rec$|\.recOn$|\.casesOn$|\.below$|\.brecOn$|\.binductionOn$|"
                      r"\.noConfusion|\.ibelow$|\.sizeOf_spec|\._sizeOf|\.ctorIdx|\.injEq$|\.inj$|\.mk\.|\._unsafe_rec)")


METIN = {
    "tr": {
        "turler": {"d": "tanım", "i": "tip / yapı", "t": "teorem", "o": "opak", "a": "aksiyom", "q": "bölüm tipi"},
        "baslik": "# İspat künyesi: `{t}`",
        "uyari": "Deneysel araç. Bu rapor Lean'in kendi dışa aktarım kaydından üretilir; ispatı yeniden doğrulamaz.",
        "ozet": "Özet", "bildirim": "bildirim",
        "zincir": "Tam ispat zinciri (dayandığı her şey)",
        "gereken": "Önermeyi anlamak için gereken",
        "okunacak": "Bunlardan okunacaklar (otomatik yardımcılar hariç)",
        "aks_sayi": "Kullanılan aksiyomlar", "iz": "Teoremin parmak izi",
        "aksiyomlar": "Aksiyomlar", "standart_disi": "standart dışı",
        "sorry": "`sorryAx` var: ispatın bir kısmı eksik (`sorry`).",
        "standart": "Yalnızca Lean'in üç standart aksiyomu kullanılıyor (ya da hiçbiri).",
        "dogrudan": "Önermede doğrudan geçenler",
        "dogrudan_not": "Okumaya buradan başlayın; aşağıdaki liste bunların dayandığı her şeyi içerir.",
        "tamami": "Önermeyi anlamak için okunması gerekenler (tamamı)",
        "izler": "Parmak izleri",
        "izler_not": "Aynı bildirim, aynı kaynaktan üretilen her kayıtta aynı izi verir. Başkasının \"doğruladık\" dediği "
                     "kaydın izleriyle karşılaştırarak elinizdeki kodun aynı olduğunu denetleyebilirsiniz.",
        "iz_tablo": "| bildirim | tür | önerme izi | tanım izi |",
        "konsol": "{c}: {z} bildirimlik zincir, önerme için {g}, aksiyom {a}",
    },
    "en": {
        "turler": {"d": "definition", "i": "type / structure", "t": "theorem", "o": "opaque", "a": "axiom",
                   "q": "quotient"},
        "baslik": "# Proof passport: `{t}`",
        "uyari": "Experimental tool. This report is generated from Lean's own export; it does not re-check the proof.",
        "ozet": "Summary", "bildirim": "declarations",
        "zincir": "Full proof chain (everything it depends on)",
        "gereken": "Needed to understand the statement",
        "okunacak": "Of these, to read (auto-generated helpers excluded)",
        "aks_sayi": "Axioms used", "iz": "Fingerprint of the theorem",
        "aksiyomlar": "Axioms", "standart_disi": "non-standard",
        "sorry": "`sorryAx` present: part of the proof is missing (`sorry`).",
        "standart": "Only Lean's three standard axioms are used (or none).",
        "dogrudan": "Mentioned directly in the statement",
        "dogrudan_not": "Start reading here; the list below contains everything these depend on.",
        "tamami": "Everything needed to understand the statement",
        "izler": "Fingerprints",
        "izler_not": "The same declaration gets the same fingerprint in every export made from the same source. Compare "
                     "with the fingerprints of an export someone says they checked to confirm your code is the same.",
        "iz_tablo": "| declaration | kind | statement fingerprint | definition fingerprint |",
        "konsol": "{c}: chain of {z} declarations, {g} for the statement, {a} axioms",
    },
}


def arac(ad):
    yol = os.path.join(BURASI, "arac", ad)
    if not os.path.exists(yol):
        subprocess.run(["g++", "-O2", "-o", yol, yol + ".cpp"], check=True)
    return yol


def kayit_al(A, gecici):
    if A.kayit:
        return A.kayit
    cikti = os.path.join(gecici, "kayit.ndjson")
    with open(cikti, "w") as f:
        subprocess.run(["lake", "env", A.lean4export, A.modul, "--", A.teorem], cwd=A.proje, stdout=f, check=True)
    return cikti


def adlar_ve_bildirimler(kayit):
    """Kayıttan ad tablosu, bildirim türleri ve aksiyomlar."""
    ad = {0: ""}
    turler = collections.Counter()
    aksiyomlar = []
    satir_sayisi = 0
    with open(kayit, encoding="utf-8") as f:
        for s in f:
            satir_sayisi += 1
            if s.startswith('{"in":'):
                d = json.loads(s)
                if "str" in d:
                    o = d["str"]
                    ad[d["in"]] = (ad[o["pre"]] + "." if o["pre"] else "") + o["str"]
                else:
                    o = d["num"]
                    ad[d["in"]] = (ad[o["pre"]] + "." if o["pre"] else "") + str(o["i"])
            elif s.startswith('{"ie"') or s.startswith('{"il"') or '"ie":' in s[:200] or '"il":' in s[:200]:
                continue
            elif s.startswith("{\""):
                anahtar = s[2:s.index('"', 2)]
                if anahtar in ("thm", "def", "opaque", "axiom", "quot", "inductive"):
                    if anahtar == "inductive":
                        d = json.loads(s)["inductive"]
                        turler["inductive"] += len(d.get("types", []))
                    else:
                        turler[anahtar] += 1
                    if anahtar == "axiom":
                        d = json.loads(s)["axiom"]
                        aksiyomlar.append(ad.get(d["name"], "?"))
    return turler, aksiyomlar, satir_sayisi


def dogrudan(kayit, teorem, ad_tablosu_siniri=5_000_000):
    """Teoremin önermesinde doğrudan geçen sabitler (küçük kayıtlarda)."""
    ad, ifade, hedef = {0: ""}, {}, None
    with open(kayit, encoding="utf-8") as f:
        for n, s in enumerate(f):
            if n > ad_tablosu_siniri:
                return None
            if s.startswith('{"in":'):
                d = json.loads(s)
                o = d.get("str") or d.get("num")
                ad[d["in"]] = (ad[o["pre"]] + "." if o["pre"] else "") + str(o.get("str", o.get("i")))
            elif '"ie":' in s:
                d = json.loads(s)
                i = d.pop("ie")
                (k, v), = d.items()
                if k == "const":
                    ifade[i] = ("c", v["name"])
                elif isinstance(v, dict):
                    ifade[i] = ("e", [v[x] for x in ("fn", "arg", "type", "body", "value", "struct", "expr") if x in v])
            elif s.startswith('{"thm"') or s.startswith('{"def"'):
                d = next(iter(json.loads(s).values()))
                if ad.get(d["name"]) == teorem:
                    hedef = d["type"]
    if hedef is None:
        return None
    gor, yig, sabit = set(), [hedef], set()
    while yig:
        e = yig.pop()
        if e in gor or e not in ifade:
            continue
        gor.add(e)
        t, v = ifade[e]
        if t == "c":
            sabit.add(ad.get(v, "?"))
        else:
            yig.extend(v)
    return sorted(sabit)


def main():
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument("--proje", default=".")
    a.add_argument("--modul")
    a.add_argument("--teorem", required=True)
    a.add_argument("--kayit", help="hazır lean4export NDJSON kaydı (verilirse derleme yapılmaz)")
    a.add_argument("--lean4export", default="lean4export")
    a.add_argument("--cikti", default="kunye.md")
    a.add_argument("--dil", choices=("tr", "en"), default="en", help="rapor dili / report language")
    a.add_argument("--siki", action="store_true",
                   help="standart dışı aksiyom ya da sorry varsa hata koduyla çık (CI için) / "
                        "exit with an error on non-standard axioms or sorry (for CI)")
    A = a.parse_args()
    if not A.kayit and not A.modul:
        a.error("--modul ya da --kayit gerekli")
    with tempfile.TemporaryDirectory() as g:
        kayit = kayit_al(A, g)
        turler, aksiyomlar, satir = adlar_ve_bildirimler(kayit)
        ortam = dict(os.environ, KUNYE_KAPASITE=str(satir + 16))
        kok = os.path.join(g, "kok.txt")
        open(kok, "w").write(A.teorem + "\n")
        with open(kayit, "rb") as f:
            subprocess.run([arac("kapanis"), os.path.join(g, "ifade.bin"), g, kok], stdin=f, env=ortam, check=True,
                           stderr=subprocess.DEVNULL)
        kapanis = [s.rstrip("\n").split("\t", 1) for s in open(kok + ".kapanis", encoding="utf-8")]
        adlar = os.path.join(g, "adlar.txt")
        open(adlar, "w").write("\n".join(x[1] for x in kapanis) + "\n")
        with open(kayit, "rb") as f:
            p = subprocess.run([arac("parmakizi"), os.path.join(g, "ozet.bin"), adlar], stdin=f, env=ortam, check=True,
                               capture_output=True, text=True)
        iz = {s.split("\t")[0]: s.split("\t") for s in p.stdout.splitlines()}
        dg = dogrudan(kayit, A.teorem)

    toplam = sum(turler.values())
    gorunur = [x for x in kapanis if not YARDIMCI.search(x[1]) and x[1] != A.teorem]
    M = METIN[A.dil]
    tur_ad = M["turler"]
    gruplar = collections.defaultdict(list)
    for t, n in gorunur:
        gruplar[tur_ad.get(t, t)].append(n)
    standart_disi = [x for x in aksiyomlar if x not in STANDART]
    kok_iz = iz.get(A.teorem, ["", "", "?", "?"])
    oran = 100 * len(kapanis) / max(1, toplam)

    r = []
    r.append(M["baslik"].format(t=A.teorem) + "\n")
    r.append("> " + M["uyari"] + "\n")
    r.append("## " + M["ozet"] + "\n")
    r.append("| | |\n|---|---:|")
    r.append(f"| {M['zincir']} | {toplam:,} {M['bildirim']} |")
    r.append(f"| {M['gereken']} | {len(kapanis):,} {M['bildirim']} ({oran:.1f}%) |")
    r.append(f"| {M['okunacak']} | {len(gorunur):,} |")
    r.append(f"| {M['aks_sayi']} | {len(aksiyomlar)} |")
    r.append(f"| {M['iz']} | `{kok_iz[2]}` |\n")
    r.append("## " + M["aksiyomlar"] + "\n")
    for x in sorted(aksiyomlar):
        r.append(f"- `{x}`" + ("" if x in STANDART else "  ⚠️ **" + M["standart_disi"] + "**"))
    if "sorryAx" in aksiyomlar:
        r.append("\n⚠️ " + M["sorry"])
    elif not standart_disi:
        r.append("\n" + M["standart"])
    if dg:
        r.append("\n## " + M["dogrudan"] + "\n")
        r.append(M["dogrudan_not"] + "\n")
        r.append(", ".join(f"`{n}`" for n in dg) + "\n")
    r.append("\n## " + M["tamami"] + "\n")
    for g_ad in tur_ad.values():
        if gruplar.get(g_ad):
            r.append(f"### {g_ad[:1].upper() + g_ad[1:]} ({len(gruplar[g_ad])})\n")
            r.append(", ".join(f"`{n}`" for n in sorted(gruplar[g_ad])) + "\n")
    r.append("## " + M["izler"] + "\n")
    r.append(M["izler_not"] + "\n")
    r.append(M["iz_tablo"] + "\n|---|---|---|---|")
    for n in [A.teorem] + sorted(x[1] for x in gorunur):
        if n in iz:
            r.append(f"| `{n}` | {iz[n][1]} | `{iz[n][2]}` | `{iz[n][3]}` |")
    open(A.cikti, "w", encoding="utf-8").write("\n".join(r) + "\n")
    print(M["konsol"].format(c=A.cikti, z=f"{toplam:,}", g=f"{len(kapanis):,}", a=len(aksiyomlar))
          + (f" ⚠️ {M['standart_disi']}: {standart_disi}" if standart_disi else ""))
    if A.siki and standart_disi:
        sys.exit(1)


if __name__ == "__main__":
    main()
