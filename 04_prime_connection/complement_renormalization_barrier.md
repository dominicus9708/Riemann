# Complement Renormalization Barrier

## 목적

`primorial_complement_duality_audit.md`의 exact scale reflection

\[
F_m^{\le}(X)=(-1)^{m+1}F_m^<(P_m/X)
\]

을 반복 사용하면 final Mertens state를 작은 scale로 renormalize할 수 있는지 감사한다.

결론은 다음과 같다.

> complement reflection은 finite state에 exact하지만, final Mertens state는 complement center에서 asymptotically 극단적으로 멀리 놓인다. reflection을 contraction으로 쓰기 전에 거의 모든 large-prime channel을 제거해야 하며, 그 제거 과정이 바로 기존 Möbius/Vaughan/Heath--Brown/Buchstab-type decomposition의 난점을 다시 담는다.

---

## 1. exact activation recursion

\[
F_m(X)=\sum_{\substack{d\mid P_m\\d\le X}}\mu(d)
\]

에 대해

\[
\boxed{
F_m(X)
=F_{m-1}(X)-F_{m-1}(\lfloor X/p_m\rfloor).
}
\]

이는 `p_m` channel을 사용하지 않는 상태와 사용하는 상태를 분리한 exact recursion이다.

complement shortcut은 integer cutoff에서

\[
\boxed{
F_m(X)
=(-1)^{m+1}
F_m\!\left(\left\lfloor\frac{P_m-1}{X}\right\rfloor\right)
}
\]

으로 쓸 수 있다.

이 shortcut이 cutoff를 실제로 줄이는 조건은

\[
\frac{P_m}{X}<X,
\]

즉

\[
\boxed{P_m<X^2.}
\]

이다.

---

## 2. final Mertens state에서는 complement가 contraction이 아니다

최종 Mertens state는

\[
M(X)=F_{\pi(X)}(X).
\]

여기서

\[
\log P_{\pi(X)}
=\vartheta(X)
=\sum_{p\le X}\log p.
\]

prime number theorem에 의해

\[
\vartheta(X)\sim X.
\]

따라서

\[
P_{\pi(X)}
=\exp((1+o(1))X),
\]

반면

\[
X^2=\exp(2\log X).
\]

그러므로 충분히 큰 `X`에서

\[
\boxed{P_{\pi(X)}\gg X^2.}
\]

즉 final state에서 complement는

\[
X\mapsto P_{\pi(X)}/X
\]

로 cutoff를 엄청나게 **증가**시킨다.

---

## 3. normalized complement coordinate는 0으로 간다

finite Boolean complement coordinate를

\[
u_X=
\frac{\log X}{\log P_{\pi(X)}}
=
\frac{\log X}{\vartheta(X)}
\]

라고 두면

\[
\boxed{
u_X\sim\frac{\log X}{X}\to0.}
\]

따라서 final Mertens state는 complement center

\[
u=1/2
\]

에 접근하는 것이 아니라 그 반대편 extreme tail

\[
u=0
\]

으로 접근한다.

### dyadic data

`X=2^10,...,2^24`에서 직접 계산:

- `X=2^10`: `u≈7.04e-3`
- `X=2^20`: `u≈1.32e-5`
- `X=2^24`: `u≈9.92e-7`

자료:

```text
data/formation/primorial_final_state_complement_distance_2pow10_24.csv
```

---

## 4. contraction regime에 들어가려면 prime index를 어디까지 줄여야 하는가

complement가 cutoff를 줄이려면

\[
\log P_m<2\log X.
\]

Chebyshev theta notation으로

\[
\vartheta(p_m)<2\log X.
\]

PNT scale에서

\[
p_m\approx2\log X.
\]

즉 final index

\[
m=\pi(X)
\]

에서 대략

\[
m\approx\pi(2\log X)
\]

까지 prime channels를 먼저 제거해야 한다.

`X=2^24`에서는

\[
\pi(X)=1,077,871,
\]

반면 contraction threshold는 첫 `12`개 prime, 마지막 prime `37` 부근에 불과하다.

즉 naive recursion 기준으로 약

\[
1,077,859
\]

개의 high-prime indices가 그 앞에 놓인다.

