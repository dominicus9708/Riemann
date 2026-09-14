# Floor-Dilation / Dirichlet-Convolution Barrier Audit

Date: 2026-09-15

## 목적

현재까지 반복해서 등장한

\[
F(\lfloor X/d\rfloor)
\]

형태의 cross-scale recurrence가 실제로 새로운 연산자 구조인지, 아니면 Dirichlet convolution의 summatory representation인지 분류한다.

---

## 1. exact operator identity

arithmetical function `b`의 summatory function을

\[
F_b(x)=\sum_{n\le x}b(n)
\]

라 하고, 임의의 coefficient sequence `a`에 대해

\[
(T_aF)(x)=\sum_{d\le x}a(d)F(\lfloor x/d\rfloor)
\]

를 정의한다.

그러면 정확히

\[
\begin{aligned}
(T_aF_b)(x)
&=\sum_{d\le x}a(d)\sum_{n\le x/d}b(n)\\
&=\sum_{m\le x}\sum_{d\mid m}a(d)b(m/d)\\
&=\sum_{m\le x}(a*b)(m).
\end{aligned}
\]

따라서

\[
\boxed{T_aF_b=F_{a*b}}
\]

이다.

상태: `EXACT`.

---

## 2. operator algebra

Dirichlet convolution의 결합법칙 때문에 summatory-function class 위에서

\[
\boxed{T_aT_b=T_{a*b}}
\]

가 성립한다.

Dirichlet identity `epsilon`에 대해 `T_epsilon=I`이고, `a`가 Dirichlet inverse `a^{-1}`를 가지면 형식적으로

\[
T_a^{-1}=T_{a^{-1}}.
\]

즉 fixed-coefficient floor-dilation algebra는 Dirichlet convolution algebra와 동형인 representation이다.

---

## 3. Mertens identity는 exact inversion이다

`mu*1=epsilon`이므로

\[
\boxed{
\sum_{d\le x}M(\lfloor x/d\rfloor)=1
}
\]

은 단순히

\[
T_1M=F_{1*\mu}=F_\epsilon=1
\]

이다.

반대로

\[
M=T_\mu 1.
\]

따라서 `T_1`이 Mertens difficulty를 없앤 것이 아니라, inverse operator `T_mu`에 정확히 되돌려 놓은 것이다.

이를 `COMPRESSION_NOT_CONTRACTION`으로 분류한다.

---

## 4. weighted-growth norm barrier

\[
\|F\|_{\infty,\sigma}
=\sup_{x\ge1}\frac{|F(x)|}{x^\sigma}
\]

와

\[
\|a\|_{1,\sigma}=\sum_{n\ge1}\frac{|a(n)|}{n^\sigma}
\]

를 둔다.

`||a||_{1,sigma}<infinity`이면

\[
\boxed{
\|T_aF\|_{\infty,\sigma}
\le
\|a\|_{1,\sigma}\|F\|_{\infty,\sigma}
}
\]

이다.

또 `c=a^{-1}`에 대해서도 `||c||_{1,sigma}<infinity`이면

\[
\|F\|_{\infty,\sigma}
\le
\|c\|_{1,\sigma}\|T_aF\|_{\infty,\sigma}.
\]

따라서 `a`와 그 Dirichlet inverse가 모두 weighted-l1에 있으면 `T_a`는 `x^sigma` growth class를 바꾸지 못한다.

### RH audit consequence

RH-scale `sigma>1/2`에서 stable invertibility가 성립하는 fixed dilation transform은

\[
M(x)=O(x^\sigma)
\quad\Longleftrightarrow\quad
T_aM(x)=O(x^\sigma)
\]

를 constants 차이만 두고 보존한다.

따라서 **bounded + stably invertible fixed dilation transform 자체는 exponent improvement mechanism이 아니다.**

---

## 5. Dirichlet-series spectral barrier

\[
A(s)=\sum_{n\ge1}\frac{a(n)}{n^s}
\]

라 하면 Mertens coefficient series는

\[
\sum\frac{\mu(n)}{n^s}=\frac1{\zeta(s)}
\]

이므로 transformed coefficient series는

\[
\boxed{
\frac{A(s)}{\zeta(s)}.
}
\]

따라서 nontrivial zero `rho`에 대해

- `A(rho) != 0`이면 `1/zeta`의 singularity는 그대로 남는다.
- `A(rho)=0`으로 이를 지우면 `1/A`는 그 지점에서 singular해져 stable inverse가 사라진다.

즉 fixed linear dilation에서

