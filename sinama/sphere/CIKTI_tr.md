# Kodun çıktısı: Smale

*Bu belge bir yapay zekâ tarafından yazılmadı. Resmi Lean kaydından, sabit kurallarla üretildi (`arac/belge.py`). Aynı kayıtla çalıştıran herkes harfi harfine aynı belgeyi elde eder. Köşeli parantez içindeki adlar koddaki adlardır.*

## 1. Kanıtlanan cümle

Kodun kanıtladığı teorem `Smale`. Önermesi:

> Öyle bir f : ℝ → Elem(sphere(0, 1)) → EuclideanSpace(ℝ, Fin(3)) vardır ki (ContMDiff(prod(modelWithCornersSelf(ℝ, ℝ), modelWithCornersSelf(ℝ, EuclideanSpace(ℝ, Fin(2)))), modelWithCornersSelf(ℝ, EuclideanSpace(ℝ, Fin(3))), some(top), uncurry(f)) ve f(0) = ((x : Elem(sphere(0, 1))) ↦ ↑x) ve f(1) = ((x : Elem(sphere(0, 1))) ↦ −↑x) ve (her t ∈ ℝ için: Immersion(modelWithCornersSelf(ℝ, EuclideanSpace(ℝ, Fin(2))), modelWithCornersSelf(ℝ, EuclideanSpace(ℝ, Fin(3))), f(t), some(top)))).

Bu cümle projeye özgü 2 tanıma ve kütüphaneden 4.976 kavrama dayanır.

## 2. İspatın omurgası

İspatın tamamı 1.715 bildirimdir. Aşağıdaki adımlar bunların içinden kurallı olarak seçildi: her seferinde, altında en çok ispat bulunan adım açıldı. Yüzde, ispatın ne kadarının yalnızca o adım için var olduğunu gösterir.

| Adım | Önerme | İspattaki payı |
|---:|---|---:|
| 1 | (uzun; aşağıda) | %100,0 |
| 2 | (uzun; aşağıda) | %79,7 |
| 3 | (uzun; aşağıda) | %64,9 |
| 4 | (uzun; aşağıda) | %52,2 |
| 5 | (uzun; aşağıda) | %29,0 |
| 6 | (uzun; aşağıda) | %20,7 |
| 7 | (uzun; aşağıda) | %9,9 |
| 8 | (uzun; aşağıda) | %8,8 |

**Adım 1 — ispatın %100,0** [`sphere_eversion`]

> Verilsin: E : Type (koşullar: [NormedAddCommGroup(E)], [InnerProductSpace(ℝ, E)], finrank(ℝ, E) = 3).
>
> O zaman: öyle bir f : ℝ → Elem(sphere(0, 1)) → E vardır ki (ContMDiff(prod(modelWithCornersSelf(ℝ, ℝ), modelWithCornersSelf(ℝ, EuclideanSpace(ℝ, Fin(2)))), modelWithCornersSelf(ℝ, E), some(top), uncurry(f)) ve f(0) = ((x : Elem(sphere(0, 1))) ↦ ↑x) ve f(1) = ((x : Elem(sphere(0, 1))) ↦ −↑x) ve (her t ∈ ℝ için: Immersion(modelWithCornersSelf(ℝ, EuclideanSpace(ℝ, Fin(2))), modelWithCornersSelf(ℝ, E), f(t), some(top)))).

Buraya şu adlar üzerinden gelinir; her birinin ispatının en az %97'si bir sonrakinin altındadır: `Smale`.

Dayandığı parçalar:
- %79,7: [`immersionRel_satisfiesHPrincipleWith`] → Adım 2
- %8,8: [`formalEversion`] → Adım 8
- %10,9: 125 küçük yardımcı sonuç

**Adım 2 — ispatın %79,7** [`RelMfld.Ample.satisfiesHPrincipleWith`]

> Verilsin: EM : Type, HM : Type, IM : ModelWithCorners(ℝ, EM, HM), M : Type, EX : Type, HX : Type, IX : ModelWithCorners(ℝ, EX, HX), X : Type, R : RelMfld(IM, M, IX, X), δ : M → ℝ, EP : Type, HP : Type, IP : ModelWithCorners(ℝ, EP, HP), P : Type ve C : Set (P × M) (koşullar: [NormedAddCommGroup(EM)], [NormedSpace(ℝ, EM)], [FiniteDimensional(ℝ, EM)], [TopologicalSpace(HM)], [Boundaryless(IM)], [TopologicalSpace(M)], [ChartedSpace(HM, M)], [IsManifold(IM, some(top), M)], [T2Space(M)], [SigmaCompactSpace(M)], [NormedAddCommGroup(EX)], [NormedSpace(ℝ, EX)], [FiniteDimensional(ℝ, EX)], [TopologicalSpace(HX)], [Boundaryless(IX)], [MetricSpace(X)], [ChartedSpace(HX, X)], [IsManifold(IX, some(top), X)], [SigmaCompactSpace(X)], [NormedAddCommGroup(EP)], [NormedSpace(ℝ, EP)], [FiniteDimensional(ℝ, EP)], [TopologicalSpace(HP)], [Boundaryless(IP)], [TopologicalSpace(P)], [ChartedSpace(HP, P)], [IsManifold(IP, some(top), P)], [SigmaCompactSpace(P)], [T2Space(P)]).
>
> Varsayalım (1): Ample(R).
>
> Varsayalım (2): IsOpen(R).
>
> Varsayalım (3): IsClosed(C).
>
> Varsayalım (4): her x : M için: 0 < δ(x).
>
> Varsayalım (5): Continuous(δ).
>
> O zaman: SatisfiesHPrincipleWith(IP, R, C, δ).

