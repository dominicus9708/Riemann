# GCD-Overlap Sector Null Audit

## 목적

Derivative-energy generating function의 exact off-diagonal interaction

\[
\Delta\mathcal G_X(t)
=
\sum_{m\ne n}\mu(m)\mu(n)(1+t)^{\omega(\gcd(m,n))}
\]

을 `r=omega(gcd(m,n))` sector로 분해해, actual prime placement가 gap-permuted pseudo-prime threshold와 구별되는지 감사한다.

---

## 1. sector decomposition

\[
C_r(X)
=
\sum_{\substack{m\ne n\le X\\\mu^2(m)=\mu^2(n)=1\\\omega(\gcd(m,n))=r}}
\mu(m)\mu(n).
\]

그러면

\[
\boxed{
\Delta\mathcal G_X(t)
=
\sum_{r\ge0}C_r(X)(1+t)^r.
}
\]

Derivative-energy coefficient difference

\[
\Delta E_k=\mathcal E_k^\mu-\overline{\mathcal E}_k
\]

와는

\[
\boxed{
\Delta E_k=\sum_{r\ge k}\binom rk C_r
}
\]

관계가 있으므로 backward binomial inversion으로 `C_r`를 exact하게 복원할 수 있다.

---

## 2. unsigned sector normalization

all-positive corner에서 같은 derivative-energy를 계산하면

\[
E_k^+-\overline E_k
=
\sum_{r\ge k}\binom rk N_r,
\]

여기서 `N_r`는 `omega(gcd)=r`인 ordered off-diagonal pair의 수다.

따라서

\[
\boxed{\rho_r(X)=C_r(X)/N_r(X)}
\]

를 sector-wise signed correlation으로 사용한다.

---

## 3. actual vs gap-permutation null

Null model은 `derivative_energy_transfer_null_audit.md`와 동일하다.

- `p<=100` 고정.
- dyadic block별 actual prime-gap multiset 보존.
- gap order만 shuffle.
- weighted subset-product threshold와 all-minus parity 유지.

### X = 2^18

| r | rho_prime | mean rho_null | null sd | z |
|---:|---:|---:|---:|---:|
| 0 | -5.2186e-6 | -5.5173e-6 | 1.9903e-6 | +0.15 |
| 1 | +5.6246e-5 | +5.6577e-5 | 1.5319e-5 | -0.02 |
| 2 | -6.5411e-4 | -6.4560e-4 | 1.4771e-4 | -0.06 |
| 3 | -6.1124e-3 | -6.0923e-3 | 1.2897e-3 | -0.02 |
| 4 | +0.192257 | +0.196404 | 0.005995 | -0.69 |
| 5 | +0.241697 | +0.229351 | 0.008303 | +1.49 |

`r=0,...,4`는 모두 absolute z < 0.7이며, 가장 큰 `r=5`도 약 `1.5 sigma`다.

`X=2^16,2^17`에서도 각 sector는 대체로 `~1 sigma` 수준에서 null과 겹쳤다.

---

## 4. 판정

\[
\boxed{
\text{raw gcd-overlap sector interaction도 현재 범위에서는 prime-specific signal이 아니다.}
}
\]

low/mid-order derivative-energy transfer뿐 아니라 그 underlying `omega(gcd)` sector correlation까지 prime-like weighted-threshold geometry가 거의 재현한다.

따라서 다음은 RH 고유 후보에서 제외한다.

1. raw `G_X(t)` crossover,
2. low-order suppression / mid-order enhancement,
3. `omega(gcd)`만으로 분해한 raw signed sector correlations.

---

## 5. 남은 정보 요구조건

후속 candidate는 적어도 `omega(gcd)`보다 더 많은 arithmetic label 정보를 보존해야 한다.

가능한 다음 분해는

\[
\gcd(m,n)=d
\]

의 **실제 radical/prime labels**를 유지한 kernel이다.

즉

\[
C_d(X)
=
\sum_{\substack{m\ne n\le X\\\gcd(m,n)=d}}
\mu(m)\mu(n)
\]

또는 prime-size bands별 overlap을 사용해, `omega(d)`로 압축했을 때 사라지는 actual prime placement information이 남는지 본다.

단, 이 refined kernel도 gap-null에서 재현되면 즉시 일반 threshold effect로 닫는다.

---

## 재현자료

```text
data/formation/gcd_overlap_sector_null_audit.csv
```

관련 문서:

```text
04_prime_connection/weighted_halfspace_parity_audit.md
04_prime_connection/derivative_energy_transfer_null_audit.md
```
