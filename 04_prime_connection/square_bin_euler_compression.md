# Square-Bin Euler Compression and Critical-Resolution Audit

Date: 2026-09-16

## 목적

`O(sqrt(p))` Beurling zero-stability lemma를 이용하여, ordinary prime의 정확한 위치를 어느 정도까지 버려도 `Re(s)>1/2`의 zeta zero/pole divisor가 보존되는지 정리한다.

핵심 결과는 **연속 제곱수 사이의 소수 개수만 보존하는 canonical generalized-prime representative**를 만들 수 있다는 것이다.

이는 RH의 증명이 아니라 `prime data -> zero divisor` 정보보존/압축 정리이다.

---

## 1. square-bin count sequence

`m>=2`에 대해

\[
I_m=[m^2,(m+1)^2),
\qquad
c_m:=\pi((m+1)^2)-\pi(m^2).
\]

제곱수 `>1`은 prime이 아니므로 endpoint convention은 본질적이지 않다.

각 `I_m` 안의 모든 ordinary prime을 generalized prime `q=m^2`로 옮기고 multiplicity를 `c_m`으로 둔다. 작은 prime `2,3`은 그대로 둔다.

따라서 canonical generalized-prime multiset은

\[
\mathcal Q_\square
=\{2,3\}\cup\bigcup_{m\ge2}\{m^2\}^{c_m}.
\]

Beurling generalized primes는 nondecreasing real sequence로 정의되므로 repeated generalized-prime values는 허용된다.

초기 half-plane `Re(s)>1`에서

\[
\boxed{
Z_\square(s)
=
(1-2^{-s})^{-1}(1-3^{-s})^{-1}
\prod_{m\ge2}(1-m^{-2s})^{-c_m}.
}
\]

이 product는 exact prime positions가 아니라 오직 count sequence `(c_m)`만 사용한다.

또 `(c_m)`은 sampled prime-count sequence `A_m=pi(m^2)`와

\[
c_m=A_{m+1}-A_m
\]

으로 동치이다.

---

## 2. exact zero-divisor preservation theorem

ordinary prime `p in I_m`에 대응하는 generalized prime을

\[
q(p)=m^2
\]

로 둔다.

그러면

\[
0<p-q(p)<2m+1=O(\sqrt p),
\]

즉

\[
|q(p)-p|=O(p^{1/2}).
\]

이전 Beurling perturbation theorem을 바로 적용하면

\[
\boxed{
Z_\square(s)=\zeta(s)e^{H_\square(s)}
\qquad (\Re s>1/2),
}
\]

where `H_square` is analytic and `exp(H_square)` is nonvanishing.

따라서

\[
\boxed{
\operatorname{Div}_{\Re s>1/2}(Z_\square)
=
\operatorname{Div}_{\Re s>1/2}(\zeta).
}
\]

즉 두 함수는 이 half-plane에서 동일한 zero/pole divisor를 갖는다.

### direct normal-convergence proof

이 결과는 PNT를 사용하지 않고 bin별로도 직접 증명할 수 있다.

compact set `K subset {Re(s)>1/2}`에서 `sigma_0=min_K Re(s)>1/2`라 하자.

local Euler logarithm

\[
L_s(x)=-\log(1-x^{-s})
\]

은 큰 `x`에서

\[
\left|\frac{d}{d\log x}L_s(x)\right|
\ll_K x^{-\sigma_0}.
\]

`p in I_m`이면

\[
|\log(p/m^2)|\ll 1/m,
\]

따라서 prime 하나의 local factor difference는

\[
|L_s(m^2)-L_s(p)|
\ll_K m^{-1}m^{-2\sigma_0}.
\]

한편 trivial count bound로

\[
c_m\le (m+1)^2-m^2=2m+1.
\]

그러므로 bin 전체 차이는

\[
\ll_K m^{-2\sigma_0}.
\]

`2 sigma_0>1`이므로

\[
\sum_{m\ge2}m^{-2\sigma_0}<\infty.
\]

따라서

\[
H_\square(s)=\log Z_\square(s)-\log\zeta(s)
\]

의 local factor difference series가 `Re(s)>1/2`에서 locally normally convergent한다.

