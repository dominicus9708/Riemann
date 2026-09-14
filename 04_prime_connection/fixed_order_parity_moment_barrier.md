# Fixed-Order Prime-Factor Moment / Parity Barrier Audit

Date: 2026-09-15

## 목적

Alladi higher-order duality와 formation phase derivative가 정확히 같은 `omega(n)^k` weighted Möbius channels를 만든다는 사실에서 한 단계 더 나아간다.

질문은 다음과 같다.

1. fixed degree polynomial in `omega` 전체가 이미 finite prime-factor order statistics로 닫히는가?
2. Möbius parity `(-1)^omega`를 fixed-order moments로 복원할 수 있는가?
3. exact parity가 아니라 RH-scale aggregate accuracy만 요구하면 현재 finite data에서 몇 order가 필요한가?

---

## 1. fixed-degree polynomial closure under Alladi duality

Alladi higher-order duality를

\[
\sum_{1<d\mid n}
\mu(d)
{\omega(d)-1\choose k-1}
 f(p_1(d))
=(-1)^k f(P_k(n))
\]

로 쓴다.

임의의 degree-`D` polynomial `Q(r)`는 Newton basis에서 정확히

\[
\boxed{
Q(r)=\sum_{j=0}^{D}\Delta^jQ(1){r-1\choose j}.
}
\]

따라서

\[
\boxed{
\sum_{1<d\mid n}
\mu(d)Q(\omega(d))f(p_1(d))
=
\sum_{j=0}^{D}
\Delta^jQ(1)(-1)^{j+1}f(P_{j+1}(n)).
}
\]

즉 **모든 fixed-degree `omega` polynomial channel**은 finitely many largest-prime order statistics의 exact linear combination이다.

특히 `Q(r)=r^k`를 몇 차수 더 올리는 것은 새로운 information class를 만들지 않는다.

상태: `EXACT`.

---

## 2. parity의 universal Newton expansion

squarefree `n`에서는

\[
\mu(n)=(-1)^{\omega(n)}.
\]

정수 `r>=0`에 대해 binomial theorem로

\[
\boxed{
(-1)^r=(1-2)^r
=\sum_{j=0}^{r}(-2)^j{r\choose j}.
}
\]

squarefree layer count를

\[
A_r(x)=\#\{n\le x:\mu(n)^2=1,\omega(n)=r\}
\]

라 하고 binomial moments를

\[
B_j(x)=\sum_{r\ge j}A_r(x){r\choose j}
=\sum_{n\le x}\mu(n)^2{\omega(n)\choose j}
\]

라고 두면 exact하게

\[
\boxed{
M(x)=\sum_{j\ge0}(-2)^jB_j(x).
}
\]

유한 cutoff에서는 `j<=m(x)`에서 끝나며

\[
m(x)=\max_{n\le x}\omega(n).
\]

이 식은 parity를 moment hierarchy로 옮긴 exact change of basis이다.

---

## 3. exact polynomial-degree barrier

`h(r)=(-1)^r`라 하자.

전진차분은

\[
\Delta h(r)=h(r+1)-h(r)=-2h(r),
\]

따라서

\[
\boxed{
\Delta^m h(0)=(-2)^m\ne0.
}
\]

degree `<m` polynomial은 `m`차 finite difference가 0이므로 `r=0,1,...,m`에서 parity를 exact하게 재현할 수 없다.

반대로 위 Newton expansion이 degree `m` representation을 준다.

따라서

\[
\boxed{
\deg_{\rm exact}\big((-1)^r\text{ on }\{0,\ldots,m\}\big)=m.
}
\]

---

## 4. uniform approximate-degree barrier

더 강하게 polynomial `P`가

\[
|P(r)-(-1)^r|<1
\qquad(r=0,1,\ldots,m)
\]

을 만족한다고 하자.

그러면 `P(r)`는 각 integer point에서 parity와 같은 부호를 가져야 한다.

따라서 모든 adjacent pair `[r,r+1]` 사이에서 `P`는 적어도 한 번 zero를 가져야 하고 총 `m`개의 서로 다른 real roots가 필요하다.

그러므로

\[
\boxed{\deg P\ge m.}
\]

즉 error bound `<1` 아래에서는 exact degree와 approximate degree가 동일하다.

이것은 Boolean PARITY의 high approximate degree와 같은 기본 장벽이며 Paturi의 symmetric-Boolean approximate-degree theory와 정합적이다.

상태: `EXACT_ELEMENTARY`; external context: Paturi (1992).

---

## 5. required order grows with x

squarefree integer `n<=x`가 가질 수 있는 최대 distinct-prime count는 smallest primes를 곱했을 때 달성되므로

