# Floor-Quotient Poset Bridge Audit

Date: 2026-09-15

## 목적

fixed floor-dilation이 Dirichlet convolution으로 재분류된 뒤, floor quotient 자체가 만드는 **별도의 incidence-poset Möbius structure**가 classical Mertens cancellation을 더 제어하기 쉬운 형태로 바꾸는지 감사한다.

기준 문헌은 Lagarias--Richman (2024), *The floor quotient partial order*이다.

---

## 1. quotient-count matrix의 exact inverse

정수 `1<=q<=n<=N`에 대해

\[
W_{nq}=\left\lfloor\frac nq\right\rfloor-
\left\lfloor\frac n{q+1}\right\rfloor
\]

로 둔다.

이는

\[
\#\{d:\lfloor n/d\rfloor=q\}
\]

이다.

Mertens function을 `M(0)=0`으로 두고

\[
U_{nq}
=M\!\left(\left\lfloor\frac nq\right\rfloor\right)
-M\!\left(\left\lfloor\frac n{q+1}\right\rfloor\right)
\]

라 두면

\[
U_{nq}
=\sum_{\substack{d\le n\\\lfloor n/d\rfloor=q}}\mu(d).
\]

앞서 증명한 `T_mu T_1=I`에서 바로

\[
\boxed{U_N=W_N^{-1}}
\]

가 모든 finite `N`에 대해 성립한다.

따라서

\[
W_N\,\mathbf M=\mathbf 1,
\qquad
\mathbf M=U_N\mathbf 1
\]

이다.

### 정보 감사

우변 `W_N M=1`이 단순한 것은 Mertens difficulty가 사라졌기 때문이 아니다.

역행렬의 entries 자체가 exact Mertens block increments이다.

\[
\boxed{
\text{forward simplification}
\Longleftrightarrow
\text{inverse conditioning carries Mertens cancellation}
}
\]

상태: `EXACT`.

---

## 2. finite conditioning diagnostic

직접 SVD 계산:

| N | cond_2(W_N) | ||W_N^{-1}||_2 | max inverse row l1 |
|---:|---:|---:|---:|
| 16 | 1.12e2 | 5.16 | 5 |
| 32 | 5.57e2 | 9.45 | 10 |
| 64 | 2.64e3 | 16.22 | 15 |
| 128 | 1.43e4 | 31.39 | 22 |
| 256 | 8.85e4 | 69.08 | 41 |
| 512 | 4.75e5 | 131.54 | 63 |

모든 경우 exact integer construction에서 `U W = I`를 오차 0으로 확인한 뒤 floating SVD만 conditioning diagnostic에 사용했다.

이 표는 asymptotic theorem이 아니다. 다만 forward quotient aggregation이 numerically well-conditioned inversion을 주는 것은 아니라는 점과 정합적이다.

---

## 3. Lagarias--Richman top-half theorem

floor quotient poset의 two-variable Möbius function을 `mu_1(d,n)`라 하자.

Lagarias--Richman Theorem 1.4는 `1<=k<=sqrt(n)`에서

\[
\boxed{
\mu_1\!\left(\left\lfloor\frac nk\right\rfloor,n\right)=\mu(k)
}
\]

를 준다.

즉 initial interval의 multiplicative top half에는 classical Möbius function이 exact하게 embedded된다.

---

## 4. Mertens lower-half bridge

`n=s(s+1)`로 둔다.

이 경우 floor-quotient initial interval은

\[
\mathcal Q^{-}(n)=\{1,\ldots,s\}
\]

와

\[
\mathcal Q^{+}(n)=
\left\{\left\lfloor\frac nk\right\rfloor:1\le k\le s\right\}
\]

로 나뉘며 두 집합은 disjoint이다. 실제로 top-half의 최소값은

\[
\left\lfloor\frac{n}{s}\right\rfloor=s+1.
\]

top-half theorem 때문에

\[
\sum_{d\in\mathcal Q^+(n)}\mu_1(d,n)
=\sum_{k=1}^{s}\mu(k)
=M(s).
\]

incidence Möbius cancellation으로 `n>1`에서

\[
\sum_{d\in\mathcal Q[1,n]}\mu_1(d,n)=0.
\]

따라서 즉시

\[
\boxed{
M(s)
=-\sum_{d=1}^{s}\mu_1(d,s(s+1)).
}
\]

을 얻는다.

이는 Lagarias--Richman top-half theorem과 standard incidence cancellation의 직접 corollary이며, 신규성은 주장하지 않는다.

상태: `EXACT_COROLLARY`.

---

## 5. lower-half cancellation audit

