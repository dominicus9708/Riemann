# Formation Generating Functions

## 목적

복소 재탐색에서 발견된 형성단어 `W(n)`과 형성트리 `T(n)`의 구조를 유한 스펙트럼 수준에 머물지 않고 Dirichlet 생성함수로 정확히 연결한다.

이 문서의 핵심 식은 먼저 **형식적 Dirichlet series의 계수 항등식**으로 사용한다. 실제 복소함수로 합을 취할 때에는 별도로 절대수렴 영역을 확인한다.

---

## 1. Prime zeta 기준층

소수 zeta 함수를

\[
P(s)=\sum_{p\ \mathrm{prime}}p^{-s}
\]

라고 한다.

표준적으로 `Re(s)>1`에서 절대수렴한다. Riemann zeta와는

\[
\log\zeta(s)=\sum_{k\ge1}\frac{P(ks)}{k}
\]

및 Möbius inversion에 의해

\[
P(s)=\sum_{k\ge1}\frac{\mu(k)}{k}\log\zeta(ks)
\]

로 연결된다. 해석적 연속에서는 로그 가지와 `zeta(ks)`의 영점/극에서 생기는 특이성을 별도 감사해야 한다.

---

## 2. 형성단어의 정확한 생성함수

`\widetilde W(n)`을 `n`을 곱하여 만드는 **순서 있는 소수열**의 개수로 정의한다.

예:

\[
12=2\cdot2\cdot3
\]

에 대해

```text
2,2,3
2,3,2
3,2,2
```

이므로

\[
\widetilde W(12)=3.
\]

소수 `p`에서는 한 항짜리 단어 `(p)`를 허용하여

\[
\widetilde W(p)=1,
\qquad
\widetilde W(1)=1
\]

로 둔다.

소인수분해

\[
n=\prod_jp_j^{a_j}
\]

에 대해서는

\[
\widetilde W(n)
=\frac{\Omega(n)!}{\prod_j a_j!}.
\]

이는 기존 실험의 `formation_word_count`와 동일하되, 소수의 한 항짜리 자명 단어를 1로 복구한 함수이다.

### 2.1 재귀식

마지막에 놓이는 소수 하나를 선택하면

\[
\boxed{
\widetilde W(n)
=\sum_{p\mid n}\widetilde W(n/p)
}
\]

이다. 합은 `n`의 서로 다른 소인수 `p`에 대해 취한다.

`2<=n<=1000` 전수검사에서 예외는 0개였다.

### 2.2 Dirichlet 생성함수

길이 `k`인 순서 있는 소수단어의 생성함수는 정확히

\[
P(s)^k
\]

이다.

따라서

\[
\sum_{n\ge1}\frac{\widetilde W(n)}{n^s}
=1+P(s)+P(s)^2+\cdots
\]

이고, 수렴이 정당한 영역에서는

\[
\boxed{
\mathcal W(s)
=\frac{1}{1-P(s)}
}
\]

이다.

현재 저장소의 `W_count`는 소수 자체를 비자명 형성으로 세지 않으므로 composite-only 생성함수는

\[
\boxed{
F_W(s)
=\sum_{n\ \mathrm{composite}}\frac{W(n)}{n^s}
=\sum_{k\ge2}P(s)^k
=\frac{P(s)^2}{1-P(s)}
}
\]

이다.

이 식은 `W_count`가 단순 임의 통계량이 아니라 prime-zeta 구조에 직접 연결됨을 뜻한다.

---

## 3. 형성트리의 정확한 함수방정식

`\widetilde T(n)`을 다음 규칙으로 정의한다.

1. 소수 `p`는 잎 하나짜리 트리이므로 `\widetilde T(p)=1`.
2. 합성수 `n=ab`, `2<=a<=b`에 대해 두 자식 subtree의 좌우교환은 동일시한다.
3. 서로 다른 괄호/계층구조는 다른 트리로 유지한다.

이는 기존 `unordered_factor_trees`의 계수와 같다.

생성함수를

\[
\mathcal T(s)
=\sum_{n\ge2}\frac{\widetilde T(n)}{n^s}
\]

라고 한다.

트리는 정확히

- prime leaf 하나, 또는
- 두 tree의 unordered pair

중 하나이다.

ordered pair의 생성함수는 `T(s)^2`이고, 동일한 subtree 두 개를 고르는 diagonal 보정은 `T(2s)`이다. 따라서 size-2 multiset의 표준 보정으로