이 숫자를 computational lower bound로 해석하지는 않는다. large-prime terms는 grouping할 수 있기 때문이다. 그러나 **complement symmetry alone이 large-prime tail을 제거하지 못한다**는 구조적 장벽은 분명하다.

---

## 5. activation tail을 grouping하면 기존 decomposition으로 돌아간다

exact activation recursion을 prime range에 걸쳐 반복하면

\[
F_m(X)
=F_k(X)
-
\sum_{k<j\le m}
F_{j-1}(\lfloor X/p_j\rfloor)
\]

형태가 된다.

특히 `p_j>sqrt(X)`이면

\[
X/p_j<sqrt(X)<p_j,
\]

이므로 remainder에는 large-prime restriction이 자동으로 사라져 ordinary Mertens values가 나타난다.

이는 이미 `late_stage_compensation_audit.md`의

\[
M(X)
=F_{\sqrt X}(X)
-
\sum_{\sqrt X<p\le X}M(\lfloor X/p\rfloor)
\]

이다.

더 일반적으로 cutoff를 `X^{1/K}`에 두고 여러 단계로 factor variables를 분리하면 multi-linear Möbius decomposition이 생긴다.

Helfgott--Thompson (2023)은 Mertens summation algorithm에서 Möbius용 Heath--Brown identity

\[
\mu(n)
=
-
\sum_{1\le k\le K}
(-1)^k\binom Kk
\sum_{\substack{m_1\cdots m_k n_1\cdots n_{k-1}=n\\m_i\le u}}
\mu(m_1)\cdots\mu(m_k),
\qquad u\ge n^{1/K},
\]

를 직접 사용한다.

따라서 complement-renormalization tree를 prime activation recursion과 결합해 펼치는 방향은 기존 Vaughan/Heath--Brown/hyperbola decomposition과 강하게 겹친다.

---

## 6. first-crossing renormalization이 왜 쉬웠는가

first primorial crossing

\[
P_{m-1}\le X<P_m
\]

에서는

\[
P_m/X\le p_m.
\]

따라서 reflected scale 자체가 매우 작고

\[
F_m(X)
=(-1)^{m+1}M(\lceil P_m/X\rceil-1)
\]

로 즉시 환원된다.

하지만 final state에서는

\[
P_{\pi(X)}/X
\]

가 astronomical scale이므로 같은 shortcut이 작동하지 않는다.

즉 first-crossing의 강한 renormalization은 **primorial boundary가 X에 막 처음 닿았기 때문**이고, final Mertens state의 global cancellation을 자동으로 설명하는 구조가 아니다.

---

## 7. 현재 판정

### 닫는 경로

\[
\text{complement reflection 반복}
\to
\text{automatic contraction}
\to RH
\]

은 닫는다.

final state가 reflection center의 반대 extreme에 있기 때문이다.

### 계산적으로 유용할 수 있는 부분

- first-crossing small-scale reduction,
- divisor-subset DP symmetry,
- adaptive exact Mertens computation의 pruning,
- threshold-complex symmetry verification.

그러나 계산 단축과 asymptotic proof는 구별한다.

### 살아 있는 문제

여전히 핵심은 large-prime activation tail을 **절댓값 없이** 제어하는 것이다.

이를 grouping하면 현재 알려진 strongest elementary frameworks인

- Vaughan identity,
- Heath--Brown identity,
- hyperbola/bilinear decompositions,
- Mertens computation algorithms

쪽으로 합류한다.

따라서 새로운 경로가 되려면 이 multilinear tail에 formation structure가 주는 기존 방법과 다른 deterministic cancellation inequality가 필요하다.

---

## 추가 선행문헌

- Harald Andrés Helfgott & Lola Thompson (2023), *Summing μ(n): a faster elementary algorithm*, Research in Number Theory 9:6, DOI 10.1007/s40993-022-00408-8.
  - Möbius용 Heath--Brown identity를 사용하여 elementary Mertens computation을 개선.
  - 본 감사에서 complement/activation tree가 multi-factor decomposition으로 돌아가는지 판별하는 강한 선행기준.
- D. R. Heath-Brown, generalized Vaughan identity 계열.
- Huxley--Watt, *Mertens Sums Requiring Fewer Values of the Möbius Function* 계열.
