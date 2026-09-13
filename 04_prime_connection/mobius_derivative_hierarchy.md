# Möbius Formation Derivative Hierarchy

## 목적

유한 formation-layer polynomial

\[
G_x(z)=\sum_{n\le x}\mu(n)^2z^{\omega(n)}
=\sum_kA_k(x)z^k
\]

의 Möbius exceptional phase `z=-1` 주변 전체 미분계층을 분석한다.

\[
H_m(x):=G_x^{(m)}(-1).
\]

목표는 이 계층이 `M(x)=H_0(x)`에 대한 새로운 유한-`x` 제약을 주는지, 아니면 `1/zeta`를 다시 표현한 것인지 판정하는 것이다.

---

## 1. 계수 형태

`m>=0`에 대해

\[
\boxed{
H_m(x)=(-1)^m
\sum_{n\le x}\mu(n)(\omega(n))_{\underline m}
}
\]

이다.

여기서

\[
(k)_{\underline m}=k(k-1)\cdots(k-m+1)
\]

은 falling factorial이다.

특히

\[
H_0(x)=M(x),
\qquad
H_1(x)=-\sum_{n\le x}\mu(n)\omega(n).
\]

---

## 2. 정확한 유한-x 재귀

이전 layer-polynomial identity

\[
G_x'(z)
=
\sum_p\sum_{r\ge1}(-z)^{r-1}
G_{\lfloor x/p^r\rfloor}(z)
\]

을 `m`번 미분하고 `z=-1`을 대입하면

\[
\boxed{
H_{m+1}(x)
=
\sum_{p^r\le x}
\sum_{a=0}^{\min(m,r-1)}
\binom ma(-1)^a(r-1)_{\underline a}
H_{m-a}\!\left(\left\lfloor\frac{x}{p^r}\right\rfloor\right)
}
\]

을 얻는다.

`x=100,1000,10000`에서 존재하는 미분차수 `1..5`를 직접 비교했으며 전부 정확히 일치했다.

따라서 formation layers에는 random-sign model에는 없는 결정론적 scale-coupling hierarchy가 실제로 존재한다.

---

## 3. dyadic 계산

`x=2^24`에서

\[
\begin{aligned}
H_0&=211,\\
H_1&=-76,387,\\
H_2&=-440,864,\\
H_3&=-715,698,\\
H_4&=4,271,592,\\
H_5&=22,665,480,\\
H_6&=33,531,840,\\
H_7&=12,358,080,\\
H_8&=241,920.
\end{aligned}
\]

전 자료는

```text
data/formation/mobius_derivative_hierarchy_dyadic_24.csv
```

에 기록한다.

`H_0`만 비정상적으로 작은 값이고 higher derivatives는 빠르게 커진다. 따라서 `z=-1`에서 작은 함수값이 넓은 flat minimum 때문에 생기는 것은 아니다.

---

## 4. Dirichlet 생성함수로 본 순환성

무한 generating family를

\[
F(s,z)
=
\sum_{n\ge1}\frac{\mu(n)^2z^{\omega(n)}}{n^s}
=
\prod_p(1+zp^{-s})
\]

라고 하자.

`z=-1`에서

\[
F(s,-1)=\frac1{\zeta(s)}.
\]

`m`차 미분에서는 product rule에 의해 서로 다른 `m`개 prime factor를 선택한다. 따라서 수렴이 정당한 영역에서

\[
\boxed{
\frac{\partial^mF}{\partial z^m}(s,-1)
=
\frac{m!}{\zeta(s)}
\,e_m\!\left(
\frac1{p^s-1}:p\in\mathbb P
\right)
}
\]

이다.

`e_m`은 elementary symmetric polynomial이다.

즉 모든 derivative layer의 Dirichlet series는 공통인자

\[
\boxed{1/\zeta(s)}
\]

를 그대로 보존한다.

### 판정

이 hierarchy를 해석적 Dirichlet series 수준에서만 이용하여 zeta zero의 위치를 제한한다면, 원래 RH 난점을 다른 가중치로 다시 표현하는 순환일 가능성이 높다.

독립 경로가 되려면 **유한 `x` 재귀 자체**에서 zeta-zero 정보를 사용하지 않고 새로운 inequality/contraction을 얻어야 한다.

---

## 5. 단순 contraction 시도의 실패

첫 재귀는

\[
H_1(x)=\sum_{p^r\le x}M(\lfloor x/p^r\rfloor).
\]

가정적으로

\[
|M(y)|\le Cy^\alpha
\]

를 각 항에 독립적으로 적용하고 triangle inequality를 쓰면

\[
|H_1(x)|
\le
Cx^\alpha
\sum_{p^r\le x}p^{-r\alpha}.
\]

RH 목표의 핵심 경계 `alpha≈1/2`에서는 이미 `r=1` 항만으로

\[
\sum_{p\le x}p^{-1/2}
\]

가 커져 수축계수가 되지 않는다.

소수정리 수준의 크기 추정으로

\[
\sum_{p\le x}p^{-1/2}
\asymp
\frac{2\sqrt{x}}{\log x}
\]

이므로 우변은 대략 `x/log x` 규모까지 커질 수 있다.

따라서 **부호/상관을 버린 절댓값 재귀는 square-root barrier를 닫지 못한다.**

결국 필요한 것은 다시

\[
M(x/p)
\]

들 사이의 signed cancellation이며, 이것이 원래의 난점과 실질적으로 같은 종류인지 감사해야 한다.

---

## 6. 현재 판정

### 양성

- formation layers 사이에 정확한 유한-`x` scale-coupling hierarchy가 존재한다.
- 이 구조는 임의 random-sign control에는 없다.
- `H_m` 전체는 계산/검증 가능한 명확한 객체이다.

### 음성

- 무한 Dirichlet series로 보내면 모든 층이 `1/zeta(s)`를 공통인자로 가진다.
- 단순 절댓값/삼각부등식으로는 `1/2` 수준 contraction이 생기지 않는다.
- 따라서 현재 형태만으로는 RH 난점을 단순화했다고 말할 수 없다.

### 다음 조건

다음 단계에서 살아남을 후보는 다음 중 하나뿐이다.

1. `M(x/p)`들 사이의 결정론적 부호상관을 직접 제어하는 유한-`x` 정리,
2. 한 prime-channel toggle이 아닌 global sign-reversing correspondence,
3. topology와 `A_k` count가 버리는 ordered/hierarchical formation information에서 생기는 독립 제약.

그 어느 것도 확인되지 않으면 derivative-hierarchy 가지도 기존 Möbius/`1/zeta` 구조의 재표현으로 닫는다.
