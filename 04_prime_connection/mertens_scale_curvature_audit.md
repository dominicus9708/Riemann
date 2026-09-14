# Mertens Multiplicative Scale-Curvature Audit

## 목적

prime-divisibility masks와 linear/tensor variance가 sieve-density barrier로 닫힌 뒤, divisibility basis에 직접 환원되지 않는 phase-sensitive cross-scale observable을 시험한다.

고정 `a>1`에 대해

\[
\boxed{
K_a(X)=M(X/a)^2-M(X)M(X/a^2)
}
\]

를 정의한다. 정수 입력에서는 `M(y)=M(floor(y))` convention을 쓴다.

log variable에서 `X=a e^u`, `h=log a`, `F(u)=M(e^u)`라 쓰면

\[
K_a(X)=F(u)^2-F(u+h)F(u-h),
\]

즉 multiplicative scale sequence의 `2x2` Hankel/Turan형 determinant다.

핵심 질문:

1. 단일 power mode를 제거하면서 서로 다른 spectral mode의 interference만 남기는가?
2. zero real part를 사전에 `1/2`로 두지 않고 growth exponent가 스스로 나타나는가?
3. 이것이 새 arithmetic bound를 주는가, 아니면 기존 weak-Mertens / zero-energy를 다시 표현하는가?

---

## 1. finite spectral identity

유한 exponential sum

\[
f(u)=\sum_{j=1}^m c_j e^{\lambda_j u}
\]

에 대해

\[
\mathcal K_h[f](u)=f(u)^2-f(u+h)f(u-h)
\]

를 둔다.

각 diagonal `j=j`는 정확히 소거되고, pair `j<k`만 남아

\[
\boxed{
\mathcal K_h[f](u)
=-4\sum_{j<k}
 c_jc_k e^{(\lambda_j+\lambda_k)u}
\sinh^2\!\left(\frac{(\lambda_j-\lambda_k)h}{2}\right).
}
\]

따라서 **single power / single exponential mode는 real part와 무관하게 exact kernel에 들어간다.**

상태: `EXACT`.

---

## 2. conjugate-pair positivity

real-valued signal에서

\[
\lambda=\beta+i\gamma,
\qquad
\bar\lambda=\beta-i\gamma,
\qquad
c_{\bar\lambda}=\bar c_\lambda
\]

인 conjugate pair의 기여는

\[
\boxed{
4|c_\lambda|^2 e^{2\beta u}\sin^2(\gamma h)\ge0.
}
\]

원래 변수에서는 `u=log(X/a)`이므로

\[
\boxed{
K_{a,\lambda,\bar\lambda}(X)
=4|c_\lambda|^2
\left(\frac Xa\right)^{2\beta}
\sin^2(\gamma\log a).
}
\]

따라서 finite spectral model에서는 conjugate pair가 실수부 `beta`를 **quadratic growth exponent `2 beta`**로 바꾼다.

이 단계에는 `beta=1/2`를 넣지 않았다.

---

## 3. spectral-abscissa detector — finite model only

finite conjugation-closed spectrum에서 최대 실수부를

\[
\beta_* = \max_j \Re\lambda_j
\]

라 하자.

최상위 `beta_*`를 갖는 nonreal modes가 있고 `sin(gamma log a) != 0`인 scale을 택하면 conjugate-pair sector는 `X^(2 beta_*)` scale을 가진다.

따라서 finite-mode truncation에서는 growth scan

\[
|K_a(X)|\sim X^{\alpha}
\]

가 `alpha/2`를 spectral real-part candidate로 읽는 구조를 제공한다.

그러나 전체 infinite zero spectrum에서는

- cross-pair cancellation,
- zero multiplicity,
- explicit-formula convergence,
- supremum이 attained되는지 여부,
- fixed scale의 accidental `sin(gamma log a)=0`,

를 별도 처리해야 한다.

따라서 이 항목은 `FINITE_SPECTRAL_EXACT / FULL_ZETA_OPEN`이다.

---

## 4. two-scale blind-spot removal

한 fixed `a`는 특정 frequency에서

\[
\sin(\gamma\log a)=0
\]

이 되어 conjugate mode를 놓칠 수 있다.

그러나 `a=2,3`을 함께 쓰면 nonzero `gamma`에 대해 두 sine이 동시에 정확히 zero일 수 없다.

