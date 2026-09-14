# Tensor Divisibility Variance Barrier

## 목적

`richter_linear_variance_barrier.md`는 centered one-prime probes

\[
Y_p(n)=p\,1_{p\mid n}-1
\]

의 임의 normalized linear combination이 `log log N` variance floor를 피하지 못함을 보였다.

`connected_boundary_flux_audit.md`에서는 higher-order label inclusion-exclusion도 lower-scale restricted Möbius kernels로 환원됨을 확인했다.

이번 단계에서는 **모든 prime-divisibility tensor order를 허용하면 variance barrier가 사라지는가**를 정확히 감사한다.

---

## 1. exact CRT probability model

유한 prime set `P`를 잡고

\[
Q=\prod_{p\in\mathcal P}p
\]

라 하자.

`n`을 modulo `Q`에서 균등하게 뽑으면 Chinese remainder theorem에 의해 사건 `p|n`은 서로 독립이고

\[
\Pr(p\mid n)=1/p.
\]

따라서

\[
Y_p(n)=p1_{p\mid n}-1
\]

에 대해 정확히

\[
\mathbb E Y_p=0,
\qquad
\mathbb E Y_p^2=p-1.
\]

서로 다른 primes에 대한 `Y_p`들은 독립이다.

이 단계는 heuristic가 아니라 finite residue space에서 `EXACT`이다.

---

## 2. tensor orthogonality

nonempty `A subset P`에 대해

\[
Y_A(n)=\prod_{p\in A}Y_p(n)
\]

를 정의한다.

그러면

\[
\mathbb E Y_A=0,
\qquad
\operatorname{Var}(Y_A)=\prod_{p\in A}(p-1).
\]

또 `A != B`이면 symmetric difference에 속하는 prime이 적어도 하나 존재하고 그 factor의 평균이 zero이므로

\[
\boxed{\mathbb E(Y_A Y_B)=0\quad(A\ne B).}
\]

즉 모든 nonempty prime tensors는 exact orthogonal family다.

---

## 3. fixed-order k barrier

`|A|=k`인 tensor만 사용해

\[
Z_k(n)=\sum_{|A|=k}\beta_A Y_A(n),
\qquad
\sum_{|A|=k}\beta_A=1
\]

로 둔다.

orthogonality 때문에

\[
\operatorname{Var}(Z_k)
=
\sum_{|A|=k}\beta_A^2\prod_{p\in A}(p-1).
\]

Cauchy--Schwarz로

\[
\boxed{
\operatorname{Var}(Z_k)
\ge
\left(
\sum_{|A|=k}\prod_{p\in A}\frac1{p-1}
\right)^{-1}.
}
\]

우변 분모를

\[
E_k=e_k\left((p-1)^{-1}:p\in\mathcal P\right)
\]

라 쓰면 equality는

\[
\beta_A\propto\prod_{p\in A}\frac1{p-1}
\]

에서 달성된다.

또

\[
E_k\le\frac1{k!}
\left(\sum_{p\in\mathcal P}\frac1{p-1}\right)^k
\]

이므로

\[
\boxed{
\operatorname{sd}(Z_k)
\ge
\frac{\sqrt{k!}}
{\left(\sum_p1/(p-1)\right)^{k/2}}.
}
\]

`p<=z`를 쓰면

\[
\sum_{p\le z}\frac1{p-1}=\log\log z+O(1).
\]

따라서 모든 **fixed k**는 오직 poly-`log log` scale의 variance improvement만 제공한다.

RH normalized scale `N^{-1/2+epsilon}`와는 polynomially 멀다.

---

## 4. all-order exact optimum

이제 모든 nonempty subsets를 동시에 허용해

\[
Z(n)=\sum_{\emptyset\ne A\subseteq\mathcal P}\beta_A Y_A(n),
\qquad
\sum_A\beta_A=1
\]

로 둔다.

동일한 inverse-variance optimization으로

\[
\operatorname{Var}(Z)
\ge
\left(
\sum_{\emptyset\ne A\subseteq\mathcal P}
\prod_{p\in A}\frac1{p-1}
\right)^{-1}.
\]

그런데 subset sum은 정확히 factorize되어

\[
\begin{aligned}
D
&=
\sum_{A\ne\emptyset}\prod_{p\in A}\frac1{p-1}\\
&=
\prod_{p\in\mathcal P}\left(1+\frac1{p-1}\right)-1\\
&=
\prod_{p\in\mathcal P}\frac p{p-1}-1.
\end{aligned}
\]

sieve density

\[
V(\mathcal P)=\prod_{p\in\mathcal P}\left(1-\frac1p\right)
\]

를 쓰면

\[
D=V^{-1}-1
\]

이므로

\[
\boxed{
\min \operatorname{Var}(Z)
=
\frac{V}{1-V}.
}
\]

