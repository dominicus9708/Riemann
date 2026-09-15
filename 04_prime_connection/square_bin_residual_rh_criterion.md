# Square-Bin Residual RH Criterion

Date: 2026-09-16

## 목적

square-bin Euler compression에서 남은 count sequence

\[
c_m=\pi((m+1)^2)-\pi(m^2)
\]

를 직접 RH-scale arithmetic residual로 바꾸고, 그 residual이 새로운 난점인지 classical Chebyshev error의 coarse reencoding인지 판정한다.

결론부터 말하면 매우 깔끔한 RH-equivalent 1차원 criterion이 얻어지지만, 현재로서는 `REENCODING / NO PROOF`이다.

---

## 1. square-bin weighted mass

`m>=2`에 대해

\[
c_m=\#\{p:m^2<p<(m+1)^2\}
\]

로 두고

\[
S_M:=\log 2+\log 3+2\sum_{m=2}^{M}c_m\log m
\]

를 정의한다.

`S_M`은 square-bin canonical generalized-prime system의 generalized Chebyshev `theta`가 scale `(M+1)^2`에서 갖는 값이다.

classical Chebyshev function은

\[
\vartheta(x)=\sum_{p\le x}\log p.
\]

각 bin `I_m=[m^2,(m+1)^2)`에서 `p`를 `m^2`로 옮길 때 log-weight error는

\[
0\le \log p-2\log m
\le 2\log(1+1/m)
\ll 1/m.
\]

또 trivial하게 `c_m<=2m+1`. 따라서 bin당 total weight error는 `O(1)`이고

\[
\boxed{
S_M=\vartheta((M+1)^2)+O(M).
}
\]

이 estimate는 PNT를 사용하지 않는다.

상태: `EXACT ELEMENTARY BOUND`.

---

## 2. local square-bin residual

square interval의 길이는

\[
(m+1)^2-m^2=2m+1.
\]

따라서

\[
\boxed{
d_m:=2c_m\log m-(2m+1)
}
\]

를 정의한다.

그러면 telescoping으로

\[
\sum_{m=2}^{M}(2m+1)=(M+1)^2-4
\]

이므로

\[
S_M-(M+1)^2
=
\sum_{m=2}^{M}d_m+(\log6-4).
\]

Section 1과 결합하면

\[
\boxed{
\sum_{m=2}^{M}d_m
=
\vartheta((M+1)^2)-(M+1)^2+O(M).
}
\]

즉 `d_m` partial sum은 classical Chebyshev error를 consecutive squares에서 sampled/coarse-grained한 것과 정확히 같은 scale이다.

---

## 3. RH-equivalent real-variable criterion

classical equivalent form:

\[
\mathrm{RH}
\iff
\vartheta(x)-x=O_\varepsilon(x^{1/2+\varepsilon})
\quad\forall\varepsilon>0.
\]

square points `x=(M+1)^2`에서 이는

\[
\vartheta((M+1)^2)-(M+1)^2
=O_\varepsilon(M^{1+\varepsilon}).
\]

반대로 square points에서 이 bound가 성립하면 임의의 `x in [M^2,(M+1)^2)`에 대해 `theta`의 monotonicity와 interval width `O(M)`을 사용하여 global bound가 복원된다.

따라서

\[
\boxed{
\mathrm{RH}
\iff
\sum_{m=2}^{M}
\left(2c_m\log m-(2m+1)\right)
=O_\varepsilon(M^{1+\varepsilon})
\quad\forall\varepsilon>0.
}
\]

RH의 standard logarithmic form을 쓰면

\[
\sum_{m\le M}d_m=O(M\log^2M)
\]

도 RH 아래 성립한다.

중요: individual `d_m`을 작게 만들 필요는 없다. 필요한 것은 **누적 signed cancellation**이다. 따라서 Legendre conjecture나 각 square interval의 expected prime count를 pointwise 증명하는 것보다 논리적으로 훨씬 약한 조건이다.

---

## 4. Dirichlet-series criterion

square-bin residual Dirichlet series를

\[
\boxed{
\mathcal D_\square(s)
:=
\sum_{m=2}^{\infty}
\frac{d_m}{m^{2s}}
=
\sum_{m=2}^{\infty}
\frac{2c_m\log m-(2m+1)}{m^{2s}}
}
\]

로 둔다.

### RH => convergence on Re(s)>1/2

RH이면 partial sums

\[
A(M):=\sum_{m\le M}d_m
=O_\varepsilon(M^{1+\varepsilon}).
\]

고정 `sigma>1/2`에 대해 `epsilon<2sigma-1`을 택하면 partial summation으로 `D_square(s)`가 `Re(s)>=sigma` compact sets에서 수렴한다.

### converse

`D_square(s)`가 모든 real `s>1/2`에서 수렴한다고 하자. 임의의 `delta>0`에 대해 exponent `2s=1+delta/2`인 series가 수렴한다. Abel summation을 역으로 적용하면

\[
A(M)=o(M^{1+\delta/2})=O(M^{1+\delta}).
\]

