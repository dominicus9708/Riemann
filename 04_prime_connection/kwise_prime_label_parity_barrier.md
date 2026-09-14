# K-wise Prime-Label Parity Invisibility Barrier

Date: 2026-09-15

## 목적

fixed/growing `omega` moment audit는 prime labels를 모두 버린 compression에 대한 장벽이었다.

여기서는 장벽을 더 강하게 하여, 서로 다른 prime labels를 유지한 **모든 K-channel 이하 local statistics**가 global Möbius parity를 일반적으로 결정할 수 있는지 검사한다.

---

## 1. Boolean parity pair

`n=K+1`개의 binary channel을

\[
x=(x_1,\ldots,x_n)\in\{0,1\}^n
\]

이라 하자.

`U_+`를 even parity states 위의 uniform distribution, `U_-`를 odd parity states 위의 uniform distribution으로 둔다.

즉

\[
\chi(x)=(-1)^{x_1+\cdots+x_n}
\]

에 대해

\[
\mathbb E_{U_+}\chi=+1,
\qquad
\mathbb E_{U_-}\chi=-1.
\]

그러나 임의의 proper coordinate set

\[
B\subsetneq[n]
\]

에 대한 marginal은 두 분포에서 모두 uniform하다.

실제로 `x_B`를 하나 고정하면 적어도 하나의 free bit가 남고, 그 free bits의 completions 중 exactly half가 even, half가 odd이다.

따라서

\[
\boxed{
(U_+)_B=(U_-)_B
\quad\text{for every }|B|\le K.
}
\]

즉 모든 K-wise label statistics가 정확히 같지만 global parity character만 반대다.

상태: `EXACT / CLASSICAL_K_WISE_PARITY_STRUCTURE`.

---

## 2. Fourier formulation

Boolean cube character를

\[
\chi_A(x)=(-1)^{\sum_{i\in A}x_i}
\]

라 하자.

`U_+`와 `U_-`의 차이는 Fourier space에서 full-set character `A=[n]`에만 존재한다.

모든

\[
|A|\le K=n-1
\]

Fourier coefficients / moments / intersections / marginals는 동일하다.

따라서 global parity는 **top-order Fourier information**이며 proper-subset statistics로 일반적으로 식별할 수 없다.

이것은 앞선

- singleton exact-label audit,
- fully-visible pair audit,
- derivative-energy low-order transfer,
- GCD-label interaction,
- divisibility tensor

의 공통 information-theoretic 배경이다.

---

## 3. arithmetic full-subcube cancellation

squarefree base `d`와, `d`와 서로소인 finite prime set `A`를 잡는다.

\[
P_A=\prod_{p\in A}p.
\]

만약

\[
\boxed{dP_A\le X}
\]

이면 모든 subset `S subset A`에 대해

\[
dP_S\le X,
\qquad
P_S=\prod_{p\in S}p.
\]

따라서 이 arithmetic block은 complete Boolean cube다.

Möbius signed sum은

\[
\sum_{S\subseteq A}\mu(dP_S)
=
\mu(d)\sum_{S\subseteq A}(-1)^{|S|}
=
\boxed{0}.
\]

더 강하게 `B subsetneq A`의 coordinates에만 의존하는 임의의 함수 `g`에 대해

\[
\boxed{
\sum_{S\subseteq A}
\mu(dP_S)g(S\cap B)=0.
}
\]

증명은 `q in A\\B` 하나를 골라 `S`와 `S triangle {q}`를 pair하면 된다.

즉 complete arithmetic subcube의 Möbius parity는 **모든 proper-subset local observables와 직교**한다.

상태: `EXACT`.

---

## 4. boundary-only theorem

모든 squarefree `n<=X`를 selected prime set `A`에 대해 unique하게

\[
n=md,
\qquad
(d\mid P_A),
\qquad
(m,P_A)=1
\]

로 쓴다.

그러면

\[
M(X)
=
\sum_{\substack{m\le X\\(m,P_A)=1}}
\mu(m)
B_A(X/m),
\]

여기서

\[
B_A(Y)
=
\sum_{\substack{d\mid P_A\\d\le Y}}\mu(d).
\]

`mP_A<=X`이면 full cube가 존재하여

\[
B_A(X/m)=\sum_{d\mid P_A}\mu(d)=0.
\]

따라서 exact하게

\[
\boxed{
M(X)
=
\sum_{\substack{X/P_A<m\le X\\(m,P_A)=1}}
\mu(m)B_A(X/m).
}
\]

즉 선택된 prime block의 interior complete cubes는 전부 사라지고 **weighted-halfspace boundary**만 Mertens parity를 운반한다.

이 formula는 sieve/Buchstab/prime-factor decomposition 계열과 강하게 겹치므로 신규성은 주장하지 않는다.

---

