# Kodun çıktısı: PFR_conjecture

*Bu belge bir yapay zekâ tarafından yazılmadı. Resmi Lean kaydından, sabit kurallarla üretildi (`arac/belge.py`). Aynı kayıtla çalıştıran herkes harfi harfine aynı belgeyi elde eder. Köşeli parantez içindeki adlar koddaki adlardır.*

## 1. Kanıtlanan cümle

Kodun kanıtladığı teorem `PFR_conjecture`. Önermesi:

> Her G : Type, A : Set G ve K ∈ ℝ (koşullar: [AddCommGroup(G)], [Module(ZMod(2), G)]) için: eğer Nonempty(A) ve Finite(A) ve ↑ncard(A + A) ≤ K · ↑ncard(A) ise öyle bir H : Submodule(ZMod(2), G) ve c : Set G vardır ki (Finite(c) ve Finite(↑H) ve ↑card(Elem(c)) < 2 · K ^ (12 : ℝ) ve ncard(↑H) ≤ ncard(A) ve A ≤ c + ↑H).

Bu cümle yalnızca standart kütüphanedeki (Mathlib) 2.220 kavramla yazılmıştır; projeye özgü hiçbir tanım içermez. Yani neyin kanıtlandığını anlamak için proje kodunun hiçbir satırını okumak gerekmez.

## 2. İspatın omurgası

İspatın tamamı 658 bildirimdir. Aşağıdaki adımlar bunların içinden kurallı olarak seçildi: her seferinde, altında en çok ispat bulunan adım açıldı. Yüzde, ispatın ne kadarının yalnızca o adım için var olduğunu gösterir.

| Adım | Önerme | İspattaki payı |
|---:|---|---:|
| 1 | (uzun; aşağıda) | %100,0 |
| 2 | (uzun; aşağıda) | %73,6 |
| 3 | (uzun; aşağıda) | %59,4 |
| 4 | (uzun; aşağıda) | %56,1 |
| 5 | (uzun; aşağıda) | %13,1 |
| 6 | (uzun; aşağıda) | %12,2 |
| 7 | (uzun; aşağıda) | %10,3 |
| 8 | (uzun; aşağıda) | %9,9 |

**Adım 1 — ispatın %100,0** [`PFR_conjecture_aux`]

> Verilsin: G : Type, A : Set G ve K ∈ ℝ (koşullar: [AddCommGroup(G)], [Countable(G)], [Module(ZMod(2), G)], [Finite(G)]).
>
> Varsayalım (1): Nonempty(A).
>
> Varsayalım (2): ↑ncard(A + A) ≤ K · ↑ncard(A).
>
> O zaman: öyle bir H : Submodule(ZMod(2), G) ve c : Set G vardır ki (↑card(Elem(c)) ≤ K ^ (13 / 2) · ↑ncard(A) ^ (1 / 2) · ↑ncard(↑H) ^ (−1 / 2) ve ↑ncard(↑H) ≤ K ^ (11 : ℝ) · ↑ncard(A) ve ↑ncard(A) ≤ K ^ (11 : ℝ) · ↑ncard(↑H) ve A ≤ c + ↑H).

Buraya şu adlar üzerinden gelinir; her birinin ispatının en az %97'si bir sonrakinin altındadır: `PFR_conjecture`.

Dayandığı parçalar:
- %73,6: [`entropic_PFR_conjecture`] → Adım 2
- %4,4: [`ProbabilityTheory.Kernel.chain_rule`]
- %3,0: [`ProbabilityTheory.measureMutualInfo_nonneg_aux`]
- %13,4: 115 küçük yardımcı sonuç

**Adım 2 — ispatın %73,6** [`entropic_PFR_conjecture`]

