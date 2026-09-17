# Stopping first-divergence parity-deferral audit — 2026-09-17

## Status
- Riemann hypothesis: OPEN.
- Common-prefix contraction: closed as a self-similar fixed-point mechanism.
- New audit: the first branch-divergence operator itself.
- Result: the Möbius signs of the shared prefix and of the two first divergent primes cancel pairwise.
- Therefore no local sign contraction is generated at a finite divergence node; parity is deferred to the post-divergence cofactors.
- If the rough-cofactor tails are then bounded/marginalized by standard means, the construction re-enters Buchstab/Ramaré/low-order-label barriers.
- Any surviving mechanism must retain the **joint tail parity across a scale-growing number of activation steps** together with the reciprocal phase.

## 1. First-divergence coordinates
Let two squarefree integers in distinct stopping branches have common initial ordered-prime prefix

\[
s=p_1\cdots p_j,
\]

and let their next prime factors be distinct primes `p` and `r` larger than all primes in `s`.

Write

\[
n=s p a,\qquad m=s r b,
\]

where the prime factors of `a` are larger than `p` and those of `b` are larger than `r`, with the additional stopping/interval restrictions inherited from the branch definitions.

Then

\[
\mu(n)=\mu(s)(-1)\mu(a),
\qquad
\mu(m)=\mu(s)(-1)\mu(b).
\]

Hence

\[
\boxed{
\mu(n)\mu(m)=\mu(a)\mu(b).
}
\]

The factors `mu(s)^2` and `(-1)^2` both disappear.

Classification:

`FIRST_DIVERGENCE_LOCAL_PARITY_CANCELLATION`.

The word cancellation here means cancellation **of the bookkeeping signs themselves**, not cancellation of the analytic sum.

## 2. Consequence
At a finite divergence node, the pair correlation does not receive an alternating sign from choosing different next primes.

The sign information is pushed entirely into the two post-divergence tails `mu(a)mu(b)`.

Therefore a hoped-for mechanism of the form

> distinct next-prime labels carry opposite Möbius signs and cancel when summed over the branch tree

is false at the pair-correlation level.

Both branches acquire one new prime and hence the two local `-1` factors multiply to `+1`.

## 3. General finite-prefix parity deferral
The same observation iterates. If one exposes `k` paired activation levels on the two sides, every level exposed symmetrically contributes an even number of Möbius sign flips to the product.

Consequently, after any finite paired stripping,

\[
\mu(n)\mu(m)
=
(\text{known constant sign from any unequal exposed depths})
\times
\mu(a_k)\mu(b_k),
\]

and the unresolved parity remains in the tails.

If the two exposed depths are equal, the known sign is `+1`.

Thus a fixed-depth operator cannot manufacture global parity cancellation merely from local activation labels.

Classification:

`FINITE_DEPTH_PAIR_PARITY_DEFERRAL`.

## 4. Relation to the earlier parity-information barrier
The earlier Boolean/marginal audit showed that global Möbius parity is orthogonal to every proper low-order prime-label marginal on a complete Boolean cube.

The present result is the ordered-factorization analogue of that fact:

- static finite labels fail because global parity lives at full interaction order;
- ordered finite prefixes fail because pairwise stripping moves parity into the unresolved tails.

The two barriers are structurally consistent.

## 5. Phase after first divergence
The reciprocal/Fourier pair phase becomes

\[
e\!\left(\alpha s(pa-rb)\right).
\]

After `beta=s alpha`, the prefix again only rescales the band to `H/s`.

The remaining first-divergence operator therefore has schematic form

\[
\sum_{p\ne r}
\sum_{a,b}
\mu(a)\mu(b)
\,W_{s,p,r}(a,b)
\,K_{H/s}(pa-rb),
\]

with roughness and stopping constraints encoded in `W`.

If one discards the signed kernel or sums `p,r` by absolute values, this is an ordinary bilinear rough-cofactor problem and re-enters standard Buchstab/Ramaré/Type-I/II machinery.

No independent contraction has been obtained.

## 6. What remains logically open
The failure is specifically a **finite local divergence** failure. It does not prove that the full stopping tree is useless.

A genuinely different mechanism could still use:

1. unequal stopping depths, where the branch constants carry `(-1)^{tau_q+tau_r}`;
2. a scale-growing number of ordered activations before tails are marginalized;
3. the full reciprocal phase coupling of the two tail products;
4. interference between many stopping labels at once rather than pairwise absolute control.

But any such mechanism must preserve global/tail parity. Replacing the tails by density, unsigned rough-number counts, or fixed-order label statistics destroys precisely the information that distinguishes `mu` from `mu^2` in the finite band audits.

## 7. Updated direction
The next audit should not descend one more fixed level in the prime tree. That would simply repeat parity deferral.

Instead, test the **stopping-depth parity decomposition** itself:

\[
P(\alpha)=\sum_j P^{(j)}(\alpha),
\qquad
P^{(j)}=\sum_{\tau_H(n)=j}\mu(n)e(\alpha n).
\]

The finite audit already suggests that Möbius depth layers are nearly band-orthogonal whereas `mu^2` depth layers exhibit large alternating cross terms.

The next precise question is whether the depth-parity transform

\[
\sum_j(-1)^j R_j(\alpha),
\]

where `R_j` carries the unsigned rough-tail mass at stopping depth `j`, admits an exact generating-function or transfer-operator representation whose contraction is **not** equivalent to a fixed-order Buchstab recursion.

If that transform collapses to the usual Buchstab generating function or sieve parity problem, the stopping route should be closed. If it does not, it is the first remaining place where the empirically active global parity has not yet been marginalized away.
