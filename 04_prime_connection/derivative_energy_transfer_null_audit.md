# Derivative-Energy Transfer Null Audit

## 목적

`weighted_halfspace_parity_audit.md`에서 발견한

\[
R_0,R_1,R_2<1,\qquad R_3,R_4,R_5>1
\]

형태와 derivative-energy generating function의 crossover가 실제 prime weights의 고유 상관인지, 아니면 일반 weighted-threshold geometry인지 분리한다.

---

## 1. generating function

\[
\mathcal G_X(t)=\sum_{k\ge0}t^k\mathcal E_k^\mu(X),
\]

\[
\overline{\mathcal G}_X(t)=\sum_{k\ge0}t^k\overline{\mathcal E}_k(X)
=\sum_{n\le X}\mu(n)^2(1+t)^{\omega(n)}.
\]

multilinearity와 Rademacher orthogonality로

\[
\boxed{
\mathcal G_X(t)=
\mathbb E_\xi\left|P_X(-\mathbf 1+\sqrt t\,\xi)\right|^2
}
\]

이다.

또 squarefree states `m,n`의 prime-support intersection을 이용하면

\[
\boxed{
\mathcal G_X(t)=
\sum_{\substack{m,n\le X\\\mu^2(m)=\mu^2(n)=1}}
\mu(m)\mu(n)(1+t)^{\omega(\gcd(m,n))}.
}
\]

random-character baseline은 정확히 diagonal contribution이다.

\[
\boxed{
\mathcal G_X(t)-\overline{\mathcal G}_X(t)
=
\sum_{\substack{m\ne n\le X\\\mu^2(m)=\mu^2(n)=1}}
\mu(m)\mu(n)(1+t)^{\omega(\gcd(m,n))}.
}
\]

따라서 crossover는 서로 다른 squarefree composite states 사이의 signed-overlap correlation이 zero를 통과하는 지점이다.

---

## 2. 실제 prime cutoff의 first positive crossover

`Delta G_X(t)=G_X(t)-Gbar_X(t)`의 첫 양의 실근을 `t_*(X)`로 둔다.

완전한 derivative order를 사용해 얻은 값:

| X | t_* |
|---:|---:|
| 2^14 | 1.37480553 |
| 2^15 | 1.40384359 |
| 2^16 | 1.40506948 |
| 2^17 | 1.40255869 |
| 2^18 | 1.40556837 |
| 2^19 | 1.41200562 |
| 2^20 | 1.41223089 |
| 2^21 | 1.42341854 |
| 2^22 | 1.44698504 |

초기에는 `~1.40` 부근에 매우 안정적으로 보였지만 `2^21,2^22`에서 위쪽 drift가 확인됐다.

### 중요 가지치기

ordered-formation word critical exponent

\[
\eta_W\approx1.3994333287
\]

와의 수치적 근접은 유지되지 않는다. 변수의 의미도 다르므로 동일 상수 또는 직접 연결로 취급하지 않는다.

---

## 3. random prime-sign corner control

실제 prime support를 그대로 두고 각 prime character sign을 independent Rademacher `+/-1`로 바꾸었다.

`X=2^18`, 80 fixed seeds:

- positive crossover가 존재한 sample: `38/80`.
- 존재한 first root의 median: 약 `1.107`.
- range: 약 `0.039`부터 `104.78`까지 매우 넓음.
- 실제 Möbius에서 관측한 `R0,R1,R2<1` and `R3>1` 패턴을 동시에 만족: `2/80`.

판정:

all-minus Möbius corner의 low-order suppression / mid-order enhancement는 arbitrary random character corner의 보편현상은 아니다.

그러나 이것만으로 prime-specific이라고 할 수 없다. all-minus corner는 coordinate-permutation symmetric한 특별한 threshold corner다.

---

## 4. gap-permuted pseudo-prime weighted-threshold control

더 강한 null model을 구성했다.

- actual prime generator counts를 유지한다.
- `p<=100`은 고정한다.
- 그 위에서 dyadic block별 actual prime-gap multiset을 유지한다.
- 각 block 안의 gap order만 shuffle한다.
- resulting positive generators의 subset product threshold `<=X`를 사용한다.
- 각 allowed subset에 all-minus parity sign `(-1)^|S|`를 그대로 적용한다.

즉 이 null은

- binary channel structure,
- all-minus symmetric character,
- 대략적인 prime density,
- dyadic local gap distribution,
- weighted-threshold geometry

를 유지하지만 실제 gap order/장거리 prime placement를 제거한다.

### 결과

| X | actual t_* | null mean +- sd | null range | samples |
|---:|---:|---:|---:|---:|
| 2^16 | 1.405069 | 1.369177 +- 0.031451 | 1.291727 -- 1.434595 | 50 |
| 2^17 | 1.402559 | 1.369481 +- 0.032623 | 1.315291 -- 1.422415 | 30 |
| 2^18 | 1.405568 | 1.365820 +- 0.038185 | 1.283051 -- 1.417128 | 20 |

실제값은 null 평균보다 약간 높은 쪽이지만 모두 null support 안에 있다.

더 중요하게 null model에서도 일반적으로

\[
R_0,R_1,R_2<1,\qquad R_3,R_4>1
\]

형태가 재현되었다.

예를 들어 `X=2^16`, 50 null samples 평균은 대략

\[
(R_0,R_1,R_2,R_3,R_4)
\approx
(0.0270,0.1603,0.8387,2.6026,2.2745).
\]

actual은

\[
(0.0049,0.1363,0.8208,2.5475,2.3154).
\]

형태 자체가 매우 가깝다.

---

## 5. 판정

\[
\boxed{
\text{low-order suppression -> mid-order enhancement -> }t\sim1.4\text{ crossover}
}
\]

는 **actual primes의 RH-specific signal로 채택하지 않는다.**

현재 자료에서는 weighted monotone-threshold geometry와 prime-like gap distribution만으로 대부분 재현된다.

따라서 이 현상을 이용해 RH를 직접 주장하는 가지를 닫는다.

---

## 6. 남은 residual target

pair-interaction identity 자체는 여전히 정확하며 유용하다.

이제 분석 대상은 raw `G_X`가 아니라

\[
\boxed{
\mathcal R_X(t)
=
\Delta\mathcal G_X^{\rm prime}(t)
-
\mathbb E_{\rm gap-null}\Delta\mathcal G_X^{\rm null}(t)
}
\]

같은 **prime-placement residual interaction**이다.

하지만 null subtraction을 증명에 직접 사용하는 것은 부적절하다. 이는 탐색/진단용이다.

증명 후보가 되려면 residual에서 발견한 패턴을 다시 deterministic arithmetic statement로 번역해야 한다.

다음 탐색에서는 raw halfspace geometry를 이미 알려진 baseline으로 분리한 뒤

1. 실제 prime gap order가 만드는 residual의 cutoff stability,
2. 어떤 gcd-overlap sectors가 residual을 담당하는지,
3. 그 sector가 PNT/known zero information 없이 deterministic하게 bounded되는지

만 검사한다.

---

## 재현자료

```text
data/formation/mobius_corner_derivative_energy_2pow14_22.csv
data/formation/derivative_energy_gap_null_summary.csv
scripts/audit_mobius_corner_derivative_energy.py
scripts/audit_derivative_energy_gap_null.py
```
