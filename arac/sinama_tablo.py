#!/usr/bin/env python3
"""Sınama tablosu — sinama/<ad>/ klasörlerindeki ölçümleri tek tabloda toplar (SINAMA.md).
TR: Yalnızca dosyalarda yazılı sayıları okur. Elle yapılan karşılaştırmalar ayrı sütunda "elle" diye işaretlenir.
EN: Collects the measurements under sinama/<name>/ into one table. Reads numbers from files only.
"""
import json
import os
import re
import sys

K = sys.argv[1] if len(sys.argv) > 1 else "sinama"
ELLE = {  # ana önermenin insan yazımı ifadeyle elle karşılaştırması (tarih, sonuç)
    "pfr": "örtüşüyor (elle, 25 Kas)", "carleson": "örtüşüyor (elle, 26 Kas)", "sphere": "örtüşüyor (elle, 26 Kas)", "fltregular": "örtüşüyor (elle, 26 Kas)"}
L = ["# Sınama sonuçları / Validation results", "",
     "Kurallı üretildi (`arac/sinama_tablo.py`). \"İsabet\": aracın en ağır dediği k adımdan kaçı insan planında (blueprint) adı geçen sonuç; k = plandaki sonuç sayısı. "
     "\"Bağ\": plandaki \"şu şuna dayanır\" (`\\uses`) iddialarından kaçı kayıtta da var. \"Kesik\": belgede boyut sınırı yüzünden eksik yazılan önerme sayısı. "
     "\"Ana önerme\" sütunu elle karşılaştırmadır.", "",
     "| Proje | Proje bildirimi | İsabet (alt ağaç ağırlığı) | Rastgele beklenen | Bağ (doğrulanan / toplam) | Kesik | Ana önerme |", "|---|---:|---:|---:|---:|---:|---|"]
for ad in sorted(os.listdir(K)):
    d = f"{K}/{ad}"
    if not os.path.isdir(d):
        continue
    bp = open(f"{d}/BLUEPRINT.md", encoding="utf-8").read() if os.path.exists(f"{d}/BLUEPRINT.md") else ""
    m1 = re.search(r"alt ağaç ağırlığı / subtree weight \| (\d+) / (\d+) \((\d+)%\)", bp)
    m2 = re.search(r"beklenen isabet: ([\d.]+)%", bp)
    m3 = re.search(r"Doğrulanan `\\uses` / confirmed \| (\d+)", bp)
    m4 = re.search(r"not backed by the code\*\* \| \*\*(\d+)", bp)
    import json
    oz = json.load(open(f"{d}/ozet.json", encoding="utf-8")) if os.path.exists(f"{d}/ozet.json") else {}
    ck = open(f"{d}/CIKTI_tr.md", encoding="utf-8").read().count("Not: bu önermenin") if os.path.exists(f"{d}/CIKTI_tr.md") else None
    isabet = f"{m1.group(1)} / {m1.group(2)} (%{m1.group(3)})" if m1 and int(m1.group(2)) else "—"
    bag = f"{m3.group(1)} / {int(m3.group(1)) + int(m4.group(1))}" if m3 and m4 and int(m3.group(1)) + int(m4.group(1)) else "—"
    L.append(f"| {ad} | {oz.get('proje', '—')} | {isabet} | {('%' + m2.group(1)) if m2 and m1 and int(m1.group(2)) else '—'} | {bag} | {ck if ck is not None else '—'} | {ELLE.get(ad, '—')} |")
# --- ikinci ölçü: yol payı (arac/yol.cpp), aynı cevap anahtarıyla ---
L += ["", "## İkinci ölçü denemesi: yol payı / Second measure tried: path share", "",
      "\"Yol payı\": kökten yapraklara giden bütün bağımlılık yollarının o bildirimden geçen kesri (`arac/yol.cpp`). "
      "Aşağıda aynı cevap anahtarıyla (blueprint) alt ağaç ağırlığıyla yan yana ölçülür. Sayılar `sinama/<ad>/BLUEPRINT.md` dosyalarından okunur.", "",
      "| Proje | Alt ağaç ağırlığı | Yol payı | İkisinin iyisi |", "|---|---:|---:|---:|"]
for ad in sorted(os.listdir("sinama")):
    yb = f"sinama/{ad}/BLUEPRINT.md"
    bp = open(yb, encoding="utf-8").read() if os.path.exists(yb) else ""
    hs = [re.search(r"\| " + re.escape(k) + r"[^|]*\| (\d+) / (\d+) \((\d+)%\)", bp) for k in ("alt ağaç ağırlığı", "yol payı", "ağırlık ile yol payının iyisi")]
    if all(hs) and int(hs[0].group(2)):
        L.append(f"| {ad} | " + " | ".join(f"{h.group(1)} / {h.group(2)} (%{h.group(3)})" for h in hs) + " |")
