# Kodun çıktısı: classical_carleson

*Bu belge bir yapay zekâ tarafından yazılmadı. Resmi Lean kaydından, sabit kurallarla üretildi (`arac/belge.py`). Aynı kayıtla çalıştıran herkes harfi harfine aynı belgeyi elde eder. Köşeli parantez içindeki adlar koddaki adlardır.*

## 1. Kanıtlanan cümle

Kodun kanıtladığı teorem `classical_carleson`. Önermesi:

> Her f : ℝ → ℂ için: eğer Continuous(f) ve Periodic(f, 2 · π) ise Eventually((x : ℝ) ↦ Tendsto((x2 : ℕ) ↦ partialFourierSum(x2, f, x), atTop, nhds(f(x))), ae(volume)).

Bu cümle projeye özgü 2 tanıma ve kütüphaneden 4.969 kavrama dayanır.

## 2. İspatın omurgası

İspatın tamamı 4.952 bildirimdir. Aşağıdaki adımlar bunların içinden kurallı olarak seçildi: her seferinde, altında en çok ispat bulunan adım açıldı. Yüzde, ispatın ne kadarının yalnızca o adım için var olduğunu gösterir.

| Adım | Önerme | İspattaki payı |
|---:|---|---:|
| 1 | (uzun; aşağıda) | %100,0 |
| 2 | (uzun; aşağıda) | %95,3 |
| 3 | (uzun; aşağıda) | %86,2 |
| 4 | (uzun; aşağıda) | %68,9 |
| 5 | (uzun; aşağıda) | %63,7 |
| 6 | (uzun; aşağıda) | %53,7 |
| 7 | (uzun; aşağıda) | %30,1 |
| 8 | (uzun; aşağıda) | %26,6 |

**Adım 1 — ispatın %100,0** [`control_approximation_effect'`]

