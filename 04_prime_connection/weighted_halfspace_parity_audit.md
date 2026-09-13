# Weighted Halfspace Parity Audit

## 목적

squarefree formation cutoff

\[
f_X(\varepsilon)=\mathbf 1_{\prod_{j=1}^{m}p_j^{\varepsilon_j}\le X},
\qquad m=\pi(X),
\]

를 Boolean weighted-threshold function으로 보고, Möbius/Mertens cancellation이 어떤 Fourier coefficient에 해당하는지 정확히 고정한다.

또 일반 halfspace Fourier/noise-stability 정리가 RH scale에 충분한지 감사하고, prime-label 정보를 보존하는 multivariate derivative hierarchy를 수치검사한다.

---

## 1. exact Boolean-Fourier representation

Boolean character를

\[
\chi_A(\varepsilon)=(-1)^{\sum_{p\in A}\varepsilon_p}
\]

로 두고 uniform normalized Fourier coefficient를

\[
\widehat f_X(A)=2^{-m}\sum_{\varepsilon\in\{0,1\}^m}f_X(\varepsilon)\chi_A(\varepsilon)
\]

로 둔다.

모든 squarefree `n<=X`는 첫 `m=pi(X)`개 prime의 유일한 subset에 대응하므로

\[
\boxed{2^m\widehat f_X([m])=M(X)}
\]

이고 constant coefficient는

\[
\boxed{2^m\widehat f_X(\varnothing)=Q(X)}
\]

이다. 여기서

\[
Q(X)=\sum_{n\le X}\mu(n)^2
\]

는 squarefree counting function이다.

따라서

\[
\boxed{
\frac{\widehat f_X([m])}{\widehat f_X(\varnothing)}
=\frac{M(X)}{Q(X)}.
}
\]

`Q(X)~(6/pi^2)X`이므로:

- PNT와 동치인 `M(X)=o(X)`는 top parity coefficient가 density에 비해 `o(1)`이 되는 것과 동치다.
- RH와 동치인 `M(X)=O_epsilon(X^(1/2+epsilon))`는 훨씬 강한 quantitative parity decorrelation이다.

즉 RH target은

\[
\boxed{
|\widehat f_X([m])|
\le 2^{-m}X^{1/2+\varepsilon}
}
\]

(up to epsilon-dependent constants) 형태다.

---

## 2. Richter--Kalai 선행 연결

Florian K. Richter의 2021년 elementary PNT proof는 bounded `g`에 대해

\[
\frac1N\sum_{n\le N}g(\Omega(n)+1)
=
\frac1N\sum_{n\le N}g(\Omega(n))+o(1)
\]

을 증명하고 PNT를 도출한다.

Gil Kalai는 이 논문을 소개하면서 weights `w_j=log p_j`, threshold `log X`인 weighted-majority function의 top Fourier coefficient가 density에 비해 `o(1)`이 되는 조건을 PNT의 Boolean-Fourier 표현으로 명시적으로 지적했다.

감사 판정:

- Boolean weighted-halfspace formulation 자체를 신규 관점으로 주장하지 않는다.
- 현재 탐색의 차별점은 PNT 수준 `o(1)`가 아니라 RH 수준 `X^(-1/2+epsilon)` relative cancellation을 어떤 formation constraint가 강제하는지에 둔다.

---

## 3. 일반 halfspace noise-stability 정리의 정량 장벽

Peres의 weighted-majority theorem은 noise rate `eta`에서 noise sensitivity를 `O(sqrt(eta))`로 제어한다.

Fourier 표현에서 `eta~1/d`를 선택하면 weighted majority의 degree `>=d` Fourier weight에 대략 `O(d^(-1/2))` 형태의 일반 상계가 나온다. 따라서 개별 degree-`m` coefficient에는 대략 polynomial-in-`m` 상계만 기대할 수 있다.

그러나 현재 arithmetic halfspace의 density 자체가

\[
\widehat f_X(\varnothing)=Q(X)2^{-m}
\]

로 exponentially small in `m`이다.

따라서 일반 halfspace spectral/noise bound는 이 rare-event regime에서 trivial density bound보다도 훨씬 약하며 RH target과는 거리가 크다.

Diakonikolas--Jaiswal--Servedio--Tan--Wan의 halfspace Fourier-spectrum concentration도 중요한 일반 구조 기준이지만, 이 arithmetic endpoint parity coefficient를 RH scale로 자동 제어하지 않는다.

---

## 4. multivariate formation polynomial

prime-label 정보를 보존하기 위해

\[
P_X(z)=
\sum_{\substack{n\le X\\\mu(n)^2=1}}
\prod_{p\mid n}z_p
\]

를 둔다.

Möbius corner는

\[
P_X(-\mathbf 1)=M(X).
\]

squarefree `a=prod_{p in A}p`에 대해 mixed derivative는 정확히

\[
\boxed{
\partial_A P_X(-\mathbf1)
=
\sum_{\substack{r\le X/a\\(r,a)=1}}\mu(r).
}
\]

즉 `k`차 local derivative는 `k`개의 지정 prime channel을 고정한 coprime Mertens sum이다.

이 값은 단순 `A_k(X)` layer count와 달리 실제 prime labels를 보존한다.

