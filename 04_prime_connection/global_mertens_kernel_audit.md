# Global Mertens Kernel Audit

## 목적

단일 prime-channel toggle이 구조적으로 실패한 뒤, 여러 채널을 동시에 묶는 **전역 형성연산자**가 Möbius 상쇄를 단순화하는지 검사한다.

가장 자연스러운 후보는 Heath–Brown/Vaughan형 분해에서 나오는 전역 quadratic kernel이다.

---

## 1. 정확한 전역 항등식

`x=N^2`라 하자.

Heath–Brown identity의 `K=2` 경우를 합하면 정확히

\[
\boxed{
M(N^2)
=2M(N)-\sum_{a,b\le N}
\mu(a)\mu(b)
\left\lfloor\frac{N^2}{ab}\right\rfloor
}
\]

을 얻는다.

벡터와 행렬을

\[
\mathbf m=(\mu(1),\ldots,\mu(N))^T,
\qquad
A_{ab}=\left\lfloor\frac{N^2}{ab}\right\rfloor
\]

라고 두면

\[
\boxed{M(N^2)=2M(N)-\mathbf m^TA\mathbf m}.
\]

이 항등식은 Huxley–Watt의 Mertens-sum matrix formulation과 동일한 기존 구조이다.

따라서 새 정리로 취급하지 않는다.

---

## 2. formation 해석

`m_a=mu(a)`는 기존 formation channel의

- repeated channel exclusion,
- active-channel parity

에서 결정되는 부호이다.

커널

\[
A_{ab}=\lfloor N^2/(ab)\rfloor
\]

은 두 형성상태 `a,b`가 남겨 두는 곱셈 budget을 센다.

즉 local toggle과 달리 모든 `a,b<=N`을 동시에 결합하는 전역 연산자이다.

---

## 3. 수치 감사

`N=64,128,256,512,1024`에서 직접 행렬을 구성하고

\[
Q_N=\mathbf m^TA\mathbf m
\]

을 계산했다.

| N | M(N) | M(N^2) | Q_N |
|---:|---:|---:|---:|
| 64 | -1 | -19 | 17 |
| 128 | -2 | -32 | 28 |
| 256 | -1 | 14 | -16 |
| 512 | -4 | 24 | -32 |
| 1024 | -4 | 257 | -265 |

모든 경우

\[
Q_N=2M(N)-M(N^2)
\]

가 정확히 일치했다.

---

## 4. raw random-sign 대조군

실제 `mu(n)!=0` support는 그대로 두고 부호만 independent random `+/-1`로 바꾼 300개 대조군을 만들었다.

대표적으로:

| N | actual Q_N | random median |P^T A P| | random sample 중 |Q|<=|Q_actual| 비율 |
|---:|---:|---:|---:|
| 64 | 17 | 4,277 | 0.033 |
| 128 | 28 | 13,712 | 0.020 |
| 256 | -16 | 68,704 | 0.0067 |
| 512 | -32 | 259,882 | 0 |
| 1024 | -265 | 1,003,069 | 0 |

raw kernel에서는 실제 Möbius vector가 극단적으로 작은 quadratic form을 만든다.

그러나 이 단계만으로 Möbius 고유 RH-level constraint라고 결론내리면 안 된다.

---

## 5. 주성분 제거

Huxley–Watt에서 사용하는 분해와 같이

\[
A=N^2\mathbf f\mathbf f^T
-\frac12\mathbf u\mathbf u^T
+Z,
\]

\[
f_n=1/n,
\qquad
u_n=1
\]

로 둔다.

그러면

\[
\mathbf m^TA\mathbf m
=
N^2\left(\sum_{n\le N}\frac{\mu(n)}n\right)^2
-\frac12M(N)^2
+\mathbf m^TZ\mathbf m.
\]

실제 vector에서

\[
\sum_{n\le N}\frac{\mu(n)}n
\]

이 이미 매우 작기 때문에 raw random-sign control과의 거대한 차이 대부분은 이 rank-one component에서 발생한다.

대표값:

| N | sum mu(n)/n | actual Z quadratic |
|---:|---:|---:|
| 128 | -0.0005691 | +29.995 |
| 256 | +0.0045500 | -16.857 |
| 512 | -0.0045639 | -29.460 |
| 1024 | -0.0014950 | -259.344 |

---

## 6. residual random control

