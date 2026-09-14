# Growing-Order Moment Identifiability Barrier

Date: 2026-09-15

## 목적

fixed-order `omega` moment branch가 닫힌 뒤 남은 질문은

\[
K=K(x)\to\infty
\]

인 growing-order moment hierarchy가 Möbius parity

\[
M(x)=\sum_r(-1)^rA_r(x)
\]

를 RH scale까지 결정할 수 있는가이다.

여기서는 계산법의 성능이 아니라 **정보 식별 가능성**부터 감사한다.

---

## 1. exact moment-matched opposite-parity pair

임의의 integer `K>=0`와 shift `r_0`를 고정한다.

`j=0,...,K+1`에 대해

\[
\nu_j=(-1)^j{K+1\choose j}
\]

를 둔다.

모든 degree `<=K` polynomial `P`에 대해 `(K+1)`차 finite difference 때문에

\[
\boxed{
\sum_{j=0}^{K+1}
u_jP(r_0+j)=0.
}
\]

반면 parity pairing은

\[
\boxed{
\sum_{j=0}^{K+1}
(-1)^{r_0+j}\nu_j
=(-1)^{r_0}2^{K+1}.
}
\]

즉 degree-`K` moment information의 exact null direction이 parity에는 maximal하게 보인다.

상태: `EXACT`.

---

## 2. probability version: identical K moments, opposite parity

두 확률분포를

\[
p_\pm(r_0+j)
=
\frac{{K+1\choose j}}{2^{K+1}}
\left(1\pm(-1)^j\right)
\]

로 정의한다.

각각 normalize되어 있고 nonnegative이며,

- `p_+`는 `j` even에만,
- `p_-`는 `j` odd에만

지지된다.

모든 degree `<=K` polynomial `P`에 대해

\[
\boxed{
\mathbb E_{p_+}P(r)=\mathbb E_{p_-}P(r)
}
\]

이지만

\[
\boxed{
\mathbb E_{p_+}(-1)^r=(-1)^{r_0},
\qquad
\mathbb E_{p_-}(-1)^r=-(-1)^{r_0}.
}
\]

따라서 first `K` moments는 parity expectation을 전혀 결정하지 못할 수 있다.

이 construction은 Boolean cube에서 even/odd parity conditioned distributions가 all proper low-dimensional marginals에서 indistinguishable한 classical `k`-wise independence phenomenon의 Hamming-weight projection이다.

상태: `EXACT / CLASSICAL_PARITY_INDISTINGUISHABILITY_STRUCTURE`.

---

## 3. actual layer-vector perturbation

실제 squarefree layer count

\[
A_r(x)=\#\{n\le x:\mu^2(n)=1,\omega(n)=r\}
\]

를 생각한다.

연속된 layers `r_0,...,r_0+K+1` 모두 positive라 하자.

위 `nu_j`를 해당 layers에 삽입하고

\[
A_r^\pm=A_r\pm t\nu_r
\]

로 둔다.

`|nu_j|<=2^{K+1}`이므로

\[
t\le
\frac{A_{\min}}{2^{K+1}},
\qquad
A_{\min}=\min_{0\le j\le K+1}A_{r_0+j},
\]

이면 양쪽 perturbation이 모두 nonnegative다.

그리고 first `K` ordinary moments뿐 아니라 모든 factorial/binomial moments

\[
B_j=\sum_rA_r{r\choose j},\qquad j\le K,
\]

도 정확히 보존된다.

parity difference는

\[
\boxed{
M_+(x)-M_-(x)
=\pm 2^{K+2}t
}
\]

이다.

즉 충분한 layer mass가 있으면 first `K` moments를 **정확히 동일하게 유지하면서** 큰 parity ambiguity를 만들 수 있다.

주의: `A^+`,`A^-`는 information-theoretic layer-count alternatives다. 둘 다 실제 정수집합에서 realizable하다고 주장하지 않는다. 따라서 이 결과는 arithmetic theorem이 아니라 moment-only information class에 대한 barrier다.

