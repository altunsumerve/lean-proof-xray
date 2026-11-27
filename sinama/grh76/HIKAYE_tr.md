> **Bu sayfa nasıl üretildi.** Bu klasördeki öteki dosyaların aksine bu anlatımı bir dil modeli (Claude, 26 Kasım 2026)
> yazdı; yalnızca [anlatıcı kurallarına](../../arac/hikaye/ANLATICI.md) uyarak. Model haritayı, aracın haritadan çıkardığı
> [zorunlu soruları](HIKAYE.questions.md) ve istediği tek tek bildirimlerin kodunu (açıklama satırları silinmiş) gördü:
> 16 işlem. Yazarın kılavuzunu, herhangi bir makaleyi ya da önceki hikâyeleri görmedi. Denetçi 43 yapısal iddianın
> tamamını doğruladı ve 10 zorunlu sorunun hepsinin cevaplandığını buldu. Matematik okuması bir matematikçi tarafından
> gözden geçirilmedi. Bu Türkçe metin, İngilizce aslının ([HIKAYE.md](HIKAYE.md)) çevirisidir; soruların cevapları asıl dildedir.

# İspatın hikâyesi

## Beş cümlede fikir

1. En üst düzey (`New.grh`; `riemannHypothesis` ondan çıkar) her şeyi tek taraflı bir kestirime indirger: sabit bir kalan sınıfındaki uygun bir d asalı için, primeError adlı ağırlıklı asal sayım hatası eninde sonunda en fazla x^(8ε − 1/2) olmalıdır; bunun Laplace dönüşümü üzerinde (kutupları, L-fonksiyonlarının sıfırlarını eksi d ile ikinci dereceden bükülmüşlerinin sıfırlarını sayar) Landau türü bir argüman, 1/2 + 8ε'nin sağında sıfır olmasını yasaklar.
2. Her büyük x için ispat, Data adında bir yardımcı seçimler paketi kurar (2'nin kuvveti olan bir m ≈ √x tam sayısı, 3'ün kuvveti olan bir r ≈ x^5 tam sayısı, log b = x^ε olan çok büyük bir b ölçeği, b^10 ile b^11 arasında iki yardımcı asal, thick adında üç terimli dizi içermeyen bir yer sınıfları kümesi) ve primeError(x)'i, m·remainder bölü m·a·#thick artı ikinci bir x₁ ölçeğindeki bir terim olarak yeniden yazar; o terim, x₁ bir pencereden seçilerek önemsiz kılınır.
3. Çekirdek olan `star_inequality`, m·remainder ≤ (log b)^2·budget der ve otomorf formlardan oluşan tek bir karmaşık vektör uzayını (rows) iki yoldan ölçerek kanıtlanır: `Data.exists_family_covolumeSq_le`, küçük bir indekse kadar tam olan ve Gram determinantı en fazla exp(n·(mainHeight − m·remainder + log b·budget)) olan, neredeyse tam bir taban üretir; `Data.integral_forms_long` ise böyle neredeyse tam, neredeyse dolu her ailenin log-determinantının en az rowDim·(mainHeight − 3·log b·budget) olması gerektiğini gösterir.
4. İki sınır karşılaştırıldığında büyük nicelik mainHeight (= m·k·dirCost) tam olarak sadeleşir ve geriye m·remainder ≤ 4·log b·budget + küçük terimler kalır; budget m ile büyümediği için, m ≈ √x'e bölmek karekök kazancını veren şeydir.
5. Alt sınır bir çarpım formülü ("yükseklik") argümanıdır: rows'un hacmi, m katlı bir kaldırma zincirinin her adımı için bir tane olmak üzere m kaldırma hacmine ayrılır; her çarpan, aşikâr büküm ile bir yardımcı bükümler ailesi arasında karşılaştırılır; p-adik paydalar, formlara iliştirilen Galois temsilleriyle (`sphericalCompat_of_odd`, `Model.exists_galois_rep`), Selmer uzunluğu / Ribet tarzı bir sınır üzerinden (`exists_isFitFamily`, `denominatorLe_rowBudget`, `ribet_columns`) kontrol edilir.

## Matematikçi için

