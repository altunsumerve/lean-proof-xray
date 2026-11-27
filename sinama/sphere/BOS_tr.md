# Boş koşul taraması

*Kurallı üretildi (`arac/bos.py`). Kapsam: dökümdeki 1703 proje bildirimi (367 tanım/yapı, ispatı okunabilen 622 teorem); projenin tamamı değil. "Kullanan": dökümde bu adı doğrudan kullanan bildirim sayısı. "En ağır pay": bunlar arasında baskınlık ağacında en ağır olanın ispattaki payı (yalnız en üst 3000 düğüm için bilinir; bilinmiyorsa —). Bir koşulun boş olması ispatı geçersiz kılmaz: ana teorem koşulsuz doğrulanmıştır. Bu tablo yalnızca hangi koşulların hiçbir şey sınamadığını gösterir.*

## A. Argümanlarına bakmadan `True` olan koşullar (0)

(yok)

## B. Alanı olmayan önerme-yapıları (0)

(yok)

## C. Tek adımla kanıtlanan teoremler (2; ispatı okunabilen 622 teorem içinde)

| Teorem | Önerme | İspat | Pay |
|---|---|---|---:|
| `SmoothPartitionOfUnity.finsupport.eq_1` | … | `Eq.refl` | <%0,1 |
| `Loop.roundTripFamily._proof_2` | Her X : Type, x : X, y : X, γ : Path(x, y) ve t ∈ ℝ (koşullar: [TopologicalSpace(X)]) için: (extend(γ))(t) = (extend(γ))(t). | `rfl` | <%0,1 |
