# Exact GCD-Label Visibility Audit

## 목적

이전 `gcd_overlap_sector_null_audit.md`에서는

\[
r=\omega(\gcd(m,n))
\]

만 보존한 sector가 gap-permutation pseudo-prime null과 거의 구별되지 않았다.

이번 단계에서는 `omega(gcd)` 압축을 제거하고 실제 공통 prime labels를 보존한다.

핵심 질문은 두 가지다.

1. exact intersection `gcd(m,n)=d`에서 실제 prime label 정보가 언제 살아 있는가?
2. 살아 있는 singleton / two-prime label sector가 prime-gap null과 실제로 구별되는가?

---

## 1. exact gcd-intersection kernel

squarefree `d<=X`에 대해 ordered off-diagonal interaction을

\[
C_d(X)
=
\sum_{\substack{m\ne n\le X\\\mu^2(m)=\mu^2(n)=1\\\gcd(m,n)=d}}
\mu(m)\mu(n)
\]

로 두고, 같은 조건의 ordered pair 수를 `N_d(X)`라 둔다.

`m=da`, `n=db`로 쓰면 `d,a,b`는 필요한 자리에서 서로 소이고

\[
Y=\left\lfloor\frac Xd\right\rfloor,
\qquad
(a,b)=1,
\qquad
(ab,d)=1.
\]

또 squarefree 조건 아래

\[
\mu(da)\mu(db)=\mu(a)\mu(b)
\]

이므로 diagonal pair `(m,n)=(d,d)` 하나를 복원하면 정확히

\[
\boxed{
C_d(X)+1
=
\sum_{\substack{a,b\le Y\\(a,b)=1\\(ab,d)=1}}
\mu(a)\mu(b)
}
\]

이다.

동일하게

\[
\boxed{
N_d(X)+1
=
\sum_{\substack{a,b\le Y\\(a,b)=1\\(ab,d)=1}}
\mu^2(a)\mu^2(b)
}
\]

이다.

---

## 2. label-visibility lemma

`Y=floor(X/d)`라 하고

\[
\boxed{
V_X(d)=\prod_{\substack{p\mid d\\p\le Y}}p
}
\]

를 **visible divisor core**라 정의한다.

`a,b<=Y`이므로 `p|d`이면서 `p>Y`인 prime은 `a`나 `b`를 나눌 수 없다.

따라서

\[
(ab,d)=1
\quad\Longleftrightarrow\quad
(ab,V_X(d))=1.
\]

즉

\[
\boxed{
(C_d(X),N_d(X))
\text{는 }d\text{ 전체가 아니라 }
\left(\left\lfloor X/d\right\rfloor,V_X(d)\right)
\text{를 통해서만 residual label information을 본다.}
}
\]

### 완전 label-blind sector

\[
P^-(d)>X/d
\]

이면 `V_X(d)=1`이므로 `d`의 실제 prime labels는 residual kernel에서 완전히 사라진다.

동치로

\[
\boxed{dP^-(d)>X}
\]

이면 exact intersection kernel은 quotient `floor(X/d)`만 본다.

### 모든 label이 살아 있는 sector

반대로

\[
P^+(d)\le X/d
\]

즉

\[
\boxed{dP^+(d)\le X}
\]

이면 `d`의 모든 prime labels가 coprimality constraint에 실제로 남는다.

그 사이에서는 일부 label만 살아 있다.

---

## 3. singleton의 exact quotient degeneracy

`d=p`가 prime이면

\[
Y=\lfloor X/p\rfloor.
\]

특히

\[
p>\sqrt X
\]

이면 `Y<p`이므로 `p\nmid a,b`는 자동이다.

따라서

\[
\boxed{
p>\sqrt X
\Longrightarrow
(C_p(X),N_p(X))
\text{는 }p\text{의 identity와 무관하고 }
\lfloor X/p\rfloor\text{만으로 결정된다.}
}
\]

이것은 큰-prime singleton profile이 dyadic cutoff를 바꾸면 한 band씩 이동하며 반복되던 현상을 정확히 설명한다.

따라서 `p>sqrt(X)` singleton sector에서 prime-specific RH signal을 찾는 것은 정보론적으로 불가능하다.

---

## 4. Boolean derivative와 exact-intersection inversion

weighted-halfspace state `S`에 대해 Möbius-corner derivative를

\[
D_A=\partial_A P_X(-\mathbf1)
\]

라 두면 `D_A^2`는 두 상태의 공통 channel set이 `A`를 포함하는 ordered-pair interaction이다.

따라서 exact common set `B`의 signed interaction을 `C'_B`라 하면

\[
D_A^2=\sum_{B\supseteq A}C'_B.
\]

Boolean-lattice Möbius inversion으로

\[
\boxed{
C'_A
=
\sum_{B\supseteq A}
(-1)^{|B|-|A|}D_B^2
}
\]

을 얻는다.

`C_A=C'_A-1`은 diagonal state `A` 하나를 제외한 값이다.

