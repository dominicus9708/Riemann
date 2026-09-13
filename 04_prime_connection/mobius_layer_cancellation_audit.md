# Möbius Formation-Layer Cancellation Audit

## 목적

Möbius 합

\[
M(x)=\sum_{n\le x}\mu(n)
\]

을 하나의 불규칙 부호합으로 보지 않고, 서로 다른 소수채널을 정확히 `k`개 사용하는 squarefree 형성층으로 완전히 분해한다.

\[
A_k(x)=\#\{n\le x:\mu(n)^2=1,\ \omega(n)=k\}.
\]

그러면 정확히

\[
\boxed{M(x)=\sum_{k\ge0}(-1)^kA_k(x)}.
\]

이번 단계의 질문은 `1/2`를 찾는 것이 아니라 다음이다.

> 실제 Möbius 상쇄에 random-sign 모델에는 없는 결정론적 층간 제약이 존재하는가?

---

## 1. 계산 범위

NumPy sieve로

\[
1\le n\le 2^{24}=16,777,216
\]

을 전수 계산했다.

각 dyadic cutoff `2^10,...,2^24`에서

- `A_k(x)`,
- 짝수/홀수 형성층 총량,
- `M(x)`,
- 인접 parity-pair 차이,
- layer polynomial,
- 두 개의 단순 독립성 null model

을 계산했다.

---

## 2. 2^24에서의 완전 층분해

\[
x=16,777,216
\]

에서

\[
(A_0,\ldots,A_8)
=
(1,
1,077,871,
3,128,647,
3,499,035,
1,907,198,
520,139,
63,904,
2,500,
6).
\]

짝수/홀수 층 총량은

\[
E(x)=5,099,756,
\qquad
O(x)=5,099,545,
\]

이므로

\[
\boxed{M(x)=E(x)-O(x)=211}.
\]

총 squarefree 수는

\[
Q(x)=10,199,301
\]

이므로 상대 parity imbalance는 약

\[
2.07\times10^{-5}
\]

이다.

---

## 3. 상쇄는 단순 인접층 균형이 아니다

인접 parity pair를

\[
D_j(x)=A_{2j}(x)-A_{2j+1}(x)
\]

라고 두면 `2^24`에서

\[
(D_0,D_1,D_2,D_3,D_4)
=
(-1,077,870,
-370,388,
1,387,059,
61,404,
6).
\]

각 항은 매우 크지만

\[
\sum_jD_j=211
\]

만 남는다.

따라서 현재 범위에서 Möbius 상쇄는

\[
A_{2j}\approx A_{2j+1}
\]

이라는 한 쌍의 국소균형만으로 설명되지 않는다.

실제 alternating partial sums는

\[
1,
-1,077,870,
2,050,777,
-1,448,258,
458,940,
-61,199,
2,705,
205,
211
\]

로 진행된다.

즉 형성차수가 증가할수록 앞선 거대한 잔차를 다음 층들이 반복적으로 보상한다.

이 현상을 여기서는 **layer compensation cascade**라는 진단명으로 기록한다. 새 정수론 용어/정리를 주장하는 명칭은 아니다.

---

## 4. dyadic 이동

후반 세 cutoff의 pair balance는 다음과 같다.

| x | D0 | D1 | D2 | D3 | M(x) |
|---:|---:|---:|---:|---:|---:|
| 4,194,304 | -295,946 | -47,380 | +333,804 | +9,750 | 228 |
| 8,388,608 | -564,162 | -142,649 | +681,966 | +24,835 | -10 |
| 16,777,216 | -1,077,870 | -370,388 | +1,387,059 | +61,404 | 211 |

보상 중심이 `x` 증가와 함께 높은 `k` 쪽으로 이동한다.

이는 `omega(n)`의 전형적 크기가 천천히 증가한다는 고전적 분포이론과 정성적으로 양립하므로, 그 자체를 새로운 현상으로 해석하지 않는다.

---

## 5. 단순 독립성 null model 감사

