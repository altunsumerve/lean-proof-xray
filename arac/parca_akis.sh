#!/bin/bash
# Dosyayı 256 MB'lık aralıklarla (HTTP Range) sırayla stdout'a akıtır; kopan parçayı yeniden ister.
URL=$1; BOY=$2; P=$((256*1024*1024)); bas=0
while [ $bas -lt $BOY ]; do
  son=$((bas+P-1)); [ $son -ge $BOY ] && son=$((BOY-1))
  for d in 1 2 3 4 5 6 7 8 9 10; do
    if curl -sSf -r $bas-$son "$URL" -o /dev/shm/parca 2>>/dev/stderr && [ $(stat -c %s /dev/shm/parca) -eq $((son-bas+1)) ]; then break; fi
    echo "parca $bas tekrar $d" >&2; sleep 3
  done
  cat /dev/shm/parca; bas=$((son+1))
done
rm -f /dev/shm/parca
