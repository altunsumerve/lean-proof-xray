# Kodun çıktısı: flt_regular

*Bu belge bir yapay zekâ tarafından yazılmadı. Resmi Lean kaydından, sabit kurallarla üretildi (`arac/belge.py`). Aynı kayıtla çalıştıran herkes harfi harfine aynı belgeyi elde eder. Köşeli parantez içindeki adlar koddaki adlardır.*

## 1. Kanıtlanan cümle

Kodun kanıtladığı teorem `flt_regular`. Önermesi:

> Her p ∈ ℕ (koşullar: Prime(p)) için: eğer IsRegularPrime(p) ve p ≠ 2 ise FermatLastTheoremFor(p).

Bu cümle projeye özgü 3 tanıma ve kütüphaneden 5.581 kavrama dayanır.

## 2. İspatın omurgası

İspatın tamamı 425 bildirimdir. Aşağıdaki adımlar bunların içinden kurallı olarak seçildi: her seferinde, altında en çok ispat bulunan adım açıldı. Yüzde, ispatın ne kadarının yalnızca o adım için var olduğunu gösterir.

| Adım | Önerme | İspattaki payı | Yoğun kullandığı alanlar |
|---:|---|---:|---|
| 1 | Her p ∈ ℕ (koşullar: Prime(p)) için: eğer IsRegularPrime(p) ve p ≠ 2 ise FermatLastTheoremFor(p). | %100,0 |  |
| 2 | (uzun; aşağıda) | %85,0 |  |
| 3 | (uzun; aşağıda) | %70,4 |  |
| 4 | (uzun; aşağıda) | %59,0 |  |
| 5 | (uzun; aşağıda) | %54,3 |  |
| 6 | (uzun; aşağıda) | %42,4 |  |

**Adım 1 — ispatın %100,0** [`flt_regular`]

> Her p ∈ ℕ (koşullar: Prime(p)) için: eğer IsRegularPrime(p) ve p ≠ 2 ise FermatLastTheoremFor(p).

Dayandığı parçalar:
- %85,0: [`FltRegular.caseII`] → Adım 2
- %13,3: [`FltRegular.caseI`]
- %1,6: 4 küçük yardımcı sonuç

**Adım 2 — ispatın %85,0** [`FltRegular.not_exists_solution`]

> Verilsin: K : Type ve p ∈ ℕ (koşullar: Prime(p), [Field(K)], [NumberField(K)], [IsCyclotomicExtension(singleton(p), ℚ, K)]).
>
> Varsayalım (1): p ≠ 2.
>
> O zaman: her  (koşullar: [Fintype(ClassGroup(RingOfIntegers(K)))]) için: eğer Coprime(p, card(ClassGroup(RingOfIntegers(K)))) ise (her ζ : K, hζ : IsPrimitiveRoot(ζ, p) ve m ∈ ℕ için: eğer 1 ≤ m ise hiçbir x' : RingOfIntegers(K), y' : RingOfIntegers(K), z' : RingOfIntegers(K) ve ε₃ : Units(RingOfIntegers(K)) için ((toInteger(hζ) − 1 ∣ y' doğru değildir) ve (toInteger(hζ) − 1 ∣ z' doğru değildir) ve x' ^ p + y' ^ p = ↑ε₃ · ((toInteger(hζ) − 1) ^ m · z') ^ p) doğru olmaz).

Buraya şu adlar üzerinden gelinir; her birinin ispatının en az %97'si bir sonrakinin altındadır: `FltRegular.caseII` → `FltRegular.not_exists_Int_solution'` → `FltRegular.not_exists_Int_solution` → `FltRegular.not_exists_solution'`.

Dayandığı parçalar:
- %70,4: [`exists_solution'`] → Adım 3
- %3,3: [`one_le_m`]
- %8,5: 27 küçük yardımcı sonuç

**Adım 3 — ispatın %70,4** [`exists_solution'`]

> Verilsin: K : Type ve p ∈ ℕ (koşullar: p ≠ 0, [Field(K)], [NumberField(K)]).
>
> Varsayalım (1): p ≠ 2.
>
> O zaman: her ζ : K, hζ : IsPrimitiveRoot(ζ, p), x : RingOfIntegers(K), y : RingOfIntegers(K), z : RingOfIntegers(K), ε : Units(RingOfIntegers(K)) ve m ∈ ℕ için: eğer x ^ p + y ^ p = ↑ε · ((toInteger(hζ) − 1) ^ (m + 1) · z) ^ p ve (toInteger(hζ) − 1 ∣ y doğru değildir) ve (toInteger(hζ) − 1 ∣ z doğru değildir) ise (her  (koşullar: Prime(p), [IsCyclotomicExtension(singleton(p), ℚ, K)], [Fintype(ClassGroup(RingOfIntegers(K)))]) için: eğer Coprime(p, card(ClassGroup(RingOfIntegers(K)))) ise öyle bir x' : RingOfIntegers(K), y' : RingOfIntegers(K), z' : RingOfIntegers(K) ve ε₃ : Units(RingOfIntegers(K)) vardır ki ((toInteger(hζ) − 1 ∣ y' doğru değildir) ve (toInteger(hζ) − 1 ∣ z' doğru değildir) ve x' ^ p + y' ^ p = ↑ε₃ · ((toInteger(hζ) − 1) ^ m · z') ^ p)).