### 5.1 fitted Poisson layer null

실제 squarefree 집합에서 평균 형성차수

\[
\bar k=2.790654869\ldots
\]

를 그대로 맞춘 Poisson 층모형은 parity imbalance 규모를

\[
Qe^{-2\bar k}\approx38,427
\]

로 예측한다.

실제값은

\[
|M(x)|=211.
\]

### 5.2 independent-channel squarefree null

각 소수 `p`의 squarefree 조건부 활성확률을 독립적으로

\[
\Pr(p\mid n\mid p^2\nmid n)\approx\frac1{p+1}
\]

라고 놓는 단순 channel-independent model에서는 parity expectation factor가

\[
\prod_{p\le x}\left(1-\frac{2}{p+1}\right)
=
\prod_{p\le x}\frac{p-1}{p+1}
\]

가 된다.

`x=2^24`에서 이 null은 약

\[
19,111
\]

을 준다.

두 null 모두 실제 `211`보다 훨씬 크다.

### 감사 해석

이는 **독립적인 채널 수 분포만으로 실제 상쇄를 설명하기 어렵다**는 진단이다.

그러나 이 null들은 정확한 Sathe-Selberg 근사나 RH 독립적 최적모형이 아니다. 따라서 차이 자체는 새로운 정리의 증거가 아니다.

또 이전 random-sign squarefree 대조군에서 `sqrt(Q)` 규모 상쇄가 쉽게 나타났으므로, 작은 `M(x)` 하나만으로 Möbius 고유 구조를 입증하지 않는다.

---

## 6. 정확한 형성층 재귀

여기서 실제 소수채널 구조에서 오는 정확한 결정론적 제약을 얻을 수 있다.

squarefree `n`이 정확히 `k+1`개 소수채널을 사용한다고 하자. 그중 하나의 소수 `p`를 표시하여 제거하면 `k`개 채널을 가진 squarefree 수가 남아야 하며, `p`는 나머지에 다시 나타나면 안 된다.

이 exclusion을 반복해서 풀면 모든 `k>=0`에 대해

\[
\boxed{
(k+1)A_{k+1}(x)
=
\sum_p\sum_{j=0}^{k}(-1)^j
A_{k-j}\!\left(\left\lfloor\frac{x}{p^{j+1}}\right\rfloor\right)
}
\]

을 얻는다.

이 식에는 평균 소수분포, zeta zero, `1/2`가 들어가지 않는다.

`x=100,500,1000,5000,10000`의 모든 존재 층에서 직접 계산한 21개 등식은 모두

```text
difference = 0
```

으로 일치했다.

---

## 7. layer polynomial 형태

유한 형성층 다항식을

\[
G_x(z)=\sum_{k\ge0}A_k(x)z^k
=\sum_{n\le x}\mu(n)^2z^{\omega(n)}
\]

라고 두자.

특정 소수 `p`를 사용하지 않는 다항식을 `G_x^(p)(z)`라고 쓰면

\[
G_x'(z)
=
\sum_pG_{\lfloor x/p\rfloor}^{(p)}(z)
\]

이고

\[
G_y^{(p)}(z)
=
G_y(z)-zG_{\lfloor y/p\rfloor}^{(p)}(z).
\]

따라서 유한하게 반복하면

\[
\boxed{
G_x'(z)
=
\sum_p\sum_{j\ge0}(-z)^j
G_{\lfloor x/p^{j+1}\rfloor}(z)
}.
\]

계수비교가 바로 앞 절의 `A_k` 재귀를 준다.

---

## 8. Möbius 예외위상 z=-1

`z=-1`에서는

\[
G_x(-1)=M(x)
\]

이고 모든 `(-z)^j`가 `+1`이므로

\[
\boxed{
G_x'(-1)
=
\sum_{p^r\le x}
M\!\left(\left\lfloor\frac{x}{p^r}\right\rfloor\right)
}.
\]

한편

\[
G_x'(-1)
=-\sum_{n\le x}\mu(n)\omega(n).
\]