그렇다면 integers `m,n`에 대해

\[
\gamma\log2=m\pi,
\qquad
\gamma\log3=n\pi
\]

이어야 하므로 `log2/log3=m/n`이 rational이어야 하는데, `2^n=3^m`은 양의 integers에서 불가능하다.

따라서 finite spectrum에서는

\[
K_2+K_3
\]

의 conjugate-pair coefficient가 모든 nonreal frequency에 대해 strictly positive하다.

주의: 이것은 total cross-pair cancellation까지 제거한다는 뜻이 아니다.

상태: `EXACT_LOCAL_COEFFICIENT_STATEMENT`.

---

## 5. RH-line specialization and autocorrelation

RH를 **가정해서 해석할 때만**

\[
M(e^t)=e^{t/2}G(t)
\]

로 쓰면

\[
\frac{K_a(X)}{X/a}
=G(u)^2-G(u+h)G(u-h),
\qquad h=\log a.
\]

log-Cesaro 평균이 존재하고 shift boundary가 무시 가능한 stationary/mean-square regime에서는 이것은 autocorrelation defect

\[
R(0)-R(2h)
\]

이며

\[
R(0)-R(2h)
=\frac12\,\langle (G(t+h)-G(t-h))^2\rangle\ge0.
\]

즉 장기평균 curvature는 새 sign law가 아니라 normalized Mertens signal의 **second-order structure function / spectral energy**다.

---

## 6. zero-residue mean formula

simple RH zeros

\[
\rho=\frac12+i\gamma
\]

의 finite explicit-formula truncation에서