Birleştirme sırası, kodda okunduğu gibi.

(a) `New.grh`: Re ρ > 1/2 olan bir ρ sıfırı verildiğinde ε = (min(Re ρ, 1) − 1/2)/51, β = 8ε + 1/2, modül M = 18480q alınır. Bir ölçüt uygulanır (d ≡ 9240q − 1 mod M, d ≡ 7 mod 8 asalları için tek taraflı primeError ≤ x^(β−1) sınırı, Re > β için sıfırlanmamayı verir); ispatı bir Landau lemmasını ve tek bir ikinci dereceden büküm için sıfırlanmama önermesini çağırır.

(b) `eventually_primeError_le_rpow`: Data'yı `exists_data`'dan alır; x₁ ölçeğini, [10^6 log x, (10^6 log x)^2] içinde primeError(N₀, e^u) − (towerDeg/#thick)·primeError(1, e^u) ≤ x^(−10^6) olan bir u noktasıyla değiştirir; remainder = a·(#thick·(primeError(x) − primeError(x₁)) + #tops·primeError(1, x₁)) özdeşliğini kullanır ve `star_inequality`'yi yerine koyar.

(c) `star_inequality`: h = mainHeight − m·remainder + L, L = log b·budget, d = rowDim olsun. Üst taraf: n ≥ (1 − 4/b²)d bağımsız form, indeks kusuru δ ≤ 5d·log(1+b²)·budget, Gram determinantları ≤ exp(n·h). Alt taraf: d(mainHeight − 3L) ≤ n·h + 2δ. Kaba bir −h ≤ b²x^99 sınırı eksik d − n vektörün bedelini öder. d'ye bölmek mainHeight'ı sadeleştirir.

(d) Üst taraf: `Data.short_forms`, "dallanmış sütunlardan" kurulan Poincaré türü formları alır; `Data.seesaw` bunların görüntüsünü açık bir Bμ formuyla özdeşleştirir; onun büyüklüğü satır başına bir yükseklikle sınırlanır ve bir Stirling hesabı bu yüksekliğin ≤ mainHeight − m·remainder + budget olduğunu gösterir: asallar üzerindeki toplamlar (primeSum) burada, ν ≤ a asallarındaki yerel büyüklükler olarak girer. `Data.exists_indexDvd_Bmu_divisible` p-adik tamlığı verir. `Data.ramifiedColumns_fill_rows` (`Filling.Fits.exists_translate_finrank_comap_le` üzerinden) ötelemelerin yayıldığını, dolayısıyla az sayıda ötelemenin neredeyse her şeyi gerdiğini gösterir.

(e) Alt taraf, `Data.integral_forms_long`: `Data.heightLe_volume_rows`, tamlığı kullanarak vol(θ)/vol(1)'in yüksekliğini n·h + 2δ + d·b ile sınırlar (tamamlayıcı vektörleri `Data.crude_rows` sağlar); `Data.heightLe_volume_ratio_sq`, tersinin karesinin yüksekliğini 2d(2L − mainHeight) ile sınırlar; bu, j = 1..m üzerinden `Data.heightLe_liftVolume_ratio`'ların çarpımıdır ve her biri B₀ = budget/(mk) olmak üzere d·k·(log b·B₀ − dirCost) değerindedir. Çarpım 1'dir, dolayısıyla yüksekliklerin toplamı ≥ 0 olur.

(f) Bükümleri `exists_isFitFamily` sağlar: `exists_mFoldTwist_selmerLengthLe` onları seçer; `denominatorLe_rowBudget` → `ribet_columns` → `sum_blockLoss_le` → `block_defect_le_at_place` → `crystalline_defect_le` paydaları bir satır bütçesiyle sınırlar.

(g) Galois girdisi: `sphericalCompat_of_odd` → `sphericalCompat_of_split` → `exists_rep_of_cuspidal_type` → `Model.exists_galois_rep` → `ellAdicCohom.woods_hole`; `exchange_theorem` theta integrallerini L-değeri çarpımlarına kadar ilişkilendirir.

## Herkes için

İspat, sıfırlar hakkındaki bir soruyu, asal sayıların belli örüntülerde ne kadar düzgün dağıldığı sorusuna çevirir. Sonra her büyük x sayısı için, çok simetrik fonksiyonlardan oluşan büyük ama sonlu boyutlu bir uzay kurar. Bu uzayın büyüklüğünü birbirinden bağımsız iki yoldan ölçer: bir kez yukarıdan, açıkça kurulmuş küçük fonksiyonlarla; bir kez aşağıdan, tam sayı türünden nesnelerin fazla küçük olamayacağı gerçeğiyle. İki ölçümün ortak, çok büyük bir terimi vardır ve o sadeleşir; geriye tam olarak asal sayım hatası kalır, yaklaşık x'in kareköküyle çarpılmış olarak. Öteki tarafta kalan küçük olduğu için hata da küçük olmak zorundadır; hipotezin istediği karekök doğruluğu budur. Aşağıdan ölçüm, paydaları kontrol etmek için derin aritmetik simetrilere (Galois temsillerine) dayanır.

## Anlayamadıklarım

- rows'un Gram determinantının Chowla–Selberg türü sabite ve dirCost'a gerçekten neden bağlı olduğu: tanımları (jetSize, primeSum, mainAsk) ve satır başına yükseklik sınırındaki Stirling adımını okudum, ama faktöriyel büyüklüklerin geometrik kaynağını görmedim.
- rows, Column, Bμ, goodLift nesnelerinin ve Y, W uzaylarının somut olarak ne olduğu (hangi gruplar, hangi ağırlıklar); yalnızca kullanıldıklarını gördüm.
- `Attached.local_global_of_eigencharacter`'ın `star_inequality` içinde nasıl kullanıldığı; `sphericalCompat_of_odd` için yolu `denominatorLe_rowBudget` ve `exists_isFitFamily`'ye kadar izledim, ama dallanmış yerel-global önermesinin ne için gerektiğini göremedim.
- `exchange_theorem`, `Data.exists_besselSystem`, `exists_isWeakBaseChange_of_matching`, `Data.exists_isTriangle` ve `Data.hasGap_gridParam`'ın `star_inequality`'ye nasıl girdiği; `exchange_theorem`'in yalnızca önermesini okudum.
- Sonsuz yerlerin sayısı f'nin towerDeg ile kıyaslanabilir olduğu (Q4'teki hesabım için gerekli; tahmin); oradaki son eşitsizlik, açmadığım otomatik bir büyüklük taktiğiyle kapatılıyor.
- thick kümesinin neden üç terimli dizi içermemesi gerektiği ve r ≈ x^5'in k = r + 1 − m ile h₂ = r^8 dışındaki rolü.
- `Model.exists_galois_rep`, `ellAdicCohom.woods_hole`, `nonempty_universalFamily`, `linearIndepOn_hodgeTateMap_pointClass`, `Filling.energy_le_of_linkEnergy_le`, `Filling.energy_le_of_level_pairs`, `Filling.sum_le_of_positive_type`, `Filling.energy_fixingSet_le`, `exists_comparison_forms` adımlarının içi ve işaret operatörü zinciri (`Data.IsMarked.hasType_prod_markOperator_pow`, `Data.IsMarked.hasType_markOperator`, `Columns.hasType_markOperator`, `TwistingData.hasType_twisted_hecke`).
- residueClass'ın bir sınıfa kısıtlanmış von Mangoldt fonksiyonu olup olmadığı (L-serisi lemma adlarından tahmin).

