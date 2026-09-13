# Dyadic Zero-Residual Audit

## 목적

`M(2^k)`의 강한 dyadic 부호교대가 새로운 formation law인지, 아니면 known zeta-zero waves의 합으로 설명되는지 더 강하게 검사한다.

기준량은

\[
y_k=\frac{M(2^k)}{2^{k/2}},\qquad k=10,\ldots,75.
\]

첫 `m`개 nontrivial zero contribution을

\[
Z_m(k)=2\Re\sum_{j=1}^m
\frac{e^{i\gamma_j k\log 2}}{\rho_j\zeta'(\rho_j)}
\]

로 두고 residual

\[
R_m(k)=y_k-Z_m(k)
\]

을 계산한다.

이 절차는 zeta zero를 입력으로 사용하므로 **독립 RH 증명 경로가 아니다.** 목적은 dyadic anomaly를 기존 zero structure로 얼마나 제거할 수 있는지 확인하는 것이다.

---

## 1. 원 신호

`k=10..75`에서:

- RMS of `y_k`: `0.166376`
- lag-1 correlation: `-0.675194`
- sign changes: `50/65`

따라서 장기 dyadic 자료에도 강한 negative nearest-neighbor correlation이 존재한다.

---

## 2. zero term 수에 따른 residual

전체 결과는

```text
data/mertens/dyadic_zero_wave_residual_10_75.csv
```

에 저장한다.

| removed first zeros | residual RMS | residual lag-1 corr | residual sign changes / 65 | zero-wave R^2 |
|---:|---:|---:|---:|---:|
| 0 | 0.16638 | -0.675 | 50 | 0 |
| 1 | 0.11563 | -0.397 | 41 | 0.517 |
| 2 | 0.10095 | -0.381 | 39 | 0.632 |
| 5 | 0.07582 | -0.304 | 37 | 0.792 |
| 10 | 0.06237 | -0.466 | 41 | 0.859 |
| 20 | 0.04981 | -0.485 | 43 | 0.910 |
| 30 | 0.04526 | -0.418 | 43 | 0.926 |
| 40 | 0.03766 | -0.358 | 43 | 0.949 |
| 50 | 0.03558 | -0.390 | 39 | 0.954 |
| 75 | 0.03046 | -0.315 | 37 | 0.966 |
| 100 | 0.02808 | -0.235 | 43 | 0.971 |

### 핵심

첫 100개 zero만으로 원 dyadic normalized signal variance의 약 `97.1%`를 설명한다.

residual RMS는

\[
0.1664\to0.0281
\]

로 약 83% 감소한다.

lag-1 negative correlation도

\[
-0.675\to-0.235
\]

로 크게 약해진다.

`sign changes` 자체는 residual amplitude가 작아질수록 zero crossing에 민감해져 단조감소하지 않는다. 따라서 이 단계에서는 sign-change count보다 RMS와 explained variance를 우선한다.

---

## 3. 감사 판정

처음 gap-permutation null에서 보인

\[
\text{실제 }M(2^k)\text{의 과도한 교대}
\]

는 실제 현상이지만, 그것의 대부분은 known nontrivial zeros의 log-frequency superposition으로 설명된다.

따라서 다음 연결은 새 증명경로가 아니다.

\[
\text{prime arrangement}
\to
M(2^k)\text{ alternation}
\to
\text{RH information}
\]

왜냐하면 `M(2^k)` alternation을 설명하는 데 이미 zeta-zero spectrum을 사용하면 다시 원래 analytic structure로 돌아가기 때문이다.

현재 dyadic branch는 **zero-wave recovery/audit branch**로 분류하고 RH 증명 후보에서는 우선 제외한다.

---

## 4. 그래도 남는 질문

`R_100(k)`는 0이 아니고 residual lag correlation도 완전히 사라지지 않는다.

그러나 이를 새로운 formation residual로 해석하기 전에 최소한 다음을 확인해야 한다.

1. zero truncation을 `100 -> 200 -> ...`로 늘리면 residual이 계속 감소하는가.
2. explicit-formula truncation/regularization 오차가 residual의 주원인인가.
3. finite `k` sampling 및 discontinuity of `M(x)`가 잔차를 만드는가.
4. formation descriptor가 residual을 설명하더라도 그 descriptor가 다시 zero information과 동치인 것은 아닌가.

이 검증 전에는 residual을 독립 신호로 승격하지 않는다.

---

## 5. 다음 방향

Dyadic sampling은 zero frequencies에 지나치게 직접 민감하므로, 다음 독립 후보는 **sampling scale을 고정하지 않는 것**이다.

예를 들어

\[
M(\lambda^k),\qquad \lambda>1
\]

에서 여러 `lambda`를 동일하게 비교하고, 특정 `lambda=2`가 만들어내는 phase-locking을 제거한다.

더 강하게는 실수축 formation-layer identity 자체에서 scale-free inequality가 나오는지 본다.

즉 다음 단계에서는

\[
\boxed{\text{dyadic phase locking을 버리고 scale-robust formation constraint를 찾는다}}
\]

를 우선한다.
