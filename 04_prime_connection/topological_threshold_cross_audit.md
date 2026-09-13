# Topological / Threshold Cross-Audit of the Möbius Formation Layers

## 목적

squarefree formation layers

\[
A_k(x)=\#\{n\le x:\mu(n)^2=1,\omega(n)=k\}
\]

을 prime-channel subset으로 해석하면

\[
\Delta_x=
\left\{S\subset\mathbb P:\prod_{p\in S}p\le x\right\}
=
\left\{S:\sum_{p\in S}\log p\le\log x\right\}
\]

라는 아래로 닫힌 simplicial/threshold complex가 된다.

이번 문서는 이 관점이 기존 연구와 얼마나 겹치는지, 그리고 기존 위상적 제약이 실제 Mertens cancellation을 얼마나 강하게 제한하는지 감사한다.

---

## 1. 선행연구와의 정확한 일치

Anders Björner, *A Cell Complex in Number Theory* (Advances in Applied Mathematics 46, 2011)는 정확히

\[
\Delta_n=\{P(k):k\le n,\ k\text{ squarefree}\}
\]

을 연구한다.

이 complex의 reduced Euler characteristic는

\[
\boxed{M(n)=-\widetilde\chi(\Delta_n)}
\]

이며 RH의 Mertens-function growth formulation도 이 언어로 옮겨진다.

Björner는 `Delta_n`가 shifted complex임을 이용해 homotopy/Betti 구조를 계산하고 Kruskal-Katona형 shadow inequalities를 얻는다.

Pakianathan–Winfree의 threshold/quota complex 연구도

\[
\sum_{p\in S}\log p\le\log x
\]

같은 weighted threshold complex를 더 일반적인 틀에서 다룬다.

### 판정

따라서 다음 자체는 새로운 경로가 아니다.

1. squarefree integers를 prime subsets로 보는 것,
2. product cutoff를 `log p` 가중 threshold로 보는 것,
3. Mertens function을 Euler characteristic로 보는 것,
4. 이 complex를 이용해 RH를 위상적으로 재표현하는 것.

이 가지는 **독립 재발견 및 교차검증**으로 보존하되 신규성 주장 대상에서 제외한다.

---

## 2. Betti layer 재현

Björner의 Betti formula를 사용하여 dyadic cutoff를 계산했다.

`x=2^24=16,777,216`에서

\[
(\beta_0,\ldots,\beta_6)
=
(513708,
1252181,
1107615,
442966,
78422,
4848,
39).
\]

총 Betti 수는

\[
\sum_k\beta_k=3,399,779
\]

이고 alternating sum은

\[
\sum_k(-1)^k\beta_k=211=M(2^{24}).
\]

`2^22`, `2^23`에서도 각각

\[
\sum(-1)^k\beta_k=228,-10
\]

으로 직접 Mertens 값과 일치했다.

재현자료:

```text
data/formation/mertens_betti_dyadic_24.csv
```

---

## 3. 위상적 정보도 같은 거대상쇄를 가진다

`x=2^24`에서는 Betti 수 각각이 수만~백만 규모인데 alternating sum은 `211`이다.

즉

\[
\boxed{
\text{face-layer cancellation}
\longrightarrow
\text{Betti-layer cancellation}
}
\]

으로 표현을 바꾸어도 핵심 어려움은 사라지지 않는다.

오일러 특성이라는 표현은 상쇄를 압축해 보여주지만, 작은 Euler characteristic 자체의 원인을 자동으로 설명하지 않는다.

이 점은 Björner가 자신의 위상적 결과가 `M(n)`의 성장률에 새로운 빛을 주기에는 부족하다고 한 평가와 일치한다.

---

## 4. Kruskal–Katona / shadow 제약의 수치 감사

shifted-complex 구조에서 얻는 대표적인 층간 제약의 실질적 강도를 확인하기 위해 Björner의 shadow inequality

\[
\partial_k\!\left(\sigma^{\rm odd}_{k+1}(x)\right)
\le
\sigma^{\rm odd}_{k}(x/2)
\]

의 좌우 비를 계산했다.

`x=2^24`에서 주요 층은:

| k | lower shadow | RHS | LHS/RHS |
|---:|---:|---:|---:|
| 1 | 2,266 | 564,162 | 0.0040 |
| 2 | 27,949 | 1,312,304 | 0.0213 |
| 3 | 51,093 | 1,079,116 | 0.0473 |
| 4 | 26,561 | 385,116 | 0.0690 |
| 5 | 4,163 | 56,601 | 0.0735 |
| 6 | 114 | 2,455 | 0.0464 |

즉 이 범위에서는 lower-shadow bound가 RHS의 약 `0.4%~7.4%`에 불과하다.

`x=2^22`, `2^23`에서도 비슷하게 매우 느슨하다.

### 판정

현재 확인한 기존 shadow 제약은

\[
M(2^{24})=211
\]

같은 미세한 alternating cancellation을 강제하기에는 수치적으로 너무 약하다.

이는 정리의 유효성을 부정하는 것이 아니라, **RH급 cancellation을 닫는 데 필요한 제약보다 훨씬 coarse하다는 감사결과**이다.

재현자료:

```text
data/formation/bjorner_shadow_audit_tail.csv
```

---

## 5. 이 가지에서 버려지는 정보

simplicial complex `Delta_x`는 squarefree prime subset만 보존한다.

따라서 다음 정보는 사라진다.

1. 반복 prime-channel multiplicity,
2. ordered formation word,
3. binary formation hierarchy/tree,
4. 같은 subset으로 가는 서로 다른 formation path,
5. squarefree layer polynomial의 `z`-방향 미분계층을 연산자 형태로 추적하는 정보.

즉 topological reformulation이 기존 연구와 겹친다고 해서 전체 formation approach가 동일해지는 것은 아니다.

---

## 6. 현재 판정

### 닫힌 가지

\[
\boxed{
\text{squarefree subset}
\to
\text{threshold simplicial complex}
\to
\text{Euler characteristic}
\to
M(x)
}
\]

만으로 진행하는 가지는 이미 알려져 있으며, 현재 확인한 기존 제약만으로는 RH bound를 닫지 못한다.

### 계속할 가지

다음 후보는

\[
H_m(x)=G_x^{(m)}(-1)
\]

의 전체 formation-layer derivative hierarchy와, topology가 버린 ordered/hierarchical formation information이다.

이 후보들도 최종적으로 기존 `1/zeta` 미분의 재표현으로만 환원되면 동일하게 닫는다.

독립경로로 남으려면 유한 `x`에서 실제로 사용할 수 있는 추가적인 contraction, sign constraint, orthogonality 또는 monotonic relation을 제공해야 한다.