## Answers to the required questions

- Q1: Data is a structure of auxiliary choices for one x: reals logX, logB, logX₁ with scale conditions (10^12·c ≤ log logB, 100·log logB ≤ logX, 10^6·logX ≤ logX₁, 10^6·logX₁ ≤ logB), s ≤ 32·logX, m = 2^(e+1) in [√x, 2√x] with s = 22(e+1), r = 3^(e'+1) in [x^5, 3x^5], a finite set thick of place classes with a three-term-freeness property, two distinct primes g0, g1 in [b^10, b^11] congruent to 1 modulo N₁(s)·d, an integer piG of norm g0·g1, and a prime-in-window property. It is produced by `exists_data` (not bounded): powers of 2 and 3 near the targets; W = exp(ε·logX/6), logX₁ = W, logB = W^6; classNumber+1 primes in short logarithmic windows from a lemma on primes ≡ 1 in log-windows (proved by a contour/derivative bound on sums of logarithmic derivatives of L-functions); a pigeonhole on ideal classes makes a product of two primes principal; thick comes from a Behrend-sphere three-term-free construction.
- Q2: remainder is the sum over the places τ in tops of (primeSum(a, τ) − mainAsk), where primeSum is a sum over ν ≤ a of lambdaClass(ν)·(a/ν − nominalWeight)⁺ and mainAsk = a(log a − 1 − chowlaSelbergConst − average log nominalWeight); by an identity it equals a·(#thick·(primeError(x) − primeError(x₁)) + #tops·primeError(1, x₁)). It is bounded above by `star_inequality`; it enters through `Data.short_forms`, where the size of the form Bμ is bounded by a per-row height (sum over an m-step chain of jet sizes minus prime sums) and a Stirling step shows that height ≤ mainHeight − m·remainder + budget.
- Q3: budget = f·a·(log b)^3 (f = number of infinite places of the field E, a = roundUp(x·b)); it is an error allowance, not a quantity that is estimated. It is spent in `Data.short_forms` (sum over primes of allowedLoss·log p ≤ budget, proved by a harmonic-sum count over primes dividing N, m·c−1, c, m·c+1 for c ≤ x₁), in the index defect, and in `exists_isFitFamily`, where B₀ = budget/(m·k) must dominate the sum of rowBudget(ℓ)·log ℓ; that is fed by `denominatorLe_rowBudget` and below it `ribet_columns` (valuation of a Ribet element ≤ rank·rowBudget).
- Q4: Data is taken with D.x = x and x₁ replaced by e^u, u in [10^6·log x, (10^6·log x)^2] from a window lemma, so that primeError(N₀, x₁) − (towerDeg/#thick)·primeError(1, x₁) ≤ x^(−10^6); the remainder identity gives primeError(x) = m·remainder/(m·a·#thick) + that term, and `star_inequality` bounds the first by (log b)^2·budget/(m·a·#thick) = f·(log b)^5/(m·#thick). Chosen sizes: m ≈ √x, r ≈ x^5, log b = x^ε, a ≈ x·b, s ≤ 32·log x, #thick ≥ towerDeg(s)/log b; so the bound is about x^(5ε)·x^ε/√x (using f/#thick ≤ log b, a guess for f ≈ towerDeg), which is below x^(8ε − 1/2).
- Q5: In `star_inequality` the term mainHeight (= m·k·dirCost) appears on both sides of d·(mainHeight − 3L) ≤ d·(mainHeight − m·remainder + L + 4x^99 + 10·log(1+b²)·budget) and cancels after dividing by d = rowDim; left is m·remainder ≤ 4·log b·budget + 4x^99 + 10·log(1+b²)·budget ≤ (log b)^2·budget.
- Q6: Yes: the lift is iterated m times (indices j = 1..m, m = 2^(e+1) ≈ √x; twists are "m-fold twists" required to be nontrivial at every power j). The volume of rows is a constant times the product over j = 1..m of lift volumes, and each j contributes height rowDim·k·(log b·B₀ − dirCost), summing to rowDim·(log b·budget − mainHeight); on the upper side the same m multiplies the prime sums (per-row height = m·(…)). m ≈ √x is right because the remainder is multiplied by m while budget is not, so dividing by m yields exactly the x^(−1/2) in the statement; a smaller m gives a weaker exponent (that a larger m would break the Data constraints is a guess). Other repetitions seen: a greedy choice of at most 5·rowDim·log(1+b²)/dim Column translates, and a strong induction over prime-degree base-change steps in `Attached.local_global_of_eigencharacter`.
- Q7: Called directly in the proof of `star_inequality` (the calc step named both); it contributes the lower bound rowDim·(mainHeight − 3·log b·budget) ≤ n·h + 2δ for the log-determinant of any nearly-integral family.
- Q8: Called by the lemma sphericalCompat_std (all ranks: theta-lift to odd rank, twist, cancel characters). That lemma is called in three places I read: in the lemma attached_galRep (which defines the Galois representation of an eigen-system and is invoked inside `denominatorLe_rowBudget`), in the lemma exists_hasRow_auxPair (invoked inside `exists_isFitFamily` to produce the rows whose Selmer length is bounded), and in `Attached.local_global_of_eigencharacter`. It contributes to `star_inequality` the existence of a Galois representation attached to each eigenform, with the Hecke polynomial killing Frobenius, which is what the denominator bound for the lift volumes (lower side) is run on.
- Q9: Called in the first line of `star_inequality`; it contributes the family y: n ≥ (1 − 4/b²)·rowDim independent forms, index defect δ ≤ 5·rowDim·log(1+b²)·budget, and Gram determinants ≤ exp(n·(mainHeight − m·remainder + log b·budget)).
- Q10: Called in `Data.enough_forms` (through `exists_few_translates`), which is used by `Data.exists_family_covolumeSq_le`; it contributes spreadness with parameter b^(−2), hence a small set t of translates whose images span at least (1 − 4/b²)·rowDim, which makes the family nearly full and keeps δ small.

## Claims

- STEP `riemannHypothesis`
- STEP `New.grh`
- STEP `eventually_primeError_le_rpow`
- STEP `star_inequality`
- STEP `Data.integral_forms_long`
- STEP `Data.exists_family_covolumeSq_le`
- STEP `exists_isFitFamily`
- STEP `Data.seesaw`
- UNDER `riemannHypothesis` `New.grh`
- UNDER `New.grh` `eventually_primeError_le_rpow`
- UNDER `eventually_primeError_le_rpow` `star_inequality`
- UNDER `star_inequality` `Data.integral_forms_long`
- UNDER `star_inequality` `sphericalCompat_of_odd`
- UNDER `star_inequality` `Data.exists_family_covolumeSq_le`
- UNDER `star_inequality` `Data.ramifiedColumns_fill_rows`
- UNDER `star_inequality` `exchange_theorem`
- UNDER `Data.integral_forms_long` `exists_isFitFamily`
- UNDER `Data.integral_forms_long` `Data.heightLe_volume_ratio_sq`
- UNDER `Data.integral_forms_long` `Data.heightLe_volume_rows`
- UNDER `Data.heightLe_volume_ratio_sq` `Data.heightLe_liftVolume_ratio`
- UNDER `Data.heightLe_volume_rows` `Data.crude_rows`
- UNDER `exists_isFitFamily` `denominatorLe_rowBudget`
- UNDER `exists_isFitFamily` `exists_mFoldTwist_selmerLengthLe`
- UNDER `denominatorLe_rowBudget` `ribet_columns`
- UNDER `ribet_columns` `sum_blockLoss_le`
- UNDER `Data.exists_family_covolumeSq_le` `Data.seesaw`
- UNDER `Data.exists_family_covolumeSq_le` `Data.short_forms`
- UNDER `Data.short_forms` `Data.exists_indexDvd_Bmu_divisible`
- UNDER `sphericalCompat_of_odd` `sphericalCompat_of_split`
- UNDER `sphericalCompat_of_split` `exists_rep_of_cuspidal_type`
- UNDER `exists_rep_of_cuspidal_type` `Model.exists_galois_rep`
- UNDER `Model.exists_galois_rep` `ellAdicCohom.woods_hole`
- UNDER `Data.ramifiedColumns_fill_rows` `Filling.Fits.exists_translate_finrank_comap_le`
- SHARE `star_inequality` 93.4
- SHARE `Data.integral_forms_long` 20.2
- SHARE `sphericalCompat_of_odd` 19.1
- SHARE `exists_rep_of_cuspidal_type` 18.2
- SHARE `exists_isFitFamily` 11.5
- SHARE `Model.exists_galois_rep` 10.4
- SHARE `Data.exists_family_covolumeSq_le` 7.8
- SHARE `denominatorLe_rowBudget` 7.0
- SHARE `Data.ramifiedColumns_fill_rows` 5.4
- SHARE `exchange_theorem` 3.8
