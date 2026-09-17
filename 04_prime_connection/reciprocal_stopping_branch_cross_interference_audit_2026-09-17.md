# Reciprocal stopping-branch cross-interference audit — 2026-09-17

## Status
- Riemann hypothesis: OPEN.
- Ordinary least-prime / ordered-prime decomposition: STANDARD Buchstab-type re-entry.
- New phase-dependent bookkeeping: stop when the cumulative ordered prime product first crosses the reciprocal resolution `H`.
- Every stopped branch individually has the required shrinking-band `L^2` scale by periodicity and Parseval alone.
- Therefore the only remaining band-energy obstruction is **cross-interference between distinct stopping branches**.
- Finite audit: Möbius cross-interference is small at tested scales, while removing parity signs (`mu^2`) produces a large negative cross term.
- No asymptotic theorem is claimed.

## 1. Standard part: ordered factorization is Buchstab
For a squarefree integer

\[
n=p_1p_2\cdots p_k,
\qquad p_1<p_2<\cdots<p_k,
\]

successively isolating the smallest remaining prime and imposing that the cofactor have no smaller prime factor is exactly the mechanism of the iterated Buchstab identity. Thus ordered prime activation **by itself** is not a new analytic device.

The present audit keeps only the extra feature that the stopping depth depends on the reciprocal resolution `H`.

## 2. Resolution stopping divisor
Assume `D<n<=2D`, `mu(n) != 0`, and `1<H<D`. Put

\[
q_j(n)=p_1p_2\cdots p_j.
\]

Since `q_k(n)=n>H`, the stopping index

\[
\tau_H(n)=\min\{j:q_j(n)\ge H\}
\]

exists. Define

\[
\boxed{q_H(n):=q_{\tau_H(n)}(n).}
\]

Then

\[
q_H(n)\ge H,
\]

and the squarefree support is partitioned into disjoint stopping branches

\[
B_q:=\{n\in(D,2D]:\mu(n)\ne0,\ q_H(n)=q\}.
\]

For each branch define

\[
P_q(\alpha)=\sum_{n\in B_q}c_n e(\alpha n),
\]

where `c_n` may be `mu(n)` or any coefficients supported on the same branch.

Because every `n in B_q` is divisible by `q`, write `n=qm` and

\[
P_q(\alpha)=\sum_{m:qm\in B_q}c_{qm}e(q\alpha m).
\]

## 3. Exact branchwise band bound
Let

\[
I_H=\left[\frac1H,\frac{\sqrt2}{H}\right].
\]

Changing variables `beta=q alpha`,

\[
\int_{I_H}|P_q(\alpha)|^2d\alpha
=
\frac1q
\int_{q/H}^{\sqrt2 q/H}
\left|\sum_{m:qm\in B_q}c_{qm}e(\beta m)\right|^2d\beta.
\]

The inner trigonometric polynomial is 1-periodic. For any interval of length `L`, periodicity and Parseval give

\[
\int_J|S(\beta)|^2d\beta
\le (L+1)\int_0^1|S(\beta)|^2d\beta.
\]

Here `L=(sqrt(2)-1)q/H`; hence

\[
\int_{I_H}|P_q|^2
\le
\left(\frac{\sqrt2-1}{H}+\frac1q\right)
\sum_{n\in B_q}|c_n|^2.
\]

Since `q>=H`,

\[
\boxed{
\int_{I_H}|P_q(\alpha)|^2d\alpha
\le
\frac{\sqrt2}{H}
\sum_{n\in B_q}|c_n|^2.
}
\]

Summing over the disjoint branches yields

\[
\boxed{
\sum_q\int_{I_H}|P_q|^2
\le
\frac{\sqrt2}{H}
\sum_{D<n\le2D}|c_n|^2.
}
\]

Classification:

`STOPPING_BRANCH_INDIVIDUAL_DIAGONAL_SCALE`.

This bound is deterministic and requires no Möbius cancellation.

## 4. Exact reduction to cross-branch interference
Since

\[
P(\alpha)=\sum_qP_q(\alpha),
\]

we have

\[
\boxed{
\int_{I_H}|P|^2
=
\sum_q\int_{I_H}|P_q|^2
+
\sum_{q\ne r}
\int_{I_H}P_q(\alpha)\overline{P_r(\alpha)}d\alpha.
}
\]

The first term already has the desired `1/H` scale. Therefore the entire unresolved mesoscopic band problem has been reduced to the second term.