---

## 4. elementary lower bound for layer masses

`r>=1`이고

\[
D_{r-1}=p_1p_2\cdots p_{r-1}
\]

라 하자 (`D_0=1`).

prime `q`가

\[
p_{r-1}<q\le x/D_{r-1}
\]

이면

\[
n=D_{r-1}q
\]

는 squarefree이고 `omega(n)=r`이다.

따라서 정확히

\[
\boxed{
A_r(x)
\ge
\pi(x/D_{r-1})-\pi(p_{r-1}).
}
\]

이 lower bound는 전체 Sathe--Selberg machinery 없이도 layer가 얼마나 큰지 충분히 보여준다.

---

## 5. half-support RH-scale ambiguity theorem

PNT consequence로

\[
\log D_r\sim r\log r.
\]

고정 `eta>0`에 대해

\[
R(x)=
\left(\frac12-\eta\right)
\frac{\log x}{\log\log x}
\]

라 하자.

그러면 uniformly `1<=r<=R(x)`에서

\[
D_{r-1}\le x^{1/2-\eta+o(1)}
\]

이고 따라서

\[
\boxed{
A_r(x)
\ge x^{1/2+\eta-o(1)}.
}
\]

이제

\[
K+2\le R(x)
\]

라고 하고 consecutive window `r=1,...,K+2`에 moment-null perturbation을 적용한다.

또

\[
2^K=x^{o(1)}
\]

이므로 충분히 큰 `x`에서 integer `t>=1`을 선택하면서

\[
|M_+-M_-|
\ge x^{1/2+\eta-o(1)}
\]

이 되게 할 수 있다.

따라서

\[
\boxed{
K\le
\left(\frac12-\eta\right)
\frac{\log x}{\log\log x}
}
\]

범위의 **moment-only information**은 nonnegative integer layer-count relaxation 안에서도 parity를 RH scale까지 식별하지 못한다.

이는 이전의 `Omega(log log x)` central-window guard보다 훨씬 강하다.

상태: finite-difference construction `EXACT`; asymptotic layer lower bound `STANDARD_PNT_CONSEQUENCE`; interpretation `RELAXED_INFORMATION_BARRIER`.

---

## 6. meaning of the new 1/2

maximum squarefree support order는

\[
m(x)\sim\frac{\log x}{\log\log x}.
\]

따라서 위 threshold는 대략

\[
K\lesssim\frac12m(x).
\]

이다.

여기의 `1/2`는 RH critical line에서 유도된 것이 아니다.

그 의미는

\[
D_r\approx x^{1/2}
\]

가 되는 **primorial budget split**이다. first `r-1` prime product가 square-root budget에 도달하기 전까지 한 개의 free prime을 붙여서 각 layer에 `>sqrt(x)`개의 states를 만들 수 있기 때문에 생긴다.

따라서 또 하나의 `GENERIC_MULTIPLICATIVE_HALF`로 분류한다.

---

## 7. finite linear-program audit on actual layers

실제 `A_r(x)`와 support `0<=r<=m(x)`를 고정하고, first `K` factorial moments

\[
B_j(x)=\sum_rA_r(x){r\choose j},\qquad j=0,...,K
\]

만 constraint로 준다.

그 뒤 nonnegative real layer vectors 중 parity

\[
\sum_r(-1)^rA_r
\]

의 최소/최대를 linear programming으로 계산했다.

대표 결과:

| x | max omega | actual M | sqrt(x) | first K forcing every feasible parity within sqrt(x) |
|---:|---:|---:|---:|---:|
| 2^16 | 6 | 14 | 256 | 6 |
| 2^18 | 6 | 24 | 512 | 6 |
| 2^20 | 7 | 257 | 1024 | 7 |
| 2^22 | 7 | 228 | 2048 | 7 |
| 2^24 | 8 | 211 | 4096 | 8 |

특히 `x=2^24`, `K=7`에서는 실제 first seven moments를 **모두 정확히 고정해도** feasible parity interval이

\[
\boxed{[-45,80211]}
\]

