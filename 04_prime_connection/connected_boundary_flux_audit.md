# Connected Boundary Flux Audit

## 목적

`gcd_label_visibility_audit.md`에서 exact-intersection kernel이 실제로 보는 prime label이 visible core

\[
V_X(d)=\prod_{p\mid d,\ p\le X/d}p
\]

에 한정됨을 확인했다.

이번 단계에서는 visible label이 경계에서 생성되는 순간의 signed flux를 lower-order 효과와 분리해 본다.

핵심 질문은 다음과 같다.

1. label set의 lower-order 기여를 정확히 제거한 connected interaction을 정의할 수 있는가?
2. `X=p^2e`에서 나타나는 visibility boundary가 새로운 Möbius cancellation을 강제하는가?
3. 여기서 다시 나타나는 `1/2`가 RH의 임계선과 독립적인 일반 기하인지 구별할 수 있는가?

---

## 1. connected label difference

유한 prime-label set `A`에 대해

\[
P_A=\prod_{p\in A}p
\]

라 두고

\[
F_Y(A)
=
\sum_{\substack{a,b\le Y\\(a,b)=1\\(ab,P_A)=1}}
\mu(a)\mu(b)
\]

를 정의한다.

이것은 labels `A`를 residual pair에서 금지한 exact kernel이다.

Boolean lattice에서 full difference를

\[
\boxed{
\kappa_Y(A)
=
\sum_{B\subseteq A}(-1)^{|A|-|B|}F_Y(B)
}
\]

로 둔다.

indicator를 전개하면

\[
\boxed{
\kappa_Y(A)
=(-1)^{|A|}
\sum_{\substack{a,b\le Y\\(a,b)=1\\P_A\mid ab}}
\mu(a)\mu(b)
}
\]

이다.

따라서 `kappa`는 lower-order label mask를 정확히 소거하고, `A`의 모든 label이 실제로 `ab`에 등장하는 pair만 남긴다.

상태: `EXACT`.

---

## 2. mandatory-label factorization

`(a,b)=1`이고 `P_A|ab`이면 각 `p in A`는 정확히 한쪽에만 들어간다.

`B subset A`를 `a` 쪽에 들어간 mandatory labels라 하고

\[
P_B=\prod_{p\in B}p,
\qquad
P_{A\setminus B}=\prod_{p\in A\setminus B}p
\]

라 두면

\[
a=P_Bu,
\qquad
b=P_{A\setminus B}v,
\]

이며

\[
(u,v)=1,
\qquad
(uv,P_A)=1.
\]

mandatory prime들의 Möbius sign은

\[
\mu(P_B)\mu(P_{A\setminus B})=(-1)^{|A|}
\]

이고 이는 `kappa` 앞의 `(-1)^|A|`와 정확히 소거된다.

따라서

\[
\boxed{
\kappa_Y(A)
=
\sum_{B\subseteq A}
\sum_{\substack{
u\le Y/P_B\\
v\le Y/P_{A\setminus B}\\
(u,v)=1\\
(uv,P_A)=1}}
\mu(u)\mu(v)
}
\]

이다.

### 핵심 판정

`X=p^2e`에서 `mu(X)=0`인 사실은 visibility boundary의 위치를 표시하지만, 그 zero 자체가 flux cancellation을 만들지는 않는다.

mandatory labels의 parity sign은 connected difference 안에서 소거되고, 난점은 다시 더 작은 scale의 restricted Möbius pair sum으로 이동한다.

즉

\[
\boxed{
\text{raw connected boundary flux는 새로운 독립 cancellation law가 아니라 lower-scale Möbius kernel의 재배열이다.}
}
\]

---

## 3. connected support threshold와 generic 1/2

모든 label이 `ab`에 등장하려면 어떤 partition `B subset A`에 대해

\[
P_B\le Y,
\qquad
P_{A\setminus B}\le Y
\]

이어야 한다.

따라서 connected term이 기하적으로 처음 가능해지는 scale은

\[
\boxed{
Y_*(A)
=
\min_{B\subseteq A}
\max(P_B,P_{A\setminus B})
}
\]

이다.

`L=log P_A`라 하면