즉 **exponentially many tensor orders를 모두 허용해도 최적 L2 variance는 정확히 classical sieve density와 같은 scale로 닫힌다.**

`P={p:p<=z}`일 때 Mertens product theorem으로

\[
V(z)\sim\frac{e^{-\gamma}}{\log z},
\]

따라서

\[
\boxed{
\min \operatorname{sd}(Z)
\sim
\frac{e^{-\gamma/2}}{\sqrt{\log z}}.
}
\]

이것은 `N^{-1/2+epsilon}`와 전혀 다른 scale다.

---

## 5. finite-N period constraint

위 orthogonality는 modulo

\[
Q(z)=\prod_{p\le z}p
\]

의 complete residue space에서 exact하다.

이를 finite interval `n<=N`에 boundary error 없이 직접 이식하려면 최소한 한 full period가 들어가는

\[
Q(z)\le N
\]

범위를 생각할 수 있다.

Chebyshev theta relation

\[
\log Q(z)=\vartheta(z)\sim z
\]

때문에 이는 대략

\[
z\lesssim\log N
\]

을 뜻한다.

그러면 all-order optimum조차

\[
\boxed{
\operatorname{sd}(Z)
\gtrsim
(\log\log N)^{-1/2}
}
\]

scale로 돌아온다.

이는 earlier Richter linear barrier와 같은 double-log floor를 **모든 tensor orders를 허용한 이상화된 CRT model에서도 다시 회수**한다.

주의: `Q(z)>N`인 영역에서 이 식을 finite interval에 그대로 적용하는 것은 허용하지 않는다. 그 경우에는 별도의 discrepancy / level-of-distribution 입력이 필요하다.

---

## 6. numerical scale check

`P={p:p<=z}`에 대해 exact all-order minimum을 계산하면:

| z | pi(z) | product p/(p-1) | min variance | min sd |
|---:|---:|---:|---:|---:|
| 100 | 25 | 8.31136 | 0.13677 | 0.36983 |
| 1,000 | 168 | 12.35098 | 0.08810 | 0.29681 |
| 10,000 | 1,229 | 16.42449 | 0.06483 | 0.25462 |
| 100,000 | 9,592 | 20.51159 | 0.05125 | 0.22639 |
| 1,000,000 | 78,498 | 24.60738 | 0.04236 | 0.20581 |

감소는 logarithmic이며 RH square-root scale과 비교할 수 없을 정도로 느리다.

---

## 7. sieve / Kubilius overlap

이 결과의 구조는 고전 sieve density와 정확히 접한다.

- `V(z)=prod_{p<=z}(1-1/p)`는 integers가 작은 prime divisors를 피하는 classical sifting density다.
- prime-divisibility indicators를 independent Bernoulli variables로 보는 관점은 classical probabilistic number theory / Kubilius model과 같은 기준선이다.
- O. Gorodetsky (2026), *A Kubilius model for sieve-theoretic sequences*, Analysis Mathematica, DOI `10.1007/s10476-026-00178-w`, 는 sieve-theoretic sequences에 대한 현대 Kubilius-model total-variation approximation을 연구한다.

현재 exact tensor calculation이 Gorodetsky의 theorem을 사용하는 것은 아니다. 다만 **independent prime-divisibility model 자체가 표준적인 선행 확률모형**임을 확인하는 문헌 기준으로 사용한다.

---

## 8. 판정

### 닫는 경로

1. fixed-order nonlinear prime-divisibility tensors만으로 Richter variance floor를 polynomial scale로 개선한다.
2. tensor order를 무한정 추가하면 L2 variance가 RH scale까지 자동으로 내려간다.
3. connected divisibility masks의 combinatorial richness 자체가 Möbius parity cancellation을 강제한다.

위 세 경로는 현재 normalized linear-combination / L2 class에서 닫힌다.

### 남는 경로

이 barrier를 벗어나려면 적어도 하나가 필요하다.

- divisibility tensor의 **linear combination**이 아닌 genuinely nonlinear phase coupling,
- complete-residue independent model을 깨는 deterministic cross-scale relation,
- additive ordering / prime placement information,
- or a norm/functional that is sensitive to Möbius all-minus phase while not collapsing to sieve density.

즉 다음 candidate는 **phase-sensitive cross-scale operator**여야 한다.

---

## 상태

- CRT independence: `EXACT`.
- tensor orthogonality: `EXACT`.
- fixed-order inverse-variance bound: `EXACT`.
- all-order optimum `V/(1-V)`: `EXACT`.
- finite-N `log log N` translation under full-period condition: `CONDITIONAL_ON_PERIOD_EMBEDDING`.
- general nonlinear methods impossibility: `NOT_CLAIMED`.
- RH: `OPEN`.