Buraya şu adlar üzerinden gelinir; her birinin ispatının en az %97'si bir sonrakinin altındadır: `immersionRel_satisfiesHPrincipleWith`.

Dayandığı parçalar:
- %64,9: [`RelMfld.Ample.satisfiesHPrinciple`] → Adım 3
- %6,4: [`RelMfld.SatisfiesHPrinciple.satisfiesHPrincipleWith`]
- %3,0: [`RelMfld.Ample.relativize`]
- %3,3: 21 küçük yardımcı sonuç

**Adım 3 — ispatın %64,9** [`RelMfld.Ample.satisfiesHPrinciple`]

> Verilsin: EM : Type, HM : Type, IM : ModelWithCorners(ℝ, EM, HM), M : Type, EX : Type, HX : Type, IX : ModelWithCorners(ℝ, EX, HX), X : Type, R : RelMfld(IM, M, IX, X), A : Set M ve δ : M → ℝ (koşullar: [NormedAddCommGroup(EM)], [NormedSpace(ℝ, EM)], [FiniteDimensional(ℝ, EM)], [TopologicalSpace(HM)], [Boundaryless(IM)], [TopologicalSpace(M)], [ChartedSpace(HM, M)], [IsManifold(IM, some(top), M)], [T2Space(M)], [SigmaCompactSpace(M)], [NormedAddCommGroup(EX)], [NormedSpace(ℝ, EX)], [FiniteDimensional(ℝ, EX)], [TopologicalSpace(HX)], [Boundaryless(IX)], [MetricSpace(X)], [ChartedSpace(HX, X)], [IsManifold(IX, some(top), X)], [SigmaCompactSpace(X)]).
>
> Varsayalım (1): Ample(R).
>
> Varsayalım (2): IsOpen(R).
>
> Varsayalım (3): IsClosed(A).
>
> Varsayalım (4): her x : M için: 0 < δ(x).
>
> Varsayalım (5): Continuous(δ).
>
> O zaman: SatisfiesHPrinciple(R, A, δ).

Dayandığı parçalar:
- %52,2: [`OpenSmoothEmbedding.improve_formalSol`] → Adım 4
- %5,2: [`exists_stability_dist`]
- %4,1: 42 küçük yardımcı sonuç

**Adım 4 — ispatın %52,2** [`OpenSmoothEmbedding.improve_formalSol`]

Bu adımın önermesi kısa bir cümleye sığmıyor (1.674 karakter); tam hali uzun çıktıdadır.

Dayandığı parçalar:
- %29,0: [`RelLoc.FormalSol.improve_htpy'`] → Adım 5
- %6,0: [`OneJetBundle.embedding`]
- %15,2: 109 küçük yardımcı sonuç

**Adım 5 — ispatın %29,0** [`RelLoc.FormalSol.improve`]

> Verilsin: E : Type, F : Type ve R : RelLoc(E, F) (koşullar: [NormedAddCommGroup(E)], [NormedSpace(ℝ, E)], [NormedAddCommGroup(F)], [NormedSpace(ℝ, F)], [FiniteDimensional(ℝ, E)], [FiniteDimensional(ℝ, F)]).
>
> Varsayalım (1): IsOpen(R).
>
> Varsayalım (2): IsAmple(R).
>
> O zaman: her L : Landscape(E) ve ε ∈ ℝ için: eğer 0 < ε ise (her 𝓕 : FormalSol(R) için: eğer Eventually((x : E) ↦ IsHolonomicAt(𝓕, x), nhdsSet(C(L))) ise öyle bir H : HtpyJetSec(E, F) vardır ki (Eventually((t : ℝ) ↦ H(t) = toJetSec(𝓕), nhdsSet(Iic(0))) ve Eventually((t : ℝ) ↦ H(t) = H(1), nhdsSet(Ici(1))) ve Eventually((x : E) ↦ ∀ (t : ℝ), (H(t))(x) = 𝓕(x), nhdsSet(C(L))) ve (her x : E için: eğer (x ∈ K₁(L) doğru değildir) ise (her t ∈ ℝ için: (H(t))(x) = 𝓕(x))) ve (her x : E ve t ∈ ℝ için: ‖f(H(t), x) − f(toJetSec(𝓕), x)‖ ≤ ε) ve (her t ∈ ℝ için: IsFormalSol(H(t), R)) ve Eventually((x : E) ↦ JetSec.IsHolonomicAt(H(1), x), nhdsSet(K₀(L))))).

