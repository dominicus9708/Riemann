# j=2 outer-prime third decomposition and all-unit self-dual persistence — 2026-09-20

## Status
- Riemann hypothesis: OPEN.
- Context: current sharp double-refined amplitude branch
  \[
  \{2;\{3/2,3/4,3/4\},\{3/2,3/4,3/4\}\}
  \]
  with standard-DLS loss H^(1/8).
- Candidate tested: isolate the sharp outer-d prime subfamily, replace \(-1\) by \(-\Lambda(d)/\log d\), and apply a third Vaughan/Heath--Brown decomposition to d~H^2.
- Result:
  - factorable daughter branches can become exactly product-balanced;
  - however the all-unit first-Type-I branch retains a single smooth d-variable of length H^2;
  - H^2 is exactly the B-process self-dual length for phase amplitude H^4;
  - transforming that smooth variable does not change the factor-scale H^(1/8) barrier.
- Classification: \`J2_OUTER_PRIME_THIRD_DECOMPOSITION_ALL_UNIT_BARRIER\`.

## 1. Sharp branch

The current sharp factor-scale witness is
\[
\boxed{
\left\{
2,\,
\frac32,\frac34,\frac34,\,
\frac32,\frac34,\frac34
\right\}.
}
\]

The full H-exponent total is 8.

The nearest subset sums to the self-dual target 4 are
\[
\frac{15}{4}
\quad\text{and}\quad
\frac{17}{4},
\]
so
\[
\Delta_H=\frac14
\]
and standard DLS gives
\[
H^{6+1/8+\varepsilon}.
\]

The exponent 2 is the outer Möbius variable
\[
d\asymp H^2.
\]

## 2. Prime d is the atomic endpoint

For prime
\[
d\asymp H^2,
\]
\[
\mu(d)=-1.
\]

Up to logarithmic factors one may write on this subfamily
\[
-1=-\frac{\Lambda(d)}{\log d}.
\]

Therefore it is legitimate as an audit to ask whether a prime identity applied to the outer d-variable improves the hard scale.

Choose Vaughan parameters
\[
U=V=H
\]
for the d-variable of total scale H^2.

## 3. Factorable Type-II daughter is exactly balanced

A central outer-d Type-II branch has
\[
d=uv,
\qquad
u,v\asymp H.
\]

Thus exponent 2 is replaced by
\[
1+1.
\]

Together with the two sharp refined H^3 branches, the exponent list becomes
\[
\left\{
1,1,\,
\frac32,\frac34,\frac34,\,
\frac32,\frac34,\frac34
\right\}.
\]

Now there is an exact exponent-4 subset, for example
\[
1+\frac32+\frac34+\frac34
=
4.
\]

Hence this daughter branch is product-balanced:
\[
\boxed{\Delta_H=0.}
\]

So the third decomposition genuinely closes its factorable daughter pieces.

## 4. But the prime signal sits in the all-unit Type-I branch

For an actual prime d>H, the only divisor d_0<=H entering the first Type-I convolution is
\[
d_0=1.
\]

Thus the first Type-I branch contains the all-unit term
\[
L(d)=\log d
\]
with d still of full length
\[
\boxed{H^2}.
\]

On the prime support this term is exactly the prime signal; the other Vaughan branches vanish pointwise there.

Therefore no exact prime identity can force every branch to split the exponent 2 into two positive pieces.

Classification:
\`OUTER_PRIME_ALL_UNIT_H2_ATOM_PERSISTS\`.

## 5. The surviving H^2 variable is smooth

The important difference from the original prime coefficient is that the all-unit daughter carries the smooth/logarithmic amplitude
\[
\log d.
\]

It is therefore legal to test a B-process in d.

The normalized reciprocal phase amplitude is
\[
F=H^4.
\]

For
\[
D=H^2,
\]
the B-process dual length is
\[
D^*=\frac FD=H^2.
\]

Hence
\[
\boxed{D=D^*=\sqrt F.}
\]

The all-unit outer-d variable lies exactly at B-process self-duality.

## 6. B-process does not change the factor-scale deficit

The stationary amplitude is
\[
D/\sqrt F=1.
\]

The transformed dual variable again has H-exponent 2.

Thus, at the factor-scale level, B-process replaces
\[
2
\]
by
\[
2
\]
and changes only the phase orientation/sign in the transformed monomial.

The tuple-length subset list remains
\[
\left\{
2,\,
\frac32,\frac34,\frac34,\,
\frac32,\frac34,\frac34
\right\}.
\]

Therefore the same
\[
\Delta_H=\frac14
\]
remains available to ordinary two-product DLS.

Classification:
\`OUTER_H2_BPROCESS_SELFDUAL_NO_H18_GAIN\`.

## 7. General all-unit warning for further prime decompositions

The same obstruction applies if one recursively decomposes one of the smaller prime atoms.

A fixed-depth Vaughan/Heath--Brown identity always contains an all-unit sector in which the prime signal survives on a single logarithmic variable of the original length.

For an atom of length
\[
H^\lambda,\qquad \lambda<2,
\]
a B-process sends it to length
\[
H^{4-\lambda}>H^2
\]
with stationary amplitude
\[
H^{\lambda-2}.
\]

This does not provide an automatic scale improvement; the primal/dual pair is on the unfavorable side of the reciprocal self-dual point.

Hence:
\[
\boxed{
\text{recursive prime identity}
+
\text{one-variable B-process}
}
\]
cannot be credited with removing the H^(1/8) residual solely by producing more formal factors.

Permanent rule:
\`ALL_UNIT_PRIME_ATOM_PERSISTS_UNDER_FIXED_DEPTH_IDENTITY\`.

## 8. Consequence

The following tempting route is now closed as an automatic mechanism:
\[
\text{decompose p}
\to
\text{decompose q}
\to
\text{decompose outer prime-like d}
\to
\text{obtain exact product balance}.
\]

Only the factorable daughter branches become exactly balanced.

The all-unit outer-d branch returns to the same H^(1/8) factor-scale obstruction.

Thus the official amplitude frontier remains
\[
\boxed{H^{1/8}}.
\]

A further advance must exploit something beyond:
- additional fixed-depth prime identities;
- one-variable reciprocal B-processes;
- ordinary two-product regrouping.

The remaining candidates are genuinely coefficient-sensitive multilinear estimates or a norm which preserves cross-branch signed cancellation.
