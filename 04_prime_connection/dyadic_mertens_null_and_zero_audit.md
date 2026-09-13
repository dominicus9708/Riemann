# Dyadic Mertens Null-Model and Zero-Wave Audit

## 목적

실제 소수채널 배열이 동일한 밀도/개수/gap 통계를 가진 가상 채널보다 Möbius parity 합

\[
M(x)=\sum_{n\le x}\mu(n)
\]

에 추가 제약을 주는지 검사한다.

특히 dyadic 표본

\[
M(2^k)
\]

에서 관찰된 강한 부호교대를 새 형성규칙으로 해석하기 전에, 대조군과 기존 zeta-zero 진동으로 설명되는지 감사한다.

---

## 1. 실제 dyadic 표본

현재 직접 sieve 범위 `2^10 <= x <= 2^24`에서

```text
-4, 7, -19, 22, -32, 26, 14, -20, 24, -125, 257, -362, 228, -10, 211
```

이다.

14개의 인접 전이 가운데 13개에서 부호가 바뀐다.

`2^10..2^20`만 보면 10개 전이 가운데 9개가 부호변화이고,

\[
y_k=\frac{M(2^k)}{\sqrt{Q(2^k)}}
\]

(`Q(x)` = squarefree count)의 lag-1 correlation은 약

\[
-0.8580
\]

이다.

이 통계를 사전에 RH 신호라고 해석하지 않는다.

---

## 2. 세 null model

모든 가상 생성자는 prime이라는 산술성 대신 `서로 다른 독립 형성채널`로 취급한다. subset product가 cutoff 이하인 상태들을 squarefree formation state로 세고 parity sum을 계산한다.

### A. calibrated Cramer density

작은 생성자를 고정하고 그 위에서는

\[
\Pr(n\text{ is a channel})=c/\log n
\]

으로 독립추출한다. `c`는 기대 채널 수가 실제 prime count와 맞도록 보정한다.

### B. dyadic fixed count

각 dyadic interval에서 실제 prime 개수와 정확히 같은 수의 integer locations를 균등 무작위 추출한다.

보존:

- dyadic one-point density,
- shell별 channel count.

제거:

- 실제 gap 분포,
- 실제 gap 순서.

### C. dyadic gap permutation

각 dyadic interval의 실제 prime gaps multiset을 그대로 보존하고 gap 순서만 permutation한다. 각 mutable block의 첫 prime과 마지막 prime은 따라서 유지된다.

보존:

- shell별 prime count,
- 해당 shell 내부 gap multiset,
- first/last endpoint.

제거:

- gap ordering 및 장거리 배열 상관.

---

## 3. 2^10..2^20 결과

실제값:

- sign changes = `9/10`
- lag-1 corr = `-0.858035...`

대조군 결과는 `data/mertens/dyadic_null_model_summary_2pow20.csv`에 저장한다.

| model | samples | mean sign changes | P(sign changes >= 9) | mean lag-1 corr | P(corr <= actual) |
|---|---:|---:|---:|---:|---:|
| calibrated Cramer | 200 | 3.710 | 0.00995 | +0.111 | 0.00498 |
| dyadic fixed count | 200 | 5.215 | 0.05970 | -0.385 | 0.00498 |
| dyadic gap permutation | 300 | 4.443 | 0.00664 | -0.372 | 0.00997 |

`P`는 finite Monte-Carlo empirical tail probability이며 theorem-level p-value가 아니다. null-model 자체가 임의 선택이므로 모델 의존성을 반드시 남긴다.

### 1차 진단

강한 dyadic alternation은 단순 Cramer density뿐 아니라 shell count 및 gap multiset을 보존한 null에서도 드물다.

따라서 `실제 gap 순서/장거리 배열`이 관련되는 후보가 생긴다.

그러나 이것만으로 prime-specific new law를 주장하지 않는다.

---

## 4. 작은 소수 고정 민감도

Gap permutation에서 실제 작은 prime들을 `10`, `100`, `1000`, `10000` 아래까지 그대로 고정하고 `2^10..2^24`를 비교했다.

실제 sign changes는 `13/14`, 실제 normalized lag-1 correlation은 약 `-0.8531`이다.

`data/mertens/dyadic_gap_freeze_sensitivity_2pow24.csv` 결과:

| freeze below | samples | mean sign changes | max observed | mean lag-1 corr |
|---:|---:|---:|---:|---:|
| 10 | 80 | 3.675 | 10 | +0.241 |
| 100 | 150 | 4.507 | 9 | +0.220 |
| 1000 | 80 | 6.850 | 10 | -0.184 |
| 10000 | 80 | 7.338 | 12 | -0.217 |

작은 prime을 더 많이 고정할수록 null도 실제의 negative correlation 방향으로 이동한다.