위 식이 Mertens를 더 작은 항들의 합으로 바꾸는지 직접 계산했다.

| s | M(s) | lower sum | lower l1 | lower l2 | max | nonzero |
|---:|---:|---:|---:|---:|---:|---:|
| 16 | -1 | +1 | 29 | 9.0 | 4 | 12 |
| 32 | -4 | +4 | 86 | 26.9 | 18 | 26 |
| 64 | -1 | +1 | 341 | 98.4 | 53 | 53 |
| 128 | -2 | +2 | 958 | 263.7 | 136 | 102 |
| 256 | -1 | +1 | 3041 | 928.7 | 745 | 203 |
| 512 | -4 | +4 | 12216 | 3729.6 | 1974 | 423 |
| 1024 | -4 | +4 | 39240 | 12048.4 | 6887 | 832 |
| 2048 | +7 | -7 | 139511 | 40855.8 | 28236 | 1661 |

특히 `s=2048`에서 최종 합은 `-7`인데 absolute mass는 `139511`이다.

따라서

\[
\boxed{
\text{lower-half representation은 cancellation을 제거하지 않고
더 큰 incidence-Möbius cancellation으로 옮긴다.}
}
\]

---

## 6. apparent growth diagnostic

`16<=s<=2048` dyadic samples의 단순 log-log regression에서는

- lower-half l1 exponent `~1.75`,
- lower-half l2 exponent `~1.75`,
- max-entry exponent `~1.79`

가 나온다.

이것은 theorem이 아니며 small finite range diagnostic이다.

흥미롭게도 Lagarias--Richman의 unconditional general bound는 floor-poset Möbius에 대해

\[
|\mu_1(d,n)|\le(n/d)^{\alpha_0},
\qquad
\zeta(\alpha_0)=2,
\quad\alpha_0\approx1.729,
\]

을 준다.

따라서 lower-half terms가 classical `mu`처럼 uniformly bounded되는 구조는 아니다.

---

## 7. differenced floor-poset Möbius와의 구분

Lagarias--Richman은 one-variable

\[
\Delta\mu_1(1,n)=\mu_1(1,n)-\mu_1(1,n-1)
\]

에 대해 special recursion을 증명하고, 이 sequence가 상당한 zero support를 가진다는 결과를 제시한다.

그러나 이것은 현재 Mertens bridge에 나타나는 **fixed-top row**

\[
d\mapsto\mu_1(d,s(s+1))
\]

와 다른 object다.

실제로 현재 lower-half row에서는 `s=2048`에서 `1661/2048` entries가 nonzero였다.

따라서 one-variable differenced sparsity를 fixed-top Mertens row에 자동 이전하지 않는다.

---

## 8. 선행문헌과의 거리

Lagarias--Richman (Advances in Applied Mathematics 153, 2024) 자체가

- floor quotient initial interval의 involution,
- top half와 divisor order의 anti-isomorphism,
- top-half Möbius = classical Möbius,
- floor-poset Möbius upper bounds,
- sign changes,
- differenced Möbius recursion

을 이미 연구한다.

Cardinal--Overholt (Experimental Mathematics 29(3), 2020)는 related divisibility matrices를 통한 Möbius inversion과 Mertens formula를 연구한다.

따라서 floor quotient / incidence Möbius route는 existing research family로 분류한다.

---

## 9. 판정

### 살아남은 사실

1. quotient aggregation matrix has an exact Mertens-block inverse.
2. classical Möbius is exactly embedded in the multiplicative top half of the floor quotient poset.
3. Mertens sum has an exact lower-half incidence-Möbius representation.

### 닫히는 기대

1. `W M=1`이 Mertens growth를 자동 제어한다.
2. floor-poset lower half가 termwise smaller/easier than classical Möbius.
3. differenced one-variable floor-poset sparsity가 fixed-top Mertens bridge를 자동으로 sparse하게 만든다.

모두 현재 exact/numerical audit에서 지지되지 않는다.

### 현재 상태

- quotient inverse formula: `EXACT`.
- Mertens lower-half bridge: `EXACT_COROLLARY`.
- lower-half mass comparison: `NUMERICAL`.
- independent RH improvement: `NOT_ESTABLISHED`.
- floor-quotient route: `EXISTING_RESEARCH / REPRESENTATION_WITH_LARGER_CANCELLATION`.
- RH: `OPEN`.

## 재현자료

```text
scripts/audit_floor_quotient_bridge.py
data/mertens/floor_quotient_lower_half_bridge.csv
data/mertens/quotient_matrix_conditioning.csv
```
