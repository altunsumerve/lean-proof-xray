# Boş koşul taraması

*Kurallı üretildi (`arac/bos.py`). Kapsam: dökümdeki 89927 proje bildirimi (45178 tanım/yapı, ispatı okunabilen 3906 teorem); projenin tamamı değil. "Kullanan": dökümde bu adı doğrudan kullanan bildirim sayısı. "En ağır pay": bunlar arasında baskınlık ağacında en ağır olanın ispattaki payı (yalnız en üst 3000 düğüm için bilinir; bilinmiyorsa —). Bir koşulun boş olması ispatı geçersiz kılmaz: ana teorem koşulsuz doğrulanmıştır. Bu tablo yalnızca hangi koşulların hiçbir şey sınamadığını gösterir.*

## A. Argümanlarına bakmadan `True` olan koşullar (8)

| Ad | Argüman | Kullanan | En ağır kullanan | En ağır pay |
|---|---:|---:|---|---:|
| `GlobalTheory.Mem.Top.Bl.anyGeometry` | 3 | 9 | `GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt` | %15,6 |
| `GlobalTheory.IndefiniteRowSideFullHecke.UnusedSlot39.trivialClassCondition` | 12 | 2 | `GlobalTheory.HkIntegral.heckeInt` | %0,1 |
| `UpperTheory.V.U3.GCond.noCondition` | 13 | 25 | `UpperTheory.V.Loc.Dat3.IY` | — |
| `Formalism.L2.Pj.trivialClassCondition` | 12 | 7 | `Formalism.L2.Pj.extAll` | — |
| `GlobalTheory.Published.UnusedSlot72` | 0 | 4 | `GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.mk` | — |
| `UpperTheory.One.M.TrivialCondition` | 0 | 2 | `UpperTheory.One.M.New.nMv` | — |
| `Formalism.L2.PjFree.trivialClassCondition` | 12 | 1 | `Formalism.L2.PjFree.regular₂._proof_2` | — |
| `UpperTheory.GalS.UnusedSlot55` | 6 | 1 | `Formalism.MainNotions.SumRepresentations.CuspidalGaloisUnramified'` | — |

## B. Alanı olmayan önerme-yapıları (0)

(yok)

## C. Tek adımla kanıtlanan teoremler (2; ispatı okunabilen 3906 teorem içinde)

| Teorem | Önerme | İspat | Pay |
|---|---|---|---:|
| `GlobalTheory.CuspRep.CG.ofChar._proof_1` | 1 ≤ 1. | `le_rfl` | — |
| `GroundTheory.GroupCoh.h1RatModIntIsoH2Int._proof_1` | 1 + 1 = 1 + 1. | `rfl` | — |

## D. Bütün kayıtta gövdesi `True` olan tanımlar (10; kayıttaki tanımların tamamı tarandı, kütüphane dahil)

| Ad | Argüman |
|---|---:|
| `Formalism.L2.Pj.trivialClassCondition` | 12 |
| `Formalism.L2.PjFree.trivialClassCondition` | 12 |
| `GlobalTheory.BigTop.Fun.trivialTieCondition` | 13 |
| `GlobalTheory.IndefiniteRowSideFullHecke.UnusedSlot39.trivialClassCondition` | 12 |
| `GlobalTheory.Mem.Top.Bl.anyGeometry` | 3 |
| `GlobalTheory.Published.UnusedSlot72` | 0 |
| `UpperTheory.GalS.NoCondition` | 1 |
| `UpperTheory.GalS.UnusedSlot55` | 6 |
| `UpperTheory.One.M.TrivialCondition` | 0 |
| `UpperTheory.V.U3.GCond.noCondition` | 13 |
