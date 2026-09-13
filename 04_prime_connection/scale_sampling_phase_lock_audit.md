# Scale-Sampling Phase-Lock Audit

## 목적

`M(2^k)`의 강한 부호교대가 `2`라는 배율 자체의 산술적 특수성인지, 아니면 zeta-zero log-frequency와 sampling scale의 위상잠금(phase locking)인지 검사한다.

일반 배율

\[
x_k=\lfloor \lambda^k\rfloor,
\qquad \lambda>1
\]

에 대해

\[
y_k(\lambda)=\frac{M(x_k)}{\sqrt{x_k}}
\]

의 lag-1 correlation을 계산한다.

직접 sieve 범위는

\[
1024\le x\le2^{24}=16,777,216
\]

이다.

---

## 1. 첫 zero의 예측

첫 zero contribution만 생각하면 normalized oscillation은 대략

\[
\cos(\gamma_1\log x+\phi)
\]

형태이다.

`x -> lambda x`에서 위상증분은

\[
\Delta\phi=\gamma_1\log\lambda.
\]

순수한 single-frequency wave라면 인접 표본의 correlation 방향은 대략

\[
\boxed{\cos(\gamma_1\log\lambda)}
\]

에 따라 움직여야 한다.

---

## 2. lambda scan

`lambda=1.10..2.20`을 동등하게 스캔했다.

충분한 표본수를 갖는 lambda들에서 empirical lag-1 correlation과

\[
\cos(\gamma_1\log\lambda)
\]

의 상관은

\[
\boxed{0.816\text{ approximately}}
\]

이었다.

대표값은 `data/mertens/scale_sampling_phase_lock.csv`에 저장한다.

| lambda | empirical lag-1 corr | first-zero prediction |
|---:|---:|---:|
| 1.20 | -0.591 | -0.845 |
| 1.40 | +0.143 | +0.044 |
| 1.50 | +0.650 | +0.851 |
| 1.53 | +0.688 | +0.963 |
| 1.60 | +0.669 | +0.936 |
| 1.80 | -0.208 | -0.439 |
| **2.00** | **-0.853** | **-0.931** |
| 2.20 | +0.202 | +0.149 |

`lambda=2`는 scan 범위에서 실제 correlation이 가장 강하게 음수가 되는 위치 부근이었다.

따라서 dyadic alternation은 `2`의 형성적 특수성보다

\[
\gamma_1\log2\approx\pi\pmod{2\pi}
\]

에 가까운 phase relation으로 설명되는 방향이 강하다.

---

## 3. 30-zero wave와 scale curve 비교

첫 30개의 known nontrivial zeros를 사용해

\[
Z_{30}(x)=2\Re\sum_{j=1}^{30}
\frac{x^{i\gamma_j}}{\rho_j\zeta'(\rho_j)}
\]

를 만들고, 각 `lambda`에서 `Z_30(lambda^k)`의 lag-1 correlation을 별도로 계산했다.

`lambda=1.10..2.20` 스캔에서

\[
\boxed{
\operatorname{corr}
(\text{empirical lag curve},\text{30-zero lag curve})
\approx0.982
}
\]

였다.

대표값:

| lambda | empirical | 30-zero wave |
|---:|---:|---:|
| 1.10 | -0.013 | -0.007 |
| 1.20 | -0.591 | -0.614 |
| 1.40 | +0.143 | +0.156 |
| 1.50 | +0.650 | +0.718 |
| 1.60 | +0.669 | +0.659 |
| 1.80 | -0.208 | -0.288 |
| 2.00 | -0.853 | -0.800 |
| 2.20 | +0.202 | +0.202 |

scale dependence 자체가 known zero spectrum에 의해 거의 재현된다.

---

## 4. 감사 판정

다음 후보는 닫는다.

> `M(2^k)`의 강한 alternating pattern이 실제 소수 형성채널의 독립적인 dyadic law이다.

관측 자체는 실제이지만,

1. 첫 zero의 phase advance가 sign reversal을 자연스럽게 선호하고,
2. 여러 lambda에서 correlation의 부호/크기가 first-zero prediction을 따라 움직이며,
3. first 30 zeros의 residue wave가 전체 lambda-correlation curve를 약 `0.982` 상관으로 재현한다.

따라서 dyadic signal을 다시 RH 근거로 사용하면

\[
\text{known zero spectrum}
\to
\text{dyadic Mertens signal}
\to
\text{RH}
\]

형태의 순환이 된다.

---

## 5. 연구상 의미

이번 가지의 가치는 음성결과에 있다.

- null model에서는 매우 특이해 보였던 통계도,
- sampling scale을 자유롭게 한 뒤,
- known zero frequencies와 비교하면

기존 analytic structure가 거의 전부 설명할 수 있었다.

따라서 앞으로 candidate statistic을 채택하려면 최소한

\[
\boxed{
\text{sampling scale을 바꾸어도 유지되고, known zero-wave를 제거해도 남아야 한다}
}
\]

는 감사조건을 추가한다.

---

## 6. 다음 단계

Dyadic/geometric sampling branch는 RH 증명 후보에서 닫는다.

다음에는 sampling scale을 사용하지 않는 finite formation identity만 남긴다.

현재 살아 있는 후보는:

1. non-squarefree fibers가 squarefree parity cancellation에 주는 결정론적 제약,
2. prime-exponent lattice 전체에서 Möbius boundary가 갖는 discrete-difference 구조,
3. ordered/hierarchical formation information 중 squarefree layer count `omega`로 환원되지 않는 정보,
4. 위 구조로부터 `M(x)`에 대한 scale-free inequality가 나오는지 여부.

단, Dirichlet series로 보냈을 때 다시 `1/zeta(s)`만 공통인자로 남으면 순환경로로 즉시 분류한다.
