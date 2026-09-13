# Richter Linear-Variance Barrier Audit

## 목적

Florian K. Richter의 elementary PNT dynamics

\[
\mathbb E_{n\le N}f(\Omega(n)+1)
=
\mathbb E_{n\le N}f(\Omega(n))+o(1)
\]

을 RH-scale로 단순 정량강화할 수 있는지 감사한다.

핵심은 proof의 gcd-variance/Cauchy--Schwarz 단계가 finite `N`에서 가질 수 있는 최선의 scale을 분리하는 것이다.

---

## 1. Richter proof의 variance object

Richter Proposition 2.1은 finite set `B`에 대해 divisibility-count variance를 gcd kernel

\[
\Phi(m,n)=\gcd(m,n)-1
\]

로 표현한다.

Proposition 2.2에서는 prime set `B_1`과 `k`-almost-prime set `B_2`를 만들어 normalized logarithmic gcd energy가 `<=eta`가 되게 한다.

최종 proof는 Cauchy--Schwarz를 거쳐

\[
\mathbb E f(\Omega(n)+k)
-
\mathbb E f(\Omega(n)+l)
=
O(\eta^{1/2}+N^{-1/2})
\]

형태를 얻고, **eta를 먼저 고정한 뒤** `N->infinity`, 이후 `eta->0`으로 보내 PNT 수준 `o(1)`을 얻는다.

이 quantifier order는 RH급 uniform bound와 다르다.

---

## 2. prime set의 exact diagonal obstruction

`B_1`이 소수만으로 이루어졌다고 하자.

로그 평균의 harmonic mass를

\[
H(B_1)=\sum_{p\in B_1}\frac1p
\]

라고 두면 distinct primes에서는 `Phi(p,q)=0`이고 diagonal에서 `Phi(p,p)=p-1`이므로

\[
E(B_1)
=
\mathbb E^{\log}_{p,p'\in B_1}\Phi(p,p')
=
\frac{\sum_{p\in B_1}(p-1)/p^2}{H(B_1)^2}.
\]

모든 prime `p>=2`에 대해

\[
\frac{p-1}{p^2}
=\frac1p-\frac1{p^2}
\ge \frac1{2p}.
\]

따라서 exact lower bound

\[
\boxed{
E(B_1)\ge\frac1{2H(B_1)}.
}
\]

그러므로 Proposition 2.2(c)의 `E(B_1)<=eta`를 만족하려면 반드시

\[
\boxed{
H(B_1)\ge\frac1{2\eta}.
}
\]

---

## 3. finite-N quantitative obstruction

finite-N dilation averages `n<=N/p`를 실제로 사용하려면 quantitative application에서 relevant primes는 `p<=N` 범위에 있어야 한다.

고전적인 reciprocal-prime bound로

\[
\sum_{p\le N}\frac1p=O(\log\log N).
\]

따라서

\[
H(B_1)\le O(\log\log N),
\]

그리고 위 lower bound와 결합하면

\[
\boxed{
\eta\gtrsim\frac1{\log\log N}.
}
\]

Cauchy--Schwarz 단계에서는 error가 `sqrt(eta)`로 들어가므로

\[
\boxed{
\text{linear gcd-variance mechanism의 natural floor}
\ \gtrsim\ (\log\log N)^{-1/2}.
}
\]

이 scale은 normalized Liouville/Möbius sum에 RH가 요구하는

\[
N^{-1/2+\varepsilon}
\]

와 polynomially 멀다.

---

## 4. arbitrary linear weighting도 개선하지 못한다

이 장벽은 Richter의 `1/p` choice만의 문제가 아니다.

centered prime-divisibility probe를

\[
Y_p(n)=p\,1_{p\mid n}-1
\]

로 두면 asymptotically

\[
\mathbb E Y_p=0,
\qquad
\operatorname{Var}(Y_p)=p-1,
\qquad
\operatorname{Cov}(Y_p,Y_q)=0\quad(p\ne q).
\]

임의의 normalized linear weights

\[
Z(n)=\sum_{p\in\mathcal P}\beta_pY_p(n),
\qquad
\sum_p\beta_p=1
\]

에 대해

\[
\operatorname{Var}(Z)=\sum_p\beta_p^2(p-1).
\]

Cauchy--Schwarz로

\[
1
=\left(\sum_p\beta_p\right)^2
\le
\left(\sum_p\beta_p^2(p-1)\right)
\left(\sum_p\frac1{p-1}\right).
\]

따라서

\[
\boxed{
\operatorname{Var}(Z)
\ge
\frac1{\sum_{p\in\mathcal P}1/(p-1)}.
}
\]

최적 weights는

\[
\beta_p\propto\frac1{p-1}\sim\frac1p.
\]

즉 Richter의 logarithmic prime weighting은 **linear prime-divisibility probes 안에서 variance-optimal에 가깝다.**

`log p/p` 등으로 total mass를 키우는 단순 수정은 이 lower bound를 우회하지 못한다.

---

## 5. 현대 quantitative benchmark

Charamaras--Richter, *Asymptotic independence of Omega(n) and Omega(n+1) along logarithmic averages*의 2026-08-19 arXiv version은 two-point logarithmic independence에 대해

\[
O\left(\frac{(\log\log\log N)^2}{\sqrt{\log\log N}}\right)
\]

을 주고, Appendix alternative argument가

\[
\boxed{O(1/\sqrt{\log\log N})}
\]

의 optimal error scale을 준다고 명시한다.

이는 별개의 theorem이지만, prime-divisibility / Omega-distribution dynamics에서 `sqrt(log log N)` fluctuation scale이 실제 quantitative barrier로 반복 출현한다는 강한 교차기준이다.

---

## 6. formation audit 판정

### 닫는 경로

1. Richter의 PNT shift-invariance에서 `eta=eta(N)`만 더 작게 잡아 RH를 얻는다.
2. prime weights를 다른 **선형** weights로 최적화해 `log log N`을 `log N`으로 바꾼다.
3. 1-prime-channel variance/Cauchy--Schwarz만으로 square-root cancellation을 강제한다.

이 셋은 위 inverse-variance lower bound 때문에 구조적으로 불충분하다.

### 살아 있는 방향

RH급 polynomial cancellation을 얻으려면 적어도 하나가 필요하다.

- nonlinear multi-prime probes,
- high-order signed interactions,
- linear variance가 보지 못하는 phase-sensitive structure,
- 또는 prime-axis harmonic mass를 단순 합하는 것과 다른 deterministic cancellation mechanism.

이는 earlier derivative-energy audit에서 low-order suppression이 order `3--5` interaction으로 이동한 현상과 정합적이다.

단, 그 derivative-energy transfer 자체는 gap-permuted threshold null에서도 재현되므로 **일반 high-order interaction이면 충분하지 않고 actual arithmetic high-order interaction이어야 한다.**

---

## 선행문헌

- Florian K. Richter (2021), *A New Elementary Proof of the Prime Number Theorem*, Bulletin of the London Mathematical Society 53, 1365--1375, DOI 10.1112/blms.12503.
- Dimitrios Charamaras & Florian K. Richter (2024--2026), *Asymptotic independence of Omega(n) and Omega(n+1) along logarithmic averages*, arXiv:2412.17583.