\[
\max(P_B,P_A/P_B)
=
\exp\left(
\frac L2+
\left|\log P_B-\frac L2\right|
\right),
\]

따라서

\[
\boxed{
\log Y_*(A)
=
\frac12\log P_A
+
\delta_A,
\qquad
\delta_A
=
\min_{B\subseteq A}
\left|\log P_B-\frac12\log P_A\right|
}
\]

이다.

즉 여기서 나타나는 `1/2`는 두 multiplicative bins를 가능한 한 균형 있게 나누는 partition geometry에서 자동으로 나온다.

이는 이전 primorial complement midpoint의 `1/2`와 같은 종류의 generic balance symmetry이며, nontrivial zero의 real part가 `1/2`임을 뜻하지 않는다.

### 판정

- `1/2` at connected support balance: `EXACT / GENERIC_GEOMETRY`.
- RH critical line evidence로 사용: `EXCLUDED`.

---

## 4. singleton boundary

`A={p}`이면 geometric boundary는 `Y=p`이다.

factorization 식에서

\[
\boxed{
\kappa_p(p)
=
2\sum_{\substack{n\le p\\(n,p)=1}}\mu(n)
=2(M(p)+1)
}
\]

이다.

따라서 singleton boundary flux는 정확히 Mertens prefix의 재표현이다.

`X=dY`이고 `d=p`이면 이 boundary는 원래 변수에서 `X=p^2`에 놓인다.

그러나 `mu(p^2)=0`이 cancellation을 제공하는 것이 아니라, boundary flux 자체가 `M(p)`를 다시 담는다.

---

## 5. two-label onset

`A={p,q}`, `p<q`이면

\[
Y_*(A)=q.
\]

`Y=q`에서는 `pq>q`이므로 두 mandatory labels는 서로 다른 쪽에만 놓일 수 있다.

따라서

\[
\boxed{
\kappa_{\{p,q\}}(q)
=
2\sum_{\substack{n\le q/p\\(n,pq)=1}}\mu(n)
}
\]

이다.

`q<p^2`이면 `q/p<p`이고 `q/p<q`이므로 coprimality restriction이 자동이 되어

\[
\boxed{
q<p^2
\Longrightarrow
\kappa_{\{p,q\}}(q)
=2M(\lfloor q/p\rfloor)
}
\]

이다.

즉 넓은 pair regime에서는 actual labels `p,q` 자체보다 quotient `floor(q/p)`만 남는다.

`q\ge p^2`이면

\[
M_p(t)=\sum_{\substack{n\le t\\(n,p)=1}}\mu(n)
\]

로 두어

\[
\kappa_{\{p,q\}}(q)=2M_p(\lfloor q/p\rfloor).
\]

또

\[
M_p(t)=M(t)+M_p(\lfloor t/p\rfloor)
\]

이므로 유한 반복으로

\[
\boxed{
M_p(t)
=
\sum_{j\ge0}M(\lfloor t/p^j\rfloor)
}
\]

을 얻는다.

따라서 two-label onset도 ordinary Mertens sums의 decreasing-scale recursion으로 닫힌다.

---

## 6. Dirichlet-series circularity audit

고정 squarefree `Q`에 대해 restricted Möbius coefficients의 Dirichlet series는 초기영역 `Re(s)>1`에서

\[
\boxed{
\sum_{(n,Q)=1}\frac{\mu(n)}{n^s}
=
\frac1{\zeta(s)}
\prod_{p\mid Q}(1-p^{-s})^{-1}
}
\]

이다.

finite Euler factors를 제외하면 analytic difficulty는 그대로 `1/zeta(s)`에 있다.

따라서 connected boundary flux를 restricted Möbius sums로 바꾼 뒤 그 합에 RH-scale bound를 직접 요구하면, 핵심 난점을 제거한 것이 아니라 다시 같은 zero-free / cancellation 문제를 요구하게 된다.

상태: `EXACT_BARRIER`.

---

## 7. singleton gap-permutation null audit

actual prime system과 기존 gap-permutation pseudo-generator system에서 singleton onset flux를 동일한 abstract channel 규칙으로 계산했다.

각 generator `g`의 onset에서

\[
B_g=2\,\mathcal M_g(g),
\]

