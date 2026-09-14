# Alladi Prime-Factor Duality / Formation-Channel Audit

Date: 2026-09-15

## 목적

현재 살아 있는 요구조건인

- first activation / smallest prime information,
- last activation / largest prime information,
- Möbius top parity,
- higher-order channel count `omega(n)`

를 동시에 다루는 기존 정리가 있는지 조사한다.

핵심 선행구조는 Alladi의 prime-factor duality와 2026년 higher-order extension이다.

---

## 1. first/last prime exact duality

`p_1(n)`을 smallest prime factor, `P_1(n)`을 largest prime factor라 하고 `f`를 primes 위의 임의 함수라 하자.

Alladi (1977)의 exact identity는

\[
\boxed{
\sum_{\substack{d\mid n\\d>1}}
\mu(d)f(p_1(d))
=-f(P_1(n)).
}
\]

반대 방향으로 smallest/largest를 교환한 dual identity도 존재한다.

이것은 repository 언어에서

\[
\boxed{
\text{first activated prime under Möbius parity}
\longleftrightarrow
\text{last activated prime}
}
\]

를 정확히 연결한다.

상태: `STANDARD_EXACT_IDENTITY`.

---

## 2. higher-order duality

`P_k(n)`을 k-th largest prime factor라 하자. Alladi의 general duality를 Möbius inversion한 형태는

\[
\boxed{
\sum_{1<d\mid n}
\mu(d)
{\omega(d)-1\choose k-1}
 f(p_1(d))
=(-1)^k f(P_k(n)).
}
\]

(`omega(n)<k`에서는 대응 prime-factor function을 0으로 두는 convention.)

따라서 higher-order connected channel count를 도입해도 first/last prime duality는 이미 exact classical structure를 가진다.

---

## 3. formation phase derivative와 정확히 같은 weighted channel

repository의 formation Euler product를

\[
F(s,z)
=\sum_{n\ge1}\frac{\mu(n)^2z^{\omega(n)}}{n^s}
=\prod_p(1+zp^{-s})
\]

라 두자.

Euler operator `D_z=z partial_z`를 쓰면 coefficientwise

\[
D_z^kF(s,z)
=\sum_n\frac{\mu(n)^2\omega(n)^k z^{\omega(n)}}{n^s}.
\]

`z=-1`에서는 squarefree `n`에 대해

\[
\mu(n)^2(-1)^{\omega(n)}=\mu(n),
\]

따라서 정확히

\[
\boxed{
\left.D_z^kF(s,z)\right|_{z=-1}
=
\sum_{n\ge1}
\frac{\mu(n)\omega(n)^k}{n^s}.
}
\]

즉 Alladi--Johnson / Alladi--Sengupta가 연구하는 weighted Möbius channels는 formation phase derivative hierarchy와 **동일한 Dirichlet-series object**다.

상태: `EXACT_IDENTIFICATION`.

---

## 4. 2026 higher-order results

Alladi--Sengupta (arXiv:2604.17832, 2026)는 fixed `k>=2`에 대해

\[
\sum_{n=2}^{\infty}\frac{\mu(n)\omega(n)^k}{n}=0
\]

을 증명하고, higher-order prime-factor dualities를 사용해 arithmetic progressions로 제한된 weighted sums도 연구한다.

또 `M_{omega^k}(x)=sum_{n<=x}mu(n)omega(n)^k=o(x)`에 대한 quantitative expansion을 전개한다.

이것은 formation phase derivative가 실제 analytic-number-theory object와 정확히 접속한다는 강한 external cross-check다.

---

## 5. 독립 RH 경로인지 감사

중요하게도 같은 논문의 Section 2는 quantitative weighted-Möbius estimates를 전개하기 전에 standard strong PNT bound

\[
\boxed{
M(x)\ll x e^{-c\sqrt{\log x}}
}
\]

와

\[
\sum_{n\le x}\frac{\mu(n)}n
\ll e^{-c\sqrt{\log x}}
\]

를 명시적으로 사용한다.

또 prime-factor residue-class duality conclusions는 PNT in arithmetic progressions / uniform distribution of largest prime factors를 입력으로 사용한다.

따라서 logical direction은 현 단계에서

\[
\text{PNT / PNTAP control}
\to
\text{higher prime-factor distribution}
\to
\text{weighted Möbius duality consequences}
\]

이다.

즉

\[
\boxed{
\text{higher-order duality is not presently an independent route to RH-scale cancellation.}
}
\]

---

## 6. why increasing omega-order does not escape

repository 내부에서 이미

- phase cumulant order `m` -> reciprocal `1/m` tail hierarchy,
- all-order prime-divisibility tensor -> sieve-density barrier,
- derivative-energy higher orders -> gap-null reproduction

을 확인했다.

Alladi higher-order duality는 별개의 exact identity이지만 `omega^k`를 계속 올리는 것 자체가 새로운 RH scale을 생성하지 않는다는 외부 교차검증을 추가한다.

특히 weighted sums가 `s=1`에서 강하게 소거된다는 사실을 `Re(s)=1/2` zero location으로 승격할 수 없다.

---

## 7. finite summed duality

first-order identity를 `n<=x`에 합하면 정확히

\[
\boxed{
\sum_{2\le n\le x}f(P_1(n))
=-\sum_{2\le d\le x}
\mu(d)f(p_1(d))
\left\lfloor\frac xd\right\rfloor.
}
\]

따라서 positive/understood largest-prime statistics를 Möbius-weighted smallest-prime statistics로 옮길 수 있다.

그러나 이 transform도 `floor(x/d)` kernel을 사용하며, quantitative error를 RH scale로 내리려면 weighted Möbius cancellation을 별도로 제어해야 한다.

현재는 `DUAL_REPRESENTATION`, not contraction.

---

## 8. 닫히는 경로

다음을 새 RH mechanism으로 사용하지 않는다.

1. smallest/largest prime duality 자체.
2. `omega(n)^k` weight order를 높이는 것 자체.
3. `sum mu(n) omega(n)^k/n = 0`을 critical-line evidence로 해석하는 것.
4. PNT/PNTAP를 입력으로 얻은 quantitative duality consequence를 다시 RH 증명 입력으로 사용하는 순환.

---

## 9. 남는 가능성

Alladi duality가 이후에도 유용할 수 있는 유일한 방향은

\[
\boxed{
\text{PNT-strength input 없이도 성립하는 new finite inequality
for the duality remainder}
}
\]

을 찾는 경우다.

즉 exact identity는 이미 알려져 있고, 필요한 것은 identity가 아니라 RH-scale **quantitative inequality**다.

## 상태

- first/last prime duality: `STANDARD_EXACT`.
- higher-order duality: `STANDARD_EXACT`.
- formation phase derivative identification: `EXACT`.
- 2026 weighted-sum results: `PRIMARY_LITERATURE / PNT-LEVEL INPUT`.
- independent RH progress: `NOT_ESTABLISHED`.
- RH: `OPEN`.

## 기준문헌

- K. Alladi (1977), *Duality between prime factors and an application to the prime number theorem for arithmetic progressions*, Journal of Number Theory 9(4), 436–451, DOI 10.1016/0022-314X(77)90005-1.
- K. Alladi & J. Johnson (2026), *Duality between prime factors and the prime number theorem for arithmetic progressions—II*, Ramanujan Journal 69(3), Article 52, DOI 10.1007/s11139-026-01325-5; preprint arXiv:2410.18259.
- K. Alladi & S. Sengupta (2026), *Duality Between Prime Factors and The Prime Number Theorem For Arithmetic Progressions -- Higher Order Dualities*, arXiv:2604.17832.
