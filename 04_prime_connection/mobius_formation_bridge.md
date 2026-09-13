# Möbius Formation Bridge

## 목적

평균 소수분포 `Li(x)`나 `x/log x`를 사전에 기준선으로 두지 않고, 기존 소수채널 형성구조 자체에서 자연스럽게 부호/상쇄 구조를 만들고 RH와 직접 접속할 수 있는지 검사한다.

핵심 객체는 Möbius 함수이다.

---

## 1. 형성채널에서 Möbius 함수의 직접 정의

기존 채널벡터를

\[
V(n)=(\nu_2(n),\nu_3(n),\nu_5(n),\ldots)
\]

라고 한다.

다음 두 속성을 정의한다.

### 반복채널 배제

\[
Q(n)=
\begin{cases}
1,&\nu_p(n)\in\{0,1\}\text{ for every prime }p,\\
0,&\text{otherwise}.
\end{cases}
\]

### 활성채널 parity

\[
S(n)=(-1)^{\omega(n)}.
\]

그러면

\[
\boxed{\mu(n)=Q(n)S(n)}
\]

이다.

즉 형성언어로는:

- 어떤 채널이라도 반복되면 `0`,
- 서로 다른 채널만 한 번씩 결합되면 채널 수가 짝수일 때 `+1`, 홀수일 때 `-1`.

이 부호는 임의의 평균 제거가 아니라 소인수 채널의 중복/홀짝 속성에서 정확히 결정된다.

---

## 2. Dirichlet 역원으로서의 의미

Möbius 함수는 상수함수 `1(n)=1`의 Dirichlet convolution inverse이다.

\[
\boxed{1*\mu=\varepsilon}
\]

여기서 `epsilon(1)=1`, `epsilon(n)=0` for `n>1`이다.

따라서 `Re(s)>1`에서

\[
\boxed{
\sum_{n\ge1}\frac{\mu(n)}{n^s}
=\frac1{\zeta(s)}
}
\]

이다.

이것은 `평균 소수밀도`를 먼저 선택하지 않고도 형성구조에서 zeta의 역함수로 직접 이동하는 경로이다.

---

## 3. RH와의 고전적 동치

Mertens function을

\[
M(x)=\sum_{n\le x}\mu(n)
\]

라고 하면 고전적으로

\[
\boxed{
\text{RH}
\iff
M(x)=O_\varepsilon(x^{1/2+\varepsilon})
\quad\text{for every }\varepsilon>0
}
\]

이다.

따라서 현재 형성채널 표현은

\[
V(n)
\to(Q(n),S(n))
\to\mu(n)
\to M(x)
\to\text{RH-equivalent growth condition}
\]

이라는 정확한 다리를 갖는다.

주의: 이 동치 자체는 고전 정수론의 결과이며 새 정리가 아니다. 현재 연구의 의미는 `mu`를 형성/속성 채널 언어로 재구성하고 이후 독립 감사량을 설계하는 데 있다.

---

## 4. 사전 1/2 없는 첫 실수축 계산

`1/2`를 사용하지 않고

\[
E(X)=\max_{n\le X}|M(n)|
\]

및 경험적 envelope exponent

\[
\beta_E(X)=\frac{\log E(X)}{\log X}
\]

를 계산했다.

`X<=5,000,000` 범위의 일부 결과:

| X | M(X) | E(X) | beta_E(X) |
|---:|---:|---:|---:|
| 32,768 | 26 | 73 | 0.412655 |
| 65,536 | 14 | 113 | 0.426261 |
| 131,072 | -20 | 132 | 0.414376 |
| 262,144 | 24 | 154 | 0.403710 |
| 524,288 | -125 | 258 | 0.421644 |
| 1,048,576 | 257 | 368 | 0.426178 |
| 2,097,152 | -362 | 550 | 0.433490 |
| 4,194,304 | 228 | 683 | 0.427988 |

이 범위만으로 `1/2` 수렴을 주장할 수 없다. 오히려 단순 envelope exponent는 매우 느리고 불안정한 진단량임을 보여준다.

---

## 5. 허수축을 포함한 blind spectral exponent

사용자가 제안한 복소 재탐색을 Möbius 형성부호에 적용한다.

Dyadic shell `2^k<n<=2^(k+1)`에서

\[
S_k(t)
=
\sum_{2^k<n\le2^{k+1}}
\mu(n)\exp\{-it\log(n/2^k)\}
\]

를 정의한다.

여기에는 실수부 `sigma`나 `1/2`를 넣지 않는다.

