# Height-Localized Mellin Barrier Audit

## 목적

`mertens_scale_curvature_audit.md`의 finite-spectrum pair filter는 유한 exponential spectrum에서는 정확하지만, 전체 zeta zero spectrum에서는 다른 높이의 mode와 convergence가 문제다.

따라서 zero locations를 입력하지 않고 **height band를 arithmetic side에서 직접 격리**할 수 있는지 감사한다.

---

## 1. soft localization: log-windowed Möbius packet

log-scale test function `w(u)`를 잡고, 예를 들어

\[
w_{\tau,T}(u)=\exp\left(-\frac{u^2}{2\tau^2}\right)e^{-iTu}
\]

를 생각한다.

arithmetic packet을

\[
A_{\tau,T}(x)
=
\sum_{n\ge1}\mu(n)
\,w_{\tau,T}(\log(n/x))
\]

처럼 정의할 수 있다.

Mellin transform은 vertical frequency `gamma≈T`에 Gaussian localization을 준다.

이 방식의 장점:

- zero 위치를 입력할 필요가 없다.
- `T`를 외부 scan parameter로 둘 수 있다.
- vertical decay가 매우 빠르므로 finite numerical spectrum 감사에는 좋다.

그러나 analytic Mellin weight가 nonzero인 한 다른 높이의 zeros를 **정확히** 제거하지는 못한다.

만약 off-band zero가 더 큰 real part `beta`를 가진다면 weight가 매우 작아도 asymptotic `x^beta`가 결국 더 작은-real-part in-band mode를 압도할 수 있다.

따라서 soft localization은 numerical diagnostics에는 유효하지만 spectral-abscissa proof에서 exact isolation을 제공하지 않는다.

상태: `USEFUL_NUMERICAL_FILTER / NOT_EXACT_ASYMPTOTIC_ISOLATION`.

---

## 2. holomorphic compact-height obstruction

contour shifting에 사용할 Mellin weight `W(s)`가 relevant strip에서 holomorphic이라고 하자.

어떤 vertical line segment의 open interval에서 `W(s)=0`이면서 다른 곳에서는 nonzero이도록 하여 exact height cutoff를 만들려고 하면, zeros가 domain 안에 accumulation point를 가지므로 identity theorem에 의해 `W`는 identically zero가 된다.

즉 **holomorphic Mellin multiplier로 exact compact vertical support를 만드는 것은 불가능**하다.

이 때문에 exact height truncation은 analytic weight가 아니라 finite contour/truncated transform 쪽으로 가야 한다.

상태: `EXACT_COMPLEX_ANALYSIS_BARRIER`.

---

## 3. exact finite-height Perron packet

`c>1`, center height `T`, half-width `H>0`에 대해

\[
\boxed{
P_{c,T,H}(x)
=
\frac{1}{2\pi i}
\int_{c+i(T-H)}^{c+i(T+H)}
\frac{x^s}{\zeta(s)}\,ds
}
\]

를 정의한다.

`Re(s)=c>1`에서는

\[
\frac1{\zeta(s)}=\sum_{n\ge1}\mu(n)n^{-s}
\]

가 absolute convergence하므로 termwise integration이 정당하다.

`L_n=log(x/n)`라 하면

\[
\boxed{
P_{c,T,H}(x)
=
\frac1\pi
\sum_{n\ge1}
\mu(n)
\left(\frac xn\right)^c
 e^{iT L_n}
\frac{\sin(HL_n)}{L_n}
}
\]

이며 `L_n=0`에서는 quotient를 limit `H`로 해석한다.

따라서 이것은 **zero data 없이 정의되는 exact arithmetic height-band observable**이다.

상태: `EXACT`.

---

## 4. contour-shift barrier

이제 right vertical segment `Re(s)=c`를 `Re(s)=sigma_0<c`로 옮겨 rectangle을 만들면 residue theorem에 의해 내부의 zeros `rho`에서

\[
\operatorname{Res}_{s=\rho}\frac{x^s}{\zeta(s)}
=
\frac{x^\rho}{\zeta'(\rho)}
\]

(simple zero case)이 나타난다.

그러나 finite rectangle에는 동시에

1. left vertical segment,
2. top horizontal segment,
3. bottom horizontal segment

가 남는다.

따라서 schematically

\[
P_{c,T,H}(x)
=
P_{\sigma_0,T,H}(x)
+
\sum_{\rho\in\mathcal R}\frac{x^\rho}{\zeta'(\rho)}
+
E_{\rm top}(x)+E_{\rm bottom}(x)
+
\text{trivial/pole terms}
\]

형태가 된다.

특정 height rectangle 안의 zero contributions만 growth detector에 넣으려면 left/horizontal terms가 그보다 작다는 uniform control이 필요하다.

그런데 horizontal terms는 rectangle across `sigma`에서 `1/zeta(s)`를 직접 포함하므로, 이 제어는 zero-free / reciprocal-zeta growth 문제와 독립적이지 않다.

### 판정

\[
\boxed{
\text{exact height localization은 가능하지만, residue isolation 비용이 contour-edge control로 이동한다.}
}
\]

즉 난점이 제거된 것이 아니라 representation channel만 바뀐다.

---

## 5. scale-curvature와 결합할 경우

`P_{c,T,H}(x)` 또는 soft packet `A_{tau,T}(x)`에 multiplicative scale curvature

\[
K_a[A](x)=A(x/a)^2-A(x)A(x/a^2)
\]

를 적용하면 finite zero residue sector에서는 이전 pair-filter identity가 그대로 작동한다.

따라서 **numerical height-localized real-part scan**에는 사용할 가치가 있다.

그러나 proof route로 사용하려면 먼저 contour-edge term을 arithmetic-only estimate로 제어해야 한다.

현재 그런 estimate는 얻지 못했다.

---

## 6. 닫히는 경로

다음은 현 단계에서 닫는다.

1. Gaussian/log window만 좁히면 asymptotically 특정 height zero만 남는다는 주장.
2. holomorphic Mellin multiplier에 exact compact height support를 주는 방식.
3. truncated Perron integral에서 rectangle edge를 무시하고 residues만 사용하는 방식.
4. height-localized curvature가 자동으로 RH를 더 쉽게 만든다는 주장.

---

## 7. 남는 활용

height-localized packet은 **proof mechanism이 아니라 audit instrument**로 남긴다.

쓸 수 있는 용도:

- finite zero-band numerical reproduction,
- `sigma`를 미리 고정하지 않은 finite-spectrum growth test,
- candidate arithmetic statistic이 어느 height band와 결합하는지 찾는 diagnostic,
- known zero-wave를 제거한 residual의 provenance 추적.

다음 proof-level 후보는 contour shift 없이 arithmetic side에서 직접 닫히는 cross-scale identity/inequality여야 한다.

---

## 상태

- exact sinc-kernel arithmetic packet at `c>1`: `EXACT`.
- soft height localization: `NUMERICAL_TOOL`.
- exact spectral isolation after contour shift: `BLOCKED_BY_EDGE_CONTROL`.
- independent RH progress: `NOT_ESTABLISHED`.
- RH: `OPEN`.