즉 작은 소수들의 실제 배열이 dyadic parity dynamics의 상당 부분을 이미 결정한다.

---

## 5. 장기 published data 교차검증

OEIS A084236은 Hurst의 계산 및 이후 Helfgott-Thompson 계산을 바탕으로 `M(2^n)`을 `n=0..75`까지 제공한다.

저장소에는

```text
data/mertens/mertens_powers_of_two_0_75.csv
```

로 원값을 보존한다.

`n=10..75`의 65개 인접 전이 가운데 실제 sign change는

\[
\boxed{50/65\approx0.7692}
\]

이다.

따라서 `2^10..2^24`의 거의 완전한 alternation은 저범위에서 특히 강하지만, 높은 범위에서도 sign-change rate가 1/2보다 상당히 높은 상태가 지속된다.

---

## 6. 첫 zeta zero가 주는 dyadic phase advance

첫 nontrivial zero를

\[
\rho_1=\frac12+i\gamma_1,
\qquad
\gamma_1\approx14.1347251417
\]

라고 하자.

`x -> 2x`이면 RH-line zero contribution의 phase는

\[
\Delta\phi_1=\gamma_1\log2
\approx9.79744488.
\]

modulo `2pi`에서는

\[
\Delta\phi_1\equiv3.51425957\pmod{2\pi}
\]

이다.

이는 `pi`보다 약간 크다.

따라서 첫 zero 성분만 존재해도 dyadic sampling은 자연스럽게 `거의 sign reversal`을 선호한다.

이 관찰은 dyadic sign alternation을 새로운 prime-gap law로 해석하기 전에 반드시 제거해야 할 baseline이다.

---

## 7. zero-wave 직접 비교

simple zero `rho`의 Mertens explicit-formula residue형 contribution을 normalized form으로

\[
Z_m(2^k)
=
2\Re\sum_{j=1}^{m}
\frac{e^{i\gamma_j k\log2}}
{\rho_j\zeta'(\rho_j)}
\]

로 계산했다.

여기서는 amplitude/phase fitting을 하지 않고 numerically known zero와 `zeta'(rho)`를 그대로 사용했다.

`M(2^k)/sqrt(2^k)`, `k=10..75`와 비교한 결과:

| first zeros used | correlation | sign accuracy | predicted sign changes / 65 | R^2 |
|---:|---:|---:|---:|---:|
| 1 | 0.721 | 0.758 | 58 | 0.517 |
| 2 | 0.796 | 0.727 | 57 | 0.632 |
| 5 | 0.891 | 0.818 | 48 | 0.792 |
| 10 | 0.928 | 0.879 | **50** | 0.859 |
| 20 | 0.955 | 0.864 | 48 | 0.910 |
| 30 | 0.963 | 0.879 | 48 | 0.926 |

실제 sign changes도 정확히 `50/65`이다.

따라서 null model에서 이상해 보였던 dyadic alternation은 **known zeta-zero oscillation이 매우 높은 설명력을 갖는다.**

---

## 8. 판정

### 닫는 해석

다음 명제는 현 단계에서 새 형성법칙 후보로 사용하지 않는다.

> 실제 prime 배열은 gap-permuted 배열보다 dyadic Möbius sign을 더 자주 반전시킨다.

그 자체는 수치적으로 참인 범위가 있지만, long-range dyadic alternation은 known zeta zeros의 log-frequency interference로 거의 직접 재현된다.

따라서 이를 다시 RH 증명에 사용하면

\[
\text{zeta zeros}
\to
M(2^k)\text{ alternation}
\to
\text{zeta zeros}
\]

형태의 순환이 된다.

### 남는 정보

Null-model audit은 쓸모가 있다.

1. 단순 밀도/gap 통계만으로는 실제 dyadic signal을 재현하지 못한다.
2. 그러나 그 잔여는 기존 zeta-zero phase structure가 설명한다.
3. 따라서 이후 새로운 candidate statistic은 **known zero-wave를 제거한 residual**에서 살아남아야 한다.

---

## 9. 다음 단계

다음 분석에서는 published `M(2^n)`에 대해 first `m` zero contribution을 제거한 residual

\[
R_m(k)
=
\frac{M(2^k)}{2^{k/2}}-Z_m(2^k)
\]

을 만든다.

그리고 다음을 감사한다.

1. `m=1,2,5,10,20,30` 증가에 따라 residual sign/correlation이 어떻게 사라지는가.
2. residual에 formation-layer statistic이 추가 설명력을 주는가.
3. 그 설명력이 zero data를 전혀 사용하지 않은 finite formation descriptor에서도 재현되는가.
4. 설명력이 사라지면 dyadic branch를 완전히 닫는다.

핵심 원칙은 **known zeta-zero component를 다시 발견하는 것을 새로운 형성규칙으로 세지 않는 것**이다.
