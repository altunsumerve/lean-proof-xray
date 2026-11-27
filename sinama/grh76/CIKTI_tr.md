# Kodun çıktısı: riemannHypothesis

*Bu belge bir yapay zekâ tarafından yazılmadı. Resmi Lean kaydından, sabit kurallarla üretildi (`arac/belge.py`). Aynı kayıtla çalıştıran herkes harfi harfine aynı belgeyi elde eder. Köşeli parantez içindeki adlar koddaki adlardır.*

## 1. Kanıtlanan cümle

Kodun kanıtladığı teorem `riemannHypothesis`. Önermesi:

> RiemannHypothesis.

Bu cümle yalnızca standart kütüphanedeki (Mathlib) 5.021 kavramla yazılmıştır; projeye özgü hiçbir tanım içermez. Yani neyin kanıtlandığını anlamak için proje kodunun hiçbir satırını okumak gerekmez.

## 2. İspatın omurgası

İspatın tamamı 37.561 bildirimdir. Aşağıdaki adımlar bunların içinden kurallı olarak seçildi: her seferinde, altında en çok ispat bulunan adım açıldı. Yüzde, ispatın ne kadarının yalnızca o adım için var olduğunu gösterir.

| Adım | Önerme | İspattaki payı |
|---:|---|---:|
| 1 | Her P : Parameters ve ε ∈ ℝ için: eğer (0 < ε / 6 ve ε < 1 / 100) ise Eventually((x : ℝ) ↦ primeError(d(P), N₀(P), x) ≤ x ^ (8 · ε + 2⁻¹ − 1), atTop). | %100,0 |
| 2 | Her P : Parameters ve D : Data(P) için: ↑m(D) · remainder(D) ≤ logB(D) ^ (2 : ℕ) · budget(D). | %93,4 |
| 3 | (uzun; aşağıda) | %20,2 |
| 4 | (uzun; aşağıda) | %19,1 |
| 5 | (uzun; aşağıda) | %18,2 |
| 6 | Her P : Parameters ve D : Data(P) için: öyle bir θ : PrimePadicIso → MFoldTwist(D) vardır ki IsFitFamily(D, θ). | %11,5 |
| 7 | (uzun; aşağıda) | %10,4 |
| 8 | Her P : Parameters ve D : Data(P) için: öyle bir n ∈ ℕ ve y : Fin(n) → SubmoduleElem(rows(D)) vardır ki (LinearIndependent(ℂ, y) ve …). | %7,8 |

**Adım 1 — ispatın %100,0** [`eventually_primeError_le_rpow`]

> Her P : Parameters ve ε ∈ ℝ için: eğer (0 < ε / 6 ve ε < 1 / 100) ise Eventually((x : ℝ) ↦ primeError(d(P), N₀(P), x) ≤ x ^ (8 · ε + 2⁻¹ − 1), atTop).

Buraya şu adlar üzerinden gelinir; her birinin ispatının en az %97'si bir sonrakinin altındadır: `riemannHypothesis` → `New.grh`.

Dayandığı parçalar:
- %93,4: [`star_inequality`] → Adım 2
- %6,3: 2.454 küçük yardımcı sonuç

**Adım 2 — ispatın %93,4** [`star_inequality`]

> Her P : Parameters ve D : Data(P) için: ↑m(D) · remainder(D) ≤ logB(D) ^ (2 : ℕ) · budget(D).

Dayandığı parçalar:
- %20,2: [`Data.integral_forms_long`] → Adım 3
- %19,1: [`sphericalCompat_of_odd`] → Adım 4
- %7,8: [`Data.exists_family_covolumeSq_le`] → Adım 8
- %5,4: [`Data.ramifiedColumns_fill_rows`]
- %3,8: [`exchange_theorem`]
- %37,1: 6.907 küçük yardımcı sonuç

**Adım 3 — ispatın %20,2** [`Data.integral_forms_long`]