Buraya şu adlar üzerinden gelinir; her birinin ispatının en az %97'si bir sonrakinin altındadır: `RelLoc.FormalSol.improve_htpy'`.

Dayandığı parçalar:
- %20,7: [`exist_loops`] → Adım 6
- %7,1: 107 küçük yardımcı sonuç

**Adım 6 — ispatın %20,7** [`exist_loops`]

> Verilsin: E : Type, F : Type, g : E → F, b : E → F, Ω : Set (E × F) ve K : Set E (koşullar: [NormedAddCommGroup(E)], [NormedSpace(ℝ, E)], [NormedAddCommGroup(F)], [NormedSpace(ℝ, F)], [FiniteDimensional(ℝ, F)], [FiniteDimensional(ℝ, E)]).
>
> Varsayalım (1): IsCompact(K).
>
> Varsayalım (2): IsOpen(Ω).
>
> Varsayalım (3): ContDiff(ℝ, some(top), g).
>
> Varsayalım (4): ContDiff(ℝ, some(top), b).
>
> Varsayalım (5): Eventually((x : E) ↦ g(x) = b(x), nhdsSet(K)).
>
> Varsayalım (6): her x : E için: g(x) ∈ (convexHull(ℝ))(connectedComponentIn(preimage(Prod.mk(x), Ω), b(x))).
>
> O zaman: öyle bir γ : ℝ → E → Loop(F) vardır ki NiceLoop(g, b, Ω, K, γ).

Dayandığı parçalar:
- %9,9: [`exist_loops_aux2`] → Adım 7
- %2,8: [`SmoothSurroundingFamily.exists_smooth_isCenteringDensity`]
- %2,5: [`SmoothSurroundingFamily.reparametrize_smooth`]
- %5,1: 101 küçük yardımcı sonuç

**Adım 7 — ispatın %9,9** [`exist_loops_aux2`]

> Verilsin: E : Type, F : Type, g : E → F, b : E → F, Ω : Set (E × F) ve K : Set E (koşullar: [NormedAddCommGroup(E)], [NormedSpace(ℝ, E)], [NormedAddCommGroup(F)], [NormedSpace(ℝ, F)], [FiniteDimensional(ℝ, F)], [FiniteDimensional(ℝ, E)]).
>
> Varsayalım (1): IsCompact(K).
>
> Varsayalım (2): IsOpen(Ω).
>
> Varsayalım (3): ContDiff(ℝ, some(top), g).
>
> Varsayalım (4): ContDiff(ℝ, some(top), b).
>
> Varsayalım (5): Eventually((x : E) ↦ g(x) = b(x), nhdsSet(K)).
>
> Varsayalım (6): her x : E için: g(x) ∈ (convexHull(ℝ))(connectedComponentIn(preimage(Prod.mk(x), Ω), b(x))).
>
> O zaman: öyle bir γ : E → ℝ → Loop(F) vardır ki (SurroundingFamilyIn(g, b, γ, univ, Ω) ve ContDiff(ℝ, some(top), uncurry(γ)) ve Eventually((x : E) ↦ ∀ (t s : ℝ), closedBall((x, b(x)), dist(Loop.toFun(γ(x, t), s), b(x))) ≤ Ω, nhdsSet(K))).

Dayandığı parçalar:
- %3,8: [`exists_surrounding_loops`]
- %5,2: 42 küçük yardımcı sonuç

**Adım 8 — ispatın %8,8** [`formalEversionAux2`]

> (E : Type) [NormedAddCommGroup(E)] [InnerProductSpace(ℝ, E)] [Fact(finrank(ℝ, E) = 3)] (ω : Orientation(ℝ, E, Fin(3))) ↦ (let __src := formalEversionAux(E, ω); FamilyFormalSol.mk(__src, _proof_1(E, ω))).

Buraya 1 ara ad üzerinden gelinir; bunlar aynı sonucu yeniden adlandırır: `formalEversion`.

Dayandığı parçalar:
- %4,8: [`formalEversionAux`]
- %2,2: [`formalEversionAux2._proof_1`]
- %1,7: 11 küçük yardımcı sonuç

## 4. Sayılar

| | |
|---|---:|
| Projenin bildirimi | 1.733 |
| Bunlardan teorem | 1.306 |
| Ana teoremin kullandığı | 1.715 |
| Ana teoremin hiç kullanmadığı | 18 |
| Önermesi başka bir teoreminkiyle birebir aynı olan fazladan teorem | 100 (%7,7) |

## 5. Bu belge nasıl denetlenir

1. Kayıt: Lean'in resmi dışa aktarımı (`solution.ndjson.zst`), Lean çekirdeği tarafından doğrulanmış haliyle.
2. Omurga: kayıttaki bağımlılıklardan hesaplanan baskınlık ağacı. "Yalnızca o adım için var" ifadesi tanım gereği kesindir.
3. Cümleler: önermenin mantık iskeleti sabit kalıplarla yazılır (her, vardır, eğer–ise, ve, veya, değil); formüller kayıttaki terimden aynen basılır.
4. Yorum yok: belgede kayıtta bulunmayan hiçbir açıklama, niyet ya da değerlendirme yer almaz.
