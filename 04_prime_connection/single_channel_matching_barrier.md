# Single-Channel Sign-Reversing Matching Barrier

## 목적

Möbius cancellation을 가장 단순한 조합적 방식으로 설명할 수 있는지 검사한다.

squarefree formation state를 prime subset `S`로 보고, 부호는

\[
(-1)^{|S|}.
\]

따라서 prime-channel 하나를 켜거나 끄는 edge

\[
S\leftrightarrow S\triangle\{p\}
\]

로 짝을 지으면 부호가 반드시 반전된다.

만약 거의 모든 state를 이런 edge로 pair할 수 있고 unmatched state가 `O(x^{1/2+epsilon})`라면 RH형 cancellation을 매우 직접적으로 설명할 수 있다.

---

## 1. cover graph

정점은

\[
\Delta_x=\{S:\prod_{p\in S}p\le x\}
\]

의 모든 face이고, edge는 정확히 prime 하나를 추가/삭제하여 두 face를 연결할 때 둔다.

짝수 크기 face와 홀수 크기 face 사이의 bipartite graph가 된다.

그 maximum matching을 작은 범위에서 직접 계산했다.

| x | even | odd | max matching | unmatched | |M(x)| |
|---:|---:|---:|---:|---:|---:|
| 100 | 31 | 30 | 20 | 21 | 1 |
| 500 | 150 | 156 | 112 | 82 | 6 |
| 1,000 | 305 | 303 | 221 | 166 | 2 |
| 5,000 | 1,522 | 1,520 | 1,099 | 844 | 2 |
| 10,000 | 3,030 | 3,053 | 2,198 | 1,687 | 23 |
| 20,000 | 6,093 | 6,067 | 4,422 | 3,316 | 26 |
| 50,000 | 15,212 | 15,189 | 11,040 | 8,321 | 23 |

실제 parity 차이 `|M(x)|`는 매우 작지만 cover-edge matching으로는 약 `0.16x` 수준의 정점이 남는다.

따라서 국소 channel-toggle matching은 실제 Möbius cancellation을 거의 설명하지 못한다.

---

## 2. 큰 소수에 의한 엄밀한 병목

이 수치현상에는 간단한 구조적 이유가 있다.

\[
\frac{x}{2}<p\le x
\]

인 소수 `p`를 생각하자.

해당 singleton state `{p}`는 product가 `p<=x`이므로 complex 안에 있다.

하지만 prime 하나를 추가하면 최소한

\[
2p>x
\]

이므로 어떤 상위 cover face도 존재하지 않는다.

아래 cover face는 공집합 하나뿐이다.

따라서 구간 `(x/2,x]`의 모든 prime singleton은 **같은 정점 `emptyset` 하나와만 연결**된다.

그 수를

\[
L(x)=\pi(x)-\pi(x/2)
\]

라고 하면, matching에서는 이들 가운데 많아야 하나만 emptyset과 pair할 수 있다.

따라서 모든 single-channel sign-reversing matching은 적어도

\[
\boxed{L(x)-1}
\]

개의 unmatched odd state를 남긴다.

소수정리에 의해

\[
L(x)\sim\frac{x}{2\log x}.
\]

그러므로 이 방식의 unmatched 수는 적어도 `x/log x` 규모이다.

이는 RH-equivalent target인

\[
x^{1/2+\varepsilon}
\]

보다, 예를 들어 어떤 고정 `0<epsilon<1/2`에 대해서도 충분히 큰 `x`에서 훨씬 크다.

### 결론

\[
\boxed{
\text{한 prime channel씩 켜고 끄는 local sign-reversing involution은 RH bound를 증명할 수 없다.}
}
\]

이것은 단순히 현재 greedy algorithm이 나빴다는 문제가 아니라 cover graph 자체의 Hall-type 병목이다.

---

## 3. sieve parity barrier와의 관계

이 실패는 고전적인 **parity problem in sieve theory**와 정성적으로 같은 경고를 준다.

local small-prime divisibility 정보를 이용하는 sieve는 소인수 개수의 짝/홀을 정밀하게 분리하는 데 본질적인 어려움이 있다.

현재 formation language에서는 그 장벽이 다음처럼 보인다.

- local prime-channel incidence는 잘 기술된다.
- 그러나 Möbius sign은 전체 활성채널 수의 parity이다.
- local cover matching은 large-prime singleton 때문에 선형에 가까운 unmatched mass를 남긴다.
- 따라서 RH 수준 cancellation에는 단순 local toggling을 넘어서는 global relation이 필요하다.

---

## 4. 어떤 matching이 남는가

한 채널 adjacency를 버리고 임의의 even state와 odd state를 pair하면, 더 작은 쪽을 전부 pair하고 정확히 `|M(x)|`개만 남길 수 있다.

그러나 이것은

\[
|E(x)-O(x)|=|M(x)|
\]

를 그대로 사용한 tautological matching일 뿐이다.

따라서 의미 있는 global correspondence는 다음을 동시에 만족해야 한다.

1. `M(x)` 또는 parity imbalance의 크기를 사전에 사용하지 않는다.
2. pairing rule이 prime/formation data에서 독립적으로 정의된다.
3. opposite parity를 보장한다.
4. exceptional/unmatched states의 수를 직접 `O_epsilon(x^(1/2+epsilon))`로 증명할 수 있다.

이 조건을 만족하는 global correspondence가 발견된다면 실제로 비순환적인 조합적 RH 경로가 될 수 있다.

---

## 5. 현재 판정

### 닫힌 단순경로

\[
\boxed{
\text{single-prime toggle}
\to
\text{local sign-reversing matching}
}
\]

은 구조적 병목 때문에 닫는다.

### 남은 경로

- 여러 channel을 동시에 재배열하는 global formation correspondence,
- product threshold를 가로질러 층들을 묶는 nonlocal relation,
- ordered/hierarchical formation data에서 자연스럽게 정의되는 parity-reversing operator.

단, 마지막 항목에서 인위적으로 순서나 위상을 넣어 cancellation을 설계하면 사전정의 문제가 다시 생기므로 계속 감사한다.