\[
\boxed{
\text{zero cancellation}
\Longleftrightarrow
\text{loss of stable invertibility at that zero}
}
\]

이다.

이것은 analytic continuation을 이용한 독립 RH proof가 아니라 operator-level information audit이다.

---

## 6. formation-layer recurrence도 같은 algebra에 속한다

\[
g_z(n)=\mu^2(n)z^{\omega(n)},
\qquad
G_z(x)=\sum_{n\le x}g_z(n)
\]

로 둔다.

Dirichlet series는

\[
F(s,z)=\prod_p(1+zp^{-s}).
\]

prime-power coefficient sequence

\[
q_z(p^r)=(-z)^{r-1},
\qquad
q_z(n)=0\quad(n\ne p^r)
\]

를 두면

\[
Q_z(s)=\sum_n\frac{q_z(n)}{n^s}
=\sum_p\frac{p^{-s}}{1+zp^{-s}}
=\partial_z\log F(s,z).
\]

따라서 coefficient level에서

\[
\partial_z g_z=q_z*g_z
\]

이고 summatory level에서

\[
\boxed{
\partial_zG_z=T_{q_z}G_z.
}
\]

`z`의 coefficient를 비교하면 기존 exact layer recurrence

\[
(k+1)A_{k+1}(x)
=
\sum_p\sum_{j=0}^k(-1)^j
A_{k-j}(\lfloor x/p^{j+1}\rfloor)
\]

가 그대로 나온다.

따라서 이 recurrence는 별도 dynamical law가 아니라 Euler-product `z`-derivative의 summatory Dirichlet-convolution realization이다.

상태: `EXACT_RECLASSIFICATION`.

---

## 7. z=-1에서의 first derivative

`z=-1`이면 `q_{-1}(p^r)=1`이므로

\[
\boxed{
-\sum_{n\le x}\mu(n)\omega(n)
=
\sum_{p^r\le x}M(\lfloor x/p^r\rfloor).
}
\]

이 역시 prime-power dilation convolution으로 닫힌다.

따라서 이 항등식을 cross-scale contraction으로 해석하지 않는다.

---

## 8. contraction failure at the critical scale

`|z|=1`이면

\[
\|q_z\|_{1,\sigma}
=\sum_{p,r\ge1}p^{-r\sigma}.
\]

prime `r=1` terms 때문에 이는 `sigma<=1`에서 발산한다.

따라서 first formation-layer operator는 RH scale `sigma=1/2+epsilon`에서 weighted-growth contraction은커녕 위 norm으로 bounded하지도 않다.

작은 transformed value가 생긴다면 그것은 absolute operator contraction이 아니라 signed arithmetic cancellation에서 나와야 하며, 바로 그 부분이 원래 난점이다.

---

## 9. 선행문헌과의 위치

summatory Dirichlet convolution과 floor-quotient expansion은 표준적인 Dirichlet hyperbola / Möbius inversion 계열이다.

또 Mertens function을 divisibility matrices로 나타내는 Redheffer-type 연구가 오래 존재하며, modern work도 Dirichlet convolution과 sparse matrix representation을 직접 사용한다.

따라서 floor-dilation representation 자체의 신규성은 주장하지 않는다.

---

## 10. 닫히는 경로

다음 전체 class를 독립 RH mechanism 후보에서 제외한다.

1. fixed coefficients `a(d)`를 사용하는 linear floor-dilation recurrence 자체.
2. formation-layer recurrence를 별도 dynamical law로 취급하는 해석.
3. `T_1M=1`을 contraction으로 해석하는 경로.
4. zero를 multiplier `A(s)`로 지운 뒤 stable inverse가 그대로 남는다고 가정하는 경로.

---

## 11. 살아 있는 조건

후속 arithmetic operator가 genuinely new하려면 적어도 하나가 필요하다.

- `x`-dependent coefficients로 fixed Dirichlet convolution algebra를 벗어날 것.
- nonlinear coupling을 사용할 것.
- 또는 noninvertible projection 뒤에도 RH-relevant information이 보존된다는 별도 theorem을 가질 것.

다만 nonlinear finite Hankel/determinant family는 별도 audit에서 known-zero spectral re-encoding으로 다시 닫힌다.

## 상태

- floor-dilation/convolution identity: `EXACT`.
- weighted-growth boundedness/invertibility statement: `EXACT`.
- formation recurrence reclassification: `EXACT`.
- fixed linear dilation as independent RH mechanism: `CLOSED_AS_REPRESENTATION_CHANGE`.
- RH: `OPEN`.
