# Stopping-branch common-prefix fixed-point audit — 2026-09-17

## Status
- Riemann hypothesis: OPEN.
- Resolution-stopping branch decomposition: retained.
- Individual branch band energy: already at the desired diagonal scale by periodicity/Parseval.
- New audit: common-prefix recursion of cross-branch interference.
- Result: prefix stripping gives an exact scale renormalization `(D,H)->(D/s,H/s)` but **no Möbius parity contraction**, because the common prefix sign squares out.
- The `s=1` divergence layer receives no scale gain at all and remains a leading obstruction.
- Therefore plain common-prefix recursion is a self-similar fixed-point reduction, not an independent contraction mechanism.

## 1. Stopping labels and common prefix
For squarefree `n in (D,2D]`, let

\[
q_H(n)=p_1\cdots p_{\tau_H(n)},\qquad
\tau_H(n)=\min\{j:p_1\cdots p_j\ge H\},
\]

with `p_1<p_2<...` the prime factors of `n`.

For two different stopping branches, let

\[
s=s(q,r)
\]

be the product of the common initial ordered prime factors before the first divergence. Then every `n in B_q` and `m in B_r` in that common-prefix class is divisible by `s`, so

\[
s\mid(n-m).
\]

For a lag `h=n-m`, cross-branch pairs in prefix class `s` therefore require

\[
\boxed{s\mid h.}
\]

This is exact arithmetic sparsity.

## 2. Exact rescaling after stripping the prefix
Write

\[
n=sa,\qquad m=sb,
\]

with `(a,s)=(b,s)=1` on the squarefree support. For the Fourier band

\[
I_H=[1/H,\sqrt2/H],
\]

one has

\[
e(\alpha(n-m))=e((s\alpha)(a-b)).
\]

With `beta=s alpha`,

\[
\int_{I_H}e(\alpha(n-m))\,d\alpha
=
\frac1s
\int_{I_{H/s}}e(\beta(a-b))\,d\beta.
\]

Thus common-prefix stripping transforms the geometry by

\[
\boxed{(D,H)\mapsto(D/s,H/s)}.
\]

The scale ratio `H/D` is unchanged, while the absolute resolution is reduced.

## 3. Möbius parity of the prefix cancels
For squarefree `n=sa` and `m=sb`,

\[
\mu(n)\mu(m)
=
\mu(s)^2\mu(a)\mu(b)
=
\mu(a)\mu(b).
\]

Therefore the common prefix contributes **no surviving sign** to the cross pair.

Classification:

`COMMON_PREFIX_PARITY_SQUARES_OUT`.

Any contraction must therefore come from the post-divergence ordered-factor structure, not from the prefix parity itself.

## 4. The fixed-point obstruction
If `s>1`, the transformed problem is a smaller copy at `(D/s,H/s)` with additional roughness/divergence restrictions.

But there is always the class

\[
\boxed{s=1},
\]

consisting of branches whose first prime factors already differ. For this class,

\[
(D,H)\mapsto(D,H),
\]

so there is no geometric scale reduction at all.

Hence a recursive estimate of the schematic form

\[
E(D,H)\le\sum_s w_s E(D/s,H/s)+\text{easy terms}
\]

cannot be a contraction merely because `s` grows along the tree: the root-divergence term `s=1` remains at the original scale, and prefix parity supplies no small coefficient.

Classification:

`COMMON_PREFIX_SELF_SIMILAR_FIXED_POINT_BARRIER`.

This does not rule out a recursion with a genuinely nontrivial post-divergence coefficient, but such a coefficient must be proved from additional arithmetic structure.

## 5. Finite band audit: first-prime layer versus full stopping layer
For a dyadic squarefree block, compare three quantities:

1. full band energy;
2. sum of band energies after grouping only by the **first prime factor**;
3. sum of band energies over the full resolution-stopping branches.

Normalize by

\[
\frac{\sqrt2-1}{H}\sum_{D<n\le2D}|c_n|^2.
\]

Representative values:

| D | H | coeff. | full | sum first-prime groups | sum stopping branches | cross between first-prime groups | cross inside first-prime groups | total stopping cross |
|---:|---:|---|---:|---:|---:|---:|---:|---:|
| 8192 | 16 | `mu` | 0.9704 | 0.9887 | 1.0040 | -0.0183 | -0.0153 | -0.0336 |
| 8192 | 16 | `mu^2` | 0.1372 | 0.5813 | 1.0038 | -0.4440 | -0.4225 | -0.8666 |
| 32768 | 32 | `mu` | 0.9912 | 1.0127 | 1.0018 | -0.0215 | +0.0109 | -0.0106 |
| 32768 | 32 | `mu^2` | 0.1442 | 0.5228 | 0.9993 | -0.3786 | -0.4765 | -0.8551 |

### Interpretation
For Möbius, both cross-prime and deeper within-first-prime interference are small at these finite scales.

For `mu^2`, branchwise diagonal energy is again essentially random baseline, but large negative cross interference appears already at the first-prime split and continues at deeper splits.

Thus the observed Möbius near-orthogonality is not explained by stopping geometry alone.

Classification:

`FINITE_FIRST_PRIME_PARITY_INTERFERENCE_SPLIT`.

This is numerical evidence, not an asymptotic theorem.

## 6. Relation to previous barriers
A common-prefix expansion may be rewritten using ordered rough cofactors and Buchstab-type recursions. If one then marginalizes labels or applies absolute values branchwise, it re-enters the already-audited sieve / restricted-Möbius architecture.

Therefore the only potentially new information left in the stopping construction is the **joint phase-sensitive cross interference after the first branch divergence**.

The following are not sufficient on their own:

- common-prefix divisibility `s|h`;
- the scale map `(D,H)->(D/s,H/s)`;
- prefix Möbius parity;
- finite-order Boolean prime-label tensors.

## 7. Updated live object
The next live object should condition on the **first divergence** itself.

Suppose two branches share prefix `s` and then activate distinct next primes `p<r`. After stripping `s`, retain simultaneously:

1. the ordering constraints that make `p` and `r` the first divergent active primes;
2. the signs contributed by the two post-prefix branches;
3. the exact reciprocal/Fourier kernel before taking absolute values.

The decisive question is:

> does summing over the distinct first-divergence primes produce a signed large-sieve / Hilbert-type contraction that is stronger than ordinary Buchstab or prime-divisibility tensor estimates?

If the answer is no, the stopping-branch route closes as another ordered-sieve reparameterization. If yes, the contraction must occur at the **divergence operator**, not in the common prefix tree itself.