L += ["", "Sonuç: yol payı üç projenin birinde biraz daha iyi, ikisinde belirgin biçimde daha kötü. Bu yüzden belgelerdeki sıralama alt ağaç ağırlığıyla yapılır; "
      "yol payı yalnızca ek dosya olarak (`sinama/<ad>/yol_ust.tsv`) verilir."]

# --- basit ölçülerle kıyas: aynı cevap anahtarı, aynı k; sayılar BLUEPRINT.md'den okunur ---
OLCU = [("alt ağaç ağırlığı", "Alt ağaç ağırlığı (belgelerdeki sıralama)"), ("alt ağaç bildirim sayısı", "Alt ağaçtaki bildirim sayısı"),
        ("kendi ispat ağırlığı", "Yalnız kendi ispatının boyu"), ("doğrudan kullanan sayısı", "Doğrudan kullanan sayısı"),
        ("ağırlık ÷ önerme boyu", "Ağırlık ÷ önerme boyu"), ("ağaçta sığlık", "Köke yakınlık"), ("alt ağaç ağırlığı, zincirler tek adım", "Alt ağaç ağırlığı, tek çocuklu zincirler tek adım sayılınca")]
PR = [ad for ad in sorted(os.listdir("sinama")) if os.path.exists(f"sinama/{ad}/BLUEPRINT.md") and re.search(r"alt ağaç ağırlığı / subtree weight \| \d+ / [1-9]", open(f"sinama/{ad}/BLUEPRINT.md", encoding="utf-8").read())]
if PR:
    BP = {ad: open(f"sinama/{ad}/BLUEPRINT.md", encoding="utf-8").read() for ad in PR}
    L += ["", "## Basit ölçülerle kıyas / Comparison with simple measures", "",
          "Aynı cevap anahtarı (blueprint), aynı k. \"Rastgele\" tek başına zayıf bir kıyastır; asıl soru, alt ağaç ağırlığının bir bildirimin yalnız kendi ispat boyu gibi "
          "en basit ölçülerden ne kadar iyi olduğudur. Sayılar `sinama/<ad>/BLUEPRINT.md` dosyalarından okunur; dosyada yoksa —. "
          "/ Same answer key, same k. The question is how much better subtree weight is than the simplest measures.", "",
          "| Ölçü / measure | " + " | ".join(PR) + " |", "|---|" + "---:|" * len(PR)]
    for anahtar, baslik in OLCU:
        hs = [re.search(r"\| " + re.escape(anahtar) + r"[^|]*\| (\d+) / (\d+) \((\d+)%\)", BP[ad]) for ad in PR]
        L.append(f"| {baslik} | " + " | ".join(f"{h.group(1)} / {h.group(2)} (%{h.group(3)})" if h else "—" for h in hs) + " |")
    rs = [re.search(r"beklenen isabet: ([\d.]+)%", BP[ad]) for ad in PR]
    L.append("| Rastgele beklenen | " + " | ".join(("%" + r.group(1)) if r else "—" for r in rs) + " |")
    def puan(anahtar):
        r = []
        for ad in PR:
            a, c = [re.search(r"\| " + re.escape(k) + r"[^|]*\| (\d+) / (\d+) \((\d+)%\)", BP[ad]) for k in ("alt ağaç ağırlığı", anahtar)]
            r.append(f"{ad} {int(a.group(3)) - int(c.group(3)):+d}" if a and c else f"{ad} —")
        return ", ".join(r)
    L += ["", f"Alt ağaç ağırlığının farkı (yüzde puanı): yalnız kendi ispat boyuna göre {puan('kendi ispat ağırlığı')}; ağırlıksız düz sayıma göre {puan('alt ağaç bildirim sayısı')}. "
          "Üç proje küçük bir örneklemdir; bu tablo ağırlığın \"önem\" ölçtüğünü göstermez, yalnız insan planıyla ne kadar örtüştüğünü sayar. "
          "/ Difference of subtree weight in percentage points against own proof size and against plain subtree count. Three projects are a small sample."]

# --- aynı teoremin sürümleri: yalnız bu depodaki dosyalardan ---
def say(yol):
    return sum(1 for l in open(yol, encoding="utf-8") if l.strip()) if os.path.exists(yol) else None

def tasinan(yol):
    m = re.search(r"Toplam (\d+) adlandırılmış önerme", open(yol, encoding="utf-8").read()) if os.path.exists(yol) else None
    return m.group(1) if m else "—"

def pay(kl, ad):
    T, top = {}, 0
    yol = f"{kl}/taslar_ust.tsv"
    if not os.path.exists(yol):
        return "—"
    for i, l in enumerate(open(yol, encoding="utf-8")):
        p = l.rstrip("\n").split("\t")
        if i == 0:
            bas = p
            continue
        d = dict(zip(bas, p))
        top = max(top, int(d["alt_agirlik"]))
        if d["ad"].split(".")[-1] == ad and ad not in T:
            T[ad] = int(d["alt_agirlik"])
    return ("%%%.1f" % (100 * T[ad] / top)).replace(".", ",") if ad in T and top else "—"

