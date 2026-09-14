# Prime-Power Tail Filtration and the Reciprocal-Hierarchy False Control

Date: 2026-09-15

## 목적

formation phase cumulant에서 나타난

\[
1/2,1/3,1/4,\ldots
\]

계층이 RH critical line과 어떤 관계인지 정확히 분류한다.

---

## 1. Euler-product logarithmic filtration

prime zeta function을

\[
P(s)=\sum_p p^{-s}
\]

라 하자.

`Re(s)>1`에서

\[
\log\zeta(s)=\sum_{r\ge1}\frac{P(rs)}r
\]

이므로

\[
\boxed{
\frac1{\zeta(s)}
=
\exp\!\left(-\sum_{r\ge1}\frac{P(rs)}r\right).
}
\]

정수 `m>=2`에 대해

\[
R_m(s)=\sum_{r\ge m}\frac{P(rs)}r
\]

를 prime-power tail이라 둔다.

그러면 초기 절대수렴 영역 `Re(s)>1`에서

\[
\boxed{
\frac1{\zeta(s)}
=
\exp\!\left(-\sum_{1\le r<m}\frac{P(rs)}r\right)
E_m(s),
\qquad
E_m(s)=e^{-R_m(s)}.
}
\]

---

## 2. exact convergence threshold of the tail

`Re(s)=sigma>1/m`이면 모든 `r>=m`에 대해 `r sigma>1`이다.

따라서 `P(rs)`는 ordinary prime series로 절대수렴하고, large `r`에서 지수적으로 작아지므로

\[
R_m(s)
\]

은 locally uniformly absolutely convergent한다.

따라서

\[
\boxed{
E_m(s)\text{ is analytic and nonzero for }\Re(s)>1/m.
}
\]

즉 reciprocal threshold

\[
\boxed{1/m}
\]

은 critical-zero geometry가 아니라 **prime-power tail을 `r>=m`에서 자른 결과의 absolute-convergence boundary**다.

---

## 3. phase cumulant와 동일한 hierarchy

formation Euler product

\[
F(s,z)=\prod_p(1+zp^{-s})
\]

에서

\[
C_m(s)=\left.\partial_z^m\log F(s,z)\right|_{z=-1}
\]

이면

\[
\boxed{
C_m(s)
=(-1)^{m-1}(m-1)!
\sum_p\frac{p^{-ms}}{(1-p^{-s})^m}
}
\]

이고

\[
\boxed{
\frac{(-1)^{m-1}}{(m-1)!}C_m(s)
=
\sum_{r=m}^\infty
\binom{r-1}{m-1}P(rs).
}
\]

첫 term이 `P(ms)`이므로 동일하게 `Re(s)>1/m`이 first ordinary-convergence boundary다.

따라서 phase-cumulant `1/m`과 Euler-log tail `1/m`은 같은 prime-power filtration의 두 표현이다.

---

## 4. why m=2 produces a seductive 1/2

`m=2`에서는

\[
R_2(s)=\sum_{r\ge2}\frac{P(rs)}r
\]

가 `Re(s)>1/2`에서 절대수렴한다.

그러므로

\[
E_2(s)=e^{-R_2(s)}
\]

는 그 half-plane에서 analytic and nonzero다.

따라서 `1/2`가 자연스럽게 나타난다.

그러나 `m=3,4,...`에도 같은 방식으로 `1/3,1/4,...`가 나타난다.

결론:

\[
\boxed{
\text{phase curvature의 }1/2
\text{는 RH line selection이 아니라 }m=2\text{ tail threshold다.}
}
\]

상태: `EXACT_FALSE_CONTROL`.

---

## 5. hard first-prime axis

`m=2` decomposition은 초기 영역에서

\[
\frac1{\zeta(s)}=e^{-P(s)}E_2(s)
\]

이다.

`E_2`는 `Re(s)>1/2`에서 이미 analytic and nonzero이므로, 그 half-plane에서 RH-relevant obstruction을 carry할 수 있는 part는 first-prime term `P(s)` 쪽이다.

prime-zeta Möbius inversion은

\[
\boxed{
P(s)=\sum_{k\ge1}\frac{\mu(k)}k\log\zeta(ks).
}
\]

따라서 `Re(s)>1/2`에서는 `k>=2` terms가 `Re(ks)>1`에 있으므로 regular하다.

즉 locally on a branch avoiding zeta zeros,

\[
\boxed{
P(s)=\log\zeta(s)+H_2(s),
}
\]

where `H_2` is analytic in `Re(s)>1/2`.

따라서 그 half-plane 안에서 prime-zeta singular structure와 zeta singular/zero structure는 regular correction을 제외하면 동일하다.

### audit consequence

first-order prime axis를 `P(s)`로 바꾸는 것은 zeta difficulty를 제거하는 것이 아니라 **logarithmic prime representation으로 옮기는 것**이다.

---

## 6. information interpretation

- higher `m` connected cumulants는 lower-order prime activations를 제거한다.
- 그 결과 absolute convergence boundary가 `1/m`까지 왼쪽으로 이동한다.
- 하지만 동시에 first-order distinct-prime axis 정보가 제거되어 RH-relevant global parity information을 잃는다.

즉 convergence improvement와 information loss가 함께 일어난다.

\[
\boxed{
\text{better convergence of connected tail}
\not\Rightarrow
\text{stronger control of }M(x).
}
\]

---

## 7. false-control rule

향후 어떤 construction에서 `1/2`가 새로 나타나면 다음을 즉시 검사한다.

1. order `m` generalization이 존재하는가?
2. 존재한다면 boundary가 `1/m`으로 이동하는가?
3. 그 `1/m`이 `P(ms)` 또는 prime-power tail `r>=m`의 ordinary convergence에서 오는가?

세 질문이 모두 yes이면 해당 `1/2`는 RH-specific evidence에서 제외한다.

---

## 8. 다음 전선에 주는 제약

새 arithmetic mechanism은

- higher prime-power tail의 쉬운 수렴만 사용해서는 안 되고,
- first-order prime-label information을 실제로 보존해야 하며,
- `P(s)=log zeta(s)+regular`라는 equivalence를 단순히 재사용해서도 안 된다.

즉 남은 어려움은 다시 **first activation / distinct prime placement / top parity coupling**으로 집중된다.

## 상태

- tail threshold `1/m`: `EXACT`.
- cumulant/tail hierarchy equivalence: `EXACT`.
- `m=2 -> 1/2` as RH evidence: `REJECTED_FALSE_CONTROL`.
- prime-axis reduction to `P(s)`: `REPRESENTATION_EQUIVALENCE`.
- RH: `OPEN`.
