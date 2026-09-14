# Parity Phase Exceptional-Point / Boundary-Layer Audit

Date: 2026-09-15

## 목적

formation phase polynomial

\[
G_x(z)=\sum_{n\le x}\mu^2(n)z^{\omega(n)}
\]

의 parity point `z=-1`가 ordinary phase points와 왜 전혀 다르게 작동하는지 분리한다.

실수 phase로는

\[
H_x(t)=G_x(e^{it})
\]

라 둔다. 그러면

\[
H_x(\pi)=M(x).
\]

핵심 질문은 다음이다.

1. `t=pi`가 단순히 여러 phase 중 하나인가, 아니면 analytic exceptional point인가?
2. `pi`에서 작은 phase error가 생기면 어떤 크기의 non-parity 성분이 다시 나타나는가?
3. phase scan / finite phase grid가 RH-scale Mertens endpoint를 보존하려면 어떤 해상도가 필요한가?

---

## 1. exact Euler-product factorization

`Re(s)>1`에서

\[
\mathcal F(s,z)
=\sum_{n\ge1}\frac{\mu^2(n)z^{\omega(n)}}{n^s}
=\prod_p(1+zp^{-s}).
\]

이를

\[
\boxed{
\mathcal F(s,z)=\zeta(s)^z\mathcal H(s,z)
}
\]

로 쓰면

\[
\mathcal H(s,z)
=\prod_p(1+zp^{-s})(1-p^{-s})^z
\]

이다. bounded `z`에 대해 `H(s,z)`는 `s=1` 근방에서 analytic한 Selberg--Delange factor다.

parity point `z=-1`에서는 모든 Euler factor가 정확히 소거되어

\[
\boxed{
\mathcal H(s,-1)=1,
\qquad
\mathcal F(s,-1)=\frac1{\zeta(s)}.
}
\]

따라서 generic phase의 `s=1` singularity가 parity point에서는 **zero**로 바뀐다.

상태: `EXACT`.

---

## 2. Selberg--Delange coefficient zero at parity

Generic fixed `z`에서는 Selberg--Delange main term이 schematic하게

\[
G_x(z)
= C(z)x(\log x)^{z-1}+\text{lower terms},
\]

\[
C(z)=\frac{\mathcal H(1,z)}{\Gamma(z)}.
\]

parity point에서는

\[
\mathcal H(1,-1)=1,
\qquad
\frac1{\Gamma(-1)}=0,
\]

이므로

\[
\boxed{C(-1)=0.}
\]

더 직접적으로 `F(s,-1)=1/zeta(s)`는 `s=1`에서 analytic zero를 가지므로, ordinary `s=1` branch/pole contribution 자체가 사라진다.

따라서 `M(x)`의 난점은 ordinary Erdos--Kac / Sathe--Selberg central mass가 아니라 `1/zeta(s)`의 다음 singularity frontier, 즉 zeta zeros 쪽으로 이동한다.

이것은 RH의 증명이 아니라 **왜 parity phase만 PNT/RH 정보를 직접 노출하는지에 대한 구조적 설명**이다.

상태: `STANDARD_SELBERG_DELANGE_INTERPRETATION`.

---

## 3. exact phase derivative at pi

직접 미분하면

\[
H_x'(t)
=i\sum_{n\le x}\mu^2(n)\omega(n)e^{it\omega(n)}.
\]

따라서

\[
\boxed{
H_x'(\pi)
=i\sum_{n\le x}\mu(n)\omega(n)
=iM_\omega(x).
}
\]

Alladi--Johnson이 정리한 Tenenbaum의 Selberg--Delange 결과는

\[
\boxed{
M_\omega(x)
=\frac{x}{\log^2x}
+O\!\left(\frac{x}{\log^3x}\right)
}
\]

이며 full asymptotic expansion의 leading coefficient가 정확히 `1`이다.

따라서 parity phase는 flat minimum이 아니다. 오히려 그 바로 옆에는 asymptotically

