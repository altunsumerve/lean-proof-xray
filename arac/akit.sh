#!/bin/bash
# Akıt / Stream — bir lean4export kaydını URL'den stdout'a akıtır; .zst ve .gz ise açar.
# TR: Dosya boyu sunucudan sorulur; indirme 256 MB'lık parçalarla yapılır (arac/parca_akis.sh), kopan parça yeniden istenir.
# EN: Streams a lean4export file from a URL to stdout in ranged chunks, decompressing .zst / .gz.
# Kullanım / usage: arac/akit.sh <url>
set -euo pipefail
U=$1; H=$(cd "$(dirname "$0")" && pwd)
BOY=$(curl -sSfIL "$U" | tr -d '\r' | awk 'tolower($1) == "content-length:" { b = $2 } END { print b }')
if [ -z "$BOY" ]; then echo "dosya boyu okunamadi / could not read the file size: $U" >&2; exit 1; fi
echo "kayit $U boy $BOY" >&2
case "${U%%\?*}" in
  *.zst) bash "$H/parca_akis.sh" "$U" "$BOY" | zstd -dc --long=31 ;;
  *.gz)  bash "$H/parca_akis.sh" "$U" "$BOY" | gzip -dc ;;
  *)     bash "$H/parca_akis.sh" "$U" "$BOY" ;;
esac
