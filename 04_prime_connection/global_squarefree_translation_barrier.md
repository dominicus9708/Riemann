# Global Squarefree Translation Barrier

## 목적

single-prime toggle barrier를 우회하기 위해, 여러 prime channels를 동시에 토글하는 **global translation**을 검사한다.

squarefree integers의 자연스러운 group operation을 사용한다.

---

## 1. squarefree group

squarefree `a,b`에 대해

\[
a\star b
=\frac{\operatorname{lcm}(a,b)}{\gcd(a,b)}
\]

라고 둔다.

prime-subset representation에서는 이것이 정확히 symmetric difference이다.

따라서 모든 squarefree integers는 이 연산 아래 elementary abelian 2-group을 이루며, Möbius sign은 character이다.

\[
\boxed{\mu(a\star b)=\mu(a)\mu(b)}.
\]

이 group/character 관점 자체는 Hilberdink 등의 기존 연구에 존재하므로 새 구조로 주장하지 않는다.

---

## 2. global parity-reversing translation

절단집합을

\[
S_x=\{n\le x:\mu(n)^2=1\}
\]

이라고 하자.

`g`가 squarefree이고

\[
\mu(g)=-1
\]

이면 translation

\[
T_g(n)=n\star g
\]

은 모든 상태의 Möbius sign을 반전한다.

따라서

\[
\sum_{n\in T_g(S_x)}\mu(n)
=-M(x).
\]

두 집합의 차를 취하면

\[
2M(x)
=
\sum_{n\in S_x}\mu(n)
-
\sum_{n\in T_g(S_x)}\mu(n),
\]

따라서

\[
\boxed{
|M(x)|
\le
\frac12|S_x\triangle T_g(S_x)|
}.
\]

즉 RH형 combinatorial proof를 위해서는 odd-parity `g`를 선택해 translation boundary를 `O_epsilon(x^(1/2+epsilon))`로 만들 수 있어야 한다.

---

## 3. large-prime obstruction

임의의 nontrivial squarefree `g>=2`를 고정한다.

\[
\frac{x}{2}<p\le x
\]

인 prime `p`를 보자.

`p`가 `g`를 나누지 않으면

\[
\gcd(p,g)=1
\]

이므로

\[
T_g(p)=pg.
\]

`g>=2`이므로

\[
pg>x.
\]

따라서 그런 singleton `p`는 반드시

\[
p\in S_x\setminus T_g(S_x)
\]

쪽의 boundary state가 된다.

이 구간의 prime 중 `g`를 나누는 것은 많아야 `omega(g)`개이다.

따라서

\[
\boxed{
|S_x\setminus T_g(S_x)|
\ge
\pi(x)-\pi(x/2)-\omega(g)
}.
\]

translation은 bijection이므로 두 집합 크기는 같고

\[
|S_x\triangle T_g(S_x)|
=2|S_x\setminus T_g(S_x)|.
\]

결국

\[
\boxed{
\frac12|S_x\triangle T_g(S_x)|
\ge
\pi(x)-\pi(x/2)-\omega(g)
}.
\]

소수정리에 의해

\[
\pi(x)-\pi(x/2)
\sim\frac{x}{2\log x}.
\]

또 `g`가 `x`에 의존하더라도 `g`의 서로 다른 prime factor 수는 `omega(g)=O(log g)` 수준이므로 large-prime mass를 제거할 수 없다.

따라서

\[
\boxed{
\text{any single global odd-parity squarefree translation has boundary }\Omega(x/\log x).
}
\]

이는 고정 `0<epsilon<1/2`에 대해 RH-equivalent target `x^(1/2+epsilon)`보다 훨씬 크다.

---

## 4. 수치 감사

`x=200000`에서 odd-parity squarefree `g<1000`을 직접 전수 비교했다.

boundary half

\[
B_g(x)=|S_x|-|S_x\cap T_g(S_x)|
\]

의 최소값은 `g=2`에서 나타났다.

대표 overlap ratio:

| g | omega(g) | overlap / |S_x| |
|---:|---:|---:|
| 2 | 1 | 0.66667 |
| 3 | 1 | 0.49998 |
| 5 | 1 | 0.33326 |
| 30 | 3 | 0.30551 |
| 7 | 1 | 0.25004 |
| 42 | 3 | 0.25004 |
| 70 | 3 | 0.20834 |

여러 채널을 동시에 토글한다고 overlap이 개선되지 않았다.

이 수치는 위 large-prime obstruction의 보조 확인일 뿐이며 증명의 핵심은 구조적 lower bound이다.

---

## 5. fixed-g asymptotic overlap

고정 squarefree `g`에 대해서는 더 세밀하게 계산할 수 있다.

`d=gcd(n,g)`라 쓰면

\[
n=dm,
\qquad
T_g(n)=\frac gd m,
\qquad
(m,g)=1.
\]

두 값이 모두 `<=x`이려면

\[
m\le\frac{x}{\max(d,g/d)}.
\]

따라서 fixed `g`의 asymptotic overlap ratio는

\[
R(g)
=
\prod_{p|g}\frac{p}{p+1}
\sum_{d|g}\frac1{\max(d,g/d)}.
\]

동일하게

\[
R(g)
=
\frac{2}{\prod_{p|g}(p+1)}
\sum_{\substack{d|g\\d<\sqrt g}}d.
\]

예를 들어 `g=2`에서는 `R=2/3`, `g=30`에서는 `R=11/36≈0.30556`이다.

fixed translation은 positive-density boundary를 남긴다.

---

## 6. 판정

### 닫힌 경로

다음 전체 계열을 닫는다.

\[
\boxed{
\text{one fixed squarefree }g
\to
n\mapsto n\star g
\to
\text{global parity reversal}
}
\]

여기에는 single-prime toggle (`g=p`)뿐 아니라 임의의 여러 channel simultaneous toggle도 포함된다.

### 이유

large prime singletons `(x/2,x]`가 항상 `Omega(x/log x)` boundary를 강제한다.

### 남은 가능성

살아남는 것은 **state-dependent global transformation**뿐이다.

즉 각 state `n`에 대해 서로 다른 channel set `g(n)`을 선택하는 correspondence가 필요하다.

그러한 규칙은 다음을 만족해야 한다.

1. `M(x)`의 값이나 even/odd total counts를 사전에 사용하지 않는다.
2. opposite Möbius sign을 보장한다.
3. involution/injection을 직접 증명할 수 있다.
4. large-prime singleton들을 서로 다른 even states로 분산시킨다.
5. unmatched/exceptional set을 독립적으로 `O_epsilon(x^(1/2+epsilon))`로 제한한다.

이 조건을 만족하지 못하면 global pairing은 단순 tautological matching으로 돌아간다.
