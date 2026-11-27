# Kodun çıktısı: riemannHypothesis

*Bu belge bir yapay zekâ tarafından yazılmadı. Resmi Lean kaydından, sabit kurallarla üretildi (`arac/belge.py`). Aynı kayıtla çalıştıran herkes harfi harfine aynı belgeyi elde eder. Köşeli parantez içindeki adlar koddaki adlardır.*

## 1. Kanıtlanan cümle

Kodun kanıtladığı teorem `riemannHypothesis`. Önermesi:

> RiemannHypothesis.

Bu cümle yalnızca standart kütüphanedeki (Mathlib) 5.021 kavramla yazılmıştır; projeye özgü hiçbir tanım içermez. Yani neyin kanıtlandığını anlamak için proje kodunun hiçbir satırını okumak gerekmez.

## 2. İspatın omurgası

İspatın tamamı 49.815 bildirimdir. Aşağıdaki adımlar bunların içinden kurallı olarak seçildi: her seferinde, altında en çok ispat bulunan adım açıldı. Yüzde, ispatın ne kadarının yalnızca o adım için var olduğunu gösterir.

| Adım | Önerme | İspattaki payı |
|---:|---|---:|
| 1 | (uzun; aşağıda) | %100,0 |
| 2 | Her P : Parameters ve D : Data(P) için: ↑m(D) · totalRemainder(D) ≤ ↑f(D) · ↑a(D) · logB(D) ^ (5 : ℕ). | %93,8 |
| 3 | (uzun; aşağıda) | %55,7 |
| 4 | (uzun; aşağıda) | %46,6 |
| 5 | Her P : Parameters ve D : Data(P) için: öyle bir θ : PrimePadicIso → MFoldTwist(D) vardır ki IsRegularFamily(D, θ). | %40,2 |
| 6 | (uzun; aşağıda) | %35,1 |
| 7 | (uzun; aşağıda) | %17,1 |
| 8 | (uzun; aşağıda) | %16,4 |

**Adım 1 — ispatın %100,0** [`New.eventually_primeRemainder_natCast_le`]

> Her P : Parameters ve ε ∈ ℝ için: eğer 0 < ε ve ε < 1 / 100 ise Eventually((x : ℕ) ↦ primeRemainder(d(P), q₀(P), ↑x) ≤ (64 · ↑totient(q₀(P)) + 3) · ↑x ^ (−1 / 2 + 6 · ε), atTop).

Buraya şu adlar üzerinden gelinir; her birinin ispatının en az %97'si bir sonrakinin altındadır: `riemannHypothesis` → `New.grh` → `New.eventually_primeRemainder_le_rpow`.

Dayandığı parçalar:
- %93,8: [`New.Data.primeRemainder_le`] → Adım 2
- %5,9: 2.487 küçük yardımcı sonuç

**Adım 2 — ispatın %93,8** [`New.star_inequality`]

> Her P : Parameters ve D : Data(P) için: ↑m(D) · totalRemainder(D) ≤ ↑f(D) · ↑a(D) · logB(D) ^ (5 : ℕ).

Buraya şu adlar üzerinden gelinir; her birinin ispatının en az %97'si bir sonrakinin altındadır: `New.Data.primeRemainder_le`.

Dayandığı parçalar:
- %55,7: [`New.Data.integral_forms_long`] → Adım 3
- %3,9: [`New.Data.seesaw_identity`]
- %3,3: [`New.Data.exists_err_gaugeLe_compositeLift`]
- %30,9: 6.854 küçük yardımcı sonuç

**Adım 3 — ispatın %55,7** [`New.Data.integral_forms_long`]

> ∀ (P : Parameters) (D : Data(P)) (n : ℕ), (Fin(n) → Subtype((x : Subtype((x : Form(spaceY(D, 0), typeKernel(paramW(D), signsY(D, 0)))) ↦ x ∈ principalForms(D, spaceY(D, 0)))) ↦ … ∈ …)) → …. [Not: bu önermenin "…" ile gösterilen kısımları dökümün boyut sınırı yüzünden kesilmiştir; cümle eksiktir.]

