# Prime-Activation Cross-Scale Coherence Audit

Date: 2026-09-15

## 목적

Formation prime activation의 마지막 남은 후보인 cross-scale parity coherence를 감사한다.

소수 `p`를 활성화할 때 같은 이전 generator state를 두 cutoff `X`와 `X/p`에서 비교하고,

- exact normalized-bias recursion,
- exact variance/dissipation identity,
- full recursive variance-tree identity,
- dyadic prime-gap permutation null,
- cutoff stability

를 함께 검사한다.

RH 자체는 `OPEN`이다.

---

## 1. exact activation recursion

`p` 직전까지의 allowed squarefree states에 대해

\[
F_0=F_{p^-}(X),\qquad Q_0=Q_{p^-}(X),
\]

\[
F_1=F_{p^-}(X/p),\qquad Q_1=Q_{p^-}(X/p)
\]

로 둔다.

`p`를 포함하는 새 state는 `pm`이고 Möbius parity가 뒤집히므로

\[
\boxed{F_p(X)=F_0-F_1},\qquad
\boxed{Q_p(X)=Q_0+Q_1}.
\]

normalized bias를

\[
r_0=F_0/Q_0,\qquad r_1=F_1/Q_1,
\]

\[
a=\frac{Q_0}{Q_0+Q_1},\qquad b=\frac{Q_1}{Q_0+Q_1}
\]

로 두면

\[
\boxed{r_p=a r_0-b r_1}.
\]

또

\[
r_p=(a-b)r_0-b(r_1-r_0),
\]

이므로 activation은 homogeneous shrink factor와 cross-scale mismatch source로 정확히 분리된다.

상태: `EXACT`.

---

## 2. exact parity-dissipation identity

직접 전개하면

\[
\boxed{
a r_0^2+b r_1^2-r_p^2
=ab(r_0+r_1)^2\ge0.
}
\]

따라서

\[
\boxed{r_p^2\le a r_0^2+b r_1^2}.
\]

parity random variable `chi in {+1,-1}`의 variance로 쓰면

\[
\boxed{
1-r_p^2
=a(1-r_0^2)+b(1-r_1^2)+D_p(X)
}
\]

where

\[
\boxed{D_p(X)=ab(r_0+r_1)^2.}
\]

`D_p`는 임의 statistic이 아니라 law of total variance의 between-branch variance다.

하지만 strict contraction은 아니다. `r_1=-r_0`이면 `D_p=0`이고 `r_p=r_0`이 가능하다.

상태: `EXACT`.

---

## 3. full recursive variance tree

위 split을 이전 prime들에 대해 각 branch에서 재귀적으로 반복한다.

root는 최종 squarefree state set이며

\[
r_{\rm root}=M(X)/Q(X).
\]

각 internal node `v`에서 node mass fraction을 `pi_v`, local branch weights를 `a_v,b_v`, child bias를 `r_{v,0},r_{v,1}`이라 하면 leaves에서는 parity가 deterministic이므로 conditional variance가 0이다.

law of total variance를 tree 전체에 telescoping하면

\[
\boxed{
1-\left(\frac{M(X)}{Q(X)}\right)^2
=
\sum_{v\,\mathrm{internal}}
\pi_v a_vb_v(r_{v,0}+r_{v,1})^2.
}
\]

따라서 full-tree total dissipation은 Mertens cancellation을 새로 설명하는 독립 invariant가 아니라 **동일한 endpoint variance의 exact decomposition**이다.

RH scale `M(X)=O(X^{1/2+epsilon})`, `Q(X)~6X/pi^2`를 이 표현으로 얻으려면 total dissipation이 `1-O(X^{-1+2epsilon})`까지 포화됨을 별도로 증명해야 한다. 그 nodewise lower bound가 바로 새 난점이다.

상태: `EXACT / REENCODING BARRIER`.

---

## 4. prime-specific numerical test

### null model

기존 formation audits와 동일하다.

- actual primes `p<=100` 고정,
- 이후 각 dyadic block에서 actual prime-gap multiset 보존,
- gap 순서만 shuffle,
- pseudo-generators를 independent Boolean channels로 사용,
- product cutoff 유지,
- all-minus parity character 유지.

prime label이 quotient scale에서도 실제로 보이는 구간만 검사하기 위해

\[
100<p\le\sqrt X
\]

로 제한했다.

각 channel에서

\[
C_p=r_0+r_1,\qquad
R_p=r_1-r_0,\qquad
D_p=abC_p^2
\]

를 계산했다.

20 fixed-seed null samples를 사용했다.

---

## 5. X = 2^18 result

label-visible movable channels: `72`.

