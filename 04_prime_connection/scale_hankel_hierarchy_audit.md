# Higher Scale-Hankel Hierarchy Audit

Date: 2026-09-15

## 목적

이전 2x2 multiplicative scale curvature

\[
K_2(2^k)=M(2^{k-1})^2-M(2^k)M(2^{k-2})
\]

가 known-zero spectral energy를 재표현한다는 판정을 더 높은 determinant order에서도 확인한다.

---

## 1. 정의

\[
y_k=M(2^k)
\]

로 두고 rank `r>=2` scale-Hankel determinant를

\[
\boxed{
H_r(k)=\det[y_{k+i+j}]_{i,j=0}^{r-1}
}
\]

로 정의한다.

`r=2`이면

\[
H_2(k)=y_ky_{k+2}-y_{k+1}^2
\]

으로 이전 curvature와 index/sign convention만 다르다.

---

## 2. finite exponential exact identity

finite exponential signal

\[
y_k=\sum_{\ell=1}^L c_\ell q_\ell^k
\]

을 생각한다.

Vandermonde matrix를 사용하면 Hankel matrix는

\[
[y_{k+i+j}]
=V\,\operatorname{diag}(c_\ell q_\ell^k)\,V^T
\]

형태가 되고 Cauchy-Binet으로

\[
\boxed{
H_r(k)
=
\sum_{\substack{S\subseteq\{1,\ldots,L\}\\|S|=r}}
\left(\prod_{\ell\in S}c_\ell q_\ell^k\right)
\prod_{\substack{i<j\\i,j\in S}}(q_j-q_i)^2.
}
\]

따라서 rank `r` determinant는 fewer-than-`r` mode signal을 정확히 annihilate하고, distinct `r`-mode subsets만 남기는 spectral mode selector다.

상태: `EXACT_FINITE_SPECTRAL`.

---

## 3. real-part growth interpretation

`q_l=2^{lambda_l}`라 하면 각 subset term의 magnitude exponent는

\[
2^{k\sum_{\ell\in S}\Re\lambda_\ell}.
\]

따라서 finite spectrum에서 dominant subset이 안정하다면

\[
\frac1r\frac{d}{dk}\log_2|H_r(k)|
\]

은 선택된 `r`개 mode의 평균 real part를 읽는다.

모든 mode가 `Re(lambda)=1/2`라면 expected slope는

\[
\boxed{r/2}.
\]

그러나 off-line spectrum에서는 이것이 반드시 spectral maximum 하나를 직접 읽는 것은 아니다. top-`r` mode competition과 cancellation을 별도로 처리해야 한다.

---

## 4. RH-line normalization

RH-line scaling을 **해석용으로만** 넣으면

\[
y_k=2^{k/2}G_k
\]

이므로

\[
H_r(k)
=
2^{rk/2+r(r-1)/2}
\det[G_{k+i+j}].
\]

따라서 normalized determinant는

\[
\boxed{
\widetilde H_r(k)
=
\frac{H_r(k)}{2^{rk/2+r(r-1)/2}}.
}
\]

수치 zero-wave 비교에서는 이 normalization을 사용한다. 실제 slope scan에서는 `1/2`를 fitting target으로 넣지 않는다.

---

## 5. published dyadic Mertens data 결과

`data/mertens/mertens_powers_of_two_0_75.csv`의 `k=10..75` 범위를 사용했다.

| rank r | samples | OLS slope | beta_eff = slope/r | late-half beta_eff |
|---:|---:|---:|---:|---:|
| 2 | 64 | 1.002489 | 0.501245 | 0.464898 |
| 3 | 62 | 1.500816 | 0.500272 | 0.472915 |
| 4 | 60 | 2.006103 | 0.501526 | 0.475101 |
| 5 | 58 | 2.540853 | 0.508171 | 0.469010 |
| 6 | 56 | 3.030213 | 0.505035 | 0.467400 |
| 7 | 54 | 3.511718 | 0.501674 | 0.456612 |
| 8 | 52 | 4.022114 | 0.502764 | 0.451792 |

전체 finite range만 보면 모든 rank에서 `beta_eff`가 놀랍게도 `~1/2`에 모인다.

