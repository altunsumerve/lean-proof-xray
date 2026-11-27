# Koni / Cone — ispat konisi ve baskınlık ağacı / proof cone and dominator tree

Kök / root: `flt_regular`

Bu sayfadaki sayılar resmi Lean kaydının (lean4export) bağımlılık grafiğinden hesaplanır; tahmin içermez. / All numbers on this page are computed from the dependency graph of the official Lean export.

## 1. Sayılar / Numbers

| | Bildirim / declarations | İfade ağırlığı / expression weight |
|---|---:|---:|
| Kayıttaki toplam / total in the export | 86.782 | 13.170.926 |
| Kütüphane (Mathlib ve altı) / library | 86.356 | 12.976.129 |
| Proje / project | 426 | 194.797 |
| &nbsp;&nbsp;kökün ispat konisinde / in the root's proof cone | 425 (%99,8) | 194.797 (%100,0) |
| &nbsp;&nbsp;**kullanılmayan / unused by the root** | **1** (%0,2) | 0 (%0,0) |
| Kökün önermesini anlamak için gereken proje bildirimi / project declarations needed to read the root's statement | 4 | |
| Konideki kütüphane bildirimi / library declarations in the cone | 85.296 | |

> Not / note: bu satır yalnızca girdideki kaydı sayar. Kayıt belirli teoremler için dışa aktarıldıysa yalnızca onların gerektirdiğini içerir; o teoremlerin kullanmadığı proje kodu kayıtta yoktur ve burada sayılmaz. / This row counts only what is in the input record. A record exported for specific theorems contains only what they need, so project code those theorems do not use is absent from it and is not counted here.

İfade ağırlığı: bildirimin kayda eklediği yeni ifade düğümü sayısı (ispatın büyüklüğünün ölçüsü). / Expression weight: number of new expression nodes the declaration added to the export.

| Tür / kind | Projede / in project | Konide / in cone |
|---|---:|---:|
| teorem | 361 | 361 |
| tanım | 62 | 62 |
| kurucu | 1 | 1 |
| tip | 1 | 1 |
| özyineleyici | 1 | 0 |

## 2. Kullanılmayan kod / Unused code

