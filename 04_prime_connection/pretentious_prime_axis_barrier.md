# Pretentious Prime-Axis Barrier Audit

## 목적

formation character picture에서 Möbius는 모든 prime channel에 `-1`을 주는 deterministic character다.

Granville–Soundararajan/Halász의 pretentious framework와 비교하여

1. prime-by-prime mismatch가 얼마만큼의 cancellation을 설명하는지,
2. 왜 그것만으로 RH의 square-root scale까지 가지 못하는지

분리한다.

---

## 1. pretentious distance

`|f(n)|<=1`인 multiplicative function에 대해 대표적인 distance는

\[
\mathbb D(f,g;X)^2
=
\sum_{p\le X}
\frac{1-\Re(f(p)\overline{g(p)})}{p}.
\]

benchmark

\[
g(n)=n^{it}
\]

를 쓰면 quantitative Halász theorem은 대략

\[
\frac1X\left|\sum_{n\le X}f(n)\right|
\ll
(M+1)e^{-M}
+\text{secondary terms},
\]

\[
M=\min_{|t|\le T}\mathbb D(f,n^{it};X)^2
\]

형태다.

Granville–Soundararajan 및 Granville–Harper–Soundararajan을 표준 선행기준으로 사용한다.

---

## 2. Möbius의 prime-axis distance

prime에서

\[
\mu(p)=-1.
\]

따라서

\[
\boxed{
\mathbb D(\mu,n^{it};X)^2
=
\sum_{p\le X}
\frac{1+\cos(t\log p)}{p}.
}
\]

`t=0`에서는

\[
\mathbb D(\mu,1;X)^2
=2\sum_{p\le X}\frac1p
=2\log\log X+O(1).
\]

`t`를 최적화해도 각 summand가 `0..2/p`이므로 항상

\[
0\le M
\le
2\sum_{p\le X}\frac1p
=
O(\log\log X).
\]

---

## 3. 구조적 한계: prime-axis energy는 log log X뿐

Halász-type decay가

\[
e^{-M}
\]

에 의해 주어진다고 할 때, prime-axis distance에서 가능한 exponent 자체가 최대

\[
O(\log\log X)
\]

이다.

따라서 가장 낙관적으로도 이 mechanism은

\[
e^{-O(\log\log X)}
=(\log X)^{-O(1)}
\]

형태의 logarithmic-power saving scale을 자연스럽게 만든다.

반면 RH-equivalent Mertens target은

\[
M(X)=O_\varepsilon(X^{1/2+\varepsilon}),
\]

즉 trivial `X` scale에서 roughly polynomial `X^{1/2}` saving을 요구한다.

그런 saving을 `e^{-M}` 하나로 만들려면

\[
M\asymp c\log X
\]

크기의 distance energy가 필요하지만, prime-wise `1/p` geometry에는 그만한 총질량이 존재하지 않는다.

### 판정

\[
\boxed{
\text{prime-by-prime nonpretentiousness alone cannot account for RH square-root cancellation.}
}
\]

이것은 Halász theorem이 약하다는 말이 아니라 **그 metric이 측정하는 one-prime energy budget 자체의 크기**에 대한 장벽이다.

---

## 4. formation language의 해석

pretentious distance는 각 prime channel을 독립 축으로 보고

\[
\frac1p
\]

가중치로 disagreement energy를 더한다.

formation language에서는 이것이 **1-channel observable**이다.

반면 Möbius Mertens sum은 squarefree states

\[
S=\{p_1,\ldots,p_k\}
\]

전체의 parity

\[
(-1)^k
\]

를 arithmetic threshold

\[
\prod_{p\in S}p\le X
\]

위에서 합한다.

따라서 RH-scale cancellation은 prime marginal들만이 아니라

- 2-channel,
- 3-channel,
- ...,
- high-order squarefree composite states

사이의 joint boundary geometry를 포함한다.

이것은 `formation_hilbert_bridge_audit.md`에서 top parity Fourier coefficient가 고차 observable로 나타난 것과 일치한다.

---

## 5. Hilbert criticality와 pretentiousness의 역할 분리

squarefree Hilbert energy에서는

\[
\sum_{n\le X}\frac{\mu(n)^2}{n^{2\sigma}}
\]

가 `sigma=1/2`에서 critical하다.

이 energy는 모든 squarefree composite states를 포함하지만 **sign을 잊는다**.

pretentious distance는 sign을 prime level에서 보존하지만 total energy가 `log log X`밖에 없다.

따라서 두 framework의 장단점은 서로 반대다.

| 구조 | composite states | Möbius sign | natural scale | 장벽 |
|---|---|---|---|---|
| Haar/Dirichlet `L²` | yes | global norm에서 사라짐 | `1/2` | pointwise sign cancellation 못 봄 |
| pretentious prime distance | prime marginals | yes | `log log X` | polynomial square-root saving 못 만듦 |

### 현재 필요한 구조

\[
\boxed{
\text{high-order composite interaction을 보존하면서 Möbius parity sign도 잃지 않는 boundary functional}
}
\]

이다.

---

## 6. random multiplicative functions와의 교차

random Rademacher multiplicative function은 prime signs를 독립 random하게 만든다.

Harper의 결과들은

- second-moment RMS는 square-root scale,
- first absolute moment는 `sqrt(X)/(log log X)^(1/4)`,
- almost surely `sqrt(X)`보다 큰 fluctuation도 무한히 자주 존재

함을 보여준다.

따라서 `random prime signs -> square-root cancellation`이라는 단순 문장도 정확하지 않다.

Möbius는 random sample이 아니라 all-minus symmetric character이므로 random model은 baseline일 뿐이다.

---

## 7. 현재 판정

### 닫힌 단순경로

\[
\text{Möbius is strongly nonpretentious}
\to
\text{Halász}
\to
X^{1/2+\varepsilon}
\]

는 닫는다.

prime-weighted distance의 total budget가 `O(log log X)`이기 때문이다.

### 남은 방향

formation route가 실제 새 정보를 주려면 prime-axis distance를 넘어

\[
\boxed{
\text{arithmetic threshold에서 high-order parity interaction을 직접 제어}
}
\]

해야 한다.

후보 수학언어는

- high-degree Boolean Fourier coefficient,
- boundary flux between factor-count layers,
- multilinear prime-factor kernels,
- martingale / conditional expectation across prime channels

이지만, 각각 기존 sieve/Hardy/random-multiplicative theory와의 중복을 계속 감사한다.

---

## 선행문헌

- Andrew Granville & K. Soundararajan (2003), *Decay of Mean Values of Multiplicative Functions*, Canadian J. Math. 55(6), 1191–1230, DOI 10.4153/CJM-2003-047-0.
- Andrew Granville & K. Soundararajan (2008), *Pretentious Multiplicative Functions and an Inequality for the Zeta-Function*, in *Anatomy of Integers*, CRM Proc. Lect. Notes 46, 179–189.
- Andrew Granville, Adam J. Harper & K. Soundararajan (2019), *A New Proof of Halász’s Theorem, and Its Consequences*, Compositio Math. 155(1), 126–163, DOI 10.1112/S0010437X18007522.
- Adam J. Harper (2020), *Moments of Random Multiplicative Functions, I*, Forum Math. Pi 8:e1, DOI 10.1017/fmp.2019.7.
- Adam J. Harper (2023), *Almost Sure Large Fluctuations of Random Multiplicative Functions*, IMRN 2023(3), 2095–2138, DOI 10.1093/imrn/rnab299.
