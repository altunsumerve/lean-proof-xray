#!/usr/bin/env python3
"""Evrak / Report — bir ispatın röntgenini tek belgede toplar (HTML; Chrome varsa PDF).

TR: Sonuç klasöründeki dosyalardan (ozet.json, taslar_ust.tsv, aksiyomlar.tsv, bos_tum.tsv, VARSAYIM, KONI) ve varsa
    hikâyeden (HIKAYE_<dil>.md, yoksa HIKAYE.md) dört bölümlük bir belge yazar: özet, herkes için, matematikçi için,
    kanıt sayfası. Bu betikte yapay zekâ yoktur; hikâye bölümleri dosyadan olduğu gibi alınır ve "dil modeli yazdı"
    diye etiketlenir. Aynı girdi aynı HTML'i verir.
EN: One document per proof from the files of a result folder, in Turkish or English. No AI here; the story sections
    are taken verbatim from the story file and labelled as written by a language model.
Kullanım / usage: evrak.py --klasor sinama/grh76 --dil tr|en [--pdf]     -> <klasor>/RAPOR_<dil>.html (ve .pdf)
"""
import argparse
import html
import json
import os
import re
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "hikaye"))
import harita  # noqa: E402

M = {
    "tr": dict(baslik="Röntgen raporu", alt="Bir Lean ispatının içinde ne var", ozet="Özet", herkes="Herkes için", mat="Matematikçi için", fikir="Beş cümlede fikir",
               bilin="Anlatıcının anlayamadıkları", kanit="Kanıt sayfası", teorem="Kök teorem", kaynak="Kaynak",
               iddia="Ne kanıtlıyor", iddia_t="Ana cümle yalnızca kütüphane kavramlarıyla yazılmış; içinde projeye özgü tanım yok.",
               iddia_p="Ana cümleyi okumak için {n} proje tanımını açmak gerekiyor.", aks="Neye dayanıyor",
               aks_t="Yalnızca Lean'in standart aksiyomları ({l}). Eksik bırakılmış ispat yok.", aks_d="Standart dışı aksiyom var: {l}.", aks_y="Aksiyom listesi bu sonuçta ölçülmedi.",
               boy="Ne kadar büyük", boy_t="İspatta {n} proje bildirimi var; {t} tanesi teorem.", yol="Hangi yoldan gidiyor", yol_t="İspatın düğüm noktası: {a} (payı %{p}; ispatın bu kadarı yalnızca onun için var).",
               bos="Hiçbir şey sınamayan koşul", bos_0="Bulunmadı (bütün kayıt tarandı).", bos_n="{n} tanım, argümanlarına bakmadan True: {l}.", bos_y="Taranmadı.",
               tas="Varsayım olarak taşınan önerme", tas_y="Güncel taramayla ölçülmedi.", tas_n="{n} adlandırılmış önerme ispat boyunca varsayım olarak taşınıyor; hepsi ispatın içinde karşılanıyor (ana teorem koşulsuz).", kop="Tekrar", kop_t="Teorem önermelerinin %{p} kadarı, başka adla zaten var olan bir cümlenin kopyası.",
               adimlar="En büyük adımlar", ad="Adım", pay="Pay", icin="Yalnızca şunun için var", denetim="Hikâyenin denetimi",
               den_t="Hikâyede adı geçen {a} adımın {b} tanesi ispatın gerçek adımı. {c} yapısal iddianın {d} tanesi haritayla doğrulandı; {e} yanlış. Hikâyenin hiç anmadığı büyük adım: {f}.",
               soru_t="Aracın haritadan çıkardığı {n} zorunlu sorudan {a} tanesi cevaplandı; {b} tanesi “bulunamadı” olarak işaretlendi.", hik_yok="Bu ispat için henüz hikâye yazılmadı. Harita hazır; hikâye adımı arac/hikaye/ANLATICI.md ile çalıştırılır.",
               kim="Kim ne yaptı", kim_t="Özet ve kanıt sayfasındaki her sayı, Lean'in kendi kaydından sabit kurallarla sayıldı; yapay zekâ kullanılmadı ve yeniden koşturan herkes aynı sayıları alır. "
               "“Herkes için”, “Beş cümlede fikir”, “Matematikçi için” ve “Anlayamadıkları” bölümlerini bir dil modeli (Claude) yazdı; model yalnızca haritayı ve istediği tek tek bildirimlerin kodunu gördü. "
               "Denetçi hikâyenin yapısını doğrular (adımlar gerçek mi, yerleri ve ağırlıkları doğru mu); matematik okumasını doğrulamaz. O okuma bir matematikçi tarafından onaylanmadı.",
               pay_not="“Pay”: ispatın yalnızca o adım için var olan kısmı. Önem ölçüsü değildir.", model="dil modeli (Claude) yazdı", arac="araç saydı", cevrilmemis="(Bu bölümün Türkçesi yok; İngilizce aslı gösteriliyor.)"),
    "en": dict(baslik="X-ray report", alt="What is inside a Lean proof", ozet="Summary", herkes="For everyone", mat="For a mathematician", fikir="The idea in five sentences",
               bilin="What the narrator could not tell", kanit="Evidence", teorem="Root theorem", kaynak="Source",
               iddia="What it proves", iddia_t="The main statement is written with library notions only; no project definition is inside it.",
               iddia_p="Reading the main statement requires opening {n} project definitions.", aks="What it rests on",
               aks_t="Only Lean's standard axioms ({l}). No missing proof.", aks_d="Non-standard axioms present: {l}.", aks_y="The axiom list was not measured in this result.",
               boy="How large", boy_t="The proof has {n} project declarations; {t} of them are theorems.", yol="Which way it goes", yol_t="The junction of the proof: {a} (share {p}%: that much of the proof exists only for it).",
               bos="Conditions that test nothing", bos_0="None found (the whole export was scanned).", bos_n="{n} definitions are True whatever their arguments: {l}.", bos_y="Not scanned.",
               tas="Statements carried as hypotheses", tas_y="Not measured with the current scan.", tas_n="{n} named statements are carried as hypotheses through the proof; all are supplied inside it (the main theorem is unconditional).", kop="Repetition", kop_t="{p}% of the theorem statements are copies, under another name, of a statement already there.",
               adimlar="The largest steps", ad="Step", pay="Share", icin="Exists only for", denetim="The check of the story",
               den_t="{b} of the {a} names in the story are real steps of the proof. {d} of {c} structural claims were confirmed against the map; {e} wrong. Heavy steps the story never mentions: {f}.",
               soru_t="Of the {n} required questions the tool derives from the map, {a} were answered and {b} were marked “not found”.", hik_yok="No story has been written for this proof yet. The map is ready; the story step is run with arac/hikaye/ANLATICI.md.",
               kim="Who did what", kim_t="Every number in the summary and on the evidence page was counted by fixed rules from Lean's own export; no AI was used and anyone who reruns it gets the same numbers. "
               "The sections “For everyone”, “The idea in five sentences”, “For a mathematician” and “What the narrator could not tell” were written by a language model (Claude), which saw only the map and the code of the single declarations it asked for. "
               "The checker confirms the structure of the story (are the steps real, in their real places, with their real weights); it does not confirm the mathematical reading. That reading has not been reviewed by a mathematician.",
               pay_not="“Share”: the part of the proof that exists only for that step. It is not a measure of importance.", model="written by a language model (Claude)", arac="counted by the tool", cevrilmemis=""),
}
STANDART = ("propext", "Classical.choice", "Quot.sound")