상태: `EXACT`.

---

## 3. RH-equivalent square-count formulation

classical RH는 nontrivial zero가 `Re(s)>1/2`에 없다는 것과 동치이므로

\[
\boxed{
\mathrm{RH}
\iff
Z_\square(s)\neq0
\quad(\Re s>1/2,\ s\neq1).
}
\]

중요:

- 이것은 `c_m`만으로 정의되는 **RH-equivalent Beurling zeta representation**이다.
- 이것은 `c_m`에서 RH bound를 쉽게 증명한다는 뜻이 아니다.
- `Z_square`의 meromorphic continuation을 실제로 제어하는 난점은 여전히 남아 있다.
- Legendre conjecture `c_m>=1`은 필요하지 않다.

따라서 연속 제곱구간마다 prime이 반드시 하나 존재하는지와 이 criterion은 논리적으로 별개다.

---

## 4. general consecutive-power hierarchy

integer `r>=2`에 대해

\[
I_m^{(r)}=[m^r,(m+1)^r),
\qquad
c_m^{(r)}=\pi((m+1)^r)-\pi(m^r).
\]

각 bin의 primes를 generalized prime `m^r`로 옮긴 canonical product를 `Z_r(s)`라 하자.

bin 폭은

\[
(m+1)^r-m^r=O(m^{r-1}),
\]

relative log displacement는 `O(1/m)`이고, bin count도 trivial하게 `O(m^{r-1})`이다.

local-factor difference의 bin 총합은

\[
O(m^{r-2-r\sigma}).
\]

따라서

\[
\sum_m m^{r-2-r\sigma}<\infty
\]

iff

\[
\boxed{
\sigma>1-\frac1r.
}
\]

그러므로

\[
\boxed{
Z_r(s)=\zeta(s)e^{H_r(s)}
\quad\text{for }\Re s>1-1/r,
}
\]

with `e^{H_r}` analytic and nonzero there.

`r=2`가 정확히 critical half-plane `Re(s)>1/2`에 해당한다.

이 hierarchy의 `1/2`는 RH를 사전에 넣은 수치 fitting이 아니라 `sqrt(x)` positional resolution과 analytic convergence가 만나는 지점이다.

---

## 5. general resolution-to-half-plane correspondence

더 일반적으로 scale `x`에서 width

\[
\Delta x=O(x^\theta),\qquad 0<\theta<1,
\]

인 partition을 만들고, 각 bin의 prime count만 보존한다고 하자.

같은 bin 내부에서 rank matching하면 automatically

\[
|q_j-p_j|=O(p_j^\theta).
\]

따라서 Beurling perturbation theorem으로

\[
\boxed{
\text{bin width }O(x^\theta)
\Longrightarrow
\text{zero-divisor preservation on }\Re s>\theta.
}
\]

이를 `RESOLUTION-TO-HALF-PLANE CORRESPONDENCE`로 기록한다.

`theta=1/2`에서는 `sqrt(x)` 폭, 즉 consecutive-square bins가 자연스럽다.

주의: 이는 **충분조건**이다. 더 거친 정보로도 특별한 cancellation 때문에 zero divisor가 보존될 가능성을 배제하는 최소성 theorem은 아니다.

---

## 6. information-compression interpretation

`x_m asymp m^{1/(1-theta)}`형 partition은 `X`까지 약

\[
O(X^{1-\theta})
\]

개의 bin만 필요하다.

따라서 `Re(s)>theta` zero divisor를 보존하는 generalized-prime representative를 만드는 데

\[
O(X^{1-\theta})
\]

개의 coarse prime counts가 sufficient하다.

RH boundary `theta=1/2`에서는

\[
\boxed{O(\sqrt X)}
\]

개의 square-bin counts가 충분하다.

이는 `~X/log X`개의 individual prime locations와 비교되는 강한 compression이지만, **minimal information lower bound는 아니다**.

rough storage upper bound로 각 count에 `O(log X)` bits를 쓰면 square-bin representation은 `O(sqrt(X) log X)` bits면 된다. 이 역시 encoding upper bound일 뿐 최적성 주장이 아니다.

---

