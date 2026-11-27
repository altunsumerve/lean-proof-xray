#!/bin/bash
# Uçtan uca / End to end — elle yazılmış küçük kayıt, xray-export iş akışının adımlarından geçer (Lean gerekmez).
# TR: koni → kütüphane ayrımı → agac → koni_rapor → ayikla (iki geçiş) → dokak → hepsi (karsila dahil).
#     Beklenen: H yapısı `build` içinde kuruluyor, G tanımı onu taşımayan `via_def` içinde kullanılıyor; propext kütüphane.
# EN: The tiny hand-made export goes through every step of the xray-export workflow; expected classes are checked.
set -euo pipefail
cd "$(dirname "$0")/.."
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
python3 -I - "$T" <<'P' > /dev/null
import sys
sys.path.insert(0, "test"); import grafik_test as g
koni, agac, kar = [g.derle(sys.argv[1], x) for x in ("koni", "agac", "karsila")]
g.kucuk_kayit(sys.argv[1], koni, agac, kar)
P
export KUNYE_KAPASITE=4096
S=$T/sonuc; mkdir -p "$S" "$T/kn"
g++ -O2 -o "$T/ayikla_x" arac/ayikla.cpp
"$T/koni" "$T/g.bin" "$T/kn" < "$T/kayit.ndjson" 2> /dev/null
printf '%s\n' root build via_def uses_H uses_G H G Q projAx lonely unusedAx > "$T/kokler.txt"
awk -F'\t' 'NR==FNR { if ($1 != "") k[$1]=1; next } { n = split($3, p, "."); b = p[1]; if (b == "_private") for (i = 2; i < n; i++) if (p[i] == "#0") { b = p[i+1]; break } if (!(b in k)) print $3 }' "$T/kokler.txt" "$T/kn/dugum.tsv" > "$T/kut.txt"
[ "$(cat "$T/kut.txt")" = "propext" ] || { echo "kütüphane ayrımı beklenmedik: $(cat "$T/kut.txt")"; exit 1; }
echo root > "$T/kok.txt"
"$T/agac" "$T/kn/dugum.tsv" "$T/kn/kenar.bin" "$T/kok.txt" "$T/kut.txt" "$S" 2> /dev/null
python3 -I arac/koni_rapor.py --koni "$S" --md "$S/KONI.md" --ust "$S/taslar_ust.tsv" > /dev/null
awk -F'\t' 'NR > 1 { print $1 }' "$S/taslar_ust.tsv" > "$T/kok_ad.txt"
python3 -I arac/onerme_koni.py "$T/kn/dugum.tsv" "$T/kn/kenar.bin" "$T/kok_ad.txt" "$T/kut.txt" > "$T/ad.txt" 2> /dev/null
grep -qx H "$T/ad.txt" && grep -qx G "$T/ad.txt" && ! grep -qx propext "$T/ad.txt" || { echo "önerme konisi beklenmedik"; cat "$T/ad.txt"; exit 1; }
awk -F'\t' 'NR > 1 && $9 <= 3000 { print $1 }' "$S/taslar_ust.tsv" > "$T/ispat.txt"
AYIKLA_BOS="$S/bos_tum.tsv" "$T/ayikla_x" 1 "$T/a.bin" "$T/ad.txt" "$T/ispat.txt" < "$T/kayit.ndjson" 2> /dev/null
"$T/ayikla_x" 2 "$T/a.bin" "$T/ad.txt" "$T/ispat.txt" < "$T/kayit.ndjson" > "$T/ay.ndjson" 2> /dev/null
python3 -I arac/dokak.py "$T/ay.ndjson" "$S/dokak.jsonl.gz" 4000 3000 > /dev/null
KARSILA_GRAFIK="$T/kn" KARSILA_TASLAR="$S/taslar.tsv" bash arac/hepsi.sh "$S" "$S/dokak.jsonl.gz" - 8 "$S/belge" > /dev/null 2>&1
for f in CIKTI_tr.md CIKTI_en.md VARSAYIM_tr.md VARSAYIM_en.md BOS_tr.md BOS_en.md karsila.tsv; do [ -s "$S/belge/$f" ] || { echo "eksik: $f"; exit 1; }; done
awk -F'\t' '$1 == "H" && $9 == "kuruluyor" && $10 ~ /^build/ { h = 1 } $1 == "G" && $9 == "iceride" { g = 1 } END { exit !(h && g) }' "$S/belge/karsila.tsv" || { echo "karsila sınıfları beklenmedik"; cat "$S/belge/karsila.tsv"; exit 1; }
# tekrarlanabilirlik: aynı girdiyle ikinci üretim bayt bayt aynı olmalı
KARSILA_GRAFIK="$T/kn" KARSILA_TASLAR="$S/taslar.tsv" bash arac/hepsi.sh "$S" "$S/dokak.jsonl.gz" - 8 "$S/belge2" > /dev/null 2>&1
for f in "$S"/belge/*; do cmp -s "$f" "$S/belge2/$(basename "$f")" || { echo "ikinci üretim farklı: $(basename "$f")"; exit 1; }; done
grep -q 'grafik: kurucusu `build` içinde kullanılıyor' "$S/belge/VARSAYIM_tr.md" || { echo "VARSAYIM belgesinde grafik satırı yok"; exit 1; }
grep -q '| `projAx` | \*\*standart dışı' "$S/KONI.md" || { echo "KONI.md aksiyom satırı yok"; exit 1; }
echo "uçtan uca: küçük kayıt bütün adımlardan geçti; aksiyom, karşılama ve belgeler beklenenle aynı"
