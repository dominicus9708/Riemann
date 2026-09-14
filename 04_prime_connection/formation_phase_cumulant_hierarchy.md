# Formation Phase Cumulant Reciprocal-Hierarchy Audit

## 목적

`F(s,z)=prod_p(1+z p^{-s})`의 Möbius phase `z=-1` 주변에서 phase derivative / curvature를 사용하면 `1/2`가 독립적으로 출현하는지 검사한다.

결론부터 말하면 `m=2` phase curvature에는 실제로 `1/2`가 구조적으로 나타난다. 그러나 정확한 일반화를 하면

\[
\boxed{1/2,1/3,1/4,\ldots}
\]

가 모두 같은 mechanism에서 나온다.

따라서 이 `1/2`는 RH critical line의 선택이 아니라 **cumulant order m이 만드는 reciprocal hierarchy**다.

---

## 1. squarefree phase generating function

초기 절대수렴영역 `Re(s)>1`에서

\[
F(s,z)
=
\sum_{n\ge1}\frac{\mu(n)^2z^{\omega(n)}}{n^s}
=
\prod_p(1+zp^{-s}).
\]

`z=-1`에서는

\[
F(s,-1)=\prod_p(1-p^{-s})=\frac1{\zeta(s)}.
\]

이 단계는 기존 `formation_phase_exception.md`의 기준식과 같다.

---

## 2. exact phase cumulants

logarithm을 취하면

\[
\log F(s,z)=\sum_p\log(1+zp^{-s}).
\]

`m>=1`에 대해

\[
\frac{\partial^m}{\partial z^m}\log(1+zu)
=
(-1)^{m-1}(m-1)!\frac{u^m}{(1+zu)^m}.
\]

따라서 `z=-1`에서

\[
\boxed{
C_m(s)
:=
\left.\partial_z^m\log F(s,z)\right|_{z=-1}
=
(-1)^{m-1}(m-1)!
\sum_p\frac{p^{-ms}}{(1-p^{-s})^m}.
}
\]

상태: `EXACT` in `Re(s)>1`, 이후 continuation은 별도 감사.

---

## 3. prime-zeta dilation expansion

\[
(1-u)^{-m}
=
\sum_{j\ge0}\binom{m+j-1}{m-1}u^j
\]

를 사용하고 `r=m+j`라 두면

\[
\boxed{
D_m(s)
:=
\frac{(-1)^{m-1}}{(m-1)!}C_m(s)
=
\sum_{r=m}^{\infty}
\binom{r-1}{m-1}P(rs),
}
\]

여기서

\[
P(s)=\sum_p p^{-s}
\]

는 prime zeta function이다.

즉 phase cumulant hierarchy는 새로운 독립 spectrum이 아니라 **dilated prime-zeta family `P(rs)`의 triangular binomial transform**이다.

---

## 4. reciprocal singularity hierarchy

`D_m`의 첫 항은

\[
P(ms).
\]

prime zeta `P(w)`는 초기 절대수렴 경계 `Re(w)=1`에서 `w=1` singularity를 가지므로, `m`차 cumulant의 첫 structural boundary는

\[
\boxed{\Re(s)=1/m.}
\]

따라서

- `m=1 -> 1`,
- `m=2 -> 1/2`,
- `m=3 -> 1/3`,
- `m=4 -> 1/4`,
- ...

가 동일한 조합론적 mechanism으로 생성된다.

### 감사 판정

`m=2`에서 `1/2`가 나오는 것은 사실이지만,

\[
\boxed{
\text{phase curvature가 RH critical line을 선택한 것이 아니다.}
}
\]

이는 `m`차 prime-channel cumulant의 generic reciprocal threshold다.

상태: `EXACT_FALSE_CONTROL_FOR_HALF`.

---

## 5. second phase curvature explicitly

`m=2`에서

\[
C_2(s)
=-\sum_p\frac{p^{-2s}}{(1-p^{-s})^2}
=-\sum_{r\ge2}(r-1)P(rs).
\]

또

\[
F F_{zz}-F_z^2
=F^2\partial_z^2\log F.
\]

`z=-1`에서

\[
\boxed{
\left.(F F_{zz}-F_z^2)\right|_{z=-1}
=
-\frac1{\zeta(s)^2}
\sum_{r\ge2}(r-1)P(rs).
}
\]

따라서 이 phase-Hessian observable에는

1. `1/zeta(s)^2`의 zero-sensitive factor,
2. `P(2s)`가 만드는 structural `1/2` boundary

가 **동시에** 들어간다.

둘을 분리하지 않고 `1/2` 출현을 RH 증거로 읽으면 circular/false-positive가 된다.

---

## 6. why the PNT main mode disappears but 1/2 appears

near `s=1`에서는 표준적으로

\[
F(s,z)=\zeta(s)^z H(s,z)
\]

형태로 regular factor `H`를 분리할 수 있다.

`log F = z log zeta + log H`이므로