> Her δ : ℝ≥0 ve ε : ℝ≥0 için: eğer 0 < δ ve 0 < ε ise (her g : ℝ → ℂ için: eğer Measurable(g) ve Periodic(g, 2 · π) ve (her x ∈ ℝ için: ‖g(x)‖ ≤ ↑C_control_approximation_effect'(δ, ε)) ise distribution((x : ℝ) ↦ iSup((N : ℕ) ↦ enorm(partialFourierSum(N, g, x))), ofNNReal(δ), restrict(volume, Ioc(0, 2 · π))) ≤ ofNNReal(ε)).

Buraya şu adlar üzerinden gelinir; her birinin ispatının en az %97'si bir sonrakinin altındadır: `classical_carleson` → `carleson_interval'` → `exceptional_set_carleson'`.

Dayandığı parçalar:
- %95,3: [`distribution_carlesonOperatorReal_le'`] → Adım 2
- %3,1: 36 küçük yardımcı sonuç

**Adım 2 — ispatın %95,3** [`rcarleson_general`]

> Her q : ℝ≥0 ve q' : ℝ≥0 için: eğer q ∈ Ioc(1, 2) ve HolderConjugate(q, q') ise (her F : Set ℝ ve G : Set ℝ için: eğer MeasurableSet(F) ve MeasurableSet(G) ise (her f : ℝ → ℂ için: eğer Measurable(f) ve (her x ∈ ℝ için: ‖f(x)‖ ≤ indicator(F, 1, x)) ise lintegral(restrict(volume, G), (x : ℝ) ↦ carlesonOperatorReal(K, f, x)) ≤ ofNNReal(C10_0_1(4, q)) · volume(G) ^ (↑q')⁻¹ · volume(F) ^ (↑q)⁻¹)).

Buraya şu adlar üzerinden gelinir; her birinin ispatının en az %97'si bir sonrakinin altındadır: `distribution_carlesonOperatorReal_le'` → `rcarleson_exceptional_set_estimate_specific''` → `rcarleson_exceptional_set_estimate_specific'` → `rcarleson_exceptional_set_estimate_specific` → `rcarleson_exceptional_set_estimate` → `rcarleson`.

Dayandığı parçalar:
- %86,2: [`two_sided_metric_carleson`] → Adım 3
- %4,7: [`Hilbert_strong_2_2`]
- %3,7: 85 küçük yardımcı sonuç

**Adım 3 — ispatın %86,2** [`two_sided_metric_carleson`]

> Verilsin: X : Type, x ∈ ℕ, q : ℝ≥0, q' : ℝ≥0, F : Set X, G : Set X ve K : X → X → ℂ (koşullar: [MetricSpace(X)], [DoublingMeasure(X, ↑defaultA(x))], [IsTwoSidedKernel(x, K)], [CompatibleFunctions(ℝ, X, defaultA(x))], [IsCancellative(X, defaultτ(x))]).
>
> Varsayalım (1): 4 ≤ x.
>
> Varsayalım (2): q ∈ Ioc(1, 2).
>
> Varsayalım (3): HolderConjugate(q, q').
>
> Varsayalım (4): MeasurableSet(F).
>
> Varsayalım (5): MeasurableSet(G).
>
> Varsayalım (6): her r ∈ ℝ için: eğer r > 0 ise HasBoundedStrongType(czOperator(K, r), 2, 2, volume, volume, ofNNReal(C_Ts(x))).
>
> O zaman: her f : X → ℂ için: eğer Measurable(f) ve (her x2 : X için: ‖f(x2)‖ ≤ indicator(F, 1, x2)) ise lintegral(restrict(volume, G), (x2 : X) ↦ carlesonOperator(K, f, x2)) ≤ ofNNReal(C10_0_1(x, q)) · volume(G) ^ (↑q')⁻¹ · volume(F) ^ (↑q)⁻¹.

Dayandığı parçalar:
- %68,9: [`metric_carleson`] → Adım 4
- %8,5: [`nontangential_from_simple`]
- %7,2: [`hasStrongType_maximalFunction_one`]
- %1,3: 84 küçük yardımcı sonuç

**Adım 4 — ispatın %68,9** [`R_truncation'`]

> Verilsin: X : Type, x ∈ ℕ, q : ℝ≥0, q' : ℝ≥0, F : Set X, G : Set X, K : X → X → ℂ, Q : SimpleFunc(X, Θ(X)) ve f : X → ℂ (koşullar: [MetricSpace(X)], [KernelProofData(x, K)], [IsCancellative(X, defaultτ(x))]).
>
> Varsayalım (1): q ∈ Ioc(1, 2).
>
> Varsayalım (2): HolderConjugate(q, q').
>
> Varsayalım (3): MeasurableSet(F).
>
> Varsayalım (4): MeasurableSet(G).
>
> Varsayalım (5): Measurable(f).
>
> Varsayalım (6): ((x2 : X) ↦ ‖f(x2)‖) ≤ indicator(F, 1).
>
> O zaman: her n ∈ ℕ ve R ∈ ℝ için: eğer R = 2 ^ n ve F ≤ ball(cancelPt(X), 2 · R) ve G ≤ ball(cancelPt(X), R) ve (her θ : Θ(X) için: HasBoundedStrongType((x1 : X → ℂ) (x2 : X) ↦ linearizedNontangentialOperator(Q, θ, K, x1, x2), 2, 2, volume, volume, ofNNReal(C_Ts(x)))) ise lintegral(restrict(volume, G), (x2 : X) ↦ iSup((R₁ : ℝ) ↦ iSup((h : R₁ ∈ Ioo(R⁻¹, R)) ↦ iSup((R₂ : ℝ) ↦ iSup((h2 : R₂ ∈ Ioo(R₁, R)) ↦ enorm(T_R(K, Q, R₁, R₂, R, f, x2))))))) ≤ ofNNReal(C1_0_2(x, q)) · volume(G) ^ (↑q')⁻¹ · volume(F) ^ (↑q)⁻¹.

Buraya şu adlar üzerinden gelinir; her birinin ispatının en az %97'si bir sonrakinin altındadır: `metric_carleson` → `linearized_metric_carleson` → `R_truncation`.

Dayandığı parçalar:
- %63,7: [`S_truncation`] → Adım 5
- %2,7: 68 küçük yardımcı sonuç

**Adım 5 — ispatın %63,7** [`finitary_carleson`]

> Verilsin: X : Type, x ∈ ℕ, q ∈ ℝ, K : X → X → ℂ, σ₁ : X → ℤ, σ₂ : X → ℤ, F : Set X ve G : Set X (koşullar: [MetricSpace(X)], [ProofData(x, q, K, σ₁, σ₂, F, G)]).
>
> O zaman: öyle bir G' : Set X vardır ki (MeasurableSet(G') ve 2 · volume(G') ≤ volume(G) ve (her f : X → ℂ için: eğer Measurable(f) ve (her x2 : X için: ‖f(x2)‖ ≤ indicator(F, 1, x2)) ise lintegral(restrict(volume, G ∖ G'), (x2 : X) ↦ enorm(sum(toFinset(Icc(σ₁(x2), σ₂(x2))), (s : ℤ) ↦ integral(volume, (y : X) ↦ Ks(s, x2, y) · f(y) · exp(I · ↑(Q(x2))(y)))))) ≤ ofNNReal(C2_0_1(x, nnq(X))) · volume(G) ^ (1 − q⁻¹) · volume(F) ^ q⁻¹)).

Buraya şu adlar üzerinden gelinir; her birinin ispatının en az %97'si bir sonrakinin altındadır: `S_truncation` → `linearized_truncation` → `finitary_carleson_step`.

Dayandığı parçalar:
- %53,7: [`discrete_carleson`] → Adım 6
- %5,4: [`grid_existence`]
- %2,4: [`tile_existence`]
- %1,3: 93 küçük yardımcı sonuç

**Adım 6 — ispatın %53,7** [`discrete_carleson`]

> Verilsin: X : Type, x ∈ ℕ, q ∈ ℝ, K : X → X → ℂ, σ₁ : X → ℤ, σ₂ : X → ℤ, F : Set X ve G : Set X (koşullar: [MetricSpace(X)], [ProofData(x, q, K, σ₁, σ₂, F, G)], [TileStructure(Q, defaultD(x), defaultκ(x), defaultS(X), cancelPt(X))]).
>
> O zaman: öyle bir G' : Set X vardır ki (MeasurableSet(G') ve 2 · volume(G') ≤ volume(G) ve (her f : X → ℂ için: eğer Measurable(f) ve (her x2 : X için: ‖f(x2)‖ ≤ indicator(F, 1, x2)) ise lintegral(restrict(volume, G ∖ G'), (x2 : X) ↦ enorm(carlesonSum(univ, f, x2))) ≤ ofNNReal(C2_0_2(x, nnq(X))) · volume(G) ^ (1 − q⁻¹) · volume(F) ^ q⁻¹)).