Kökün ispatına hiç girmeyen proje bildirimi: **1** (bunların 1 tanesi Lean'in otomatik yardımcısı). / Project declarations never used by the root's proof: 1 (1 of them Lean-generated auxiliaries).

| Ad alanı / namespace | Bildirim | Ağırlık / weight |
|---|---:|---:|
| `systemOfUnits.rec` | 1 | 0 |

## 3. Kopya önermeler / Duplicate statements

Proje teoremi: 361. Önermesi (tipi) başka bir teoreminkiyle yapısal olarak aynı olan gruplar: **16**; fazladan kopya: **18** (%5,0). Yardımcı adlar hariç: 0 grup, 0 fazladan kopya. / Project theorems: 361. Groups whose statement (type) is structurally identical: 16; redundant copies: 18. Excluding auxiliary names: 0 groups, 0 redundant copies.

Not: parmak izi 64 bit ve yapısaldır (bağlı değişken adları sayılmaz); evren parametre adları farklıysa kopya sayılmaz. / The fingerprint is 64-bit and structural.

## 4. Baskınlık ağacı / Dominator tree

X, Y'nin üstündeyse kökten Y'ye giden her bağımlılık yolu X'ten geçer: Y yalnızca X için vardır. Bir satırın alt ağacı, makalede o başlığın altına girecek her şeydir. / If X is above Y, every dependency path from the root to Y passes through X.

Ağaçtaki düğüm: 425; kökün doğrudan çocukları: 6; en derin düzey: 19.

| Alt ağaç büyüklüğü / subtree size | Düğüm / nodes |
|---|---:|
| ≥ 10 bildirim | 30 |
| ≥ 100 bildirim | 13 |
| ≥ 1.000 bildirim | 0 |
| ≥ 10.000 bildirim | 0 |
| ≥ 100.000 bildirim | 0 |

Aşağıda ağırlığı toplamın en az %0,5'i olan dallar (en çok 5 düzey). Sütunlar: alt ağaçtaki bildirim, ağırlık payı, bu bildirimi doğrudan kullanan sayısı.

```
flt_regular  [teorem]  alt=425  %100,0  kullanan=1
  FltRegular.caseII  [teorem]  alt=345  %85,0  kullanan=1
    FltRegular.not_exists_Int_solution'  [teorem]  alt=340  %84,3  kullanan=1
      FltRegular.not_exists_Int_solution  [teorem]  alt=339  %84,0  kullanan=1
        FltRegular.not_exists_solution'  [teorem]  alt=338  %83,2  kullanan=1
          FltRegular.not_exists_solution  [teorem]  alt=337  %82,6  kullanan=1
    … ve 4 küçük çocuk daha
  FltRegular.caseI  [teorem]  alt=70  %13,3  kullanan=1
    FltRegular.caseI_easier  [teorem]  alt=48  %10,5  kullanan=1
      FltRegular.ex_fin_div  [teorem]  alt=33  %7,6  kullanan=1
        FltRegular.CaseI.exists_int_sum_eq_zero  [teorem]  alt=9  %3,3  kullanan=1
          FltRegular.CaseI.exists_int_sum_eq_zero'  [teorem]  alt=8  %3,2  kullanan=1
        FltRegular.is_principal  [teorem]  alt=18  %2,8  kullanan=1
          FltRegular.exists_ideal  [teorem]  alt=16  %2,4  kullanan=1
          … ve 1 küçük çocuk daha
        … ve 5 küçük çocuk daha
      dvd_coeff_cycl_integer  [teorem]  alt=2  %1,3  kullanan=1
        … ve 1 küçük çocuk daha
      _private.FltRegular.CaseI.Statement.#0.FltRegular.sum_caseICoeff  [teorem]  alt=1  %0,6  kullanan=1
      … ve 5 küçük çocuk daha
    FltRegular.CaseI.may_assume  [teorem]  alt=21  %2,8  kullanan=1
      FltRegular.a_not_cong_b  [teorem]  alt=11  %1,0  kullanan=1
        … ve 7 küçük çocuk daha
      FltRegular.MayAssume.coprime  [teorem]  alt=3  %0,8  kullanan=1
        … ve 2 küçük çocuk daha
      … ve 6 küçük çocuk daha
  exists_dvd_pow_sub_Int_pow  [teorem]  alt=2  %1,2  kullanan=2
    … ve 1 küçük çocuk daha
  … ve 3 küçük çocuk daha
```

## 5. En büyük kilometre taşları / Largest milestones

Kök dışındaki, yardımcı olmayan teoremler; alt ağaç ağırlığına göre. Önerme metni projenin kaynağından alınmıştır (atlas verildiyse). / Non-auxiliary theorems other than the root, by subtree weight; statement text is from the source when available.

| # | Teorem | Alt ağaç | Pay | Üstü / dominator | Kaynak |
|---:|---|---:|---:|---|---|
| 1 | `FltRegular.caseII` | 345 | %85,0 | `flt_regular` |  |
| 2 | `FltRegular.not_exists_Int_solution'` | 340 | %84,3 | `FltRegular.caseII` |  |
| 3 | `FltRegular.not_exists_Int_solution` | 339 | %84,0 | `FltRegular.not_exists_Int_solution'` |  |
| 4 | `FltRegular.not_exists_solution'` | 338 | %83,2 | `FltRegular.not_exists_Int_solution` |  |
| 5 | `FltRegular.not_exists_solution` | 337 | %82,6 | `FltRegular.not_exists_solution'` |  |
| 6 | `exists_solution'` | 283 | %70,4 | `FltRegular.not_exists_solution` |  |
| 7 | `eq_pow_prime_of_unit_of_congruent` | 249 | %59,0 | `exists_solution'` |  |
| 8 | `exists_pow_eq_of_zeta_sub_one_pow_dvd_sub_one` | 242 | %54,3 | `eq_pow_prime_of_unit_of_congruent` |  |
| 9 | `dvd_card_classGroup_of_unramified_isCyclic` | 208 | %42,4 | `exists_pow_eq_of_zeta_sub_one_pow_dvd_sub_one` |  |
| 10 | `exists_not_isPrincipal_and_isPrincipal_map` | 206 | %41,8 | `dvd_card_classGroup_of_unramified_isCyclic` |  |
| 11 | `Hilbert92` | 196 | %34,6 | `exists_not_isPrincipal_and_isPrincipal_map` |  |
| 12 | `almostHilbert92` | 195 | %34,6 | `Hilbert92` |  |
| 13 | `FltRegular.caseI` | 70 | %13,3 | `flt_regular` |  |
| 14 | `KummersLemma.isUnramified` | 33 | %10,9 | `exists_pow_eq_of_zeta_sub_one_pow_dvd_sub_one` |  |
| 15 | `FltRegular.caseI_easier` | 48 | %10,5 | `FltRegular.caseI` |  |
| 16 | `exists_solution` | 31 | %9,3 | `exists_solution'` |  |
| 17 | `FltRegular.ex_fin_div` | 33 | %7,6 | `FltRegular.caseI_easier` |  |
| 18 | `exists_not_isPrincipal_and_isPrincipal_map_aux` | 9 | %6,7 | `exists_not_isPrincipal_and_isPrincipal_map` |  |
| 19 | `lh_pow_free` | 13 | %4,7 | `almostHilbert92` |  |
| 20 | `lh_pow_free'` | 11 | %4,5 | `lh_pow_free` |  |
| 21 | `comap_map_eq_of_unramified` | 7 | %4,4 | `exists_not_isPrincipal_and_isPrincipal_map_aux` |  |
| 22 | `systemOfUnits.IsFundamental.corollary` | 13 | %4,2 | `almostHilbert92` |  |
| 23 | `isTors'` | 4 | %4,1 | `relativeUnitsModule` |  |
| 24 | `exists_not_dvd_spanSingleton_eq_a_div_a_zero` | 7 | %3,9 | `exists_solution` |  |
| 25 | `one_le_m` | 5 | %3,3 | `FltRegular.not_exists_solution` |  |
| 26 | `KummersLemma.separable_poly` | 9 | %3,3 | `KummersLemma.isUnramified` |  |
| 27 | `FltRegular.CaseI.exists_int_sum_eq_zero` | 9 | %3,3 | `FltRegular.ex_fin_div` |  |
| 28 | `FltRegular.CaseI.exists_int_sum_eq_zero'` | 8 | %3,2 | `FltRegular.CaseI.exists_int_sum_eq_zero` |  |
| 29 | `KummersLemma.separable_poly_aux` | 8 | %2,8 | `KummersLemma.separable_poly` |  |
| 30 | `systemOfUnits.IsFundamental.lemma2` | 7 | %2,8 | `systemOfUnits.IsFundamental.corollary` |  |
| 31 | `FltRegular.CaseI.may_assume` | 21 | %2,8 | `FltRegular.caseI` |  |
| 32 | `FltRegular.is_principal` | 18 | %2,8 | `FltRegular.ex_fin_div` |  |
| 33 | `zeta_sub_one_pow_dvd_norm_sub_pow` | 3 | %2,7 | `eq_pow_prime_of_unit_of_congruent` |  |
| 34 | `h_exists'` | 2 | %2,5 | `almostHilbert92` |  |
| 35 | `exists_not_dvd_spanSingleton_eq` | 2 | %2,5 | `exists_not_dvd_spanSingleton_eq_a_div_a_zero` |  |
| 36 | `FltRegular.exists_ideal` | 16 | %2,4 | `FltRegular.is_principal` |  |
| 37 | `KummersLemma.minpoly_polyRoot'` | 4 | %2,1 | `KummersLemma.isUnramified` |  |
| 38 | `formula` | 7 | %2,0 | `exists_solution` |  |
| 39 | `KummersLemma.minpoly_polyRoot''` | 3 | %1,9 | `KummersLemma.minpoly_polyRoot'` |  |
| 40 | `fltIdeals_coprime` | 11 | %1,9 | `FltRegular.exists_ideal` |  |
| 41 | `KummersLemma.irreducible_map_poly` | 2 | %1,7 | `KummersLemma.minpoly_polyRoot''` |  |
| 42 | `div_one_sub_zeta_mem` | 3 | %1,6 | `divZetaSubOne` |  |
| 43 | `unit_inv_conj_is_root_of_unity` | 4 | %1,6 | `FltRegular.CaseI.exists_int_sum_eq_zero'` |  |
| 44 | `Hilbert92_aux2` | 3 | %1,6 | `almostHilbert92` |  |
| 45 | `fltIdeals_coprime2` | 6 | %1,6 | `fltIdeals_coprime` |  |
| 46 | `isUnramifiedAt_of_Separable_minpoly` | 2 | %1,6 | `KummersLemma.isUnramified` |  |
| 47 | `fltIdeals_coprime2_lemma` | 4 | %1,5 | `fltIdeals_coprime2` |  |
| 48 | `KummersLemma.map_poly_eq_prod` | 7 | %1,5 | `KummersLemma.separable_poly_aux` |  |
| 49 | `Hilbert91` | 8 | %1,5 | `almostHilbert92` |  |
| 50 | `exists_ideal_pow_eq_c` | 6 | %1,5 | `FltRegular.not_exists_solution` |  |

