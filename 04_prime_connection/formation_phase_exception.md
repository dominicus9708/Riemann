# Formation-Phase Exceptional Point

## 목적

Möbius 부호 `(-1)^omega(n)`를 처음부터 선택하지 않고, squarefree 형성상태의 활성채널 수 `omega(n)`에 일반 복소 위상

\[
z=e^{i\theta}
\]

를 부여하여 어떤 `theta`가 데이터에서 예외적 상쇄점으로 나타나는지 탐색한다.

---

## 1. 형성 위상 가족

\[
a_\theta(n)
=\mu(n)^2 e^{i\theta\omega(n)}.
\]

- `theta=0`: 모든 squarefree 형성을 양수로 집계.
- `theta=pi`: `a_pi(n)=mu(n)`.
- 그 외: 채널 개수에 따른 복소 위상 집계.

Dirichlet 생성함수는

\[
F(s,z)
=\sum_{n\ge1}\frac{\mu^2(n)z^{\omega(n)}}{n^s}
=\prod_p(1+zp^{-s}),
\qquad z=e^{i\theta}.
\]

---

## 2. theta를 동등하게 스캔한 결과

`theta`를 `0`부터 `2pi`까지 `pi/12` 간격으로 동등하게 스캔했다.

각 theta에서 기존 Möbius 복소 shell과 동일하게

\[
S_{k,\theta}(t)
=\sum_{2^k<n\le2^{k+1}}
\mu^2(n)e^{i\theta\omega(n)}e^{-it\log(n/2^k)}
\]

를 계산하고 `t=5,10,...,50` RMS의 dyadic 성장지수를 최근 8개 shell에서 회귀했다.

대표값:

| theta/pi | growth exponent |
|---:|---:|
| 0.000 | 1.0001 |
| 0.500 | 0.9332 |
| 0.667 | 0.8749 |
| 0.750 | 0.8145 |
| 0.833 | 0.6678 |
| 0.917 | 0.5242 |
| **1.000** | **0.4995** |
| 1.083 | 0.5249 |
| 1.167 | 0.6608 |
| 1.250 | 0.8112 |
| 1.500 | 0.9378 |
| 2.000 | 1.0001 |

`theta=pi`가 전체 scan에서 뚜렷한 최소점이었다.

이 계산에서 `1/2`는 목표값으로 사용되지 않았고 `theta=pi` 역시 사전에 최적점으로 지정하지 않았다.

---

## 3. 절단범위 안정성

`theta/pi = 5/6, 11/12, 1, 13/12, 7/6`를 동일하게 비교하고 최근 6 shell 회귀를 사용했다.

| maximum N | 5/6 | 11/12 | 1 | 13/12 | 7/6 | minimum |
|---:|---:|---:|---:|---:|---:|---:|
| 524,288 | 0.6084 | 0.5069 | **0.5028** | 0.5102 | 0.6043 | pi |
| 1,048,576 | 0.6179 | 0.5138 | **0.5047** | 0.5229 | 0.6271 | pi |
| 2,097,152 | 0.6574 | 0.4976 | **0.4921** | 0.5113 | 0.6437 | pi |
| 4,194,304 | 0.7182 | 0.5650 | **0.5260** | 0.5635 | 0.7314 | pi |

따라서 현재 계산범위에서는 `theta=pi`라는 형성위상 최소점이 절단범위 변화에도 유지된다.

---

## 4. 이론적 이유

일반 `z`에 대해

\[
F(s,z)=\prod_p(1+zp^{-s}).
\]

특히

\[
z=-1=e^{i\pi}
\]

이면

\[
\boxed{
F(s,-1)=\prod_p(1-p^{-s})=\frac1{\zeta(s)}
}
\]

이다.

즉 `theta=pi`는 단순히 수치적으로 우연히 최소가 된 위상이 아니라, squarefree formation channel의 parity가 정확히 zeta Euler product의 역원을 만드는 위치이다.

형성관점:

\[
\boxed{
\text{각 새 독립 채널마다 위상 }-1\text{을 곱하고 반복채널을 0으로 제거}
\Rightarrow
1/\zeta(s)
}
\]

이다.

---

## 5. Selberg-Delange 기준층

고전적으로

\[
F(s,z)
=\zeta(s)^z H(s,z)
\]

형태로 분리할 수 있고, bounded `z`에 대해 보정 Euler product `H`는 `Re(s)>1/2`까지 좋은 해석적 성질을 갖는 영역이 존재한다.

일반 `z`에서는 `s=1`의 zeta 주구조가 남지만 `z=-1`에서는

\[
F(s,-1)=1/\zeta(s)
\]

로 정확히 특수화된다.

따라서 `theta=pi`는 **일반 squarefree channel aggregation에서 Möbius cancellation으로 전환되는 예외위상**이다.

이 현상 자체는 Selberg-Delange/analytic number theory의 기존 구조와 일치하므로 새로운 정리로 주장하지 않는다.

---

## 6. RH와의 정확한 관계

`theta=pi`가 예외라는 사실만으로 RH가 나오지 않는다.

이 위치에서

\[
F(s,-1)=1/\zeta(s)
\]

이므로, 비자명한 zeta zero `rho`는 `F(s,-1)`의 pole이 된다.

따라서 질문은

\[
\boxed{
\text{formation parity phase }\theta=\pi\text{에서 오른쪽에 있는 비자명 특이점들이 모두 }\Re s=1/2\text{인가?}
}
\]

로 바뀐다.

이는 정확히 RH와 동등한 난점을 다른 형성표현으로 옮긴 것이다.

현재의 장점은 `Li(x)` 같은 평균 소수분포를 먼저 선택하지 않아도 이 질문에 도달했다는 점이다.

---

## 7. 사전정의 감사

### 입력한 것

- 정수의 소인수 채널
- squarefree 여부
- 활성채널 수 `omega(n)`
- 모든 channel-count phase `theta`를 동등하게 탐색
- 복소 위치가중 `e^{-it log n}`

### 입력하지 않은 것

- `sigma=1/2`
- zeta 비자명 영점의 위치
- `Li(x)` 또는 `x/log x` 평균선
- `theta=pi`가 최적이라는 가정

### 사후에 나온 것

- `theta=pi`가 안정된 최소 formation phase.
- 그 위치에서 blind shell growth가 약 `1/2` 근방.
- 정확한 Euler product는 그 위상이 `1/zeta(s)`임을 설명.

### 남은 위험

- `beta≈1/2`는 random-sign squarefree model에서도 나타나는 square-root cancellation과 구별되지 않는다.
- 유한범위 수치는 off-critical-line zero의 부재를 증명하지 않는다.
- `1/zeta`라는 정확한 동일성 때문에 이후 `1/2`를 zeta 이론에서 가져오면 독립성이 사라진다.

---

## 8. 다음 연구조건

다음 단계의 목표는 `theta=pi`를 다시 발견하는 것이 아니다.

다음 중 하나가 필요하다.

1. formation-channel 조합 자체에서 `F(s,-1)`의 모든 비자명 pole에 대한 real-part bound를 도출한다.
2. `M(x)`의 cancellation을 channel-count layers별로 분해한 뒤 uniform `x^(1/2+epsilon)` bound로 닫을 수 있는 구조를 찾는다.
3. random-sign model에는 없는 deterministic inter-layer constraint를 찾고 그 constraint가 `1/2` barrier를 강제함을 증명한다.

이 중 어느 것도 아직 성립하지 않았다.
