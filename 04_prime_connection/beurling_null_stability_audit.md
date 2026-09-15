# Beurling Null Rigidity and Zero-Stability Audit

Date: 2026-09-16

## 목적

기존 dyadic prime-gap permutation null이 실제 산술 구조를 얼마나 보존하는지 재평가하고, RH와 직접 논리적으로 연결되는 더 강한 null class를 정의한다.

핵심 구분은 다음 세 가지이다.

1. ordinary-prime system의 exact generalized-integer count `N_P(x)=floor(x)`가 갖는 강성,
2. ordinary primes `p_j`를 generalized primes `q_j`로 perturb했을 때 Euler-product zero set이 언제 보존되는지,
3. `|q_j-p_j|=O(sqrt(p_j))`를 보장하는 local gap shuffle로 `Re(s)>1/2` zero set을 정확히 보존하는 비자명 Beurling null을 구성할 수 있는지.

RH 자체는 `OPEN`이다.

---

## 1. exact integer-semigroup rigidity

Beurling generalized prime system `Q={q_j}`가 생성하는 generalized integers를 multiplicity까지 세어 `N_Q(x)`라 하자.

ordinary primes `P`에서는

\[
N_P(x)=\lfloor x\rfloor
\]

이 정확히 성립한다.

반대로 모든 `x>=1`에 대해

\[
N_Q(x)=\lfloor x\rfloor
\]

가 정확히 성립하면 generalized-integer multiset은 ordinary positive integers와 정확히 같다. 이 multiplicative monoid의 atoms는 ordinary primes뿐이므로 generalized-prime multiset도 ordinary primes와 정확히 같아야 한다.

따라서

\[
\boxed{
N_Q(x)=\lfloor x\rfloor\ \forall x
\quad\Longrightarrow\quad
Q=P.
}
\]

즉 exact integer-completeness와 unique-factorization structure를 보존하는 비자명 prime-position null은 존재하지 않는다.

상태: `EXACT / ELEMENTARY MONOID RIGIDITY`.

---

## 2. generalized-integer defect and additive zeta difference

\[
E_Q(x):=N_Q(x)-\lfloor x\rfloor
\]

로 두면 `Re(s)>1`에서 Stieltjes integration으로

\[
\zeta_Q(s)-\zeta(s)
=
\int_{1^-}^{\infty}x^{-s}\,dE_Q(x).
\]

경계항이 소거되는 범위에서

\[
\zeta_Q(s)-\zeta(s)
=
s\int_1^\infty E_Q(x)x^{-s-1}\,dx.
\]

따라서 `E_Q(x)=O(x^beta)`이면 additive difference는 `Re(s)>beta`로 analytic continuation된다.

그러나 additive closeness만으로 zero set은 보존되지 않는다. zero preservation에는 Euler-product ratio가 더 직접적이다.

---

## 3. prime-position perturbation zero-stability theorem

ordinary primes를 `p_j`, increasing generalized primes를 `q_j`라 하며 `q_j/p_j`가 위아래로 bounded되어 있다고 하자.

어떤 `theta<1`에 대해

\[
|q_j-p_j|\ll p_j^\theta
\]

가 충분히 큰 `j`에서 성립한다고 가정한다.

그러면

\[
\epsilon_j:=\log(q_j/p_j)=O(p_j^{\theta-1}).
\]

`Re(s)>1`에서

\[
H(s)
:=
\log\frac{\zeta_Q(s)}{\zeta(s)}
=
\sum_j\sum_{k\ge1}
\frac{q_j^{-ks}-p_j^{-ks}}{k}.
\]

compact set `Re(s)>=sigma>theta`에서 각 prime factor의 log-difference는

\[
\ll |\epsilon_j|p_j^{-\sigma},
\]

이고

\[
\sum_j |\epsilon_j|p_j^{-\sigma}
\ll
\sum_p p^{-1-(\sigma-\theta)}<\infty.
\]

