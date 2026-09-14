# Reflection-Symmetry Finite-Resolution Barrier

Date: 2026-09-15

## 목적

여러 numerical `sigma`-emergence / scale-growth 진단이 `1/2` 부근으로 모일 때, **functional-equation reflection symmetry 자체가 finite cutoff에서 off-line displacement를 얼마나 숨길 수 있는지** 정량화한다.

이 문서는 off-critical zeta zero의 존재를 가정하거나 주장하지 않는다. `1/2` finite-fit에 대한 false-control이다.

---

## 1. reflection symmetry baseline

Riemann xi function은

\[
\boxed{\xi(s)=\xi(1-s)}
\]

을 만족한다.

따라서 spectral construction이 reflection을 대칭적으로 처리하면 `beta=1/2+delta`와 `1/2-delta`가 동시에 들어가는 구조가 자연스럽다.

가장 단순한 positive-envelope false control은

\[
S_\delta(x)
=x^{1/2+\delta}+x^{1/2-\delta}
=2x^{1/2}\cosh(\delta\log x).
\]

---

## 2. exact effective exponent

local log-growth exponent를

\[
\alpha_\delta(x)
=\frac{d\log S_\delta(x)}{d\log x}
\]

라고 하면 정확히

\[
\boxed{
\alpha_\delta(x)
=\frac12+\delta\tanh(\delta\log x).
}
\]

따라서 `delta != 0`이어도 finite `x`에서 exponent가 `1/2`에 매우 가까울 수 있다.

small-resolution regime

\[
|\delta|\log x\ll1
\]

에서는

\[
\boxed{
\alpha_\delta(x)
=\frac12+\delta^2\log x
+O(\delta^4(\log x)^3).
}
\]

즉 reflection-symmetric diagnostic의 first-order sensitivity to `delta`는 사라지고 displacement는 **quadratic order**에서만 보인다.

---

## 3. resolution parameter

두 reflected power의 amplitude ratio는

\[
\frac{x^{1/2+\delta}}{x^{1/2-\delta}}
=x^{2\delta}=e^{2\delta\log x}.
\]

따라서 finite range `x<=X`에서 두 branch가 order-one 수준으로 분리되려면 최소한

\[
\boxed{|\delta|\log X\gtrsim1}
\]

이 필요하다.

이를 보수적 reflection resolution scale로

\[
\boxed{
\Delta_{\rm res}(X)=\frac1{\log X}
}
\]

라 기록한다.

이것은 impossibility theorem for all conceivable statistics가 아니라, reflection-symmetric power-growth diagnostics에 대한 mandatory false-control scale이다.

---

## 4. dyadic ranges

`X=2^K`이면

\[
\Delta_{\rm res}(2^K)=\frac1{K\log2}.
\]

대표값:

| K | 1/(K log 2) |
|---:|---:|
| 19 | 0.07593 |
| 24 | 0.06011 |
| 75 | 0.01924 |
| 100 | 0.01443 |
| 1000 | 0.001443 |

따라서 이전 formation `sigma` scan의 `X<=2^19`는 reflection-symmetric displacement `|delta| << 0.076`을 growth fit만으로 구별할 해상도가 없다.

published dyadic Mertens sequence `k<=75`를 이용한 determinant/growth scan도 보수적 scale가 약 `0.0192`이다.

---

## 5. finite OLS false-control

`k=10..75`에서

\[
S_\delta(2^k)
=2^{(1/2+\delta)k}+2^{(1/2-\delta)k}
\]

에 대해 `log_2 S`를 `k`에 OLS fitting했다.

| delta | delta log X | fitted exponent |
|---:|---:|---:|
| 0.001 | 0.0520 | 0.500029 |
| 0.002 | 0.1040 | 0.500118 |
| 0.005 | 0.2599 | 0.500729 |
| 0.010 | 0.5199 | 0.502836 |
| 0.020 | 1.0397 | 0.510278 |
| 0.030 | 1.5596 | 0.520287 |
| 0.050 | 2.5993 | 0.542639 |
| 0.100 | 5.1986 | 0.597205 |

특히 actual spectral real part가 `0.51/0.49`인 **synthetic reflected pair**라도 이 finite window에서는 exponent가 `0.50284`로 보인다.

따라서 `0.500...`에 가까운 regression 자체는 off-line displacement exclusion evidence가 아니다.

---

## 6. oscillatory quartet version

nonreal reflected quartet의 단순 equal-envelope model은

\[
Q_{\delta,\gamma}(x)
=4x^{1/2}\cosh(\delta\log x)
\cos(\gamma\log x+\phi).
\]

oscillation을 제외한 envelope growth는 위 `S_delta`와 동일하다.

실제 `1/zeta` explicit-formula residues는 reflected pair에 equal coefficients를 가질 필요가 없으므로 이 식을 actual Mertens reconstruction으로 사용하지 않는다.

반면 `xi(s)=xi(1-s)`를 직접 symmetric하게 사용하는 diagnostic에서는 reflection-even dependence가 구조적으로 자연스럽기 때문에 이 false control을 반드시 통과해야 한다.

---

## 7. relation to Hankel / curvature audit

higher scale-Hankel determinants의 full-range rank-normalized slopes가 `~1/2`에 모였던 결과는 already-known critical-line zero wave가 대부분 재현했다.

이번 audit은 별도의 경고를 추가한다.

설령 future synthetic or arithmetic spectral model에서 small off-line reflected pair가 존재하더라도, finite dynamic range가

\[
|\delta|\log X\lesssim1
\]

이면 reflection symmetry 때문에 `1/2`-like finite exponent가 쉽게 나타난다.

따라서 future sigma-emergence claim은 최소한

1. cutoff growth,
2. fitted sigma drift,
3. `1/log X` reflection resolution,
4. synthetic reflected-pair false controls

를 함께 보고해야 한다.

---

## 8. DSD-style information audit

finite cutoff `X`는 reflected branches의 relative amplitude에 대해 최대

\[
e^{2|\delta|\log X}
\]

의 contrast만 제공한다.

`|delta| log X << 1`에서는 두 branches가 observation scale에서 거의 indistinguishable하다.

따라서 `1/2` near-fit을 **정확한 spectral location**으로 승격하는 것은 해상도 조건을 위반한다.

이를 향후 `REFLECTION_RESOLUTION_GUARD`로 사용한다.

---

## 9. 판정

- xi reflection symmetry: `STANDARD_THEOREM`.
- symmetric-pair effective exponent formula: `EXACT`.
- `1/log X` resolution scale: `EXACT_SCALE_DIAGNOSTIC / NOT_UNIVERSAL_IMPOSSIBILITY_THEOREM`.
- dyadic OLS examples: `NUMERICAL_FALSE_CONTROL`.
- finite near-1/2 regression as RH evidence: `REJECT_WITHOUT_RESOLUTION_AUDIT`.
- RH: `OPEN`.

## 재현자료

```text
scripts/audit_reflection_resolution.py
data/mertens/reflection_resolution_false_control.csv
```

## 기준문헌

NIST DLMF §25.4 records the reflection formula and

\[
\xi(s)=\xi(1-s).
\]