\[
\boxed{
m(x)=\max\{m:p_m^\#\le x\}.}
\]

Prime Number Theorem을 사용하면

\[
\log p_m^\#=\vartheta(p_m)\sim p_m,
\qquad
p_m\sim m\log m,
\]

따라서

\[
\boxed{
m(x)\sim\frac{\log x}{\log\log x}.}
\]

즉 exact endpoint parity는 **fixed order가 아니라 growing order**를 요구한다.

---

## 6. current dyadic layer audit

기존 exact layer table

```text
data/formation/mobius_layer_counts_dyadic_24.csv
```

에서 universal expansion의 partial sums

\[
S_K(x)=\sum_{j=0}^{K}(-2)^jB_j(x)
\]

을 계산했다.

대표 결과:

### x = 2^16, M(x)=14, max omega=6

```text
K=0    39844
K=1  -152506
K=2   188358
K=3   -93746
K=4    16846
K=5     -434
K=6       14
```

### x = 2^18, M(x)=24, max omega=6

```text
159360 -> -644284 -> 877760 -> -513272 -> 124408 -> -8744 -> 24
```

### x = 2^20, M(x)=257, max omega=7

```text
637461 -> -2701927 -> 3992177 -> -2653391
       -> 797697 -> -87935 -> 1409 -> 257
```

### x = 2^22, M(x)=228, max omega=7

```text
2549834 -> -11262900 -> 17818596 -> -13148476
        -> 4674308 -> -705564 -> 27492 -> 228
```

### x = 2^24, M(x)=211, max omega=8

```text
10199301 -> -46726157 -> 78400075 -> -63160989
         -> 25708979 -> -4895789 -> 324819 -> -1325 -> 211
```

따라서 fixed low-order partial sums는 작은 Mertens endpoint를 안정적으로 근사하지 않는다. 큰 alternating layer terms가 nearly full support order까지 취소된다.

상태: `NUMERICAL`.

---

## 7. square-root target order in the universal expansion

각 cutoff에서

\[
|S_K(x)-M(x)|\le\sqrt{x}
\]

를 처음 만족하는 `K`를 기록했다.

| x | max omega | first K within sqrt(x) |
|---:|---:|---:|
| 2^10 | 4 | 4 |
| 2^12 | 5 | 5 |
| 2^14 | 5 | 5 |
| 2^16 | 6 | 6 |
| 2^18 | 6 | 6 |
| 2^20 | 7 | 7 |
| 2^22 | 7 | 7 |
| 2^24 | 8 | 7 |

`2^24`에서 one-below-max order가 square-root error에 들어오는 이유는 final omitted term이

\[
(-2)^8A_8(x)=256\cdot6=1536<\sqrt{2^{24}}=4096
\]

이기 때문이다.

따라서 **exact max order 자체가 RH-scale accuracy에 항상 필요한 것은 아니다.**

이 구분은 중요하다.

- exact parity representation lower bound: theorem-level growing order.
- universal binomial truncation의 square-root target: finite numerical diagnostic.
- all possible x-dependent approximants에 대한 RH-scale order lower bound: `OPEN`.

---

## 8. central-layer sign guard

Erdos--Kac theory에서 `omega(n)`의 typical center는 `log log x`, width는 `sqrt(log log x)`이며 squarefree restriction에도 analogous normal law가 성립한다.

따라서 central region에는 growing number of consecutive relevant `omega` layers가 존재한다.

만약 어떤 polynomial surrogate가 그 central consecutive layers 각각에서 parity를 sign-preserving error `<1`로 근사해야 한다면 root-count argument로 polynomial degree도 그 central-window length와 함께 증가해야 한다.

heuristically this scale is at least

\[
\Omega(\sqrt{\log\log x})
\]

for a fixed-width Gaussian central window.

그러나 **Mertens aggregate error에서는 서로 다른 layer approximation errors가 다시 cancellation할 수 있으므로**, 이를 unrestricted RH-scale lower bound라고 주장하지 않는다.

상태: `CONDITIONAL_GUARD / NOT_RH_LOWER_BOUND`.

---

## 9. relation to sieve parity problem

이 결과는 classical sieve parity obstruction과 방향이 일치한다.

low/fixed-order local divisibility information이나 finitely many prime-factor moments만으로는 alternating prime-factor parity를 안정적으로 복원하기 어렵다.

다만 repository의 exact polynomial-degree statement는 sieve parity theorem의 대체증명이 아니다. 현재 formation moment representation 안에서 무엇이 부족한지를 특정하는 information audit이다.

---

## 10. fixed-order branch closure

다음을 독립 RH 후보에서 닫는다.

1. `omega, omega^2, ..., omega^K`를 어떤 fixed `K`까지만 더 계산하면 parity endpoint가 드러난다는 기대.
2. fixed-degree polynomial in `omega`가 Alladi higher-order duality를 넘어 새로운 first/last-prime information을 만든다는 기대.
3. fixed low-order phase derivatives가 full Möbius parity를 uniform하게 근사한다는 기대.

---

## 11. genuine remaining frontier

남는 문제는 fixed order가 아니라

\[
\boxed{K=K(x)\to\infty}
\]

인 **nonuniform growing-order hierarchy**다.

특히 구분해야 한다.

1. exact parity를 위한 support order
   \[
   K\sim \log x/\log\log x;
   \]
2. central-layer sign resolution을 위한 smaller growing order;
3. aggregate RH-scale error
   \[
   |M(x)-\text{moment approximation}|\le x^{1/2+\epsilon}
   \]
   에 실제로 필요한 minimal order.

세 번째가 현재 `OPEN`이다.

이를 해결하려면 fixed-k asymptotics가 아니라 **k가 x와 함께 증가하는 uniform Sathe--Selberg / Selberg--Delange regime와 parity-sensitive polynomial approximation**을 결합해야 한다.

## 상태

- fixed-degree Alladi closure: `EXACT`.
- parity Newton expansion: `EXACT`.
- exact/uniform `<1` parity degree = max omega: `EXACT`.
- max omega asymptotic: `STANDARD_PNT_CONSEQUENCE`.
- universal moment truncation data: `NUMERICAL`.
- unrestricted RH-scale minimal growing order: `OPEN`.
- RH: `OPEN`.

## 재현자료

```text
scripts/audit_parity_moment_order.py
data/formation/parity_moment_truncation_selected.csv
data/formation/parity_moment_truncation_summary.csv
```

## 선행문헌 기준

- Krishnaswami Alladi & Sroyon Sengupta (2026), higher-order prime-factor dualities, arXiv:2604.17832.
- Ramamohan Paturi (1992), *On the Degree of Polynomials that Approximate Symmetric Boolean Functions*, STOC 1992, DOI 10.1145/129712.129758.
- classical Erdos--Kac / Sathe--Selberg theory for the distribution of `omega(n)`; squarefree variants used only for central-window context.