여기서 `M_g(g)`는 channel `g`를 제외한 signed subset-prefix이다.

actual primes에서는 정확히 `B_p=2(M(p)+1)`이다.

설정:

- maximum generator: `2^18 = 262144`.
- `g<=100` freeze.
- dyadic prime-gap multiset 보존, gap order만 shuffle.
- null samples: `20`.
- movable channels compared: `22975`.

결과:

- actual maximum individual `|z| = 4.4754113728`.
- leave-one-out null maximum이 이를 넘는 비율: `7/20 = 0.35`.
- actual mean `z^2 = 1.3434903108`.
- leave-one-out null mean-`z^2` exceed fraction: `7/20 = 0.35`.
- dyadic-band `B_g/sqrt(g)` RMS에서 actual maximum band deviation: `1.7107626897 sigma`.
- leave-one-out null band maximum이 이를 넘는 비율: `15/20 = 0.75`.

개별 큰 z-score는 존재하지만 인접 generator에서 강하게 군집하고, global / band statistic 모두 gap-null ensemble 밖으로 나오지 않는다.

### 판정

\[
\boxed{
\text{singleton visibility-boundary flux는 현재 범위에서 prime-specific signal이 아니다.}
}
\]

이는 exact identity가 이미 `M(p)` 재표현임을 보여주는 대수 감사와도 일치한다.

---

## 8. sieve/parity 문헌과의 교차감사

이 구조는 prime divisibility masks에 Boolean inclusion-exclusion을 반복하는 형태이므로 고전 sieve의 parity obstruction과 직접 비교해야 한다.

- Terence Tao, *Open question: The parity problem in sieve theory* (2007): divisor-sum / Möbius-type sieve information만으로 odd/even prime-factor parity를 구별하기 어려운 표준 barrier를 정리한다.
- D. R. Heath-Brown, *A parity problem from sieve theory*, Mathematika 29 (1982), 1–6, DOI `10.1112/S0025579300012109`.
- M. Huxley & N. Watt, *Mertens sums requiring fewer values of the Möbius function*, Chebyshevskii Sbornik 19(3) (2018), 20–34: `M(N^d)`를 lower-scale Möbius products / bilinear forms로 재표현하는 identity 계열을 연구한다.

현재 connected-flux identity가 이 문헌들의 특정 정리와 동일하다고 주장하지 않는다.

다만 **higher-order divisibility inclusion-exclusion을 lower-scale Möbius bilinear sums로 바꾸는 것 자체는 이미 잘 알려진 sieve / Mertens decomposition 세계와 같은 방향**이므로, 새 RH mechanism을 주장하려면 이 재표현을 넘어서는 추가 구조가 필요하다.

---

## 9. 닫히는 경로와 남는 경로

### 닫음

1. `mu(p^2 e)=0` 자체가 visibility-boundary cancellation을 강제한다는 해석.
2. raw Boolean connected difference만으로 새로운 Möbius cancellation law를 얻는 경로.
3. connected-support threshold의 log-half `1/2`를 RH critical line의 독립 증거로 사용하는 경로.
4. singleton boundary flux를 새 observable로 간주하는 경로: exact `M(p)` re-encoding.
5. two-label onset flux를 새 observable로 간주하는 경로: quotient / restricted Mertens recursion으로 환원.

### 유지

새 후보는 restricted-Mertens recursion을 먼저 subtract한 뒤에도 남는 구조여야 한다.

구체적으로는

- cross-scale transport between the same visible label,
- phase/orientation information not expressible by divisibility masks alone,
- a residual operator whose Dirichlet series is not merely `1/zeta(s)` times finite Euler factors,
- or a deterministic inequality that beats the gap-null while not assuming Mertens square-root cancellation.

다음 우선순위는 **cross-scale connected residual**이다.

---

## 상태

- connected Boolean difference identity: `EXACT`.
- mandatory-label factorization: `EXACT`.
- balanced support threshold / half-log formula: `EXACT`.
- singleton / pair onset reduction to Mertens: `EXACT`.
- singleton gap-null comparison through `2^18`: `NUMERICAL`.
- independent RH progress from raw boundary flux: `CLOSED_AS_REENCODING`.
- RH: `OPEN`.