Dayandığı parçalar:
- %46,6: [`New.Data.exists_hasSmallRatios_heightLe_liftDeterminant_div`] → Adım 4
- %3,9: [`New.Exchange.exchange_identity`]
- %2,1: [`New.Data.exists_span_isAuxiliaryForm_eq_top`]
- %3,2: 658 küçük yardımcı sonuç

**Adım 4 — ispatın %46,6** [`New.Data.exists_hasSmallRatios_heightLe_liftDeterminant_div`]

> Her P : Parameters ve D : Data(P) için: öyle bir θ : PrimePadicIso → MFoldTwist(D) vardır ki (HasSmallRatios(D, θ) ve (her j ∈ ℕ için: eğer j ∈ Icc(1, m(D)) ise HeightLe(↑targetDim(D) · (↑f(D) · ↑a(D) · logB(D) ^ (4 : ℕ) / ↑m(D) − ↑k(D) · directionAmount(D)), (ι : PrimePadicIso) ↦ liftDeterminant(D, 1, j) / liftDeterminant(D, θ(ι), j)))).

Dayandığı parçalar:
- %40,2: [`New.exists_isRegularFamily`] → Adım 5
- %5,3: [`New.Data.heightLe_liftDeterminant_ratio`]
- %1,1: 276 küçük yardımcı sonuç

**Adım 5 — ispatın %40,2** [`New.exists_isRegularFamily`]

> Her P : Parameters ve D : Data(P) için: öyle bir θ : PrimePadicIso → MFoldTwist(D) vardır ki IsRegularFamily(D, θ).

Dayandığı parçalar:
- %35,1: [`New.Selmer.exists_mFoldTwist_hasDenominatorsLe`] → Adım 6
- %4,3: [`New.Selmer.sum_clearingBound_add_padicValNat_le`]
- %0,9: 155 küçük yardımcı sonuç

**Adım 6 — ispatın %35,1** [`New.Selmer.exists_mFoldTwist_hasDenominatorsLe`]

> Verilsin: P : Parameters, D : Data(P), ℓ ∈ ℕ ve ι : PadicIso(ℓ) (koşullar: [ThePrime(ℓ)]).
>
> O zaman: öyle bir τ : MFoldTwist(D) vardır ki (Coprime(ℓ, normQ(toTameChar(toTwist(τ)))) ve (her j : Elem(LiftIndex(D)), p : CriticalPair(D) ve s : Units(ℤ) için: eğer IsRamified(p) ise ‖ιℓ((ratio(p, toTameChar(powTwist(τ, j)), s))⁻¹)‖ ≤ exp(↑twistError(ℓ, D) · log(↑ℓ))) ve (her j : Elem(LiftIndex(D)) için: HasDenominatorsLe(D, ιℓ, powTwist(τ, j), ↑j, ↑clearingBound(D, ℓ) · log(↑ℓ) + ↑padicValNat(ℓ, card(StdClasses(chosenLevel))) · log(↑ℓ)))).

Dayandığı parçalar:
- %17,1: [`New.GaloisRep.sphericalCompat_of_odd`] → Adım 7
- %7,2: [`New.Selmer.denominatorLe_clearingBound`]
- %10,8: 1.749 küçük yardımcı sonuç

**Adım 7 — ispatın %17,1** [`New.GaloisRep.sphericalCompat_of_split`]

> Verilsin: ℓ ∈ ℕ, E : Type, x ∈ ℕ ve D ∈ ℕ (koşullar: [ThePrime(ℓ)], [PadicIso(ℓ)], [Field(E)], [CMType(E)], [EmbeddedNumberField(E)], [HasPrimitiveRoot5040(E)]).
>
> Varsayalım (1): Odd(x).
>
> O zaman: her u : FinPlace(E) (koşullar: [HasQuadSubfield(D, E)]) için: eğer (her v : FinPlace(E) için: eğer (↑ℓ ∈ asIdeal(v) veya v = u) ise IsSplitPrimeToDisc(below(Subtype((x2 : ℂ) ↦ x2 ∈ QuadField(D)), v))) ise SphericalCompat(E, Fin(x), x, u).