\[
\boxed{
\mathcal T(s)
=P(s)
+\frac12\left(
\mathcal T(s)^2+\mathcal T(2s)
\right)
}
\]

을 얻는다.

### 3.1 계수 감사

계수 수준에서는 합성수 `n`에 대해

\[
\widetilde T(n)
=
\sum_{\substack{ab=n\\2\le a<b}}
\widetilde T(a)\widetilde T(b)
+
\mathbf1_{n=m^2}
\frac{\widetilde T(m)(\widetilde T(m)+1)}{2}
\]

로 동일한 내용을 쓸 수 있다.

저장소의 기존 `2<=n<=1000` 트리 전수값과 위 함수방정식의 계수를 비교한 결과:

```text
mismatches = 0
```

이었다.

따라서 복소 `T_count` 분석은 임의적인 트리 수열에 가중치를 준 것이 아니라, `P(s)`에서 출발하는 명시적인 재귀적 Dirichlet 구조를 가진다.

---

## 4. `W`와 `T`의 차이

형성단어는 결합계층을 버리고 소수잎의 순서만 보존한다.

\[
W:\quad (2,3,2)
\]

형성트리는 부분곱의 결합계층까지 보존한다.

\[
T:\quad (2\times(3\times2)),\quad ((2\times3)\times2),\ldots
\]

따라서

\[
\mathcal W(s)=\frac1{1-P(s)}
\]

은 기하급수 형태로 닫히지만,

\[
\mathcal T(s)
=P(s)+\frac12(\mathcal T(s)^2+\mathcal T(2s))
\]

은 scale-doubling `2s`를 포함하는 재귀적 구조가 된다.

이 `s -> 2s` 결합은 이후 복소영역 탐색에서 별도 분석할 가치가 있다.

---

## 5. 기존 연구와의 경계

`W(n)`은 표준적으로 알려진 **ordered prime factorizations**의 개수와 일치한다. OEIS A008480도 이를 `multinomial coefficients in prime factorization order`, `number of distinct permutations of the multiset of prime factors`로 기술한다.

일반적인 `ordered factorization` 문헌은 인수를 반드시 소수로 제한하지 않는 경우가 많고, 그 경우 생성함수는 다른 형태(예: `1/(2-zeta(s))`)가 된다. 따라서 두 대상을 혼동하지 않는다.

`factorisatio numerorum` / multiplicative partition 문헌도 주로 임의의 정수 인수 분해를 다루므로 현재 prime-leaf word/tree와 정확히 같은 객체가 아니다.

형성트리 자체와 유사한 binary factorization tree 개념도 기존에 존재한다. 현 단계에서는 위 `T(s)` 함수방정식의 **신규성은 주장하지 않는다**. 저장소에서는 우선 정의에 대한 정확한 계수 항등식과 재현 가능한 감사결과로만 사용한다.

---

## 6. RH와의 현재 관계

Prime zeta는 Riemann zeta와

\[
P(s)=\sum_{k\ge1}\frac{\mu(k)}{k}\log\zeta(ks)
\]

로 연결되므로 `W`와 `T` 역시 간접적으로 zeta의 영점/극 구조의 영향을 받는다.

그러나 이것만으로

\[
\Re(\rho)=1/2
\]

가 유도되지는 않는다.

오히려 다음을 분리해야 한다.

1. `P(s)`에서 이미 알려진 zeta 정보가 `W,T`로 단순 전파되는 부분.
2. `W,T`의 조합/재귀구조가 추가로 만드는 특이성.
3. 유한 절단이 만드는 가짜 최소점.
4. analytic continuation에서만 정의되는 구조.

이 네 층을 분리한 뒤에만 RH 관련 후보를 평가한다.

---

## 7. 다음 계산

1. `P(s)`의 표준 analytic continuation과 branch/singularity 구조를 기준층으로 고정한다.
2. `F_W(s)=P(s)^2/(1-P(s))`를 직접 계산하여 기존 finite `W_count` 스펙트럼과 `analytic part + cutoff remainder`로 분해한다.
3. `T(s)` 함수방정식을 반복해석하여 안정한 수렴영역을 찾고 finite-tree spectrum과 비교한다.
4. `s -> 2s` 항 때문에 생기는 특이점 전파계보를 추적한다.
5. `sigma=1/2`를 사전 지정하지 않고 전체 `(sigma,t)`에서 특이성 구조를 계산한 뒤 사후 비교한다.

이 단계부터는 단순한 복소 Fourier식 재탐색보다 생성함수 자체의 구조를 분석하는 것이 우선이다.