Classification:

`STOPPING_BRANCH_CROSS_INTERFERENCE_REDUCTION`.

## 5. Near-lag separation is automatically cross-branch
If `n,n+h` lie in the same branch `B_q`, then `q` divides both integers and hence `q|h`.

Because `q>=H`, for

\[
0<|h|<H
\]

this is impossible. Thus

\[
\boxed{
q_H(n)=q_H(n+h),\ 0<|h|<H
\quad\Longrightarrow\quad\text{impossible}.
}
\]

Every dangerous near-diagonal correlation at shifts below the reciprocal resolution is therefore an interaction between **different** stopping branches.

Classification:

`NEAR_LAG_STOPPING_BRANCH_SEPARATION`.

## 6. Finite exact/numerical audit
The audit used squarefree integers in `(D,2D]`, stopping labels `q_H(n)`, and the band

\[
[1/H,\sqrt2/H].
\]

Band energies were normalized by

\[
\frac{\sqrt2-1}{H}\sum_{D<n\le2D}|c_n|^2.
\]

Representative values:

| D | H | coefficients | full band | sum of branch bands | cross term |
|---:|---:|---|---:|---:|---:|
| 8192 | 16 | `mu` | 0.9703 | 1.0040 | -0.0336 |
| 8192 | 16 | `mu^2` | 0.1372 | 1.0038 | -0.8666 |
| 32768 | 32 | `mu` | 0.9910 | 1.0018 | -0.0108 |
| 32768 | 32 | `mu^2` | 0.1442 | 0.9993 | -0.8551 |

Thus the branchwise diagonal scale is essentially the same for `mu` and `mu^2`; their radically different full band energies are almost entirely a cross-branch phenomenon.

Classification:

`FINITE_STOPPING_BRANCH_PARITY_INTERFERENCE`.

This is `NUMERICAL`, not a theorem.

## 7. Stopping-depth matrix
Let `P^{(j)}` denote the sum of branches with stopping depth `tau_H(n)=j`. At `D=32768`, `H=32`, the normalized real band-energy matrix for Möbius is approximately

\[
\begin{pmatrix}
0.2434&-0.0019&-0.0085&0.0011\\
-0.0019&0.5293&0.0047&0.0008\\
-0.0085&0.0047&0.2110&0.0007\\
0.0011&0.0008&0.0007&0.0136
\end{pmatrix}.
\]

The diagonal masses closely follow the squarefree mass of each depth layer, while cross-depth entries are small in this finite sample.

For `mu^2` on the same support the matrix is approximately

\[
\begin{pmatrix}
0.1296&-0.1899&0.0908&-0.0203\\
-0.1899&0.4288&-0.2197&0.0490\\
0.0908&-0.2197&0.2269&-0.0378\\
-0.0203&0.0490&-0.0378&0.0146
\end{pmatrix}.
\]

Hence the finite near-orthogonality of depth layers is associated with the retained Möbius parity, not with stopping geometry alone.

Permanent guard:

`STOPPING_DEPTH_NUMERICAL_ORTHOGONALITY_NOT_THEOREM`.

## 8. Relation to standard sieve decompositions
The decomposition into ordered prime factors and rough cofactors is standard Buchstab/iterated-sieve structure. The current reduction must therefore **not** be advertised as a new factorization identity.

What is specific to the present reciprocal problem is:

1. the stopping boundary is the dynamically generated resolution `H`;
2. crossing this boundary makes every individual branch have a full/constant-width Fourier period after the change `beta=q alpha`;
3. the unresolved analytic burden is isolated entirely in cross-branch parity interference.

No novelty claim is made until that cross-interference is controlled by a mechanism not equivalent to existing Buchstab/Ramaré/Type-I/II machinery.

## 9. Next direct audit: common-prefix tree
For two distinct stopping labels `q_H(n)` and `q_H(n')`, let `s` be the product of their common initial ordered prime factors before the first branch divergence.

If `s>1`, then `s|n` and `s|n'`, so

\[
s\mid(n-n').
\]

Thus a cross-branch pair at shift `h` can occur only when its common-prefix product divides `h`. For `|h|<H` this creates an exact arithmetic sparsity depending on the position of the branch divergence.

The next question is whether stratifying cross-branch interference by this common-prefix tree gives a summable contraction after Möbius parity is retained, or whether the resulting recursion is merely another form of Buchstab/Ramaré decomposition.