\[
c_\rho=\frac1{\rho\zeta'(\rho)}
\]

라 두면, distinct non-aliased frequencies에 대한 long log-average는 cross-frequency terms를 제거하고 conjugate energy를 남긴다.

따라서

\[
\boxed{
\left\langle\frac{K_a(X)}X\right\rangle
=\frac4a\sum_{\gamma>0}
\frac{\sin^2(\gamma\log a)}{|\rho\zeta'(\rho)|^2}
}
\]

가 finite zero truncation에서 exact하고, infinite sum으로의 passage는 별도 convergence assumptions가 필요하다.

`a=2`에서는

\[
\boxed{
\left\langle\frac{K_2(X)}X\right\rangle
=2\sum_{\gamma>0}
\frac{\sin^2(\gamma\log2)}{|\rho\zeta'(\rho)|^2}.
}
\]

이 식이 weak Mertens / negative moments of `zeta'` 문헌과 직접 만난다.

---

## 7. published M(2^k) numerical audit

저장된 published dyadic Mertens data

```text
data/mertens/mertens_powers_of_two_0_75.csv
```

에서

\[
K_2(2^k)=M(2^{k-1})^2-M(2^k)M(2^{k-2})
\]

를 `k=10..75`에 계산했다.

결과:

- samples: `66`.
- positive `K_2`: `54/66 = 0.81818...`.
- mean `K_2(2^k)/2^k`: `0.0107178611908`.
- RMS `|K_2|/2^k`: `0.019190...` (finite-sample descriptive statistic).
- ordinary least-squares slope of `log2 |K_2|` against `k`, `k=10..75`: `0.99925846`, corresponding naive `beta_eff = 0.49962923`.
- Theil-Sen slope on the same interval: `0.99828010`, with approximate slope interval `[0.97703496, 1.01973951]` from the implementation used in the audit.

이 finite regression은 proof가 아니다. 특히 late windows에서 slope가 크게 흔들린다.

그럼에도 `1/2`를 regression target으로 넣지 않았을 때 전체 published dyadic range에서 quadratic exponent가 near `1`로 나오는 것은 **NUMERICAL diagnostic**으로 보존한다.

---

## 8. known-zero energy reconstruction

알려진 critical-line zeros와 `zeta'(rho)`를 직접 사용해 위 energy sum을 계산했다.

`a=2`에서 first `m` zeros contribution:

| m | predicted mean K2/X |
|---:|---:|
| 1 | 0.00210684620 |
| 2 | 0.00498722174 |
| 5 | 0.00799527545 |
| 10 | 0.00887009489 |
| 20 | 0.00954079977 |
| 30 | 0.00982619968 |
| 50 | 0.01014720153 |
| 75 | 0.01031011842 |
| 100 | 0.01039876235 |

published `k=10..75` empirical mean is

\[
0.01071786119.
\]

first-100-zero energy predictionとの差는 약 `3.07%` of the predicted value.

따라서 curvature mean의 대부분은 이미 known zeta-zero spectral energy로 직접 재구성된다.

### 판정

\[
\boxed{
\text{dyadic scale curvature의 평균 신호는 새로운 formation law가 아니라 known zero energy의 재표현이다.}
}
\]

---

## 9. weak Mertens barrier

Weak Mertens Conjecture는

\[
\int_1^X\left(\frac{M(x)}x\right)^2dx\ll\log X.
\]

`x=e^t`를 넣으면 정확히

\[
\int_0^{\log X}\left(e^{-t/2}M(e^t)\right)^2dt\ll\log X,
\]

즉 RH-normalized log signal `G(t)`의 mean-square control이다.

Titchmarsh 계열의 고전 결과에 따르면 이 weak Mertens condition은 RH뿐 아니라 nontrivial zeros의 simplicity 및

\[
\sum_\rho \frac1{|\rho\zeta'(\rho)|^2}<\infty
\]

도 함의한다.

Ng (2004)는 RH와 Gonek-Hejhal-type negative-moment assumptions 아래 더 강한 mean-square asymptotic / limiting-distribution 결과를 연구한다.

따라서 curvature long-average를 직접 uniform하게 제어하려는 경로는 이미 weak-Mertens spectral-energy 난점과 매우 가깝다.

### 핵심 감사

- curvature가 phase-sensitive인 것은 맞다.
- single mode cancellation과 conjugate-pair positivity도 exact하다.
- 그러나 long-average positivity는 essentially autocorrelation / second-order energy다.
- 이를 RH-scale에서 bound하는 독립 arithmetic mechanism을 아직 얻지 못했다.

따라서 현재 branch는 `SPECTRAL_REENCODING`, 증명경로는 `OPEN_BUT_NO_INDEPENDENT_BOUND`로 둔다.

---

## 10. 선행문헌 중복 감사

Targeted search에서 exact observable

\[
M(X/a)^2-M(X)M(X/a^2)
\]

를 RH criterion으로 사용하는 표준 published 경로는 현재까지 직접 확인하지 못했다.

그러나 다음 overlap은 강하다.

1. Nathan Ng (2004): `M(e^t)e^{-t/2}`의 limiting distribution과 weak-Mertens mean square를 zero residues와 연결.
2. Titchmarsh weak Mertens theory: mean-square control이 RH + simple zeros + reciprocal-derivative square-summability를 강제.
3. recent explicit-Laplace-transform work: smoothed Möbius sums를 zero-expansion 및 RH criteria와 연결.
4. Hankel determinants 자체를 RH와 연결하는 다른 최근 preprints도 존재하므로, **Hankel determinant라는 명칭 자체의 novelty는 주장하지 않는다.**

따라서 신규성 검토 대상은 오직 이 multiplicative-scale `2x2` determinant의 exact pair filter identity뿐이며, 그것도 현재는 novelty claim을 보류한다.

---

## 11. 다음 전선

raw curvature mean은 known zero-energy를 재현하므로 그대로는 닫는다.

남길 수 있는 질문은 하나다.

\[
\boxed{
\text{known spectral-energy prediction을 제거한 curvature residual에
zero data를 사용하지 않는 arithmetic cross-scale constraint가 남는가?}
}
\]

다음 단계에서는

1. `a=2`에 고정하지 않고 several scales를 사용,
2. each scale의 zero-energy / finite sampling effect를 구분,
3. arithmetic-only predictor가 residual을 설명하는지 검사,
4. 설명력이 zero-wave를 재발견하는 것이라면 branch를 완전히 종료한다.

---

## 상태

- finite exponential pair identity: `EXACT`.
- conjugate-pair positivity: `EXACT`.
- finite-spectrum real-part growth detector: `EXACT_FINITE_MODEL`.
- full zeta-spectrum detector theorem: `OPEN / REQUIRES_ANALYTIC_CONTROL`.
- dyadic `beta_eff ~ 1/2`: `NUMERICAL`.
- first-100-zero reconstruction of mean curvature: `NUMERICAL / ZERO-INFORMED`.
- independent RH progress: `NOT_ESTABLISHED`.
- RH: `OPEN`.