모든 `delta>0`에 대해 성립하므로 Section 3에 의해 RH가 따른다.

따라서

\[
\boxed{
\mathrm{RH}
\iff
\mathcal D_\square(s)
\text{ converges throughout }\Re s>1/2.
}
\]

동등하게 ordinary Dirichlet variable `w=2s`를 쓰면 `sum d_m m^{-w}`의 convergence abscissa가 `<=1`이라는 criterion이다.

상태: `DERIVED RH-EQUIVALENT CRITERION / NOT A PROOF`.

---

## 5. exact log-derivative decomposition

square-bin Beurling zeta는

\[
Z_\square(s)
=(1-2^{-s})^{-1}(1-3^{-s})^{-1}
\prod_{m\ge2}(1-m^{-2s})^{-c_m}.
\]

`Re(s)>1`에서

\[
-\frac{Z_\square'}{Z_\square}(s)
=
\frac{\log2}{2^s-1}
+
\frac{\log3}{3^s-1}
+
2\sum_{m\ge2}c_m\log m\frac{m^{-2s}}{1-m^{-2s}}.
\]

첫 generalized-prime-power와 higher powers를 분리하면

\[
\frac{m^{-2s}}{1-m^{-2s}}
=m^{-2s}+
\frac{m^{-4s}}{1-m^{-2s}}.
\]

또

\[
\sum_{m\ge2}(2m+1)m^{-2s}
=
2\zeta(2s-1)+\zeta(2s)-3.
\]

따라서

\[
\boxed{
-\frac{Z_\square'}{Z_\square}(s)
=
\mathcal D_\square(s)
+2\zeta(2s-1)+\zeta(2s)-3
+R_{\ge2}(s)+E_{2,3}(s),
}
\]

where

\[
R_{\ge2}(s)
=
2\sum_{m\ge2}c_m\log m
\frac{m^{-4s}}{1-m^{-2s}},
\]

and

\[
E_{2,3}(s)=\frac{\log2}{2^s-1}+\frac{\log3}{3^s-1}.
\]

trivial bound `c_m=O(m)` gives

\[
R_{\ge2}\text{ absolutely analytic on }\Re s>1/2.
\]

`zeta(2s)`의 pole은 boundary `s=1/2`에 있고, `2zeta(2s-1)`은 open half-plane에서 `s=1`에만 pole을 갖는다.

따라서 open half-plane `Re(s)>1/2`에서 실제 비자명 singularity를 운반할 수 있는 count-only term이 정확히 `D_square`임이 드러난다.

이 decomposition은 square-bin residual criterion과 Beurling zero-divisor theorem이 같은 구조임을 확인한다.

---

## 6. finite audit

exact prime counts로 `M=2^j`, `j=4,...,11`을 계산했다.

| M | (M+1)^2 | c_M | sum d_m | theta-x | S_M-theta | sum d/(M log^2 M) |
|---:|---:|---:|---:|---:|---:|---:|
| 16 | 289 | 7 | -22.116 | -17.655 | -6.669 | -0.1798 |
| 32 | 1089 | 9 | -51.910 | -42.423 | -11.695 | -0.1351 |
| 64 | 4225 | 14 | -98.632 | -80.930 | -19.910 | -0.0891 |
| 128 | 16641 | 24 | -184.367 | -152.825 | -33.750 | -0.0612 |
| 256 | 66049 | 53 | -342.744 | -286.762 | -58.190 | -0.0435 |
| 512 | 263169 | 79 | -832.049 | -732.993 | -101.264 | -0.0418 |
| 1024 | 1050625 | 149 | -1440.681 | -1264.283 | -178.606 | -0.0293 |
| 2048 | 4198401 | 265 | -2449.205 | -2132.675 | -318.738 | -0.0206 |

여기서 `S_M-theta=O(M)`인 deterministic compression error가 실제로 작게 유지됨을 확인한다.

상태: `NUMERICAL CONSISTENCY ONLY`.

---

## 7. interpretation

이번 criterion은 정보압축 측면에서는 유용하지만 난제를 해결하지 않는다.

원래 문제:

\[
\vartheta(x)-x\text{의 square-root cancellation}
\]

을

\[
\sum_{m\le M}
\bigl[2c_m\log m-(2m+1)\bigr]
\text{의 near-linear cancellation}
\]

으로 옮긴 것이다.

즉 exact prime positions를 제거하는 데는 성공했지만, 난점은 **square-bin count residual 사이의 장거리 deterministic cancellation**으로 이동한다.

현재 판정:

- exact prime positions: `NOT NECESSARY` within RH-equivalent Beurling class;
- square-bin counts: `SUFFICIENT INFORMATION`;
- weighted cumulative residual criterion: `EXACT RH EQUIVALENCE`;
- independent proof progress: `NOT ESTABLISHED`;
- next possible frontier: correlation/transport law among `d_m` that survives Beurling critical-resolution quotient and is not ordinary explicit-formula reencoding.