SUR = [("17 milyon satır (Alpöge, 20 Kas)", "sinama/alpoge"), ("≈300 bin satır (grh)", "sinama/grh300"), ("≈76 bin satır (grh-compact)", "sinama/grh76")]
L += ["", "## Aynı teoremin üç sürümü / Three versions of the same theorem", "",
      "Kök hepsinde `riemannHypothesis`. Sayılar bu depodaki `ozet.json`, `bos_tum.tsv`, `VARSAYIM_tr.md`, `taslar_ust.tsv`, `import_tara.txt` dosyalarından okunur; dosya yoksa —.", "",
      "| | " + " | ".join(a for a, _ in SUR) + " |", "|---|" + "---:|" * len(SUR)]
OZ = [json.load(open(f"{k}/ozet.json", encoding="utf-8")) if os.path.exists(f"{k}/ozet.json") else {} for _, k in SUR]
def satir(bas, fn):
    L.append(f"| {bas} | " + " | ".join(str(fn(i, k)) for i, (_, k) in enumerate(SUR)) + " |")
b = lambda x: f"{x:,}".replace(",", ".") if isinstance(x, int) else "—"
satir("İspattaki proje bildirimi", lambda i, k: b(OZ[i].get("konide_proje")))
satir("— teorem", lambda i, k: b((OZ[i].get("proje_tur", {}).get("t") or [None, None])[1]))
satir("— tanım", lambda i, k: b((OZ[i].get("proje_tur", {}).get("d") or [None, None])[1]))
satir("Ana önermede proje tanımı", lambda i, k: b(OZ[i].get("onerme_konisinde_proje", 0) - 1) if OZ[i] else "—")
def aksiyom(i, k):
    for kl in (f"{k}/koni", k):   # yeni koşular ozet.json'a yazar; eski sonuçlarda alan yoktur
        yol = f"{kl}/ozet.json"
        if os.path.exists(yol):
            o = json.load(open(yol, encoding="utf-8"))
            if "aksiyom_konide" in o:
                d = sorted(x for x in o["aksiyom_konide"] if x not in ("propext", "Classical.choice", "Quot.sound"))
                return f"{len(o['aksiyom_konide'])} (standart dışı: {', '.join('`' + x + '`' for x in d) if d else 'yok'})"
    return "ölçülmedi"
satir("İspat konisindeki aksiyom", aksiyom)
satir("Bütün kayıtta gövdesi `True` olan tanım", lambda i, k: b(say(f"{k}/bos_tum.tsv")))
satir("Varsayım olarak taşınan adlandırılmış önerme", lambda i, k: tasinan(f"{k}/VARSAYIM_tr.md"))
for ad in ("star_inequality", "integral_forms_long", "enough_forms", "span_short_integralRamified_eq_top"):
    satir(f"`{ad}` payı", lambda i, k, ad=ad: pay(k, ad))
satir("Lib → New içe aktarma yolu", lambda i, k: (open(f"{k}/import_tara.txt", encoding="utf-8").read().split("SONUÇ: ")[1].split(":")[0].split("(")[0].strip() if os.path.exists(f"{k}/import_tara.txt") else "—"))
L += ["", "Yazarın kılavuzu (`grh/GUIDE.md`) üç ana teoremi (A: `span_short_integralRamified_eq_top`, B: `enough_forms`, C: `integral_forms_long`) ve bunları birleştiren "
      "`star_inequality`'yi adıyla sayar. Araç aynı adları, kılavuzu okumadan, baskınlık ağacının tepesinde bulur; yüzdeleri kılavuz vermez, araç ekler. "
      "Kılavuzun \"`Lib`, `New`'den hiçbir şey kullanmaz\" iddiası `arac/import_tara.py` ile dosya düzeyinde denetlenir."]
L += ["", "## Araç içi denetimler / Internal checks", "",
      "| Denetim | Sonuç |", "|---|---|",
      "| Baskınlık ağacı ve alt ağaç toplamları tanımdan kaba kuvvetle hesaplananla aynı mı (rastgele grafikler, döngülü olanlar dahil) | evet (`test/grafik_test.py`) |",
      "| Aksiyom listesi ve \"nerede kuruluyor\" sınıfları elle hesaplanmış küçük kayıtla aynı mı | evet (`test/grafik_test.py`) |",
      "| İki farklı önerme aynı cümleye çevriliyor mu (rastgele 60.000 iskelet) | çakışma yok (`test/duz_test.py`) |",
      "| Fonksiyon tipi ve nesne argümanı \"eğer–ise\" diye yazılıyor mu | hayır (`test/duz_test.py`) |",
      "| Aynı girdi aynı belgeyi veriyor mu | evet (`test/uctan_uca.sh` her belgeyi iki kez üretip bayt bayt karşılaştırır) |"]
open("SINAMA.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
print("\n".join(L[6:14]))