### profile multiple-comparison audit

| observable | actual max abs z | null max exceed | actual mean z^2 | null mean-z^2 exceed |
|---|---:|---:|---:|---:|
| `r0` | 2.3429 | 0.30 | 2.1477 | 0.20 |
| `r1` | 2.7705 | 0.45 | 1.2378 | 0.45 |
| `C=r0+r1` | 2.8742 | 0.40 | 1.2975 | 0.35 |
| `R=r1-r0` | 2.4560 | 0.65 | 1.2133 | 0.45 |
| `D` | 2.9616 | 0.35 | 1.3691 | 0.35 |

### aggregate statistics

| statistic | actual | null mean | null sd | z | null >= actual |
|---|---:|---:|---:|---:|---:|
| mean `D` | 1.2951168e-4 | 1.3062159e-4 | 2.54288e-6 | -0.4365 | 0.65 |
| RMS `C` | 0.0818370 | 0.0817979 | 0.00083287 | +0.0470 | 0.55 |
| RMS `R` | 0.1265212 | 0.1258814 | 0.00265514 | +0.2410 | 0.50 |

판정: prime-specific cross-scale signal 없음.

---

## 6. X = 2^20 result

label-visible movable channels: `147`.

### profile multiple-comparison audit

| observable | actual max abs z | null max exceed | actual mean z^2 | null mean-z^2 exceed |
|---|---:|---:|---:|---:|
| `r0` | 2.6424 | 0.20 | 3.4642 | 0.05 |
| `r1` | 2.9349 | 0.65 | 1.7921 | 0.05 |
| `C=r0+r1` | 2.8243 | 0.65 | 1.7133 | 0.15 |
| `R=r1-r0` | 3.1239 | 0.50 | 1.8970 | 0.05 |
| `D` | 2.9674 | 0.70 | 1.6474 | 0.15 |

### aggregate statistics

| statistic | actual | null mean | null sd | z | null >= actual |
|---|---:|---:|---:|---:|---:|
| mean `D` | 5.2686852e-5 | 5.1590028e-5 | 7.81459e-7 | +1.4036 | 0.05 |
| RMS `C` | 0.0732041 | 0.0721422 | 0.000545675 | +1.9460 | 0/20 |
| RMS `R` | 0.1081236 | 0.1086949 | 0.00147572 | -0.3871 | 0.55 |

`RMS C`만 one-cutoff scalar statistic에서 약 `1.95 sigma` 상승했지만,

1. profile-wide max/mean-square multiple-comparison에서는 null과 분리되지 않고,
2. `X=2^18`에서 전혀 재현되지 않으며,
3. `D` profile 자체도 null-like이고,
4. 20-null empirical tail은 해상도가 거칠다.

따라서 이를 signal로 승격하지 않는다.

상태: `NUMERICAL / CUTOFF-UNSTABLE`.

---

## 7. final branch verdict

### exact structure retained

- prime activation recursion: `EXACT`.
- parity-dissipation identity: `EXACT`.
- recursive variance-tree decomposition: `EXACT`.

### closed as proof mechanism

- 단순 activation을 strict contraction으로 해석하는 경로: `CLOSED`.
- total dissipation sum 자체를 새 RH invariant로 쓰는 경로: `CLOSED_AS_VARIANCE_REENCODING`.
- top-level label-visible cross-scale coherence `r(X)+r(X/p)`를 raw prime-specific signal로 쓰는 경로: tested scales에서 `NOT SEPARATED FROM GAP NULL`.

### residual status

`X=2^20`의 약 1.95 sigma aggregate coherence는 cutoff stability를 통과하지 못했으므로 `NO SIGNAL CLAIM`이다.

더 진행하려면 raw activation observable을 반복 계산하는 것이 아니라, **gap-null도 보존하지 못하는 별도의 deterministic arithmetic constraint**를 먼저 제시해야 한다.

---

## 8. project conclusion for this branch

현재 formation-side에서 검사한

- low/fixed-order moments,
- K-wise marginals,
- raw GCD label correlations,
- boundary flux,
- connected visibility flux,
- divisibility tensors,
- linear boundary-shell averaging,
- slack smoothing,
- finite spectral/Hankel transforms,
- local generating-polynomial root motion,
- prime-activation cross-scale bias

은 모두 exact reencoding, known barrier, 또는 current gap-null에서 분리되지 않는 numerical structure로 분류되었다.

따라서 현재 Riemann project의 이 탐색 구간은 여기서 **마감**한다.

새 전선은 기존 quantity의 변형이 아니라, 기존 null model이 보존하지 않는 명시적 arithmetic invariant가 먼저 제시될 때만 연다.