그러나 late-half window에서는 `~0.45-0.48`로 크게 이동한다.

따라서 전체-range `1/2` 근접성은 `NUMERICAL`이며 cutoff-stable theorem으로 승격하지 않는다.

---

## 6. first-100-known-zero reconstruction

known critical-line zeros `rho_j=1/2+i gamma_j`와

\[
c_j=\frac1{\rho_j\zeta'(\rho_j)}
\]

를 사용하여

\[
\frac{M(2^k)}{2^{k/2}}
\approx
2\Re\sum_{j=1}^{100}c_j e^{i\gamma_jk\log2}
\]

인 finite zero-wave를 만들고 동일한 `H_r`를 계산했다.

결과:

| rank r | corr(actual, first-100-zero determinant) | R^2 |
|---:|---:|---:|
| 2 | 0.932811 | 0.869769 |
| 3 | 0.959013 | 0.911349 |
| 4 | 0.954112 | 0.870632 |
| 5 | 0.964465 | 0.893291 |
| 6 | 0.913992 | 0.775732 |
| 7 | 0.893361 | 0.682185 |
| 8 | 0.899452 | 0.594621 |

rank `2..5`에서는 시계열 자체가 `0.93-0.96` correlation으로 재현된다.

높은 rank에서 `R^2`가 떨어지지만 determinant가 작은 Mertens reconstruction error를 polynomially 증폭하므로 이를 새 residual 신호로 해석하지 않는다.

---

## 7. 핵심 판정

rank를 높이면 single-mode 또는 low-rank spectral component를 더 많이 제거할 수는 있다.

그러나 실제 관측된 near-`r/2` growth와 determinant fluctuation 대부분은 **already-known zero wave의 nonlinear image**다.

따라서

\[
\boxed{
\text{finite scale-Hankel hierarchy}
=
\text{spectral mode-selection / re-encoding}
}
\]

으로 분류한다.

`r=2`만 우연히 zero energy를 본 것이 아니라 hierarchy 전체가 같은 구조다.

---

## 8. 선행문헌 감사

Hankel determinants constructed from zeta values 자체는 기존 연구가 있으며, 최근에도 RH와 Hankel positivity를 연결하는 서로 다른 construction들이 등장한다.

이번 targeted search에서는

\[
\det[M(2^{k+i+j})]
\]

그 자체를 standard RH criterion으로 사용하는 peer-reviewed route를 직접 확인하지 못했다.

그러나 `Hankel determinant`라는 방법론 또는 RH 연결의 신규성은 주장하지 않는다.

현재 repository의 독립 contribution 후보는 오직 위 finite exponential mode-selection identity를 Mertens dyadic data audit에 적용한 방식이며, 이것도 proof claim이 아니다.

---

## 9. 닫히는 경로

1. 2x2 curvature가 실패했으니 3x3, 4x4 determinant를 올리면 zero information을 벗어난다는 기대.
2. full-range `slope/r ~ 1/2`를 critical-line proof evidence로 사용하는 해석.
3. finite known-zero reconstruction과 같은 spectral signal을 다시 formation law로 세는 해석.

모두 닫는다.

---

## 10. 다음 후보 조건

이제 후속 nonlinear operator는 최소한 다음을 만족해야 한다.

- finite exponential mode selector만으로 환원되지 않을 것.
- known-zero wave를 입력했을 때 자동으로 재현되는 statistic이 아닐 것.
- arithmetic side에서 독립 sign/positivity/contraction theorem을 가질 것.
- fixed Dirichlet convolution algebra에도 속하지 않을 것.

## 재현자료

```text
data/mertens/scale_hankel_hierarchy_summary.csv
scripts/audit_scale_hankel_hierarchy.py
```

## 상태

- finite Cauchy-Binet identity: `EXACT`.
- dyadic slopes: `NUMERICAL`.
- first-100-zero reconstruction: `NUMERICAL / ZERO-INFORMED`.
- finite scale-Hankel hierarchy as independent RH route: `CLOSED_AS_SPECTRAL_REENCODING`.
- RH: `OPEN`.