---

## 5. local derivative energy와 random-character baseline

정의:

\[
\mathcal E_k^{\mu}(X)
=
\sum_{\substack{a\le X\\\mu(a)^2=1\\\omega(a)=k}}
\left|
\sum_{\substack{r\le X/a\\(r,a)=1}}\mu(r)
\right|^2.
\]

Boolean character `r_p in {+1,-1}`를 uniform random하게 고르면 orthogonality로

\[
\boxed{
\mathbb E_r\,\mathcal E_k(r;X)
=
\overline{\mathcal E}_k(X)
=
\sum_{n\le X}\mu(n)^2\binom{\omega(n)}k.
}
\]

따라서 ratio

\[
R_k(X)=\frac{\mathcal E_k^{\mu}(X)}{\overline{\mathcal E}_k(X)}
\]

는 all-minus Möbius corner가 random-character ensemble에 비해 해당 derivative order에서 얼마나 flat/rough한지 측정한다.

### X = 2^20

계산 결과:

| k | R_k |
|---:|---:|
| 0 | 0.103613 |
| 1 | 0.127918 |
| 2 | 0.402506 |
| 3 | 1.887347 |
| 4 | 3.731623 |
| 5 | 2.305535 |
| 6 | 0.941261 |
| 7 | 1.000000 |

해석:

- `k=0`: value `M(X)` 자체는 ensemble RMS보다 작다.
- `k=1,2`: gradient/Hessian-level energy도 강하게 억제된다.
- `k=3,4,5`: 반대로 Möbius corner의 derivative energy가 ensemble 평균보다 커진다.
- 따라서 Möbius corner가 **모든 차수에서 uniformly flat**하다는 가설은 거짓이다.

저차 suppression은 사라진 것이 아니라 중간 고차 interaction으로 재배치된다.

---

## 6. cutoff stability

`X=2^14,...,2^20`에서 주요 ratio:

| X | R0 | R1 | R2 | R3 | R4 |
|---:|---:|---:|---:|---:|---:|
| 16384 | 0.102791 | 0.143395 | 1.233114 | 2.513926 | 1.198529 |
| 32768 | 0.033936 | 0.202643 | 0.870732 | 2.729107 | 1.678186 |
| 65536 | 0.004919 | 0.136304 | 0.820808 | 2.547458 | 2.315394 |
| 131072 | 0.005020 | 0.118170 | 0.702949 | 2.423072 | 2.837744 |
| 262144 | 0.003614 | 0.116718 | 0.572932 | 2.292704 | 3.242128 |
| 524288 | 0.049023 | 0.101835 | 0.510646 | 2.024463 | 3.646092 |
| 1048576 | 0.103613 | 0.127918 | 0.402506 | 1.887347 | 3.731623 |

`R1` suppression은 이 범위에서 비교적 안정적이고 `R2`도 감소하지만, `R3-R4` enhancement가 동시에 존재한다.

---

## 7. 현재 판정

### 닫힌 단순 후보

1. `M(X)`를 일반 halfspace high-degree Fourier concentration만으로 제어한다.
   - rare-event density scale을 반영하지 못해 너무 약하다.
2. Möbius corner가 모든 derivative order에서 unusually flat하다고 가정한다.
   - `k=3,4,5` 데이터가 직접 반박한다.
3. low-order Sobolev/gradient control만으로 endpoint `P_X(-1)`을 제어한다.
   - interaction energy가 higher orders로 이동하므로 닫히지 않는다.

### 살아 있는 질문

저차 energy suppression과 중간차 energy enhancement 사이에 **signed conservation/transfer law**가 존재하는가?

즉

\[
R_0,R_1,R_2<1,
\qquad
R_3,R_4,R_5>1
\]

이라는 재배치가 단순 finite-size artifact인지, threshold boundary의 정확한 interaction flow인지 검사할 필요가 있다.

이 다음 단계에서는 derivative-energy generating function

\[
\mathcal G_X(t)
=
\sum_{k\ge0}t^k\mathcal E_k^{\mu}(X)
\]

을 사용해 order 간 energy transfer를 하나의 동역학적 양으로 묶고, random-character baseline

\[
\overline{\mathcal G}_X(t)
=
\sum_{n\le X}\mu(n)^2(1+t)^{\omega(n)}
\]

과 비교한다.

---

## 재현자료

```text
data/formation/mobius_corner_derivative_energy_2pow14_20.csv
scripts/audit_mobius_corner_derivative_energy.py
```

## 선행문헌

- Florian K. Richter (2021), *A new elementary proof of the Prime Number Theorem*, Bull. London Math. Soc. 53, 1365--1375, DOI 10.1112/blms.12503.
- Yuval Peres (2004/2021), *Noise Stability of Weighted Majority*, arXiv:math/0412377; later book-chapter publication.
- I. Diakonikolas, R. Jaiswal, R. A. Servedio, L.-Y. Tan, A. Wan (2012), *On the Distribution of the Fourier Spectrum of Halfspaces*, arXiv:1202.6680.
- Gil Kalai (2020), expository blog discussion of Richter's proof and the weighted-majority/top-Fourier-coefficient PNT formulation. Use as commentary, not as a primary theorem source.
