# Zero Counting: N(T) and Riemann–von Mangoldt Audit

## 1. Why N(T) is required

A list of zeros found numerically is not automatically complete. To distinguish

- `zeros found on the critical line`, and
- `all zeros in the strip up to height T`,

an independent zero-counting mechanism is required.

This is the main reason N(T) is part of the repository baseline before pattern analysis.

## 2. Argument-principle count

Bombieri's official CMI description explains a contour-counting method. For a rectangle containing the critical strip up to height T, Cauchy's argument principle applied to zeta counts zeros minus the pole at s=1 through an integral of zeta'/zeta.

This gives, in principle, an exact integer zero count when the contour avoids zeros and the numerical evaluation is rigorous enough.

Status: `THEOREM_ESTABLISHED / EXACT_COUNTING_PRINCIPLE`.

Audit point: rounding a non-rigorous floating approximation to the nearest integer is not automatically a proof. Error bounds must certify that the rounded integer is unique.

## 3. Riemann–von Mangoldt formula

For the standard zero-counting function N(T),

\[
N(T)=\frac{T}{2\pi}\log\left(\frac{T}{2\pi}\right)-\frac{T}{2\pi}+\frac78+S(T)+O\!\left(\frac1T\right),
\]

where

\[
S(T)=\frac1\pi\arg\zeta\!\left(\frac12+iT\right)
\]

with the argument defined by continuous continuation along the standard path.

A coarser form is

\[
N(T)=\frac{T}{2\pi}\log\left(\frac{T}{2\pi}\right)-\frac{T}{2\pi}+O(\log T).
\]

Status: `THEOREM_ESTABLISHED`.

## 4. Mean zero density and spacing

Differentiating only the smooth main term heuristically gives local density

\[
\frac{1}{2\pi}\log\left(\frac{T}{2\pi}\right),
\]

so the corresponding local mean spacing is approximately

\[
\bar\Delta(T)\approx\frac{2\pi}{\log(T/(2\pi))}.
\]

This is why the baseline normalized gap uses

\[
\delta_n=(\gamma_{n+1}-\gamma_n)\frac{\log(\gamma_n/(2\pi))}{2\pi}.
\]

Audit warning: the derivative of an asymptotic counting formula is not an exact formula for individual gaps. Local fluctuations can be large.

## 5. Initial numerical regression

Using mpmath only as a non-certifying implementation check:

| T | nzeros(T) | smooth main + 7/8 | S(T) | theta(T)/pi + 1 + S(T) |
|---:|---:|---:|---:|---:|
| 50 | 10 | 9.4227817898 | 0.5770855779 | 10 |
| 100 | 29 | 29.0023435873 | -0.0024099023 | 29 |
| 143.12 | 50 | 49.2971606080 | 0.7027930570 | 50 |
| 1000 | 649 | 648.6162353130 | 0.3837580556 | 649 |
| 10000 | 10142 | 10142.9653475268 | -0.9653481900 | 10142 |

These checks confirm internal consistency of the implementation, not the mathematical theorem itself.

## 6. Audit traps

### A. Asymptotic-as-exact error
The smooth main term is not an integer zero count and must not be rounded without a certified error estimate.

### B. Sign-change completeness error
The number of observed sign changes of Z(t) may undercount zeros if sampling is too coarse or if an even-multiplicity zero occurs.

### C. RH contamination
N(T) counts zeros in the critical strip independently of whether RH is true. A zero-counting algorithm must not silently assume every zero is already on the critical line.

### D. Endpoint convention
Definitions may count zeros at gamma=T with full or half weight. Every comparison must state the convention.

## 7. Source audit

- CMI/Bombieri: accepted for the argument-principle logic and official classical context. Its old numerical records are historical, not current records.
- Riemann–von Mangoldt formula: standard theorem; modern peer-reviewed literature such as Chirre (2021) states the refined formula explicitly while citing standard monographs.
- mpmath: accepted only as a convenient regression implementation; not a source of proof or completeness certification.

## References

- Enrico Bombieri, “The Riemann Hypothesis”, official CMI Millennium Prize problem description, especially the numerical verification discussion.
- NIST DLMF §25.10: https://dlmf.nist.gov/25.10
- E. Chirre, “Large oscillations of the argument of the Riemann zeta-function”, Bulletin of the London Mathematical Society (2021), for a modern statement of the Riemann–von Mangoldt formula.
