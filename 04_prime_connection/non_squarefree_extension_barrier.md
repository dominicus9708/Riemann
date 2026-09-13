# Non-Squarefree Extension Barrier

## 목적

Möbius 함수가 0으로 버리는 repeated prime-channel states를 formation analysis에 다시 포함하면 RH 난점이 단순해지는지 감사한다.

핵심 질문:

> squarefree boundary 밖의 exponent/fiber 정보가 `1/zeta(s)` 난점을 제거하거나 더 강한 finite-x constraint를 주는가?

---

## 1. radical fiber

각 정수는

\[
r=\operatorname{rad}(n)=\prod_{p\mid n}p
\]

라는 squarefree radical을 가진다.

같은 `r`를 공유하는 정수들은 동일한 활성 prime-channel set을 가지며 exponent vector만 다르다.

Möbius는 이 fiber에서 base point `n=r`에만

\[
\mu(r)=(-1)^{\omega(r)}
\]

를 주고 repeated exponent state에는 0을 준다.

---

## 2. 가장 자연스러운 repeated-channel sign extension

반복지수를 무시하고 활성채널 parity만 유지하면

\[
\mu^*(n)=(-1)^{\omega(n)}
\]

을 얻는다.

이는 고전적으로 **unitary Möbius function**이다.

Euler factor는

\[
1+\sum_{e\ge1}\frac{-1}{p^{es}}
=
\frac{1-2p^{-s}}{1-p^{-s}}.
\]

따라서

\[
\sum_{n\ge1}\frac{\mu^*(n)}{n^s}
=
\prod_p\frac{1-2p^{-s}}{1-p^{-s}}.
\]

Möbius Euler product

\[
\frac1{\zeta(s)}=\prod_p(1-p^{-s})
\]

를 분리하면

\[
\boxed{
\sum_{n\ge1}\frac{\mu^*(n)}{n^s}
=
\frac{H_*(s)}{\zeta(s)}
}
\]

with

\[
H_*(s)=
\prod_p\frac{1-2p^{-s}}{(1-p^{-s})^2}.
\]

---

## 3. powerful-number correction

local correction을 `x=p^{-s}`로 쓰면

\[
\frac{1-2x}{(1-x)^2}
=1+\sum_{e\ge2}(1-e)x^e.
\]

따라서 `H_*`의 Dirichlet coefficient `h`는 multiplicative이고

\[
h(p)=0,
\qquad
h(p^e)=1-e\quad(e\ge2).
\]

즉 `h(n)`은 어떤 prime exponent가 1이면 0이다.

따라서 support는

\[
\boxed{\text{powerful/squareful integers}}
\]

에만 놓인다.

convolution으로는

\[
\boxed{\mu^*=\mu*h}.
\]

summatory form:

\[
\sum_{n\le x}\mu^*(n)
=
\sum_{q\le x}h(q)
M\!\left(\left\lfloor\frac{x}{q}\right\rfloor\right).
\]

즉 repeated-channel fiber는 Möbius 합을 powerful-supported correction으로 섞을 뿐이다.

---

## 4. multiplicity parity extension도 같은 구조

모든 prime multiplicity를 세어

\[
\lambda(n)=(-1)^{\Omega(n)}
\]

로 연장하면 Liouville function이다.

그 Dirichlet series는

\[
\boxed{
\sum_{n\ge1}\frac{\lambda(n)}{n^s}
=
\frac{\zeta(2s)}{\zeta(s)}
}.
\]

따라서 distinct-channel parity와 multiplicity parity라는 두 가장 자연스러운 full exponent-lattice extension 모두 공통적으로

\[
\boxed{1/\zeta(s)}
\]

를 보존한다.

---

## 5. 일반 multiplicative extension barrier

multiplicative `a(n)`이 모든 prime에서

\[
a(p)=-1
\]

을 유지하고 repeated powers `a(p^e), e>=2`만 새로 정의한다고 하자.

local factor를

\[
A_p(z)=1-z+\sum_{e\ge2}a(p^e)z^e
\]

라고 쓰면

\[
\frac{A_p(z)}{1-z}=1+O(z^2)
\]

이다.

따라서 repeated-power coefficients가 자연스러운 uniform growth bound를 만족하면

\[
\boxed{
A(s)=\sum_n\frac{a(n)}{n^s}
=
\frac{H_a(s)}{\zeta(s)}
}
\]

이며 `H_a`의 Euler factors는

\[
1+O(p^{-2s})
\]

이다.

그래서 `H_a` 쪽 Euler product는 `1/zeta`보다 훨씬 오른쪽 문제가 적고, `Re(s)>1/2`에서 절대수렴하는 자연스러운 범위가 생긴다.

### 감사 해석

반복채널을 multiplicative하게 채워 넣는 것만으로는 zeta inverse의 어려운 인자를 제거하지 못한다.

새 extension에서 RH 정보를 얻은 뒤 다시 Möbius로 돌아오려면 결국

- `1/zeta` pole structure를 제어하거나,
- correction factor의 정교한 cancellation을 증명해야 한다.

따라서 단순 fiber completion은 새 증명경로로 보지 않는다.

---

## 6. ordered word / tree count의 squarefree collapse

Möbius support에서 `n`은 squarefree이고

\[
\omega(n)=k
\]

라고 하자.

모든 prime leaf가 서로 다르므로 formation-word count는

\[
\boxed{|W(n)|=k!}
\]

이다.

unordered binary formation-tree count는 labeled leaves의 rooted non-plane binary tree count이므로

\[
\boxed{|T(n)|=(2k-3)!!}
\]

이다 (`k>=2`).

따라서 squarefree Möbius support에서는 단순 `W-count`, `T-count`가 실제 prime label에 대한 새 정보를 주지 않고 **오직 `k=omega(n)`의 함수로 축약**된다.

이미 분석한 layer counts

\[
A_k(x)
\]

를 다시 가중하는 것에 해당한다.

`mu(n)`에 `omega(n)`의 polynomial/falling-factorial weight를 곱한 경우는 이전 derivative hierarchy

\[
\partial_z^m F(s,z)|_{z=-1}
\]

로 환원되고 모든 층이 `1/zeta(s)`를 공통인자로 갖는다.

---

## 7. 닫히는 가지

다음은 독립 RH 후보에서 닫는다.

1. `mu=0`인 repeated-channel states에 단순 distinct-parity sign을 부여.
2. multiplicity parity `(-1)^Omega` 사용.
3. prime-power별 multiplicative extension만 변경.
4. squarefree 상태에서 `|W|`, `|T|` 같은 count만 추가.

이들은 모두 기존 `1/zeta` 구조를 보존하거나 `omega` layer weighting으로 축약된다.

---

## 8. 아직 남는 정보

살아남으려면 descriptor가 최소한 다음 중 하나를 포함해야 한다.

- 실제 prime label/value에 의존하는 ordered path geometry,
- 서로 다른 prime channels 사이의 비대칭 relation,
- multiplicative local factorization으로 분리되지 않는 global coupling,
- squarefree `omega` 하나로 환원되지 않는 canonical path statistic.

단, 인위적인 prime ordering이나 phase를 넣으면 사전정의 문제가 다시 생긴다.

따라서 다음 단계에서는 **prime labels를 사용하되 선택 없이 canonical하게 정의되는 구조**만 검사한다.