> Verilsin: Ω₀₁ : Type, Ω₀₂ : Type, G : Type ve p : refPackage(Ω₀₁, Ω₀₂, G) (koşullar: [MeasureSpace(Ω₀₁)], [MeasureSpace(Ω₀₂)], [IsProbabilityMeasure(volume)], [IsProbabilityMeasure(volume)], [AddCommGroup(G)], [Module(ZMod(2), G)], [Finite(G)], [MeasurableSpace(G)], [MeasurableSingletonClass(G)]).
>
> Varsayalım (1): η(p) = 1 / 9.
>
> O zaman: öyle bir H : Submodule(ZMod(2), G), Ω : Type, mΩ : MeasureSpace(Ω) ve U : Ω → G vardır ki (IsProbabilityMeasure(volume) ve Measurable(U) ve IsUniform(↑H, U, volume) ve rdist(X₀₁(p), U, volume, volume) + rdist(X₀₂(p), U, volume, volume) ≤ 11 · rdist(X₀₁(p), X₀₂(p), volume, volume) ve rdist(X₀₁(p), U, volume, volume) ≤ 6 · rdist(X₀₁(p), X₀₂(p), volume, volume) ve rdist(X₀₂(p), U, volume, volume) ≤ 6 · rdist(X₀₁(p), X₀₂(p), volume, volume)).

Dayandığı parçalar:
- %59,4: [`tau_strictly_decreases`] → Adım 3
- %2,5: [`exists_isUniform_of_rdist_eq_zero`]
- %2,5: [`ProbabilityTheory.independent_copies3_nondep_finiteRange`]
- %7,7: 29 küçük yardımcı sonuç

**Adım 3 — ispatın %59,4** [`tau_strictly_decreases`]

> Verilsin: Ω₀₁ : Type, Ω₀₂ : Type, Ω : Type, G : Type, p : refPackage(Ω₀₁, Ω₀₂, G), X₁ : Ω → G ve X₂ : Ω → G (koşullar: [MeasureSpace(Ω₀₁)], [MeasureSpace(Ω₀₂)], [MeasureSpace(Ω)], [IsProbabilityMeasure(volume)], [IsProbabilityMeasure(volume)], [IsProbabilityMeasure(volume)], [AddCommGroup(G)], [Module(ZMod(2), G)], [Finite(G)], [MeasurableSpace(G)], [MeasurableSingletonClass(G)]).
>
> Varsayalım (1): Measurable(X₁).
>
> Varsayalım (2): Measurable(X₂).
>
> Varsayalım (3): TauMinimizes(p, X₁, X₂).
>
> Varsayalım (4): η(p) = 1 / 9.
>
> O zaman: rdist(X₁, X₂, volume, volume) = 0.

Dayandığı parçalar:
- %56,1: [`tau_strictly_decreases_aux`] → Adım 4
- %3,1: 3 küçük yardımcı sonuç

**Adım 4 — ispatın %56,1** [`tau_strictly_decreases_aux`]