def md(s):
    """Hikâye metni için en küçük Markdown: paragraf, madde, numaralı liste, `kod`, **kalın**, [bağlantı](x) -> metin."""
    def ic(t):
        t = html.escape(t)
        t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
        t = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", t)
        return re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)
    r, liste = [], None
    for l in s.strip().split("\n"):
        m = re.match(r"\s*(?:(-)|(\d+)\.)\s+(.*)", l)
        if m:
            tur = "ul" if m.group(1) else "ol"
            if liste != tur:
                if liste:
                    r.append(f"</{liste}>")
                r.append(f"<{tur}>")
                liste = tur
            r.append(f"<li>{ic(m.group(3))}</li>")
            continue
        if liste:
            r.append(f"</{liste}>")
            liste = None
        if l.strip():
            r.append(f"<p>{ic(l.strip())}</p>")
    if liste:
        r.append(f"</{liste}>")
    return "\n".join(r)


def sayi(n, dil):
    return f"{n:,}".replace(",", "." if dil == "tr" else ",")


def yuzde(x, dil):
    return f"{x:.1f}".replace(".", "," if dil == "tr" else ".")


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--klasor", required=True)
    a.add_argument("--dil", choices=["tr", "en"], default="en")
    a.add_argument("--pdf", action="store_true")
    A = a.parse_args()
    K, dil, S = A.klasor.rstrip("/"), A.dil, M[A.dil]
    oku = lambda f: open(f"{K}/{f}", encoding="utf-8").read() if os.path.exists(f"{K}/{f}") else None
    O = json.loads(oku("ozet.json"))
    T, top = harita.agac(K)
    pay = lambda n: 100 * int(T[n]["alt_agirlik"]) / top
    kok = O["kok"][0]
    # --- özet satırları (araç saydı) ---
    satir = []
    n = max(0, O["onerme_konisinde_proje"] - 1)   # kökün kendisi sayılmaz
    satir.append(("ok" if n == 0 else "bilgi", S["iddia"], S["iddia_t"] if n == 0 else S["iddia_p"].format(n=sayi(n, dil))))
    if "aksiyom_konide" in O:
        disi = [x for x in O["aksiyom_konide"] if x not in STANDART]
        satir.append(("uyari", S["aks"], S["aks_d"].format(l=", ".join(disi))) if disi else ("ok", S["aks"], S["aks_t"].format(l=", ".join(sorted(O["aksiyom_konide"])))))
    else:
        satir.append(("bilgi", S["aks"], S["aks_y"]))
    satir.append(("bilgi", S["boy"], S["boy_t"].format(n=sayi(O["konide_proje"], dil), t=sayi(O["proje_tur"].get("t", [0, 0])[1], dil))))
    # en çok ispat taşıyan, kök zincirinin dışındaki ilk adım: payı %100'den küçük ilk teorem
    sirali = sorted(T, key=lambda n: (-int(T[n]["alt_agirlik"]), n))
    ilk = next((n for n in sirali if T[n]["tur"] == "t" and pay(n) < 99.0), None)
    if ilk:
        satir.append(("bilgi", S["yol"], S["yol_t"].format(a=f"<code>{html.escape(ilk)}</code>", p=yuzde(pay(ilk), dil))))
    b = oku("bos_tum.tsv")
    if b is None:
        satir.append(("bilgi", S["bos"], S["bos_y"]))
    else:
        adlar = [l.split("\t")[0] for l in b.splitlines() if l.strip()]
        satir.append(("ok", S["bos"], S["bos_0"]) if not adlar else ("uyari", S["bos"], S["bos_n"].format(n=len(adlar), l=", ".join(f"<code>{html.escape(x.split('.')[-1])}</code>" for x in adlar[:10]))))
    v = oku(f"VARSAYIM_{dil}.md") or oku("VARSAYIM_tr.md") or ""
    m = re.search(r"(?:Toplam|Total|In total)[^\d]*(\d+)", v)
    if m and oku("karsila.tsv") is not None:      # karsila.tsv: tanımları açan güncel taramanın izi
        satir.append(("bilgi", S["tas"], S["tas_n"].format(n=m.group(1))) if int(m.group(1)) else ("ok", S["tas"], "0"))
    else:
        satir.append(("bilgi", S["tas"], S["tas_y"]))
    k = re.search(r"fazladan kopya: \*\*[\d.]+\*\* \(%([\d,]+)\)", oku("KONI.md") or "")
    if k:
        satir.append(("bilgi", S["kop"], S["kop_t"].format(p=k.group(1) if dil == "tr" else k.group(1).replace(",", "."))))
    isaret = {"ok": "✓", "uyari": "!", "bilgi": "·"}
    # --- hikâye (dil modeli yazdı; dosyadan olduğu gibi) ---
    h = oku(f"HIKAYE_{dil}.md")
    cevrilmemis = False
    if h is None and oku("HIKAYE.md"):
        h, cevrilmemis = oku("HIKAYE.md"), dil != "en"
    bolum = {}
    if h:
        govde = h.split("\n# ", 1)[-1].split("\n## Claims")[0]
        parcalar = re.split(r"\n## [^\n]*\n", "\n" + govde.split("\n", 1)[1])[1:]
        for ad, p in zip(("fikir", "mat", "herkes", "bilin"), parcalar):
            bolum[ad] = md(p)
    # --- denetim (araç saydı) ---
    c = oku("HIKAYE.check.txt") or ""
    d1 = re.search(r"names in the story: (\d+); steps of the proof: (\d+)", c)
    d2 = re.search(r"claims: (\d+); confirmed (\d+); wrong (\d+)", c)
    d3 = re.search(r"never mentions: (\d+)", c)
    denetim = S["den_t"].format(a=d1.group(1), b=d1.group(2), c=d2.group(1), d=d2.group(2), e=d2.group(3), f=d3.group(1)) if d1 and d2 and d3 else None
    d4 = re.search(r"required questions: (\d+); answered (\d+); answered NOT FOUND (\d+)", c)
    if denetim and d4:
        denetim += " " + S["soru_t"].format(n=d4.group(1), a=d4.group(2), b=d4.group(3))
    # --- HTML ---
    e = html.escape
    Y = [f"<!DOCTYPE html><html lang='{dil}'><head><meta charset='utf-8'><title>{S['baslik']}: {e(kok)}</title><style>",
         "@page{size:A4;margin:18mm 17mm}body{font-family:'DejaVu Sans','Noto Sans',Arial,sans-serif;font-size:10.5pt;line-height:1.5;color:#1a1a1a;max-width:176mm;margin:0 auto}",
         "h1{font-size:21pt;margin:0 0 2pt}h2{font-size:13.5pt;margin:20pt 0 6pt;padding-bottom:3pt;border-bottom:1.5pt solid #1a1a1a}h2 small{font-size:8pt;font-weight:normal;color:#666;float:right;margin-top:5pt}",
         ".alt{color:#555;margin:0 0 12pt}.kunye{font-size:9pt;color:#444;margin-bottom:10pt}code{font-family:'DejaVu Sans Mono',monospace;font-size:9pt;background:#f1f1ee;padding:0 2pt;border-radius:2pt;word-break:break-all}",
         "table{border-collapse:collapse;width:100%;font-size:9.5pt}td,th{padding:4pt 6pt;border-bottom:.5pt solid #ccc;vertical-align:top;text-align:left}th{border-bottom:1pt solid #1a1a1a}td.s{text-align:right;white-space:nowrap}",
         ".ozet td:first-child{width:14pt;font-weight:bold;text-align:center}.ozet td:nth-child(2){width:32%;font-weight:bold}.ok td:first-child{color:#1c7c3c}.uyari td:first-child{color:#b45309}.bilgi td:first-child{color:#777}",
         ".herkes{font-size:11.5pt;line-height:1.6}.not{font-size:8.5pt;color:#555}.kutu{background:#f6f6f3;border-left:3pt solid #999;padding:7pt 10pt;font-size:9pt;margin-top:8pt}li{margin-bottom:4pt}.sayfa{page-break-before:always}",
         "</style></head><body>",
         f"<h1>{S['baslik']}</h1><p class='alt'>{S['alt']}</p>",
         f"<p class='kunye'><b>{S['teorem']}:</b> <code>{e(kok)}</code><br><b>{S['kaynak']}:</b> {e((oku('kaynak.txt') or '').strip())}</p>",
         f"<h2>{S['ozet']} <small>{S['arac']}</small></h2><table class='ozet'>"]
    for tur, ad, metin in satir:
        Y.append(f"<tr class='{tur}'><td>{isaret[tur]}</td><td>{ad}</td><td>{metin}</td></tr>")
    Y.append("</table>")
    if bolum:
        not_ = f"<p class='not'>{S['cevrilmemis']}</p>" if cevrilmemis else ""
        Y.append(f"<h2>{S['herkes']} <small>{S['model']}</small></h2>{not_}<div class='herkes'>{bolum.get('herkes', '')}</div>")
        Y.append(f"<h2 class='sayfa'>{S['fikir']} <small>{S['model']}</small></h2>{bolum.get('fikir', '')}")
        Y.append(f"<h2>{S['mat']} <small>{S['model']}</small></h2>{bolum.get('mat', '')}")
        Y.append(f"<h2>{S['bilin']} <small>{S['model']}</small></h2>{bolum.get('bilin', '')}")
    else:
        Y.append(f"<h2>{S['herkes']}</h2><p>{S['hik_yok']}</p>")
    Y.append(f"<h2 class='sayfa'>{S['kanit']} <small>{S['arac']}</small></h2><h3>{S['adimlar']}</h3><table><tr><th>{S['ad']}</th><th>{S['pay']}</th><th>{S['icin']}</th></tr>")
    for n in [x for x in sirali if T[x]["tur"] == "t"][:14]:
        Y.append(f"<tr><td><code>{e(n)}</code></td><td class='s'>%{yuzde(pay(n), dil)}</td><td>{'—' if T[n]['baskin'] == '<kok>' else '<code>' + e(T[n]['baskin']) + '</code>'}</td></tr>")
    Y.append(f"</table><p class='not'>{S['pay_not']}</p>")
    if denetim:
        Y.append(f"<h3>{S['denetim']}</h3><p>{denetim}</p>")
    Y.append(f"<div class='kutu'><b>{S['kim']}.</b> {S['kim_t']}</div><p class='not'>lean-proof-xray · github.com/altunsumerve/lean-proof-xray</p></body></html>")
    cikti = f"{K}/RAPOR_{dil}.html"
    open(cikti, "w", encoding="utf-8").write("\n".join(Y) + "\n")
    print(cikti)
    if A.pdf:
        chrome = next((x for x in ("google-chrome", "chromium", "chromium-browser") if shutil.which(x)), None)
        if not chrome:
            print("PDF için Chrome bulunamadı / no Chrome for the PDF", file=sys.stderr)
            return 1
        pdf = cikti[:-5] + ".pdf"
        subprocess.run([chrome, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={pdf}", "file://" + os.path.abspath(cikti)],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(pdf)
    return 0


if __name__ == "__main__":
    sys.exit(main())