따라서 `H(s)`는 `Re(s)>theta`에서 locally normally convergent analytic function으로 연장된다. 그러므로

\[
\boxed{
\zeta_Q(s)=\zeta(s)e^{H(s)}
\qquad (\operatorname{Re}s>\theta)
}
\]

이며 `e^{H(s)}`는 그 영역에서 zero-free이다.

결론:

\[
\boxed{
\zeta_Q\text{와 }\zeta\text{는 }\operatorname{Re}s>\theta
\text{에서 zero/pole divisor를 공유한다.}
}
\]

특히 `theta=1/2`이면

\[
\boxed{
\zeta_Q(s)=0\text{ in }\Re s>1/2
\iff
\zeta(s)=0\text{ in }\Re s>1/2.
}
\]

따라서 generalized system의 right-half-plane RH truth value가 classical RH와 정확히 같다.

상태: `DERIVED EXACT STABILITY THEOREM`; broader Beurling perturbation literature exists, novelty claim 없음.

---

## 4. square-root local gap null construction

각 dyadic block `[2^k,2^{k+1})`를 길이

\[
L_k=\lceil 2^{k/2}\rceil
\]

인 subblocks로 나눈다.

각 subblock `[a,b)` 안의 ordinary primes

\[
p_1<\cdots<p_m
\]

에 대해 anchor `a-1`에서 시작하는 positive gaps

\[
g_1=p_1-(a-1),\qquad g_i=p_i-p_{i-1}
\]

의 multiset을 그대로 유지하고 순서만 permutation한다. shuffled cumulative gaps로 pseudo-primes `q_i`를 정의한다.

그러면:

- channel count와 subblock endpoint는 보존된다.
- pseudo-primes는 strictly increasing이다.
- 모든 `p_j,q_j`는 같은 subblock 안에 있으므로

\[
|q_j-p_j|\le L_k=O(\sqrt{p_j}).
\]

따라서 Section 3의 theorem으로 이 null의 Beurling zeta는

\[
\boxed{
\zeta_Q(s)=\zeta(s)e^{H(s)},\qquad \Re s>1/2,
}
\]

이며 `Re(s)>1/2` zero set을 classical zeta와 정확히 공유한다.

이 null을 `SQRT-LOCAL RH-EQUIVALENT BEURLING NULL`이라 부른다.

---

## 5. 기존 dyadic-gap null에 대한 범위 정정

기존 null은 dyadic block 전체에서 gap order를 섞는다. 이는 local prime-density drift까지 파괴하므로 rank displacement가 단순 random-bridge `sqrt(P log P)`만으로 설명되지 않는다.

실제 finite audit에서 normalized displacement `RMS(|q-p|)/sqrt(P log P)`가 큰 dyadic blocks에서 증가했다. 따라서 기존 dyadic null을 `theta=1/2` stability class로 간주하면 안 된다.

판정:

- 기존 dyadic gap-null: 강한 falsification baseline이지만 RH-equivalent null이라는 보장은 없음.
- sqrt-local null: construction 자체가 `|q-p|=O(sqrt p)`를 강제하므로 zero-stability theorem을 exact하게 적용 가능.

---

## 6. finite numerical audit of sqrt-local null

20 fixed-seed samples, freeze `p<=100`.

`X=2^14,...,2^20`에서 generalized Möbius squarefree sum `M_Q(X)`를 계산했다.

| X | actual M(X) | null mean | null sd | actual z |
|---:|---:|---:|---:|---:|
| 2^14 | -32 | -29.25 | 3.447 | -0.798 |
| 2^15 | 26 | 28.40 | 5.246 | -0.458 |
| 2^16 | 14 | 13.95 | 5.236 | 0.010 |
| 2^17 | -20 | -29.20 | 7.083 | 1.299 |
| 2^18 | 24 | 8.60 | 11.232 | 1.371 |
| 2^19 | -125 | -125.95 | 17.866 | 0.053 |
| 2^20 | 257 | 257.95 | 21.279 | -0.045 |

