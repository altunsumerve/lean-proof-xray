#!/bin/bash
# Hepsi / All — bir projenin bütün belgelerini tek komutla üretir.
# TR: Girdi klasörü (ağaç: taslar_ust.tsv, ozet.json, KONI.md) ve terim dökümü verilir; CIKTI, MANTIK, VARSAYIM, BOS, SOZLUK
#     belgeleri iki dilde yazılır. Süreçler sırayla çalışır (büyük dökümlerde bellek için).
# EN: Produces every document for a project from its tree folder and term dump, in both languages, sequentially.
# Kullanım / usage: arac/hepsi.sh <klasor> <dok.jsonl.gz> <kok_onerme_ya_da_-> [adim=8] [cikti_klasoru=<klasor>]
set -euo pipefail
K=$1; DK=$2; KOK=${3:--}; ADIM=${4:-8}; C=${5:-$K}
H=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$C"
# Taşınan önermeler konide nerede kuruluyor: tam grafik elde ise (KARSILA_GRAFIK=dugum.tsv ve kenar.bin'in klasörü,
# KARSILA_TASLAR=agac.cpp'nin taslar.tsv'si) arac/karsila.cpp koşar; değilse klasörde duran karsila.tsv kullanılır.
# Grafikte sayı bileşenleri `#0`, dökümde `0` yazılır: adlar gidişte ve dönüşte çevrilir.
KT="$K/karsila.tsv"
if [ -n "${KARSILA_GRAFIK:-}" ] && [ -f "$KARSILA_GRAFIK/kenar.bin" ] && [ -f "${KARSILA_TASLAR:-}" ]; then
  G=$(mktemp -d)
  if g++ -O2 -o "$G/karsila" "$H/karsila.cpp" \
     && python3 "$H/varsayim.py" --kok "$K" --dok "$DK" --dil tr --adlar-yaz "$G/adlar.txt" --cikti "$G/gecici.md" > /dev/null \
     && sed -E ':a; s/\.([0-9]+)(\.|$)/.#\1\2/; ta' "$G/adlar.txt" > "$G/hedef.txt" \
     && "$G/karsila" "$KARSILA_GRAFIK/dugum.tsv" "$KARSILA_GRAFIK/kenar.bin" "$G/hedef.txt" "$KARSILA_TASLAR" "$G/k.tsv"; then
    sed -E 's/\.#([0-9]+)/.\1/g' "$G/k.tsv" > "$C/karsila.tsv"; KT="$C/karsila.tsv"
  else
    echo "karsila kosmadi; VARSAYIM belgesi grafik sutunu olmadan yazilacak" >&2
  fi
  rm -rf "$G"
fi
KA=(); [ -f "$KT" ] && KA=(--karsila "$KT")
# bütün kayıtta gövdesi True olan tanımlar (ayikla.cpp AYIKLA_BOS çıktısı) klasörde duruyorsa BOS belgesine D bölümü olarak girer
BT=(); [ -f "$K/bos_tum.tsv" ] && BT=(--tum "$K/bos_tum.tsv")
for d in tr en; do
  python3 "$H/belge.py" --kok "$K" --dok "$DK" --dil $d --adim "$ADIM" --cikti "$C/CIKTI_$d.md"
  python3 "$H/varsayim.py" --kok "$K" --dok "$DK" --dil $d "${KA[@]}" --cikti "$C/VARSAYIM_$d.md"
  python3 "$H/bos.py" --kok "$K" --dok "$DK" --dil $d "${BT[@]}" --cikti "$C/BOS_$d.md"
  if [ "$KOK" != "-" ]; then
    python3 "$H/mantik.py" --kok "$K" --dok "$DK" --dil $d --kok-onerme "$KOK" --cikti "$C/MANTIK_$d.md"
  fi
done
echo "bitti: $C"