Dayandığı parçalar:
- %59,0: [`eq_pow_prime_of_unit_of_congruent`] → Adım 4
- %9,3: [`exists_solution`]
- %0,9: 1 küçük yardımcı sonuç

**Adım 4 — ispatın %59,0** [`eq_pow_prime_of_unit_of_congruent`]

> Verilsin: K : Type ve p ∈ ℕ (koşullar: Prime(p), [Field(K)], [NumberField(K)]).
>
> Varsayalım (1): p ≠ 2.
>
> O zaman: her  (koşullar: [Fintype(ClassGroup(RingOfIntegers(K)))]) için: eğer Coprime(p, card(ClassGroup(RingOfIntegers(K)))) ise (her u : Units(RingOfIntegers(K)) (koşullar: [IsCyclotomicExtension(singleton(p), ℚ, K)]) için: eğer (öyle bir n ∈ ℤ vardır ki ↑p ∣ ↑u − ↑n) ise öyle bir v : Units(RingOfIntegers(K)) vardır ki u = v ^ p).

Dayandığı parçalar:
- %54,3: [`exists_pow_eq_of_zeta_sub_one_pow_dvd_sub_one`] → Adım 5
- %2,7: [`zeta_sub_one_pow_dvd_norm_sub_pow`]
- %0,8: 3 küçük yardımcı sonuç

**Adım 5 — ispatın %54,3** [`exists_pow_eq_of_zeta_sub_one_pow_dvd_sub_one`]

> Verilsin: K : Type ve p ∈ ℕ (koşullar: Prime(p), [Field(K)], [NumberField(K)]).
>
> Varsayalım (1): p ≠ 2.
>
> O zaman: her  (koşullar: [Fintype(ClassGroup(RingOfIntegers(K)))]) için: eğer Coprime(p, card(ClassGroup(RingOfIntegers(K)))) ise (her ζ : K, hζ : IsPrimitiveRoot(ζ, p) ve u : Units(RingOfIntegers(K)) için: eğer (toInteger(hζ) − 1) ^ p ∣ ↑u − 1 ise öyle bir v : K vardır ki v ^ p = (algebraMap(RingOfIntegers(K), K))(↑u)).

Dayandığı parçalar:
- %42,4: [`dvd_card_classGroup_of_unramified_isCyclic`] → Adım 6
- %10,9: [`KummersLemma.isUnramified`]

**Adım 6 — ispatın %42,4** [`exists_not_isPrincipal_and_isPrincipal_map`]

> Verilsin: K : Type ve L : Type (koşullar: [Field(K)], [Field(L)], [NumberField(K)], [NumberField(L)], [Algebra(K, L)], [FiniteDimensional(K, L)], [IsGalois(K, L)], [Unramified(RingOfIntegers(K), RingOfIntegers(L))], [IsCyclic(AlgEquiv(K, L, L))]).
>
> Varsayalım (1): Prime(finrank(K, L)).
>
> Varsayalım (2): finrank(K, L) ≠ 2.
>
> O zaman: öyle bir I : Ideal (RingOfIntegers(K)) vardır ki ((IsPrincipal(I) doğru değildir) ve IsPrincipal(map(algebraMap(RingOfIntegers(K), RingOfIntegers(L)), I))).

Buraya şu adlar üzerinden gelinir; her birinin ispatının en az %97'si bir sonrakinin altındadır: `dvd_card_classGroup_of_unramified_isCyclic`.

Dayandığı parçalar:
- %34,6: [`Hilbert92`]
- %6,7: [`exists_not_isPrincipal_and_isPrincipal_map_aux`]

## 4. Sayılar

| | |
|---|---:|
| Projenin bildirimi | 426 |
| Bunlardan teorem | 361 |
| Ana teoremin kullandığı | 425 |
| Ana teoremin hiç kullanmadığı | 1 |
| Önermesi başka bir teoreminkiyle birebir aynı olan fazladan teorem | 18 (%5,0) |

## 5. Bu belge nasıl denetlenir

1. Kayıt: Lean'in resmi dışa aktarımı (`solution.ndjson.zst`), Lean çekirdeği tarafından doğrulanmış haliyle.
2. Omurga: kayıttaki bağımlılıklardan hesaplanan baskınlık ağacı. "Yalnızca o adım için var" ifadesi tanım gereği kesindir.
3. Cümleler: önermenin mantık iskeleti sabit kalıplarla yazılır (her, vardır, eğer–ise, ve, veya, değil); formüller kayıttaki terimden aynen basılır.
4. Yorum yok: belgede kayıtta bulunmayan hiçbir açıklama, niyet ya da değerlendirme yer almaz.