현재 범위에서 classical Mertens endpoint는 RH-equivalent local-null family 안에서 특별한 outlier가 아니다.

이는 RH의 증거가 아니다. 오히려 finite Mertens 값 자체가 동일 right-half-plane zero divisor를 가진 generalized-prime systems 사이에서 상당히 움직일 수 있음을 보여준다.

### generalized-integer defect

같은 null에서 `N_Q(X)-X`는 exact 0이 아니지만 dyadic-global null보다 훨씬 작다.

| X | defect mean | defect sd | min | max |
|---:|---:|---:|---:|---:|
| 2^14 | 0.95 | 8.38 | -19 | 14 |
| 2^15 | -1.00 | 13.89 | -37 | 21 |
| 2^16 | -5.80 | 26.41 | -67 | 44 |
| 2^17 | -11.70 | 53.15 | -134 | 86 |
| 2^18 | -23.55 | 108.31 | -271 | 181 |

상태: `NUMERICAL ONLY`.

---

## 7. methodological consequence

이제 null은 두 층으로 분리한다.

### A. falsification null

prime density, gap multiset, selected low-order statistics를 보존하지만 zeta zero divisor 보존은 요구하지 않는다.

목적: 관측량이 단순 threshold/gap geometry로 재현되는지 검사.

### B. RH-equivalent Beurling null

`|q_p-p|=O(p^{1/2})` 또는 더 강한 weighted Mellin perturbation 조건을 만족하여 `Re(s)>1/2` zero divisor를 정확히 보존한다.

목적: proposed mechanism이 RH와 무관한 exact-prime microstructure에 의존하는지 검사.

중요한 방향 전환:

- falsification null에서 재현된다고 해서 RH mechanism 후보에서 자동 탈락시키는 것은 가능하다.
- RH-equivalent null에서 재현되는 것은 오히려 결격 사유가 아니다. zero-free property에 필요한 구조가 deformation-invariant일 가능성을 지지한다.
- 반대로 RH-equivalent null에서 사라지는 property는 classical primes에 특수한 충분조건일 수는 있지만, RH zero divisor 자체의 필수구조는 아니다.

---

## 8. literature audit

직접 관련 계보:

- Beurling generalized primes and associated zeta functions.
- Hilberdink--Lapidus, analytic properties / well-behaved generalized prime systems.
- Olofsson, properties of Beurling generalized primes and comparison of generalized integer counts with ordinary integers.
- Diamond--Montgomery--Vorhauer / Zhang, generalized-prime systems with RH or large oscillation.
- Neamah--Hilberdink, *The average order of the Möbius function for Beurling primes* (IJNT 2020): well-behaved exponents for `psi_P`, `N_P`, `M_P` satisfy that the two largest exponents coincide and are at least `1/2`.
- Broucke--Debruyne--Vindas and related work on Beurling systems satisfying RH with nonclassical generalized-integer behavior.

A targeted search found perturbation/stability questions and closely related Beurling constructions, but no source was identified in this audit that states exactly the above `|q_j-p_j|=O(p_j^theta) => same zero divisor in Re(s)>theta` formulation. Treat this as a derived lemma, not a novelty claim.

---

## 9. current verdict

The previous `gap-null = fake prime system` interpretation is refined as follows.

\[
\boxed{
\text{prime-position perturbation exponent }\theta
\Longrightarrow
\text{zero-divisor stability for }\Re s>\theta.
}
\]

The critical square-root scale `theta=1/2` therefore has a direct analytic meaning independent of a finite regression fit.

This creates a new audit rule:

`BEURLING ZERO-STABILITY GUARD` — any proposed prime-placement mechanism should state whether it is invariant under `O(sqrt p)` generalized-prime perturbations. If not, it uses information finer than what is required to preserve the RH right-half-plane zero divisor.

This does not prove RH. It narrows which arithmetic information can be structurally necessary for RH.