이다.

actual `M=211`이며 interval width는 `80256`, `sqrt(x)=4096`보다 훨씬 크다.

반면 universal Newton truncation은 우연히 `K=7`에서 square-root target에 들어왔었다. 따라서 그 finite success는 first seven moments가 parity를 정보론적으로 결정했기 때문이 아니다.

상태: `NUMERICAL_LINEAR_PROGRAM_RELAXATION`.

---

## 8. exact K=m-1 null direction

support가 `0,...,m`이고 moments를 degree `m-1`까지 고정하면 feasible affine nullspace는 1-dimensional이다.

그 방향은

\[
\nu_r=(-1)^r{m\choose r}.
\]

따라서 `K=m-1`에서도 parity ambiguity는 exact하게

\[
2^m t
\]

scale로 움직인다.

`x=2^24`, `m=8`에서는 이 exact one-dimensional freedom이 위 `[-45,80211]` interval을 만든다.

즉 **support order보다 moment order 하나가 부족한 것만으로도** current finite data에서 square-root보다 큰 ambiguity가 남는다.

---

## 9. relation to k-wise independence / moment problem

위 `p_+`,`p_-` construction은 Boolean parity의 classical low-order indistinguishability와 같다.

- uniform even-parity strings,
- uniform odd-parity strings

on `K+1` bits는 모든 proper low-dimensional marginals에서는 같지만 global parity는 반대다.

Hamming-weight projection이 정확히 위 binomial moment pair를 준다.

따라서 이 장벽은 새로운 pseudorandomness theorem이 아니다. repository에서는 arithmetic layer compression이 어떤 정보를 버리는지 밝히는 DSD information audit로 사용한다.

---

## 10. branch closure

다음을 닫는다.

1. `K=o(log x/log log x)`인 first moments만으로 parity endpoint를 information-theoretically 거의 결정할 수 있다는 기대.
2. first `K` moments + nonnegativity + known support만으로 RH-scale Mertens cancellation을 강제한다는 기대, 적어도 `K<(1/2-o(1)) max_omega` 범위.
3. finite `K=7` 같은 universal truncation success를 moment sufficiency evidence로 해석하는 것.

---

## 11. genuine remaining frontier

moment-only hierarchy가 아니라 추가 arithmetic information이 필요하다.

가능한 정보는

- prime labels,
- ordered largest/smallest-prime statistics,
- cross-layer label coupling,
- weighted-halfspace boundary geometry,
- 또는 `K`가 at least half-support scale 이상으로 증가하는 genuinely nonuniform identities

이다.

그러나 low-order label intersections와 raw boundary flux는 앞선 null audits에서 이미 닫혔다.

따라서 다음 질문은

\[
\boxed{
\text{half-support scale 이상의 growing order를 쓰지 않고도
prime-label/order information이 parity ambiguity를 제거할 수 있는가?}
}
\]

이다.

## 상태

- finite-difference moment-null vector: `EXACT`.
- opposite-parity equal-K-moment distributions: `EXACT`.
- actual-layer integer perturbation mechanism: `EXACT_WHEN_NONNEGATIVITY_MARGIN_EXISTS`.
- layer lower bound from primorial × free prime: `EXACT + PNT_ASYMPTOTIC`.
- half-support RH-scale moment ambiguity: `RELAXED_INFORMATION_BARRIER`.
- finite LP audit: `NUMERICAL`.
- claim about all arithmetic proofs: `NOT_MADE`.
- RH: `OPEN`.

## 선행문헌 문맥

- Ramamohan Paturi (1992), polynomial approximate degree of symmetric Boolean functions.
- Itai Benjamini, Ori Gurel-Gurevich & Ron Peled (2012), *On K-wise Independent Distributions and Boolean Functions*, for k-wise independence / classical moment-problem context.
- Sathe--Selberg / Erdos--Kac theory for arithmetic layer sizes; the strongest half-support lower bound above only needs the elementary primorial-times-free-prime construction plus PNT asymptotics.