따라서

\[
\boxed{
\sum_{n\le x}\mu(n)\omega(n)
=
-\sum_{p^r\le x}
M\!\left(\left\lfloor\frac{x}{p^r}\right\rfloor\right)
}
\]

이다.

이 1차 identity는 기존 Möbius-convolution 문헌과 일치한다. 특히 `mu(n) omega(n)`가 prime-power characteristic function과 Möbius 함수의 convolution으로 표현된다는 결과가 알려져 있다.

따라서 **새 정리라고 주장하지 않는다.** 현재의 의미는 이것이 전체 formation-layer polynomial의 정확한 재귀에서 자연스럽게 나온다는 점이다.

---

## 9. 수치적 prime-power 분해

`x=2^24`에서

\[
G_x'(-1)=-76,387.
\]

prime first-power 부분

\[
\sum_{p\le x}M(\lfloor x/p\rfloor)
=-75,803
\]

이 전체의 약 `99.24%`를 차지했다.

나머지 `p^2,p^3,...` 전체 합은 `-584`였다.

따라서 현재 범위에서는 예외위상 주변의 1차 변화가 거의

\[
\sum_p M(x/p)
\]

라는 prime-scaled self-interaction으로 지배된다.

이것은 다음 단계에서 검사할 가장 구체적인 결정론적 구조이다.

---

## 10. z=-1 근처 finite root

`G_x(z)`의 `-1`에 가장 가까운 실수근도 계산했다.

예:

- `x=2^22`: `z≈-0.99078810`
- `x=2^23`: `z≈-1.00023971`
- `x=2^24`: `z≈-0.99725946`

그러나 이것을 새 영점현상으로 해석하지 않는다.

Taylor 전개상

\[
z_x+1\approx-\frac{M(x)}{G_x'(-1)}
\]

이므로 `M(x)`가 작으면 근이 `-1` 가까이에 생기는 것은 상당 부분 같은 상쇄현상의 다른 표현이다.

따라서 이 근은 진단량이지 독립 RH 증거가 아니다.

---

## 11. 이번 단계의 판정

### 확인된 것

1. Möbius 상쇄는 단일 인접층 균형이 아니라 여러 `A_k` 층의 전역 보상으로 이루어진다.
2. 단순 Poisson/독립-channel null은 실제 parity cancellation을 재현하지 못한다.
3. 실제 prime-channel 구조에는 `A_k`들 사이의 정확한 결정론적 재귀가 존재한다.
4. `z=-1`에서 그 재귀는 prime-power scaled Mertens sums로 압축된다.
5. 이 1차 압축은 알려진 Möbius/prime-power convolution과 일치하므로 순환 가능성을 계속 경계해야 한다.

### 아직 확인되지 않은 것

\[
\boxed{
\text{이 결정론적 재귀만으로 }
M(x)=O_\varepsilon(x^{1/2+\varepsilon})
\text{를 강제할 수 있는가?}
}
\]

현재는 답이 없다.

---

## 12. 다음 단계

다음 감사는 `G_x'(-1)`에서 멈추지 않고

\[
G_x''(-1),\ G_x'''(-1),\ldots
\]

의 formation-layer hierarchy를 전개한다.

목표는 각 미분이 `M(x/q)`들의 어떤 prime-channel convolution으로 닫히는지 확인하고, 이 계층 전체가

1. 단순히 `1/zeta`의 미분을 다시 쓴 것인지,
2. 유한 `x`에서 사용할 수 있는 새로운 수축/직교/부호 제약을 제공하는지

분리하는 것이다.

특히 다음 operator를 우선 검사한다.

\[
\mathcal L M(x)
=
\sum_{p^r\le x}M(\lfloor x/p^r\rfloor).
\]

현재 단계에서는 `\mathcal L`이 RH bound를 자동으로 주는 contraction이라고 주장하지 않는다. 이를 증명하지 못하면 이 가지는 기존 Möbius 구조의 재표현으로 판정한다.
