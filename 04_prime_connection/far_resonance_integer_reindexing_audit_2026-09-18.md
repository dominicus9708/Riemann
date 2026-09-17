# Far-resonance integer reindexing audit — 2026-09-18

## Status
- Riemann hypothesis: OPEN.
- Context: low-`Q` / long-Möbius Type-II far-shift sector after the near-shift cell has been separated.
- Candidate audited: whether the integer stationary index introduced by the reciprocal B-process imposes a genuinely sparse arithmetic condition on Möbius shift pairs.
- Conclusion: NO. The integer index is an analytic reindexing of a continuous derivative range; it does not by itself thin the `(w,h)` pairs.

## 1. Far-shift phase
After preserving the long Möbius factor and differencing it by `h`, the short smooth factor `d~M` carries phase

\[
\Phi(d)=C_{n,w,h}d^{-1/2},
\qquad
C_{n,w,h}=2K\sqrt n\left(w^{-1/2}-(w+h)^{-1/2}\right).
\]

For `w~L`, `h=o(L)` one has

\[
C_{n,w,h}\asymp K\sqrt n\,hL^{-3/2}.
\]

With total product scale `D=ML`, define

\[
H_n:=\frac{D^{3/2}}{K\sqrt n}.
\]

Then the derivative scale on `d~M` is

\[
|\Phi'(d)|\asymp \frac{h}{H_n}.
\]

Thus the already-closed near cell is `h\lesssim H_n`, while the stationary/far regime begins at `h\gtrsim H_n`.

## 2. Exact B-process stationary index
Since

\[
\Phi'(d)=-\frac{C}{2}d^{-3/2},
\]

a dual integer `r>=1` satisfies

\[
-\Phi'(d_r)=r.
\]

Hence

\[
\boxed{d_r=\left(\frac{C}{2r}\right)^{2/3}.}
\]

The condition `d_r~M` is equivalent to `r` lying in an interval

\[
\frac{C}{2(2M)^{3/2}}\lesssim r\lesssim \frac{C}{2M^{3/2}}.
\]

The length of this interval is

\[
\asymp C M^{-3/2}\asymp \frac{h}{H_n}.
\]

Therefore the number of admissible stationary integers is

\[
\boxed{\#\{r:d_r\asymp M\}\asymp \frac{h}{H_n}}
\]

throughout the genuine far region.

In particular, for every far-shift pair `(w,h)` there are not fewer but typically MORE admissible stationary integers as `h/H_n` grows.

Classification:

`FAR_RESONANCE_INTEGER_INDEX_NOT_ARITHMETIC_SPARSE`.

## 3. Exact dual phase
At the stationary point,

\[
\Phi(d_r)+rd_r
=3\cdot2^{-2/3}C^{2/3}r^{1/3}.
\]

Also

\[
\Phi''(d_r)
\asymp C^{-2/3}r^{5/3},
\]

so the stationary amplitude has scale

\[
|\Phi''(d_r)|^{-1/2}
\asymp C^{1/3}r^{-5/6}.
\]

Thus the reciprocal exponent `-1/2` is transformed to a dual `+1/3` exponent in the stationary index.

## 4. Small-shift form of the dual phase
For `h=o(L)`,

\[
C^{2/3}
\asymp
(K\sqrt n\,h)^{2/3}w^{-1}.
\]

Since the relevant dual integers have `r\asymp h/H_n`, the dual phase has leading scale

\[
C^{2/3}r^{1/3}
\asymp
\frac{K\sqrt n}{\sqrt D}\frac{h}{w}.
\]

Writing

\[
X_n:=\frac{K\sqrt n}{\sqrt D}=\frac{D}{H_n},
\]

the transformed phase is therefore of reciprocal-shift type

\[
\boxed{\Psi\asymp X_n\frac{h}{w}.}
\]

The B-process does not turn the long Möbius factor into a generic linear twist. It leaves a reciprocal phase coupled to the Möbius two-point coefficient

\[
\mu(w)\mu(w+h).
\]

## 5. Consequence
The hoped-for route

`integer stationary condition -> sparse (w,h) pairs -> easy far resonance`

is closed.

The integer `r` is an analytic label for the number of derivative crossings. It is not a new congruence or Diophantine restriction on the Möbius shifts.

After transformation the arithmetic core remains a weighted binary Möbius correlation of schematic form

\[
\sum_{h}\sum_w \mu(w)\mu(w+h)
\sum_{r\asymp h/H_n}
A_{n,w,h,r}
 e\!\left(c\,C_{n,w,h}^{2/3}r^{1/3}\right).
\]

Any further gain must therefore come from one of:
1. averaging/cancellation in the long Möbius variable before it becomes a binary correlation;
2. a coefficient-sensitive bilinear estimate;
3. a genuinely useful average over the outer `n` variable;
4. a new estimate for the weighted binary correlation itself.

Do not count `r in Z` as arithmetic sparsity in future audits.