`t` 대역 `B`에 대해 RMS 크기

\[
R_k(B)
=
\left(
\frac1{|B|}\sum_{t\in B}|S_k(t)|^2
\right)^{1/2}
\]

를 계산하고

\[
\log_2 R_k(B)\approx \beta_B k+c
\]

로 회귀한다.

이 `beta_B`가 **데이터가 스스로 선택하는 복소 shell 성장지수**이다.

---

## 6. 계산 결과

`N<=4,194,304`에서 broad frequency bands를 사용했다.

### 최근 8개 dyadic shell 회귀

| t band | blind beta estimate |
|---|---:|
| 5..25 step 5 | 0.465680 |
| 30..50 step 5 | 0.521006 |
| 5..50 step 5 | 0.499453 |
| 10..100 step 10 | 0.500913 |

### 최근 shell 수에 따른 변화 (`t=5..50`)

| regression shells | beta |
|---:|---:|
| 5 | 0.584449 |
| 6 | 0.526033 |
| 7 | 0.488766 |
| 8 | 0.499453 |
| 9 | 0.511097 |
| 10 | 0.516441 |

### 절단범위 증가 (`t=5..50`, rolling 8 shells)

| maximum N | beta |
|---:|---:|
| 262,144 | 0.471542 |
| 524,288 | 0.463146 |
| 1,048,576 | 0.527026 |
| 2,097,152 | 0.518109 |
| 4,194,304 | 0.499453 |

따라서 broad-band 복소 shell 통계에서는 `1/2`를 입력하지 않았는데도 `beta≈0.5`가 반복적으로 나온다.

---

## 7. 즉시 수행한 무작위 대조군

이 결과를 RH 신호라고 해석하면 안 된다.

동일한 squarefree support `|mu(n)|`를 유지하고 부호만 독립적인 random `±1`로 바꾼 대조군을 만들었다.

10개 고정 seed에서 `t=5..50`, 최근 8 shell의 blind beta는:

```text
0.54136, 0.45550, 0.46558, 0.50046, 0.53676,
0.49569, 0.46356, 0.49287, 0.39360, 0.54946
```

평균과 표준편차는 대략

\[
\boxed{0.4895\pm0.0450}
\]

이었다.

실제 Möbius 값 `0.49945`는 이 분포 안에 평범하게 들어간다.

반대로 부호를 제거한 positive squarefree indicator `|mu(n)|`는 같은 계산에서

\[
\beta\approx1.0001
\]

을 보였다.

### 감사 결론

현재 관측된 `beta≈1/2`는

\[
\boxed{
\text{Möbius의 특수한 RH 신호라기보다 signed cancellation의 square-root scaling과 양립}
}
\]

한다.

따라서 이것은 **중요한 양성 현상**이지만 RH 증거로 승격하지 않는다.

---

## 8. 왜 그래도 중요하나

이번에는 세 종류의 기준이 생겼다.

1. `W`의 양수 형성계수: 사전값 없이 `eta_W≈1.3994333`을 안정적으로 회복.
2. 유한 complex minima: 일시적으로 `1/2`처럼 보여도 절단을 늘리면 이동하는 가짜 양성.
3. Möbius signed spectrum: `1/2`가 사전 입력 없이 나타나지만 random-sign 대조군에서도 나타나는 **보편적 cancellation 양성**.

즉 앞으로 필요한 것은 단순히 `1/2`를 재현하는 것이 아니라

\[
\boxed{
\text{random square-root cancellation보다 강한, Möbius 고유의 구조적 제약을 찾는 것}
}
\]

이다.

---

## 9. 다음 단계

다음 감사는 평균 크기가 아니라 **최악방향(worst-direction)**을 본다.

RMS over `t`는 평균적인 square-root cancellation을 강하게 반영하므로 RH 동치의 `O(x^{1/2+epsilon})`와 같은 uniform/worst-case 요구보다 약하다.

따라서 다음에는:

1. 각 dyadic shell에서 `max_t |S_k(t)|`의 성장지수,
2. `t` 격자 확대에 대한 최대값 안정성,
3. random-sign squarefree 대조군의 극값분포,
4. 실제 Möbius가 random 대조군의 극값 envelope를 체계적으로 벗어나는지,
5. 실수축 `M(x)` envelope와 복소 극값의 연결

을 검사한다.

여기에서만 `1/2` 근방의 **uniform barrier**가 독립적으로 나타난다면 RH 동치조건과 더 가까운 후보가 된다.
