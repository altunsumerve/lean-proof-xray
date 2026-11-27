#!/usr/bin/env python3
"""Döküm birleştir — kayıttan çıkan döküm (dokak) + varsa Lean dökümünün bağlayıcı tablosu.

TR: Resmi kayıt, α-denk ifadeleri tek kopyada tuttuğu için bazı sabitlerin "argüman açık mı örtük mü" işaretini
    kaybedebilir (ölçüm: 47.808 sabitte 28). Lean dökümü (Dok.lean) elde varsa bu işaretler oradan alınır.
    Bildirimlerin terimleri kayıttan gelir; iki dökümde ortak olan bildirimler bağlı değişken adları dışında aynıdır.
EN: Merge: declarations from the export-based dump; binder-kind table overridden by the Lean-based dump where available.
Kullanım: dok_birlestir.py dokak.jsonl.gz lean_dok.jsonl.gz cikti.jsonl.gz
"""
import gzip
import json
import sys


def main():
    a, b, c = sys.argv[1:4]
    tablo, onerme, lean_b = {}, set(), {}
    with gzip.open(b, "rt", encoding="utf-8") as f:
        for l in f:
            d = json.loads(l)
            if "baglayici" in d:
                tablo.update(d["baglayici"])
                onerme.update(d.get("onerme", []))
            else:
                lean_b[d["ad"]] = d["b"]
    n = duz = 0
    with gzip.open(a, "rt", encoding="utf-8") as f, gzip.open(c, "wt", encoding="utf-8", compresslevel=9) as o:
        for l in f:
            d = json.loads(l)
            if "baglayici" in d:
                t = d["baglayici"]
                duz = sum(1 for k in t if k in tablo and tablo[k] != t[k])
                t.update(tablo)
                o.write(json.dumps({"baglayici": t, "onerme": sorted(set(d.get("onerme", [])) | onerme)}, ensure_ascii=False, separators=(",", ":")) + "\n")
            else:
                if d["ad"] in lean_b:
                    d["b"] = lean_b[d["ad"]]
                o.write(json.dumps(d, ensure_ascii=False, separators=(",", ":")) + "\n")
                n += 1
    print("bildirim", n, "düzeltilen bağlayıcı", duz)


if __name__ == "__main__":
    main()