\[
\boxed{|H_x'(\pi)|\sim x/\log^2x}
\]

인 매우 큰 slope가 존재한다.

상태: derivative identity `EXACT`; asymptotic `KNOWN_SELBERG_DELANGE`.

---

## 4. local Taylor structure

exact하게

\[
H_x(\pi+\delta)
=M(x)
+i\delta M_\omega(x)
-\frac{\delta^2}{2}M_{\omega^2}(x)
+\cdots,
\]

여기서

\[
M_{\omega^j}(x)=\sum_{n\le x}\mu(n)\omega(n)^j.
\]

fixed higher derivatives는 differentiated Selberg--Delange 구조에서

\[
M_{\omega^j}(x)
=O_j\!\left(
\frac{x(\log\log x)^{j-1}}{\log^2x}
\right)
\]

형태를 갖는 것이 natural하다. 따라서 `delta log log x -> 0`인 local regime에서는 first derivative가 지배하는 boundary layer가 예상된다.

저장소에서는 higher-order uniformity를 별도 theorem으로 승격하지 않고, first-order exact identity + known `M_omega` asymptotic + numerical local audit로 사용한다.

---

## 5. RH-target phase-resolution scale

만약 phase approximation error `delta`가 만드는 first-order contamination을 RH target

\[
x^{1/2+\varepsilon}
\]

보다 작게 유지하려면 natural first-order scale은

\[
|\delta|\frac{x}{\log^2x}
\lesssim x^{1/2+\varepsilon},
\]

즉

\[
\boxed{
|\delta|
\lesssim
x^{-1/2+\varepsilon}\log^2x.
}
\]

이다.

이것은 RH를 증명하는 inequality가 아니다. `M(x)` 자체를 이미 target scale로 bound했다고 가정하는 것도 아니다. 의미는 다음과 같다.

> RH-scale parity signal을 nearby non-parity phase로 대체하려는 방법은 polynomially shrinking phase resolution을 요구한다.

따라서 이전의 `1/log x` reflection-resolution guard보다 훨씬 강한 **parity phase-resolution guard**다.

상태: `FIRST_ORDER_RESOLUTION_GUARD`, not an RH theorem.

---

## 6. finite layer numerical audit

기존 exact squarefree layer table

```text
data/formation/mobius_layer_counts_dyadic_24.csv
```

으로

\[
H_x(t)=\sum_r A_r(x)e^{itr}
\]

를 직접 계산했다.

또

\[
D_1(x)=\sum_r rA_r(x)(-1)^r
=\sum_{n\le x}\mu(n)\omega(n)
\]

를 계산했다.

`D_1 log^2(x)/x`는 큰 cutoff에서 다음 값을 보였다.

```text
x=2^20 : 1.49445
x=2^21 : 1.18389
x=2^22 : 1.33908
x=2^23 : 1.26483
x=2^24 : 1.26001
```

현재 범위는 asymptotic constant `1`에 아직 도달하지 않았지만 scale `x/log^2 x`와 정합적이다.

### sqrt(x) crossing width

`delta_obs`를 `delta>=0` 중

\[
|H_x(\pi+\delta)|=\sqrt{x}
\]

가 처음 성립하는 지점으로 잡았다.

linear prediction은 exact finite derivative를 사용해

\[
\delta_{\rm lin}
=\frac{\sqrt{x-M(x)^2}}{|D_1(x)|}
\]

로 두었다.

대표값:

| x | observed delta | linear delta | ratio |
|---:|---:|---:|---:|
| 2^21 | 0.119517 | 0.119660 | 0.9988 |
| 2^22 | 0.080706 | 0.084266 | 0.9578 |
| 2^23 | 0.068089 | 0.069379 | 0.9814 |
| 2^24 | 0.052623 | 0.053550 | 0.9827 |

따라서 현재 가장 큰 dyadic cutoffs에서는 `sqrt(x)` boundary width가 first derivative 하나만으로 거의 재현된다.

이 결과는 proof가 아니라 `NUMERICAL_LOCAL_CONFIRMATION`이다.

---

## 7. mod-Poisson / characteristic-function interpretation

squarefree integers에 대한 normalized layer law를

\[
\Pr_x(\omega=r)=A_r(x)/Q(x)
\]

라 두면

\[
\frac{M(x)}{Q(x)}
=\mathbb E_x[e^{i\pi\omega}]
\]

이다.

따라서 Mertens cancellation은 `omega`의 low moments보다 **fixed lattice frequency pi의 characteristic function**이다.

Erdos--Kac normality는 중심 scale의 characteristic function을 설명하지만, parity point는 Selberg--Delange limiting factor가 zero가 되는 exceptional Fourier point다.

Kowalski--Nikeghbali의 mod-Poisson framework는 prime-factor count의 characteristic-function asymptotics를 systematic하게 해석하는 선행계보다. 현재 audit의 신규성은 주장하지 않는다.

---

## 8. branch closure / guard

다음을 독립 RH candidate에서 제외한다.

1. coarse phase grid에서 `theta≈pi`를 찾아 parity endpoint를 대체한다.
2. `1/log x` 정도의 phase resolution이면 RH-scale structure를 충분히 보존한다고 가정한다.
3. generic Erdos--Kac / Gaussian characteristic-function approximation을 `t=pi`까지 그대로 연장한다.

parity point는 analytic exceptional point이며 nearby phase는 ordinary `s=1` Selberg--Delange term을 즉시 복구한다.

---

## 9. remaining question

parity phase를 exact하게 유지한 채 RH-scale을 얻으려면 phase approximation이 아니라 **arithmetic structure at exactly z=-1**을 제어해야 한다.

따라서 다음 전선은 moment/phase approximation 자체가 아니라, exact parity information을 얼마나 많은 growing-order arithmetic data가 필요로 하는지에 대한 information audit이다.

## 상태

- `F(s,-1)=1/zeta(s)`: `EXACT`.
- Selberg--Delange coefficient zero at parity: `STANDARD_EXACT_FACTOR / KNOWN_METHOD`.
- `H'_x(pi)=i sum mu omega`: `EXACT`.
- `sum mu omega ~ x/log^2 x`: `KNOWN_THEOREM`.
- phase boundary scale `log^2 x / sqrt(x)`: `FIRST_ORDER_RH_TARGET_GUARD`.
- finite dyadic crossing audit: `NUMERICAL`.
- independent RH progress: `NOT_ESTABLISHED`.

## 선행문헌

- Krishnaswami Alladi & Jason Johnson, *Duality Between Prime Factors and the Prime Number Theorem for Arithmetic Progressions -- II*; Section 3 records Tenenbaum's Selberg--Delange expansion and leading coefficient `1` for `sum mu(n) omega(n)`.
- Gérald Tenenbaum, standard Selberg--Delange theory as cited therein.
- Emmanuel Kowalski & Ashkan Nikeghbali (2009), *Mod-Poisson convergence in probability and number theory*, arXiv:0905.0318.