Dayandığı parçalar:
- %30,1: [`forest_union`] → Adım 7
- %12,8: [`forest_complement`]
- %4,3: [`exceptional_set`]
- %2,3: [`holder_van_der_corput`]
- %4,1: 199 küçük yardımcı sonuç

**Adım 7 — ispatın %30,1** [`forest_union_aux`]

> Verilsin: X : Type, x ∈ ℕ, q ∈ ℝ, K : X → X → ℂ, σ₁ : X → ℤ, σ₂ : X → ℤ, F : Set X, G : Set X ve f : X → ℂ (koşullar: [MetricSpace(X)], [ProofData(x, q, K, σ₁, σ₂, F, G)], [TileStructure(Q, defaultD(x), defaultκ(x), defaultS(X), cancelPt(X))]).
>
> Varsayalım (1): her x2 : X için: ‖f(x2)‖ ≤ indicator(F, 1, x2).
>
> Varsayalım (2): Measurable(f).
>
> O zaman: lintegral(restrict(volume, G ∖ G'), (x2 : X) ↦ enorm(carlesonSum(𝔓₁, f, x2))) ≤ ofNNReal(C2_0_4_base(x)) · 2 ^ (↑x + 5 / 2) · volume(G) ^ (1 − q⁻¹) · volume(F) ^ q⁻¹ · sum(Iic(maxℭ(X)), (n : ℕ) ↦ sum(Iic(n), (_k : ℕ) ↦ sum(Iic(2 · n + 3), (_j : ℕ) ↦ sum(Iio(4 · n + 12), (_l : ℕ) ↦ 2 ^ (−(q − 1) / q · ↑n))))).

Buraya şu adlar üzerinden gelinir; her birinin ispatının en az %97'si bir sonrakinin altındadır: `forest_union` → `forest_union_optimized`.

Dayandığı parçalar:
- %26,6: [`lintegral_carlesonSum_forest'`] → Adım 8
- %2,6: 59 küçük yardımcı sonuç

**Adım 8 — ispatın %26,6** [`lintegral_carlesonSum_forest`]

> Verilsin: X : Type, x ∈ ℕ, q ∈ ℝ, K : X → X → ℂ, σ₁ : X → ℤ, σ₂ : X → ℤ, F : Set X, G : Set X, k ∈ ℕ, n ∈ ℕ, j ∈ ℕ, l ∈ ℕ ve f : X → ℂ (koşullar: [MetricSpace(X)], [ProofData(x, q, K, σ₁, σ₂, F, G)], [TileStructure(Q, defaultD(x), defaultκ(x), defaultS(X), cancelPt(X))]).
>
> Varsayalım (1): Measurable(f).
>
> Varsayalım (2): her x2 : X için: ‖f(x2)‖ ≤ indicator(F, 1, x2).
>
> O zaman: lintegral(restrict(volume, G ∖ G'), (x2 : X) ↦ enorm(carlesonSum(iUnion((u : 𝔓(X)) ↦ iUnion((h : u ∈ 𝔘₄(k, n, j, l)) ↦ 𝔗₂(k, n, j, u))), f, x2))) ≤ ofNNReal(C2_0_4(x, q, n)) · (2 ^ (2 · x + 5) · volume(F) / volume(G)) ^ (q⁻¹ − 2⁻¹) · volume(F) ^ (1 / 2) · volume(G) ^ (1 / 2).

Buraya şu adlar üzerinden gelinir; her birinin ispatının en az %97'si bir sonrakinin altındadır: `lintegral_carlesonSum_forest'`.

Dayandığı parçalar:
- %24,2: [`forest_operator_le_volume`]
- %2,1: 14 küçük yardımcı sonuç

## 4. Sayılar

| | |
|---|---:|
| Projenin bildirimi | 4.974 |
| Bunlardan teorem | 4.239 |
| Ana teoremin kullandığı | 4.952 |
| Ana teoremin hiç kullanmadığı | 22 |
| Önermesi başka bir teoreminkiyle birebir aynı olan fazladan teorem | 1.300 (%30,7) |

## 5. Bu belge nasıl denetlenir

1. Kayıt: Lean'in resmi dışa aktarımı (`solution.ndjson.zst`), Lean çekirdeği tarafından doğrulanmış haliyle.
2. Omurga: kayıttaki bağımlılıklardan hesaplanan baskınlık ağacı. "Yalnızca o adım için var" ifadesi tanım gereği kesindir.
3. Cümleler: önermenin mantık iskeleti sabit kalıplarla yazılır (her, vardır, eğer–ise, ve, veya, değil); formüller kayıttaki terimden aynen basılır.
4. Yorum yok: belgede kayıtta bulunmayan hiçbir açıklama, niyet ya da değerlendirme yer almaz.
