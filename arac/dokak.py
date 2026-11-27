#!/usr/bin/env python3
"""Dökak — lean4export NDJSON'undan (ayikla.cpp çıktısı) terim dökümü; Lean derlemesi gerekmez.

TR: `kitapcik/Dok.lean` ile aynı biçimde yazar (sozel.py / duz.py / belge.py doğrudan okur). Girdi küçük olmalıdır:
    resmi kayıt önce `arac/ayikla.cpp` ile istenen bildirimlere indirilir. Teoremin ispatı kayıtta varsa ve
    düğüm bütçesine sığıyorsa "ispat" alanına yazılır (yapıştırıcı adımlarda "kim kimi kullanıyor" için).
EN: Converts a (filtered) lean4export NDJSON into the same term-dump format as Dok.lean, without building Lean.

Kullanım / usage: dokak.py ayiklanmis.ndjson cikti.jsonl[.gz] [dugum_butcesi=4000] [ispat_butcesi=400]
"""
import gzip
import json
import sys

BK = {"default": "e", "implicit": "i", "strictImplicit": "i", "instImplicit": "c"}


def main():
    yol, cikti = sys.argv[1], sys.argv[2]
    butce0 = int(sys.argv[3]) if len(sys.argv) > 3 else 4000
    ispat_butce = int(sys.argv[4]) if len(sys.argv) > 4 else min(butce0, 400)   # ispat terimi için düğüm bütçesi
    class Adlar:
        """Ad tablosu: tam ad istenince kurulur (milyonlarca adın hepsini dizgeye çevirmemek için)."""
        def __init__(self):
            self.pre, self.par, self.tam = [0], [""], {0: ""}

        def ekle(self, i, pre, par):
            assert i == len(self.pre), "ad sırası"
            self.pre.append(pre)
            self.par.append(par)

        def __getitem__(self, i):
            t = self.tam.get(i)
            if t is None:
                zincir, j = [], i
                while j not in self.tam:
                    zincir.append(j)
                    j = self.pre[j]
                t = self.tam[j]
                for k in reversed(zincir):
                    t = (t + "." if t else "") + self.par[k]
                    self.tam[k] = t
            return t

    adlar, ifade, bild = Adlar(), [], []
    ac = gzip.open if yol.endswith(".gz") else open
    with ac(yol, "rt", encoding="utf-8") as f:
        for s in f:
            d = json.loads(s)       # anahtar sırası kayıtta değişebilir: satır türü anahtarlara bakılarak belirlenir
            if "in" in d:
                if "str" in d:
                    adlar.ekle(d["in"], d["str"]["pre"], d["str"]["str"])
                else:
                    adlar.ekle(d["in"], d["num"]["pre"], str(d["num"]["i"]))
            elif "ie" in d:
                assert d["ie"] == len(ifade), f"ifade sırası: {d['ie']} != {len(ifade)}"
                # sıkı gösterim (bellek için): demet
                if "app" in d:
                    t = ("a", d["app"]["fn"], d["app"]["arg"])
                elif "bvar" in d:
                    t = ("b", d["bvar"])
                elif "const" in d:
                    t = ("c", d["const"]["name"])
                elif "sort" in d:
                    t = ("s", d["sort"])
                elif "lam" in d or "forallE" in d:
                    k = "l" if "lam" in d else "p"
                    v = d["lam" if k == "l" else "forallE"]
                    t = (k, v["name"], BK.get(v.get("binderInfo", "default"), "e"), v["type"], v["body"])
                elif "letE" in d:
                    v = d["letE"]
                    t = ("z", v["name"], v["type"], v["value"], v["body"])
                elif "proj" in d:
                    v = d["proj"]
                    t = ("j", v["typeName"], v["idx"], v["struct"])
                elif "natVal" in d:
                    t = ("n", int(d["natVal"]))
                elif "strVal" in d:
                    t = ("t", d["strVal"])
                elif "mdata" in d:
                    t = ("m", d["mdata"]["expr"])
                else:
                    t = ("?",)
                ifade.append(t)
            elif "il" in d or "meta" in d:
                continue
            else:
                bild.append(d)

    def yaz(i, B):
        """ifade kimliği → ağaç; B: [kalan düğüm bütçesi]."""
        if B[0] <= 0 or i < 0:
            return "…"
        B[0] -= 1
        d = ifade[i]
        k = d[0]
        if k == "b":
            return ["b", d[1]]
        if k == "s":
            return ["s", "Prop" if d[1] == 0 else "Type"]
        if k == "c":
            return ["c", adlar[d[1]]]
        if k == "a":
            args, j = [], i
            while ifade[j][0] == "a":
                args.append(ifade[j][2])
                j = ifade[j][1]
            r = ["a", yaz(j, B)]
            for x in reversed(args):
                r.append(yaz(x, B))
            return r
        if k in ("l", "p"):
            return [k, adlar[d[1]], d[2], yaz(d[3], B), yaz(d[4], B)]
        if k == "z":
            return ["z", adlar[d[1]], yaz(d[2], B), yaz(d[3], B), yaz(d[4], B)]
        if k == "j":
            return ["j", adlar[d[1]], d[2], yaz(d[3], B)]
        if k in ("n", "t"):
            return [k, d[1]]
        if k == "m":
            B[0] += 1
            return yaz(d[1], B)
        return "…"

    def bag(i):
        s = ""
        while i >= 0:
            d = ifade[i]
            if d[0] == "m":
                i = d[1]
            elif d[0] == "p":
                s += d[2]
                i = d[4]
            else:
                break
        return s

    def prop_mu(i):
        while i >= 0 and ifade[i][0] in ("p", "m"):
            i = ifade[i][4] if ifade[i][0] == "p" else ifade[i][1]
        return i >= 0 and ifade[i][0] == "s" and ifade[i][1] == 0

    sys.setrecursionlimit(200000)
    tablo, onerme, satirlar = {}, [], []

    def kayit(ad, tur, tip, deger=None, ispat=None, ek=None):
        if tip is None or tip < 0:
            return
        if tur != "tip" and (deger is None or deger < 0) and (ispat is None or ispat < 0) and tur in ("tanim",):
            # yalnız tipi yazılmış sabit (kullanıldığı için eklendi): tabloya girer, bildirim olarak yazılmaz
            tablo[ad] = bag(tip)
            if prop_mu(tip):
                onerme.append(ad)
            return
        B = [butce0]
        jt = yaz(tip, B)
        o = {"ad": ad, "tur": tur, "b": bag(tip), "tip": jt, "tipTam": B[0] > 0}
        if deger is not None and deger >= 0:
            B = [butce0]
            o["govde"] = yaz(deger, B)
            o["govdeTam"] = B[0] > 0
        if ispat is not None and ispat >= 0:
            B = [ispat_butce]
            j = yaz(ispat, B)
            if B[0] > 0:
                o["ispat"] = j
        if ek:
            o.update(ek)
        tablo[ad] = o["b"]
        if prop_mu(tip):
            onerme.append(ad)
        satirlar.append(o)

    for d in bild:
        if "thm" in d:
            v = d["thm"]
            kayit(adlar[v["name"]], "teorem", v["type"], ispat=v.get("value", -1))
        elif "def" in d:
            v = d["def"]
            kayit(adlar[v["name"]], "tanim", v["type"], deger=v.get("value", -1))
        elif "opaque" in d:
            v = d["opaque"]
            kayit(adlar[v["name"]], "opak", v["type"])
        elif "axiom" in d:
            v = d["axiom"]
            kayit(adlar[v["name"]], "aksiyom", v["type"])
        elif "inductive" in d:
            v = d["inductive"]
            for t in v.get("types", []):
                kayit(adlar[t["name"]], "tip", t["type"], ek={"kurucular": [adlar[c] for c in t.get("ctors", [])], "parametre": t.get("numParams", 0)})
            for c in v.get("ctors", []):
                kayit(adlar[c["name"]], "kurucu", c["type"])
    # gzip başlığına saat ve dosya adı yazılmaz: aynı girdi, bayt bayt aynı çıktı
    import io
    if cikti.endswith(".gz"):
        ham = open(cikti, "wb")
        o = io.TextIOWrapper(gzip.GzipFile(filename="", mode="wb", fileobj=ham, mtime=0), encoding="utf-8")
    else:
        o = open(cikti, "w", encoding="utf-8")
    with o:
        for s in satirlar:
            o.write(json.dumps(s, ensure_ascii=False, separators=(",", ":")) + "\n")
        o.write(json.dumps({"baglayici": tablo, "onerme": sorted(onerme)}, ensure_ascii=False, separators=(",", ":")) + "\n")
    print("bildirim", len(satirlar), "ifade", len(ifade), file=sys.stderr)


if __name__ == "__main__":
    main()