\[
\partial_z^m\log F
\]

에서 `m>=2`이면 linear term `z log zeta`는 사라진다.

즉 second/higher phase cumulant는 `s=1`의 직접적인 first-order PNT mode를 제거한다.

그러나 그 대가로 prime-channel self-interaction이 `P(ms)`를 생성하고, 새로운 structural boundary `1/m`가 나타난다.

이것은 DSD 관점에서 중요한 정보변환이다:

\[
\boxed{
\text{1차 공통모드 제거}
\not\Rightarrow
\text{zero-only residual};
\quad
\text{새 조합론적 경계가 생성될 수 있다.}
}
\]

---

## 7. triangular invertibility

고정 `s`에서

\[
D_m=\sum_{r\ge m}\binom{r-1}{m-1}q_r,
\qquad q_r=P(rs)
\]

는 upper-triangular binomial transform이다.

적절한 convergence 아래 binomial inversion으로

\[
\boxed{
P(ms)
=
\sum_{r\ge m}
(-1)^{r-m}
\binom{r-1}{m-1}D_r(s).
}
\]

이는 identity

\[
\sum_{r=m}^{k}
(-1)^{r-m}
\binom{r-1}{m-1}
\binom{k-1}{r-1}
=\delta_{mk}
\]

에서 따른다.

따라서 **전체 phase-cumulant hierarchy와 전체 dilated prime-zeta hierarchy는 정보적으로 서로 가역**이다.

새 독립 spectral information을 추가하지 않는다.

상태: `EXACT_INFORMATION_EQUIVALENCE` under convergence/interchange conditions.

---

## 8. arithmetic coefficient interpretation

`a_z(n)=mu(n)^2 z^omega(n)`라 두면 `z=-1`에서

\[
a(n)=\mu(n),
\]

\[
b(n)=\left.\partial_z a_z(n)\right|_{-1}
=-\mu(n)\omega(n),
\]

\[
c(n)=\left.\partial_z^2 a_z(n)\right|_{-1}
=\mu(n)\omega(n)(\omega(n)-1).
\]

따라서 second phase determinant의 Dirichlet coefficients는

\[
\boxed{
d=(\mu*c)-(b*b)
}
\]

(`*` = Dirichlet convolution)로 arithmetic side에서도 정확히 정의할 수 있다.

즉 phase-Hessian은 zero data를 넣지 않고 계산 가능하지만, 그 Dirichlet transform은 위 `1/zeta^2 × prime-zeta-dilation` 구조로 정확히 닫힌다.

---

## 9. numerical false-control

직접 Möbius sieve에서

\[
G_x'(-1)=-\sum_{n\le x}\mu(n)\omega(n)
\]

을 계산하면 `s=1` first derivative가 smooth main term을 갖는 현상이 보인다.

대표값:

| x | G'_x(-1) | -x/(log x)^2 | ratio |
|---:|---:|---:|---:|
| 2^16 | -861 | -532.83 | 1.616 |
| 2^18 | -2458 | -1684.01 | 1.460 |
| 2^20 | -8154 | -5456.18 | 1.494 |
| 2^22 | -24153 | -18036.97 | 1.339 |
| 2^24 | -76387 | -60624.27 | 1.260 |

이는 phase differentiation이 무조건 RH-scale cancellation을 강화하는 것이 아니라 PNT/prime-zeta smooth modes를 새 형태로 노출할 수 있음을 보여주는 보조 수치자료다.

이 표는 asymptotic proof가 아니라 `NUMERICAL_FALSE_CONTROL`이다.

---

## 10. 닫히는 경로

1. second phase derivative/curvature에서 `1/2`가 보인다는 사실만으로 RH evidence를 주장한다.
2. `m=2`를 특별한 formation order라고 사후 선택한다.
3. higher phase cumulants가 `1/zeta`와 독립인 새 spectrum을 만든다고 주장한다.
4. PNT first mode를 제거했으므로 남는 singularity가 모두 nontrivial zeros에서 온다고 가정한다.

모두 닫는다.

---

## 11. 남는 의미

이 결과는 오히려 강한 감사 도구다.

앞으로 어떤 construction에서 `1/2`가 나타나면 반드시

\[
\boxed{
\text{그 construction을 m차로 일반화했을 때 }1/m\text{ hierarchy가 생기는가?}
}
\]

를 먼저 검사한다.

생긴다면 그 `1/2`는 RH 선택이 아니라 combinatorial order artifact일 가능성이 높다.

이 규칙을 `reciprocal-hierarchy false-control`로 사용한다.

---

## 상태

- phase cumulant formula: `EXACT`.
- prime-zeta triangular expansion: `EXACT`.
- `1/m` reciprocal hierarchy: `EXACT_STRUCTURAL_BOUNDARY`.
- binomial invertibility: `EXACT` subject to convergence/interchange.
- `1/2` as RH evidence from m=2 phase curvature: `EXCLUDED`.
- RH: `OPEN`.