Buraya şu adlar üzerinden gelinir; her birinin ispatının en az %97'si bir sonrakinin altındadır: `New.GaloisRep.sphericalCompat_of_odd`.

Dayandığı parçalar:
- %16,4: [`_private.Lib.GaloisRep.Main.SplitCase.0.New.GaloisRep.exists_rep_of_free_weight`] → Adım 8
- %0,5: 53 küçük yardımcı sonuç

**Adım 8 — ispatın %16,4** [`_private.Lib.GaloisRep.Main.SeedRepresentation.0.New.GaloisRep.exists_padicRep_of_cuspidal_type_at_embedding`]

> Verilsin: ℓ ∈ ℕ, E : Type, x ∈ ℕ ve d ∈ ℕ (koşullar: [ThePrime(ℓ)], [PadicIso(ℓ)], [Field(E)], [CMType(E)], [EmbeddedNumberField(E)], [HasQuadSubfield(d, E)], [HasPrimitiveRoot5040(E)]).
>
> Varsayalım (1): Odd(x).
>
> O zaman: ∀ (κ : Weight(E)) (f : Gf(E, Fin(x)) → WeylIndex(Fin(x), κ.1) → ℂ), f ∈ forms(stdSpace(E, Fin(x)), κ) → (∀ (S : Finset (FinPlace(E))) (P : FinPlace(E) → Polynomial(ℂ)), IsSphericalOff(S, f, P) → (∀ (w₀ : FinPlace(E)), FinPlace(E) → w₀ ∈ S → IsSplitPrimeToDisc(below(Subtype((x2 : ℂ) ↦ x2 ∈ QuadField(d)), w₀)) → (∀ (χ : Subtype((x2 : GeneralLinearGroup(Fin(x), LocField(w₀))) ↦ x2 ∈ localCongruence(Fin(x), w₀, 0)) →* ℂ), IsCuspidalType(localCongruence(Fin(x), w₀, 0), χ) → (Subtype((x2 : GeneralLinearGroup(Fin(x), LocField(w₀))) ↦ … ∈ …) → …) → …))).

Buraya şu adlar üzerinden gelinir; her birinin ispatının en az %97'si bir sonrakinin altındadır: `_private.Lib.GaloisRep.Main.SplitCase.0.New.GaloisRep.exists_rep_of_free_weight` → `New.GaloisRep.exists_rep_of_cuspidal_type`.

Dayandığı parçalar:
- %15,1: [`_private.Lib.GaloisRep.Main.SeedRepresentation.0.New.GaloisRep.exists_padicRep_of_pel`]
- %1,0: 193 küçük yardımcı sonuç

## 4. Sayılar

| | |
|---|---:|
| Projenin bildirimi | 50.275 |
| Bunlardan teorem | 42.204 |
| Ana teoremin kullandığı | 49.815 |
| Ana teoremin hiç kullanmadığı | 460 |
| Önermesi başka bir teoreminkiyle birebir aynı olan fazladan teorem | 8.586 (%20,3) |

## 5. Bu belge nasıl denetlenir

1. Kayıt: Lean'in resmi dışa aktarımı (`solution.ndjson.zst`), Lean çekirdeği tarafından doğrulanmış haliyle.
2. Omurga: kayıttaki bağımlılıklardan hesaplanan baskınlık ağacı. "Yalnızca o adım için var" ifadesi tanım gereği kesindir.
3. Cümleler: önermenin mantık iskeleti sabit kalıplarla yazılır (her, vardır, eğer–ise, ve, veya, değil); formüller kayıttaki terimden aynen basılır.
4. Yorum yok: belgede kayıtta bulunmayan hiçbir açıklama, niyet ya da değerlendirme yer almaz.