동일 random-sign vectors에 대해서도 동일하게 rank-one term과 constant-vector term을 제거하여 `Z` quadratic form만 비교했다.

| N | actual m^T Z m | random std | random median absolute | random sample 중 |Zq|<=|actual| 비율 |
|---:|---:|---:|---:|---:|
| 128 | +29.995 | 33.85 | 21.08 | 0.64 |
| 256 | -16.857 | 67.76 | 46.70 | 0.21 |
| 512 | -29.460 | 119.30 | 76.65 | 0.17 |
| 1024 | -259.344 | 273.66 | 180.44 | 0.67 |

따라서 obvious rank-one component를 제거하면 실제 Möbius vector의 residual quadratic form은 random-sign 대조군에서 더 이상 예외적이지 않다.

### 감사 결론

\[
\boxed{
\text{raw quadratic exceptionalness}
\approx
\text{small }\sum_{n\le N}\mu(n)/n
+\text{ordinary residual fluctuation}
}
\]

으로 보인다.

`sum mu(n)/n -> 0` 자체는 prime number theorem과 동치인 고전적 cancellation 층과 연결되므로, 이 결과만으로 RH 수준의 새 구조를 얻은 것은 아니다.

---

## 7. square-root split의 사전정의 감사

이 분해에서 `u=sqrt(x)`가 자연스럽게 나타난다.

하지만 이를 RH critical real part `1/2`와 연결하면 안 된다.

일반 Heath–Brown identity는 정수 `K>=1`에 대해

\[
u\ge n^{1/K}
\]

인 `K`-fold decomposition을 허용한다.

따라서 같은 구성에서

\[
1/2,1/3,1/4,\ldots
\]

가 모두 decomposition thresholds로 나타난다.

즉 여기의 `1/2`는

\[
\boxed{
K=2\text{를 선택했기 때문에 생기는 multiplicative cutoff}
}
\]

이며 RH 임계선의 독립적 출현으로 분류하지 않는다.

---

## 8. largest-prime split

동일한 전역 구조를 largest prime factor로도 볼 수 있다.

`y>=sqrt(x)`일 때 squarefree `n<=x`에서 `P^+(n)>y`이면 유일하게

\[
n=pm,
\qquad
p>y,
\quad
m\le x/y\le\sqrt{x}<p
\]

로 쓸 수 있다.

따라서

\[
\boxed{
M(x)
=S(x,y)
-\sum_{m\le x/y}\mu(m)
\{\pi(x/m)-\pi(y)\}
}
\]

이다.

여기서

\[
S(x,y)=\sum_{\substack{n\le x\\P^+(n)\le y}}\mu(n).
\]

`x=2^22`, `y=sqrt(x)=2048`에서는

\[
S(x,y)=-22,239,
\qquad
\text{large-prime contribution}=+22,467,
\]

그래서

\[
M(x)=228
\]

이 남았다.

이 전역 cancellation은 명확하지만 Buchstab/Heath–Brown/Vaughan형 decomposition과 같은 기존 계보에 속한다.

---

## 9. 현재 판정

### 살아남은 사실

- local channel toggle과 달리 global multiplicative kernel은 큰-prime singleton 병목을 제거한다.
- `M(N^2)`를 `mu(1..N)`만으로 압축하는 exact finite identity가 존재한다.
- 실제 Möbius vector는 raw kernel에서 random signs와 매우 다르다.

### 닫힌 기대

- 차이의 대부분은 rank-one direction `f=(1,1/2,...,1/N)`에서 온다.
- 그 방향을 제거한 residual은 현재 계산에서 random-sign control과 분리되지 않는다.
- `sqrt(x)`의 출현은 general `x^(1/K)` hierarchy 중 하나이므로 RH의 `1/2`로 해석할 수 없다.

### 다음 후보

전역 operator를 계속 사용할 가치가 있으려면 `Z` residual에 대해 random signs에는 없는 deterministic correlation을 찾아야 한다.

현재 `N<=1024`에서는 그런 신호를 확인하지 못했다.

따라서 우선순위는 다음으로 이동한다.

1. `Z` residual보다 더 formation-specific한 ordered/hierarchical channel data,
2. 여러 formation layers를 한꺼번에 연결하되 PNT-level projection을 제거한 operator,
3. known Heath–Brown/Buchstab identities와 동치가 아닌 finite relation.