## 7. finite real-axis ratio audit

truncated local-factor difference

\[
H_{\square,X}(\sigma)
=
\sum_{p\le X,\ p\ge5}
\left[
-\log(1-q(p)^{-\sigma})
+\log(1-p^{-\sigma})
\right]
\]

를 계산했다.

| X | sigma=.50 | .52 | .55 | .60 | .75 |
|---:|---:|---:|---:|---:|---:|
| 2^12 | 1.029663 | 0.981370 | 0.914229 | 0.814990 | 0.591172 |
| 2^14 | 1.106282 | 1.047815 | 0.967778 | 0.852174 | 0.603242 |
| 2^16 | 1.173496 | 1.104557 | 1.011691 | 0.880664 | 0.610770 |
| 2^18 | 1.232437 | 1.152972 | 1.047648 | 0.902440 | 0.615444 |
| 2^20 | 1.285215 | 1.195150 | 1.077705 | 0.919428 | 0.618406 |
| 2^22 | 1.332945 | 1.232254 | 1.103072 | 0.932807 | 0.620301 |

`Re(s)>1/2`의 convergence와 `sigma=1/2` 경계적 성장에 정성적으로 부합한다.

상태: `NUMERICAL CONSISTENCY CHECK ONLY`.

---

## 8. literature boundary

consecutive squares/powers 사이 prime distribution 자체는 별도의 고전 short-interval 문제다. Bazzanella 등의 연구에서 consecutive squares 사이 항상 prime이 존재한다는 명제는 RH만으로도 알려져 있지 않다.

본 construction은 그 문제를 풀거나 `c_m>0`을 요구하지 않는다. 실제 count `c_m`을 입력 데이터로 사용하여 generalized Euler product를 만든다.

Beurling generalized-prime perturbation/stability 문헌은 존재하지만, 이번 targeted audit에서는 `consecutive-square prime counts -> canonical Euler product with identical Re(s)>1/2 zero divisor`를 이 형태로 명시한 선행정리는 확인하지 못했다.

따라서 현재 분류:

- underlying Beurling framework: `PRIOR ART`;
- perturbation analytic-unit mechanism: `DERIVED / STANDARD-TYPE ARGUMENT`;
- square-bin canonical compression formulation: `DERIVED FORMULATION / NOVELTY NOT CLAIMED`.

---

## 9. methodological consequence

이제 exact individual prime gaps, residue ordering, within-square prime positions는 `Re(s)>1/2` zero divisor의 **필수 정보가 아님**을 Beurling equivalence class 안에서 분리할 수 있다.

향후 RH mechanism 후보가 exact prime microstructure를 필수라고 주장하려면 다음 질문을 통과해야 한다.

1. 그 property는 square-bin rearrangement에서 왜 사라져도 RH-equivalent zero divisor가 유지되는가?
2. property가 사라진다면 그것은 RH의 필수조건이 아니라 classical primes에 특수한 sufficient mechanism에 불과한가?
3. square-bin counts `(c_m)` 또는 동등한 sampled sequence `pi(m^2)` 수준으로 quotient-out한 뒤에도 남는 invariant는 무엇인가?

새 감사 규칙:

`CRITICAL-RESOLUTION GUARD` — RH의 필수 prime-placement 정보라고 주장하는 구조는 최소한 `O(sqrt(p))` Beurling perturbation / square-bin rearrangement에 대한 상태를 명시해야 한다.

---

## 10. next frontier

다음 후보는 exact prime positions가 아니라 **square-bin count sequence** 자체의 구조다.

우선순위:

1. `c_m`의 smooth main term을 제거한 residual이 어떤 Dirichlet/Mellin object를 만드는지 exact하게 유도.
2. 그 residual transform이 다시 `zeta'/zeta`의 sampling/reencoding인지 감사.
3. `pi(m^2)` sampled data만으로 정의되는 arithmetic-side inequality가 `Re(s)>1/2` zero-free condition을 강제할 수 있는지 조사.
4. 이 과정에서 Legendre conjecture나 prime-in-short-interval bound처럼 RH보다 강한 문제를 무의식적으로 요구하지 않는지 지속 감사.