all-positive derivative count `H_A`에도 같은 inversion을 적용하면 exact ordered pair count `N_A`를 얻는다.

이 방식은 actual primes뿐 아니라 abstract pseudo-prime generator null에도 동일하게 적용된다.

---

## 5. singleton label null audit

Null은 기존 derivative-energy audit와 동일하다.

- `p<=100`은 고정.
- 이후 실제 prime-gap multiset을 dyadic block별로 보존.
- gap order만 shuffle.
- weighted product cutoff와 all-minus character를 유지.

`X=2^18=262144`에서 실제 label이 살아 있는 비교영역을

\[
100<p\le\sqrt X
\]

으로 제한하고 `N_p>=1000`인 72개 singleton channel을 비교했다.

20개 fixed-seed gap-null ensemble 기준:

- actual maximum individual `|z|`: `3.4498`.
- leave-one-out null maximum이 이보다 큰 비율: `5/20 = 0.25`.
- actual mean `z^2`: `1.2288`.
- leave-one-out null mean-square가 이보다 큰 비율: `10/20 = 0.50`.

따라서 개별 `3 sigma` 수준의 spike는 존재하지만 multiple-channel null fluctuation 범위를 벗어나지 않는다.

prime-size band aggregate에서도 최대 편차는 `|z|≈1.66`이었다.

### 판정

\[
\boxed{
\text{현재 범위에서 label-visible singleton correlation은 prime-specific signal이 아니다.}
}
\]

---

## 6. fully-visible two-prime audit

`d=pq`, `p<q`인 경우 두 label이 모두 보이려면

\[
q\le\left\lfloor\frac X{pq}\right\rfloor,
\]

즉 대략

\[
pq^2\le X
\]

가 필요하다.

`X=2^18`에서

- `q>100`으로 null에서 실제로 움직이는 channel만 선택,
- `N_{pq}>=1000`,
- full visibility를 만족하는 159개 pair를 선택했다.

20개 gap-null ensemble과 비교한 결과:

- actual maximum individual `|z|`: `3.8224`.
- leave-one-out null maximum이 이를 넘는 비율: `7/20 = 0.35`.
- actual mean `z^2`: `1.3161`.
- null mean-square가 이를 넘는 비율: `5/20 = 0.25`.

가장 큰 개별 residual 중 하나는 `(p,q)=(2,197)`이었지만 global multiple-comparison 기준으로 예외적이지 않다.

### 판정

\[
\boxed{
\text{fully-visible two-prime exact intersections도 현재 범위에서 gap-null과 구별되지 않는다.}
}
\]

즉 `omega(gcd)` 압축을 제거하고 actual labels를 복원하는 것만으로는 충분하지 않다.

---

## 7. 이번 단계에서 닫히는 경로

다음 단순 후보는 현재 기준에서 닫는다.

1. `p>sqrt(X)` singleton exact-intersection에서 prime identity를 찾는 경로.
   - exact quotient degeneracy 때문에 label 정보 자체가 없다.
2. `p<=sqrt(X)` singleton label correlation 자체를 RH-specific signal로 사용하는 경로.
   - gap-null과 구별되지 않는다.
3. fully-visible two-prime exact-intersection raw correlation 자체를 사용하는 경로.
   - 현재 global null statistic에서 유의한 분리가 없다.

---

## 8. 남은 후보의 정보 요구조건

후속 candidate는 적어도 다음 중 하나를 추가로 보존해야 한다.

1. **cross-scale coupling**: 동일 prime label이 서로 다른 quotient `floor(X/d)` 층에서 어떻게 연결되는지.
2. **signed orientation / phase**: exact gcd label만으로 사라지는 Möbius phase relation.
3. **higher-order fully-visible intersections**: 단, raw `k`-tuple correlation이 아니라 lower-order null을 제거한 connected/cumulant형 interaction.
4. **boundary flux**: `dP^+(d)<=X`의 visible region에서 label이 생성·소실되는 경계를 따라 생기는 signed flux.

특히 단순 higher-order raw moment는 이전 derivative-energy audit에서 threshold null이 쉽게 재현했으므로 우선순위를 낮춘다.

다음 주 계산 후보는 **visible-core boundary flux / connected interaction**이다.

---

## 재현자료

```text
data/formation/gcd_label_visibility_band_2pow18.csv
data/formation/gcd_label_visibility_pairs_2pow18.csv
scripts/audit_gcd_label_visibility.py
```

관련 문서:

```text
04_prime_connection/gcd_overlap_sector_null_audit.md
04_prime_connection/weighted_halfspace_parity_audit.md
04_prime_connection/derivative_energy_transfer_null_audit.md
```

## 상태

- label-visibility lemma: `EXACT`.
- singleton quotient degeneracy for `p>sqrt(X)`: `EXACT`.
- singleton / two-prime null comparison: `NUMERICAL`.
- RH: `OPEN`.