> Verilsin: G : Type, Ω₀₁ : Type, Ω₀₂ : Type, p : refPackage(Ω₀₁, Ω₀₂, G), Ω : Type, X₁ : Ω → G, X₂ : Ω → G, X₁' : Ω → G ve X₂' : Ω → G (koşullar: [AddCommGroup(G)], [Finite(G)], [MeasurableSpace(G)], [MeasurableSingletonClass(G)], [MeasureSpace(Ω₀₁)], [MeasureSpace(Ω₀₂)], [IsProbabilityMeasure(volume)], [IsProbabilityMeasure(volume)], [MeasureSpace(Ω)]).
>
> Varsayalım (1): Measurable(X₁).
>
> Varsayalım (2): Measurable(X₂).
>
> Varsayalım (3): Measurable(X₁').
>
> Varsayalım (4): Measurable(X₂').
>
> Varsayalım (5): IdentDistrib(X₁, X₁', volume, volume).
>
> Varsayalım (6): IdentDistrib(X₂, X₂', volume, volume).
>
> Varsayalım (7): iIndepFun(vecCons(X₁, vecCons(X₂, vecCons(X₁', vecCons(X₂', vecEmpty)))), volume).
>
> Varsayalım (8): TauMinimizes(p, X₁, X₂).
>
> O zaman: her  (koşullar: [IsProbabilityMeasure(volume)], [Module(ZMod(2), G)]) için: eğer η(p) = 1 / 9 ise rdist(X₁, X₂, volume, volume) = 0.

Dayandığı parçalar:
- %13,1: [`cond_construct_good`] → Adım 5
- %10,3: [`sum_dist_diff_le`] → Adım 7
- %7,7: [`sum_condMutual_le`]
- %3,4: [`comparison_of_ruzsa_distances`]
- %3,3: [`sum_of_rdist_eq_char_2`]
- %3,2: [`condRuzsaDist_le'`]
- %2,1: [`condRuzsaDistance_ge_of_min`]
- %11,2: 50 küçük yardımcı sonuç

**Adım 5 — ispatın %13,1** [`cond_construct_good`]

> Verilsin: G : Type, Ω₀₁ : Type, Ω₀₂ : Type, p : refPackage(Ω₀₁, Ω₀₂, G), Ω : Type, X₁ : Ω → G ve X₂ : Ω → G (koşullar: [AddCommGroup(G)], [Finite(G)], [MeasurableSpace(G)], [MeasurableSingletonClass(G)], [MeasureSpace(Ω₀₁)], [MeasureSpace(Ω₀₂)], [IsProbabilityMeasure(volume)], [IsProbabilityMeasure(volume)], [MeasureSpace(Ω)]).
>
> Varsayalım (1): TauMinimizes(p, X₁, X₂).
>
> O zaman: her Ω' : Type, T₁ : Ω' → G, T₂ : Ω' → G ve T₃ : Ω' → G (koşullar: [MeasureSpace(Ω')]) için: eğer T₁ + T₂ + T₃ = 0 ve Measurable(T₁) ve Measurable(T₂) ve Measurable(T₃) ise (her R : Ω' → G (koşullar: [IsProbabilityMeasure(volume)], [Module(ZMod(2), G)]) için: eğer Measurable(R) ise rdist(X₁, X₂, volume, volume) ≤ condMutualInfo(T₁, T₂, R, volume) + condMutualInfo(T₂, T₃, R, volume) + condMutualInfo(T₃, T₁, R, volume) + η(p) / 3 · (condMutualInfo(T₁, T₂, R, volume) + condMutualInfo(T₂, T₃, R, volume) + condMutualInfo(T₃, T₁, R, volume) + (condRuzsaDist'(X₀₁(p), T₁, R, volume, volume) − rdist(X₀₁(p), X₁, volume, volume) + (condRuzsaDist'(X₀₂(p), T₁, R, volume, volume) − rdist(X₀₂(p), X₂, volume, volume))) + (condRuzsaDist'(X₀₁(p), T₂, R, volume, volume) − rdist(X₀₁(p), X₁, volume, volume) + (condRuzsaDist'(X₀₂(p), T₂, R, volume, volume) − rdist(X₀₂(p), X₂, volume, volume))) + (condRuzsaDist'(X₀₁(p), T₃, R, volume, volume) − rdist(X₀₁(p), X₁, volume, volume) + (condRuzsaDist'(X₀₂(p), T₃, R, volume, volume) − rdist(X₀₂(p), X₂, volume, volume))))).

Dayandığı parçalar:
- %12,2: [`construct_good'`] → Adım 6
- %0,5: 4 küçük yardımcı sonuç

**Adım 6 — ispatın %12,2** [`construct_good`]

> Verilsin: G : Type, Ω₀₁ : Type, Ω₀₂ : Type, p : refPackage(Ω₀₁, Ω₀₂, G), Ω : Type, X₁ : Ω → G ve X₂ : Ω → G (koşullar: [AddCommGroup(G)], [Finite(G)], [MeasurableSpace(G)], [MeasurableSingletonClass(G)], [MeasureSpace(Ω₀₁)], [MeasureSpace(Ω₀₂)], [IsProbabilityMeasure(volume)], [IsProbabilityMeasure(volume)], [MeasureSpace(Ω)]).
>
> Varsayalım (1): TauMinimizes(p, X₁, X₂).
>
> O zaman: her Ω' : Type, T₁ : Ω' → G, T₂ : Ω' → G ve T₃ : Ω' → G (koşullar: [MeasureSpace(Ω')]) için: eğer T₁ + T₂ + T₃ = 0 ve Measurable(T₁) ve Measurable(T₂) ve Measurable(T₃) ise (her  (koşullar: [IsProbabilityMeasure(volume)], [Module(ZMod(2), G)]) için: rdist(X₁, X₂, volume, volume) ≤ mutualInfo(T₁, T₂, volume) + mutualInfo(T₂, T₃, volume) + mutualInfo(T₃, T₁, volume) + η(p) / 3 · (mutualInfo(T₁, T₂, volume) + mutualInfo(T₂, T₃, volume) + mutualInfo(T₃, T₁, volume) + (rdist(X₀₁(p), T₁, volume, volume) − rdist(X₀₁(p), X₁, volume, volume) + (rdist(X₀₂(p), T₁, volume, volume) − rdist(X₀₂(p), X₂, volume, volume))) + (rdist(X₀₁(p), T₂, volume, volume) − rdist(X₀₁(p), X₁, volume, volume) + (rdist(X₀₂(p), T₂, volume, volume) − rdist(X₀₂(p), X₂, volume, volume))) + (rdist(X₀₁(p), T₃, volume, volume) − rdist(X₀₁(p), X₁, volume, volume) + (rdist(X₀₂(p), T₃, volume, volume) − rdist(X₀₂(p), X₂, volume, volume))))).

Buraya şu adlar üzerinden gelinir; her birinin ispatının en az %97'si bir sonrakinin altındadır: `construct_good'`.

Dayandığı parçalar:
- %9,9: [`construct_good_prelim`] → Adım 8
- %0,1: 3 küçük yardımcı sonuç

**Adım 7 — ispatın %10,3** [`sum_dist_diff_le`]

> Verilsin: G : Type, Ω₀₁ : Type, Ω₀₂ : Type, p : refPackage(Ω₀₁, Ω₀₂, G), Ω : Type, X₁ : Ω → G, X₂ : Ω → G, X₁' : Ω → G ve X₂' : Ω → G (koşullar: [AddCommGroup(G)], [Finite(G)], [MeasurableSpace(G)], [MeasurableSingletonClass(G)], [MeasureSpace(Ω₀₁)], [MeasureSpace(Ω₀₂)], [IsProbabilityMeasure(volume)], [IsProbabilityMeasure(volume)], [MeasureSpace(Ω)]).
>
> Varsayalım (1): Measurable(X₁).
>
> Varsayalım (2): Measurable(X₂).
>
> Varsayalım (3): Measurable(X₁').
>
> Varsayalım (4): Measurable(X₂').
>
> Varsayalım (5): IdentDistrib(X₁, X₁', volume, volume).
>
> Varsayalım (6): IdentDistrib(X₂, X₂', volume, volume).
>
> Varsayalım (7): iIndepFun(vecCons(X₁, vecCons(X₂, vecCons(X₁', vecCons(X₂', vecEmpty)))), volume).
>
> Varsayalım (8): TauMinimizes(p, X₁, X₂).
>
> O zaman: her  (koşullar: [IsProbabilityMeasure(volume)], [Module(ZMod(2), G)]) için: condRuzsaDist'(X₀₁(p), X₁ + X₂, X₁ + X₂ + X₁' + X₂', volume, volume) − rdist(X₀₁(p), X₁, volume, volume) + (condRuzsaDist'(X₀₂(p), X₁ + X₂, X₁ + X₂ + X₁' + X₂', volume, volume) − rdist(X₀₂(p), X₂, volume, volume)) + (condRuzsaDist'(X₀₁(p), X₁' + X₂, X₁ + X₂ + X₁' + X₂', volume, volume) − rdist(X₀₁(p), X₁, volume, volume) + (condRuzsaDist'(X₀₂(p), X₁' + X₂, X₁ + X₂ + X₁' + X₂', volume, volume) − rdist(X₀₂(p), X₂, volume, volume))) + (condRuzsaDist'(X₀₁(p), X₁' + X₁, X₁ + X₂ + X₁' + X₂', volume, volume) − rdist(X₀₁(p), X₁, volume, volume) + (condRuzsaDist'(X₀₂(p), X₁' + X₁, X₁ + X₂ + X₁' + X₂', volume, volume) − rdist(X₀₂(p), X₂, volume, volume))) ≤ (6 − 3 · η(p)) · rdist(X₁, X₂, volume, volume) + 3 · (2 · η(p) · rdist(X₁, X₂, volume, volume) − condMutualInfo(X₁ + X₂, X₁' + X₂, X₁ + X₂ + X₁' + X₂', volume)).

Dayandığı parçalar:
- %2,5: [`independenceCondition1`]
- %2,3: [`condRuzsaDist'_of_inj_map'`]
- %2,1: 11 küçük yardımcı sonuç

**Adım 8 — ispatın %9,9** [`construct_good_prelim`]

> Verilsin: G : Type, Ω₀₁ : Type, Ω₀₂ : Type, p : refPackage(Ω₀₁, Ω₀₂, G), Ω : Type, X₁ : Ω → G ve X₂ : Ω → G (koşullar: [AddCommGroup(G)], [Finite(G)], [MeasurableSpace(G)], [MeasurableSingletonClass(G)], [MeasureSpace(Ω₀₁)], [MeasureSpace(Ω₀₂)], [IsProbabilityMeasure(volume)], [IsProbabilityMeasure(volume)], [MeasureSpace(Ω)]).
>
> Varsayalım (1): TauMinimizes(p, X₁, X₂).
>
> O zaman: her Ω' : Type, T₁ : Ω' → G, T₂ : Ω' → G ve T₃ : Ω' → G (koşullar: [MeasureSpace(Ω')]) için: eğer T₁ + T₂ + T₃ = 0 ve Measurable(T₁) ve Measurable(T₂) ve Measurable(T₃) ise (her  (koşullar: [IsProbabilityMeasure(volume)], [Module(ZMod(2), G)]) için: rdist(X₁, X₂, volume, volume) ≤ mutualInfo(T₁, T₂, volume) + mutualInfo(T₂, T₃, volume) + mutualInfo(T₃, T₁, volume) + η(p) · (rdist(X₀₁(p), T₁, volume, volume) − rdist(X₀₁(p), X₁, volume, volume) + (rdist(X₀₂(p), T₂, volume, volume) − rdist(X₀₂(p), X₂, volume, volume))) + η(p) · (mutualInfo(T₁, T₃, volume) + mutualInfo(T₂, T₃, volume)) / 2).

Dayandığı parçalar:
- %7,2: [`ent_bsg`]
- <%0,1: 2 küçük yardımcı sonuç

## 4. Sayılar

| | |
|---|---:|
| Projenin bildirimi | 662 |
| Bunlardan teorem | 582 |
| Ana teoremin kullandığı | 658 |
| Ana teoremin hiç kullanmadığı | 4 |
| Önermesi başka bir teoreminkiyle birebir aynı olan fazladan teorem | 71 (%12,2) |

## 5. Bu belge nasıl denetlenir

1. Kayıt: Lean'in resmi dışa aktarımı (`solution.ndjson.zst`), Lean çekirdeği tarafından doğrulanmış haliyle.
2. Omurga: kayıttaki bağımlılıklardan hesaplanan baskınlık ağacı. "Yalnızca o adım için var" ifadesi tanım gereği kesindir.
3. Cümleler: önermenin mantık iskeleti sabit kalıplarla yazılır (her, vardır, eğer–ise, ve, veya, değil); formüller kayıttaki terimden aynen basılır.
4. Yorum yok: belgede kayıtta bulunmayan hiçbir açıklama, niyet ya da değerlendirme yer almaz.