> ∀ (P : Parameters) (D : Data(P)) (n : ℕ) (y : Fin(n) → SubmoduleElem(rows(D))) (δ : ℝ), ℝ → LinearIndependent(ℂ, y) → (1 − 4 / b(D) ^ (2 : ℕ)) · ↑rowDim(D) ≤ ↑n → IndexLe(D, y, δ) → (RingEquiv(ℂ, ℂ) → covolumeSq(… ∘ …, …) ≤ …) → …. [Not: bu önermenin "…" ile gösterilen kısımları dökümün boyut sınırı yüzünden kesilmiştir; cümle eksiktir.]

Dayandığı parçalar:
- %11,5: [`exists_isFitFamily`] → Adım 6
- %4,7: [`Data.heightLe_volume_ratio_sq`]
- %2,9: [`Data.heightLe_volume_rows`]
- %1,1: 153 küçük yardımcı sonuç

**Adım 4 — ispatın %19,1** [`sphericalCompat_of_split`]

> Verilsin: ℓ ∈ ℕ, E : Type, x ∈ ℕ ve D ∈ ℕ (koşullar: [ThePrime(ℓ)], [PadicIso(ℓ)], [Field(E)], [CMType(E)], [EmbeddedNumberField(E)], [StablyUnram(E)]).
>
> Varsayalım (1): Odd(x).
>
> O zaman: her u : FinPlace(E) (koşullar: [HasQuadSubfield(D, E)]) için: eğer (her v : FinPlace(E) için: eğer (↑ℓ ∈ asIdeal(v) veya v = u) ise IsSplitPrimeToDisc(below(Subtype((x2 : ℂ) ↦ x2 ∈ QuadField(D)), v))) ise SphericalCompat(E, Fin(x), x, u).

Buraya şu adlar üzerinden gelinir; her birinin ispatının en az %97'si bir sonrakinin altındadır: `sphericalCompat_of_odd`.

Dayandığı parçalar:
- %18,2: [`exists_rep_of_cuspidal_type`] → Adım 5
- %0,5: 54 küçük yardımcı sonuç

**Adım 5 — ispatın %18,2** [`exists_rep_of_cuspidal_type`]

> Verilsin: ℓ ∈ ℕ, E : Type, x ∈ ℕ ve d ∈ ℕ (koşullar: [ThePrime(ℓ)], [PadicIso(ℓ)], [Field(E)], [CMType(E)], [EmbeddedNumberField(E)], [HasQuadSubfield(d, E)], [StablyUnram(E)]).
>
> Varsayalım (1): Odd(x).
>
> O zaman: ∀ (κ : Weight(E)) (f : Gf(E, Fin(x)) → WeylIndex(Fin(x), κ.1) → ℂ), f ∈ forms(stdSpace(E, Fin(x)), κ) → (∀ (S : Finset (FinPlace(E))) (P : FinPlace(E) → Polynomial(ℂ)), IsSphericalOff(S, f, P) → (∀ (w₀ : FinPlace(E)), FinPlace(E) → w₀ ∈ S → IsSplitPrimeToDisc(below(Subtype((x2 : ℂ) ↦ x2 ∈ QuadField(d)), w₀)) → (∀ (χ : Subtype((x2 : GeneralLinearGroup(Fin(x), LocField(w₀))) ↦ x2 ∈ localCongruence(Fin(x), w₀, 0)) →* ℂ), IsCuspidalType(localCongruence(Fin(x), w₀, 0), χ) → (Subtype((x2 : GeneralLinearGroup(Fin(x), LocField(w₀))) ↦ x2 ∈ localCongruence(Fin(x), w₀, 0)) → …(…) = …) → …))).

Dayandığı parçalar:
- %10,4: [`Model.exists_galois_rep`] → Adım 7
- %2,1: [`nonempty_universalFamily`]
- %5,6: 882 küçük yardımcı sonuç

**Adım 6 — ispatın %11,5** [`exists_isFitFamily`]

