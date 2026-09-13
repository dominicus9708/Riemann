# Three-Channel Matching: Topological Audit

## 목적

이전 실험에서 squarefree formation states를 parity에 따라 나누고

\[
|S\triangle T|\le3,
\qquad
||S|-|T||=1
\]

인 상태들을 greedy/max matching으로 pairing했을 때 작은 범위에서 정확히 `|M(X)|`개만 unmatched로 남는 현상이 관찰되었다.

이번 감사는 이 pairing을 discrete Morse / topological cancellation로 해석할 수 있는지 검증한다.

---

## 1. 정수 복합체

\[
\Delta_X
=
\{S\subset\mathbb P:\prod_{p\in S}p\le X\}
\]

는 squarefree integers `<=X`의 divisibility simplicial complex이다.

Björner는 이 complex가 shifted complex임을 보였고, reduced Euler characteristic은

\[
\widetilde\chi(\Delta_X)=-M(X)
\]

이다.

---

## 2. Betti 수의 정확한 식

Björner의 Theorem 3.1에 의해

\[
\boxed{
\beta_k(\Delta_X)
=
\sigma_{k+1}^{\mathrm{odd}}(X)
-
\sigma_{k+1}^{\mathrm{odd}}(X/2)
}
\]

이다.

즉 `k`차 homology rank는 정확히

- odd squarefree,
- `k+1`개의 prime factor,
- interval `(X/2,X]`

에 놓인 정수의 개수다.

따라서 homology 자체가 sparse한 `|M(X)|` 수준으로 collapse하지 않는다.

Björner는 전체 Betti 수에 대해

\[
\sum_k\beta_k(\Delta_X)
=
\frac{2X}{\pi^2}+O(X^\theta)
\]

형태의 선형 main term도 얻는다.

---

## 3. single-channel Morse matching과의 일치

Hasse diagram의 합법적인 simplicial cover move는 prime 하나를 추가/삭제하는

\[
S\leftrightarrow S\cup\{p\}
\]

이다.

따라서 discrete Morse matching은 본질적으로 single-channel cover edge를 사용해야 한다.

이전 감사에서 `(X/2,X]`의 large-prime singleton 때문에 모든 single-channel matching에 많은 unmatched state가 강제된다는 병목을 발견했다.

Björner의 Betti formula는 이 큰 unmatched/topological mass가 우연이 아니라 실제 homology와 일치함을 보여준다.

---

## 4. 왜 3-channel matching은 다른가

3-channel rule은 예를 들어

\[
\{p\}
\longleftrightarrow
\{q,r\}
\]

처럼 symmetric difference가 3인 상태들을 직접 pair할 수 있다.

그러나 이 두 face는 simplicial Hasse diagram에서 cover relation이 아니다.

즉 중간 cell들을 건너뛴다.

따라서 이 pairing은

- Forman discrete Morse matching이 아니고,
- chain collapse를 정의하지 않으며,
- homology를 보존하는 cancellation이라고 볼 수 없다.

만약 이것이 합법적인 Morse matching이면서 `|M(X)|`개의 critical cells만 남긴다면 Morse inequalities에 의해 total Betti rank도 `<=|M(X)|`이어야 하는데, 실제 total Betti rank는 선형 크기이므로 모순이다.

---

## 5. `X/2` odd residual과의 관계

곱셈 by 2 pairing을 먼저 하면

\[
M(X)
=
\sum_{\substack{X/2<n\le X\\n\ \mathrm{odd}}}\mu(n)
\]

이라는 exact residual을 얻는다.

Björner의 Betti formula도 바로 이 top-half odd squarefree layers를 차수별로 센다.

즉 우리가 독립적으로 발견한 `2-channel elimination residual`은 shifted-complex homology 구조와 정확히 같은 경계를 보고 있었다.

하지만 그 residual 내부에서 3-channel arbitrary pairing으로 parity를 더 지우는 것은 topology가 아니라 단순 cardinality matching이다.

---

## 6. 판정

### 확인

- 3-channel matching은 combinatorial parity pairing으로는 강력하다.
- generic shifted/threshold complexes에서도 잘 작동한다는 이전 null-model 결과와 일치한다.

### 폐쇄 이유

\[
\boxed{
\text{3-channel matching은 homology-preserving discrete Morse cancellation이 아니다.}
}
\]

따라서 `|M(X)|` unmatched를 직접 RH proof mechanism으로 해석하지 않는다.

### 남는 의미

3-channel pairing은 heuristic reorganization / algorithmic cancellation order로는 사용할 수 있다.

그러나 증명경로가 되려면 pairing 자체가 아니라, unmatched count를 독립적으로 bound하는 arithmetic theorem이 필요하다. 그 theorem은 다시 원래 Mertens cancellation 문제와 동등한 난점을 가질 가능성이 높다.
