# j=2 Blomer--Pascadi critical-range near-match and inverse-support obstruction — 2026-09-20

## Status
- Riemann hypothesis: OPEN.
- Context: current double-refined branchwise deficit H^(1/8), with sharp refined factors of length H^(3/2)=sqrt(H^3).
- Literature tested: Blomer--Pascadi (2026), bilinear forms with Kloosterman sums via quadratic characters.
- Result:
  - the critical-length exponent is numerically very close to the required residual;
  - one valid application at modulus p~H^3 would save H^(-3/32), reducing H^(1/8) to H^(1/32);
  - however the direct determinant completion produces an inverse-supported argument set, not the short ordinary intervals required by the theorem.
- Therefore the theorem is a strong near-match, but no legal black-box closure or H^(1/32) improvement is claimed.
- Classification: \`BLOMER_PASCADI_H1_32_NEARMATCH_INVERSE_SUPPORT_OPEN\`.

## 1. Current required saving

The double-refined central branch satisfies
\[
T_{\rm ref\times ref}
\ll_\varepsilon
H^{6+1/8+\varepsilon}.
\]

The target is
\[
H^{6+\varepsilon}.
\]

Hence the missing amplitude saving is
\[
\boxed{H^{-1/8}=H^{-4/32}.}
\]

## 2. Critical Kloosterman modulus and refined length

In the determinant/Kloosterman formulation the natural prime modulus is
\[
c=p\asymp H^3.
\]

The sharp double-refined branch contains distinguished factors of length
\[
\boxed{
N=H^{3/2}=\sqrt p.
}
\]

Thus the factor length lies exactly in the critical range of the 2026 Blomer--Pascadi theorem.

## 3. Blomer--Pascadi theorem at the critical point

Their Theorem 1.1 gives, schematically,
\[
\sum_{m,n}
\alpha_m\beta_n S(am,n;c)
\ll
\|\alpha\|\|\beta\|c^{1+o(1)}
\left(
\frac{N^{1/8}}{c^{3/32}}
+
\frac{N^{5/16}}{c^{3/16}}
+
\frac{N^{2/3}}{c^{7/18}}
\right).
\]

At
\[
N=c^{1/2},
\]
the first two terms are
\[
c^{-1/32},
\]
while the third is smaller.

Hence the critical saving is
\[
\boxed{c^{-1/32}.}
\]

For
\[
c=p\asymp H^3,
\]
this becomes
\[
\boxed{
H^{-3/32}.
}
\]

If this saving could be inserted once into the exact refined j=2 branch, the residual would formally become
\[
H^{1/8}H^{-3/32}
=
\boxed{H^{1/32}}.
\]

This is only a numerical benchmark until the exact transformed sum matches the theorem.

## 4. Determinant completion produces a reciprocal index

The centered determinant shell has, after a favorable Poisson/completion model, the reciprocal phase
\[
e\!\left(
\frac{A\,\overline{p'}}{p}
\right),
\qquad
p,p'\asymp H^3.
\]

In the sharp refined block factor
\[
p'=mn,
\qquad
m,n\asymp H^{3/2}.
\]

Then
\[
\overline{p'}
=
\bar m\,\bar n
\pmod p,
\]
so the phase is
\[
e\!\left(
\frac{A\bar m\bar n}{p}
\right).
\]

Completing the m-sum modulo p produces Kloosterman sums whose other argument depends on
\[
\bar n\pmod p.
\]

Thus the remaining family is naturally indexed by the modular inverses of a short interval.

## 5. Why Theorem 1.1 is not yet a black box

Blomer--Pascadi Theorem 1.1 assumes its two bilinear index sequences are supported in ordinary integer intervals of length at most N.

For
\[
n\asymp\sqrt p,
\]
the set
\[
\{\bar n\bmod p\}
\]
is not, in general, contained in an interval of length \(p^{1/2+o(1)}\).

Treating it as an arbitrary subset of the full residue interval would enlarge the effective support to p and destroy the critical \(N=\sqrt p\) parameter match.

Therefore the implication
\[
\text{refined determinant completion}
\Longrightarrow
\text{Blomer--Pascadi critical bilinear form}
\]
has not been established.

Permanent guard:
\`MODULAR_INVERSE_OF_SHORT_INTERVAL_IS_NOT_SHORT_INTERVAL\`.

## 6. Kloosterman scaling identities do not automatically fix support

For invertible arguments one may use identities such as
\[
S(a,b;p)=S(1,ab;p)
\]
after a change of variable.

This can move multiplicative factors between the two Kloosterman arguments.

But it does not turn the inverse set
\[
\{\bar n:n\sim\sqrt p\}
\]
into an ordinary short additive interval.

Thus a formal algebraic rewrite is insufficient.

## 7. What would make the theorem applicable

A legal map would require one of the following:

1. derive a completion in which the two refined \(H^{3/2}\) factors enter the Kloosterman arguments **linearly**, rather than through modular inversion;

2. prove a version of the Blomer--Pascadi bound stable for inverse images of short intervals;

3. average over the modulus/frame variables strongly enough that inverse-support localization can be replaced by a short ordinary interval after a second reciprocity transformation.

None of these has yet been proved in the project.

## 8. Quantitative significance

The near-match is still important.

The latest general-modulus critical theorem supplies
\[
H^{-3/32},
\]
while the project needs
\[
H^{-4/32}.
\]

So even after finding a legal critical-range normal form, one application would leave only
\[
\boxed{H^{1/32}}
\]
of the current branchwise deficit.

This is much smaller than the original
\[
H^{1/2},\ H^{1/4},\ H^{1/6},\ H^{1/8}
\]
frontiers.

But until the support issue is resolved, the official frontier remains
\[
\boxed{H^{1/8}}.
\]

## 9. Next exact algebraic target

Starting from the unimodular parametrization
\[
p=k\bar a+b\ell,
\qquad
p'=a\ell+k t_{a,b},
\]
and the double-refined prime decompositions, derive every possible one-variable completion order.

For each order record:
- modulus;
- two Kloosterman arguments;
- support lengths before and after inversion;
- whether both variable supports remain ordinary intervals of length \(c^{1/2+o(1)}\).

The goal is to find a normal form genuinely covered by Blomer--Pascadi Theorem 1.1, or to close this route as an inverse-support barrier.

Permanent priority:
\`SEARCH_LINEAR_ARGUMENT_KLOOSTERMAN_NORMAL_FORM_BEFORE_CLAIMING_BP_GAIN\`.