> Her P : Parameters ve D : Data(P) için: öyle bir θ : PrimePadicIso → MFoldTwist(D) vardır ki IsFitFamily(D, θ).

Dayandığı parçalar:
- %7,0: [`denominatorLe_rowBudget`]
- %4,5: 410 küçük yardımcı sonuç

**Adım 7 — ispatın %10,4** [`Model.exists_galois_rep`]

> Verilsin: E : Type, x ∈ ℕ, d₀ ∈ ℕ, 𝔑 : RingOfIntegers(E), ν ∈ ℕ, R : Subalgebra(RingOfIntegers(E), E), X : Model(Fin(x), d₀, 𝔑, ν, R) ve ℓ ∈ ℕ (koşullar: [Field(E)], [CMBase(E)], [HasQuadSubfield(d₀, E)], x ≠ 0).
>
> Varsayalım (1): IsNeat(Fin(x), 𝔑).
>
> O zaman: her M : Submonoid(RingOfIntegers(E)) (koşullar: [ThePrime(ℓ)], [Algebra(E, Ω)]) için: eğer (her w : FinPlace(E) için: eğer IsSafe(𝔑, w) ise M ≤ primeCompl(asIdeal(w))) ise (her θ : SafePlace(𝔑) → ℕ → ℂ ve J : Multiset ℤ (koşullar: [IsLocalization(M, Subtype((x2 : E) ↦ x2 ∈ R))], [PadicIso(ℓ)]) için: eğer (her u ∈ ℤ için: eğer u ∈ J ise 0 ≤ u ve OccursInWeight(x, ν, θ, toNat(u))) ise öyle bir ρ : PadicRep(AlgEquiv(E, Ω, Ω), ℓ) vardır ki (Continuous(rep(ρ)) ve (her w : SafePlace(𝔑) için: SphericalClause(rep(ρ), OccursIn, (x2 : E →+* ℂ) ↦ ite(algebraMap(E, ℂ) = x2, J, 0), ↑↑w, heckePoly(q(↑↑w), x, (x2 : ℕ) ↦ ιℓ(θ(w, x2))))))).

Dayandığı parçalar:
- %2,6: [`ellAdicCohom.woods_hole`]
- %7,6: 1.237 küçük yardımcı sonuç

**Adım 8 — ispatın %7,8** [`Data.exists_family_covolumeSq_le`]

> Her P : Parameters ve D : Data(P) için: öyle bir n ∈ ℕ ve y : Fin(n) → SubmoduleElem(rows(D)) vardır ki (LinearIndependent(ℂ, y) ve …). [Not: bu önermenin "…" ile gösterilen kısımları dökümün boyut sınırı yüzünden kesilmiştir; cümle eksiktir.]

Dayandığı parçalar:
- %4,2: [`Data.seesaw`]
- %3,5: [`Data.short_forms`]
- %0,1: 93 küçük yardımcı sonuç

## 4. Sayılar

| | |
|---|---:|
| Projenin bildirimi | 37.770 |
| Bunlardan teorem | 30.418 |
| Ana teoremin kullandığı | 37.561 |
| Ana teoremin hiç kullanmadığı | 209 |
| Önermesi başka bir teoreminkiyle birebir aynı olan fazladan teorem | 7.901 (%26,0) |

## 5. Bu belge nasıl denetlenir

1. Kayıt: Lean'in resmi dışa aktarımı (`solution.ndjson.zst`), Lean çekirdeği tarafından doğrulanmış haliyle.
2. Omurga: kayıttaki bağımlılıklardan hesaplanan baskınlık ağacı. "Yalnızca o adım için var" ifadesi tanım gereği kesindir.
3. Cümleler: önermenin mantık iskeleti sabit kalıplarla yazılır (her, vardır, eğer–ise, ve, veya, değil); formüller kayıttaki terimden aynen basılır.
4. Yorum yok: belgede kayıtta bulunmayan hiçbir açıklama, niyet ya da değerlendirme yer almaz.
