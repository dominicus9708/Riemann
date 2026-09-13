# Möbius Worst-Direction Audit

## 목적

`mobius_formation_bridge.md`의 RMS spectral exponent가 random-sign square-root cancellation과 구별되지 않았으므로, 평균 대신 고정된 주파수 격자에서의 **최대 복소 진폭**을 사용하여 더 강한 진단을 시도한다.

Dyadic shell에서

\[
S_k(t)=\sum_{2^k<n\le2^{k+1}}\mu(n)e^{-it\log(n/2^k)}
\]

를 두고

\[
X_k(B)=\max_{t\in B}|S_k(t)|
\]

를 계산한다.

`1/2`는 정의에 사용하지 않는다.

---

## 1. 고정 격자 결과

주파수 격자:

\[
B=\{0,5,10,\ldots,100\}.
\]

`N<=4,194,304`, 최근 8개 dyadic shell에서

\[
\log_2 X_k\approx\beta_{\max}k+c
\]

를 회귀했다.

실제 Möbius:

\[
\boxed{\beta_{\max}\approx0.47363}
\]

이다.

마지막 다섯 shell의 최대값과 그 위치는 대략:

| shell upper | max amplitude | maximizing t |
|---:|---:|---:|
| 262,144 | 403.35 | 95 |
| 524,288 | 828.75 | 65 |
| 1,048,576 | 935.88 | 45 |
| 2,097,152 | 1210.85 | 50 |
| 4,194,304 | 1894.71 | 90 |

최대 주파수 위치는 고정되지 않는다.

---

## 2. random-sign squarefree control

동일한 `|mu(n)|` support를 유지하고 squarefree 위치의 부호만 독립 random `±1`로 바꾼 5개 seed의 같은 회귀값은:

```text
0.46720
0.46932
0.50301
0.46477
0.52614
```

평균은 약

\[
0.48609
\]

이고 표준편차는 약

\[
0.02443
\]

이다.

실제 Möbius의 `0.47363`은 이 대조군 범위 안에 들어간다.

따라서 현재 유한 범위/고정 격자에서는 실제 Möbius의 worst-direction exponent가 random squarefree-sign model과 분리되지 않는다.

---

## 3. 주파수 범위 민감도

격자를 `0<=t<=200`, step `5`로 확대하면 실제 Möbius의 회귀 기울기는 shell window에 따라 대략

```text
recent 6 shells: 0.3760
recent 8 shells: 0.4226
recent 10 shells: 0.4510
```

으로 크게 이동했다.

따라서 현재의 `max over sampled t`는 연속 supremum을 안정적으로 근사하지 못한다.

이 결과 때문에 최대값 분석 역시 아직 RH-equivalent uniform bound의 수치 대리량으로 사용할 수 없다.

---

## 4. 감사 결론

현재까지 얻은 `1/2` 근방 현상은 세 단계로 분류된다.

1. finite complex minima에서의 `1/2`: 절단 이동으로 기각.
2. Möbius RMS growth에서의 `1/2`: random-sign control에서도 재현.
3. sampled worst-direction growth: 실제 Möbius와 random control이 분리되지 않고 `t` 범위에도 민감.

따라서 아직 **Möbius 고유의 non-random residual**은 발견하지 못했다.

이 음성 결과는 중요하다. 단순 square-root cancellation을 RH 특유 신호로 오인하는 경로를 차단한다.

---

## 5. 다음 단계

다음 분석은 더 많은 목적함수를 만드는 것이 아니라, 정확한 RH 동치량으로 되돌아간다.

\[
M(x)=\sum_{n\le x}\mu(n)
\]

의 성장을 형성채널 단위로 역분해할 수 있는지 조사한다.

특히 squarefree integer `n=p_1...p_k`가 주는 부호

\[
(-1)^k
\]

를 각 채널 조합 차수 `k`별로 나누어

\[
M(x)=\sum_{k\ge0}(-1)^k A_k(x)
\]

형태로 기록한다. 여기서 `A_k(x)`는 `n<=x`인 squarefree `k`-prime products의 수이다.

각 `A_k`는 양수이며 큰 값을 가지지만 전체에서는 강하게 상쇄된다.

향후 핵심 질문은:

- 이 상쇄가 단순 random parity로 충분히 설명되는가,
- 각 `k` 층 사이에 체계적 상관이 있는가,
- 그 상관을 정적집계했을 때 random control에서 사라지고 실제 Möbius에서만 남는 잔차가 있는가

이다.