## 5. local Boolean depth

squarefree base `d`에 대해 `d`를 나누지 않는 가장 작은 primes를

\[
q_1(d)<q_2(d)<\cdots
\]

라 하자.

local complete-cube depth를

\[
\boxed{
\mathfrak b_X(d)
=
\max\left\{r:
 d\prod_{j=1}^{r}q_j(d)\le X
\right\}
}
\]

로 정의한다.

그러면 dimension `<=b_X(d)`인 smallest-label activation cube는 complete이고, 그 내부에서는 top parity가 모든 proper marginal과 exact하게 직교한다.

따라서 parity information은 local Boolean depth가 깨지는 **incomplete-cube boundary**에 집중된다.

---

## 6. half-support scale reappears

`d=1`이고 first `r` primes를 쓰면 complete-cube condition은

\[
p_r^\#\le X.
\]

최대 dimension은

\[
m(X)\sim\frac{\log X}{\log\log X}.
\]

residual budget이 `sqrt(X)`이면

\[
p_r^\#\le\sqrt X
\]

의 최대 `r`은 asymptotically

\[
\boxed{
\left(\frac12+o(1)\right)
\frac{\log X}{\log\log X}.
}
\]

따라서 growing-moment audit에서 나온 half-support threshold가 Boolean full-cube depth에서도 동일하게 재출현한다.

여기의 `1/2` 역시 RH critical line이 아니라 multiplicative budget split이다.

---

## 7. finite dyadic depth

first-prime primorial만으로 계산하면 `X=2^24`에서

\[
2\cdot3\cdot5\cdot7\cdot11\cdot13\cdot17\cdot19
=9,699,690<2^{24},
\]

다음 prime `23`까지 곱하면 cutoff를 넘는다.

따라서 global smallest-prime complete cube dimension은 `8`이다.

`sqrt(2^24)=4096` budget에서는

\[
2\cdot3\cdot5\cdot7\cdot11=2310<4096,
\]

반면 `*13=30030>4096`, 따라서 depth는 `5`다.

finite ratio는 아직 asymptotic `1/2`에 가깝지 않지만, same primorial-budget mechanism을 확인한다.

---

## 8. relation to classical k-wise independence

Uniform even-parity and odd-parity distributions on `K+1` bits are the canonical example of two distributions that agree on every `K`-coordinate marginal while differing completely on global parity.

This sits inside the classical theory of k-wise independent distributions and the discrete moment problem. Repository에서는 이를 새로운 probability theorem으로 주장하지 않는다.

외부 문맥:

- Itai Benjamini, Ori Gurel-Gurevich, Ron Peled (2012), *On K-wise Independent Distributions and Boolean Functions*, arXiv:1201.3261.
- related discrete moment / k-wise independence literature.

---

## 9. consequence for previous label audits

이 결과는 `singleton -> pair -> fixed K-label`을 단순히 더 올리는 연구전략에 일반 guard를 준다.

`K`-wise label statistics가 아무리 정밀해도, global parity character는 일반적으로 `K+1`차 정보에 독립적으로 남을 수 있다.

따라서 앞으로 어떤 low-order prime-label statistic이 anomalous하게 보이더라도 다음을 먼저 검사한다.

1. 그것이 proper-subset marginal / Fourier coefficient인가?
2. complete subcube 내부에서 parity와 exact orthogonal인가?
3. observed signal이 weighted-halfspace boundary incompleteness만 재측정하는가?

그렇다면 독립 RH mechanism으로 승격하지 않는다.

---

## 10. remaining arithmetic escape hatch

이 barrier는 arbitrary distributions / complete local cubes에 대한 것이다.

실제 arithmetic support는 arbitrary distribution이 아니라

\[
\sum_p x_p\log p\le\log X
\]

라는 매우 특수한 weighted halfspace다.

따라서 살아 있는 가능성은 **low-order marginals 자체가 아니라 이 halfspace boundary의 deterministic geometry**가 top parity를 강제하는 경우다.

하지만 raw boundary flux와 low-order exact-label interaction은 이전 gap-null audit에서 이미 분리되지 않았다.

따라서 다음 genuine frontier는

\[
\boxed{
\text{high-order weighted-halfspace boundary geometry}
}
\]

이며, 단순 K-wise local statistics와 구분해야 한다.

## 상태

- even/odd parity K-wise indistinguishability: `EXACT / CLASSICAL`.
- arithmetic complete-subcube cancellation: `EXACT`.
- boundary-only representation: `EXACT`.
- half-support depth: `STANDARD_PRIMORIAL_ASYMPTOTIC`.
- all possible arithmetic proofs blocked: `NOT_CLAIMED`.
- low-order label-statistic strategy: `CLOSED_AS_GENERAL_INFORMATION_CLASS`.
- RH: `OPEN`.
