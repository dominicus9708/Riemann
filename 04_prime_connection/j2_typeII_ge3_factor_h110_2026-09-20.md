# j=2 nonzero Type-II support with >=3 small factors: H^(1/10) bound — 2026-09-20

## Status
- Riemann hypothesis: OPEN.
- Context: support-aware Vaughan Type-II
  \[
  q=e k,\qquad e>H,\quad H<k<H^2,
  \]
  with
  \[
  b_H(k)=\sum_{\substack{d\mid k\\d\le H}}\mu(d).
  \]
- Previous generic support-aware divisor lemma gave branchwise H^(1/6).
- New result: if k is squarefree, H-smooth, \(b_H(k)\ne0\), and k has at least three prime factors, then the complete branch factor list has a subset within H-exponent 1/5 of the self-dual target.
- Therefore this entire >=3-factor Type-II sector satisfies
  \[
  H^{6+1/10+\varepsilon}.
  \]
- The only squarefree Type-II support not covered by the new lemma is the exactly-two-small-factor class. Its pointwise inter-branch cancellation is exact, but this does not by itself imply a restricted-subfamily analytic bound.
- Classification: \`J2_TYPEII_GE3_FACTOR_H1_10\`.

## 1. Factor exponents

Let
\[
k=\prod_{i=1}^r p_i
\]
be squarefree and H-smooth, with
\[
p_i\asymp H^{\lambda_i},
\qquad
0<\lambda_i\le1.
\]

Write
\[
s:=\sum_i\lambda_i,
\qquad
1<s<2,
\]
and
\[
e\asymp H^z,
\qquad
z=3-s\in(1,2).
\]

The H^3 branch exponent list is
\[
\boxed{
\mathcal B=\{z,\lambda_1,\dots,\lambda_r\}.
}
\]

The full sharp j=2 sum also contains
\[
d_0\asymp H^2
\]
and the opposite large-prime variable of exponent 3.

If \(\mathcal B\) has a subset of exponent t with
\[
|t-2|\le1/5,
\]
then adjoining outer d_0 gives a product group of exponent
\[
2+t=4+O(1/5),
\]
and the complementary group has the opposite discrepancy.

Thus
\[
\Delta_H\le1/5
\]
and standard DLS gives
\[
H^{6+1/10+\varepsilon}.
\]

It remains to prove the subset lemma.

## 2. Threshold-complex form of b_H(k)

Since k is squarefree and every prime factor is <=H,
\[
b_H(k)
=
\sum_{\substack{
S\subseteq\{1,\dots,r\}\\
\sum_{i\in S}\lambda_i\le1
}}
(-1)^{|S|}.
\]

Thus \(b_H(k)\) is the alternating sum of the weighted threshold complex
\[
\mathcal K
=
\left\{
S:\sum_{i\in S}\lambda_i\le1
\right\}.
\]

Set
\[
\tau:=s-1.
\]

Since
\[
z=3-s=2-\tau,
\]
a small-factor subset of exponent u with
\[
|u-\tau|\le1/5
\]
gives
\[
|z+u-2|\le1/5.
\]

## 3. Cone lemma for a small atom

Let
\[
\lambda_*=\min_i\lambda_i.
\]

Assume
\[
\lambda_*\le1/5.
\]

If every face S not containing the corresponding vertex * and satisfying
\[
w(S)\le1
\]
also satisfied
\[
w(S)+\lambda_*\le1,
\]
then the threshold complex would be a cone with apex *.

Its alternating sum would therefore vanish:
\[
b_H(k)=0.
\]

Since
\[
b_H(k)\ne0,
\]
there exists a face S not containing * such that
\[
1-\lambda_*<w(S)\le1.
\]

Let C be its complement in the full factor set. Then
\[
w(C)=s-w(S),
\]
so
\[
\tau
\le
w(C)
<
\tau+\lambda_*
\le
\tau+\frac15.
\]

Hence
\[
\boxed{
|w(C)-\tau|\le1/5.
}
\]

Therefore the desired subset exists whenever the smallest prime-factor exponent is <=1/5.

Classification:
\`NONZERO_TRUNCATED_MOBIUS_COMPLEX_NOT_A_CONE\`.

## 4. Reduce to all atoms >1/5

We may now assume
\[
\lambda_i>1/5
\quad\text{for all }i.
\]

If
\[
s\le6/5,
\]
then
\[
z=3-s\ge9/5
\]
and z itself lies within 1/5 of 2.

If
\[
s\ge9/5,
\]
then the full small-factor sum s lies within 1/5 of 2.

Thus only
\[
\boxed{
6/5<s<9/5
}
\]
remains.

Equivalently,
\[
\boxed{
1/5<\tau<4/5.
}
\]

## 5. Exactly three small factors

Let
\[
r=3,
\qquad
a\le b\le c.
\]

Because the triple product exceeds H while every single prime is <=H,
\[
b_H(k)
=
1-3+N_2
=
N_2-2,
\]
where \(N_2\) is the number of pair sums among
\[
a+b,\ a+c,\ b+c
\]
which are <=1.

The condition
\[
b_H(k)\ne0
\]
means
\[
N_2\ne2.
\]

### Case N_2=3

All pair sums are <=1.

Then
\[
b+c\le1,
\]
so
\[
a=s-(b+c)\ge s-1=\tau.
\]

Also
\[
a\le s/3.
\]

Hence
\[
0\le a-\tau
\le
\frac s3-(s-1)
=
1-\frac{2s}{3}
\le\frac15,
\]
because \(s\ge6/5\).

Thus a is within 1/5 of tau.

### Case N_2=1

Exactly
\[
a+b\le1<a+c\le b+c.
\]

The four quantities
\[
\tau-a=b+c-1,
\]
\[
\tau-b=a+c-1,
\]
\[
(a+b)-\tau=1-c,
\]
\[
c-\tau=1-a-b
\]
are all nonnegative.

If all four exceeded 1/5, then
\[
c<4/5,
\qquad
a+b<4/5,
\]
and
\[
a+c>6/5,
\qquad
b+c>6/5.
\]

From \(c<4/5\) and \(a+c>6/5\) one gets
\[
a>2/5.
\]

Since \(b\ge a\),
\[
a+b>4/5,
\]
contradicting \(a+b<4/5\).

Therefore at least one legal subset is within 1/5 of tau.

### Case N_2=0

All pair sums exceed 1.

If no single or pair subset were within 1/5 of tau, then:
- each single-to-tau error >1/5 forces every pair sum >6/5;
- each pair-to-tau error >1/5 forces every atom <4/5.

But the sum of the three pair sums equals
\[
2s.
\]

Thus
\[
2s>3\cdot\frac65=\frac{18}{5},
\]
so
\[
s>\frac95,
\]
contradicting the hard range.

Hence a legal subset lies within 1/5 of tau.

The excluded case \(N_2=2\) is exactly
\[
b_H(k)=0.
\]

Therefore the r=3 lemma is proved.

The constant 1/5 is sharp within this class, e.g. at symmetric boundary patterns equivalent to small-factor exponents 2/5 or 3/5.

## 6. Four or more small factors, all >1/5

Sort
\[
\lambda_1\le\cdots\le\lambda_r,
\qquad r\ge4.
\]

Let
\[
t_j=\lambda_1+\cdots+\lambda_j.
\]

Suppose for contradiction that no subset lies in
\[
[\tau-1/5,\tau+1/5].
\]

In particular no partial sum t_j lies there.

Let j be the first index for which
\[
t_j>\tau+1/5.
\]

Then
\[
t_{j-1}<\tau-1/5
\]
and hence
\[
\lambda_j>2/5.
\]

Because every atom is >1/5 and
\[
\tau-1/5<3/5,
\]
we must have
\[
j\le3.
\]

### j=1

Then every one of the r>=4 atoms exceeds \(\tau+1/5\), so
\[
s>4(\tau+1/5).
\]

Since \(s=1+\tau\), this implies
\[
\tau<1/15,
\]
contrary to \(\tau>1/5\).

### j=2

We have
\[
\lambda_1<\tau-1/5,
\]
and
\[
\lambda_2>\tau+1/5-\lambda_1.
\]

Since \(r\ge4\),
\[
s
\ge
\lambda_1+3\lambda_2
>
3\tau+\frac35-2\lambda_1.
\]

Using
\[
\lambda_1<\tau-\frac15
\]
gives
\[
s>1+\tau,
\]
contradiction.

### j=3, r>=6

Here
\[
t_2>2/5
\]
and
\[
\lambda_3>2/5.
\]

There are at least four atoms from \(\lambda_3\) onward, so
\[
s>2/5+4(2/5)=2,
\]
contradiction.

### j=3, r=5

We have
\[
\tau>3/5.
\]

The subset
\[
u=\lambda_1+\lambda_3
\]
satisfies
\[
u>3/5>\tau-1/5.
\]

If \(u\le\tau+1/5\), we are done.

Otherwise
\[
\lambda_1+\lambda_3>\tau+1/5.
\]

Since \(\lambda_2\ge\lambda_1\),
\[
\lambda_2+\lambda_3>\tau+1/5.
\]

Also
\[
\lambda_3>2/5.
\]

Hence
\[
s
\ge
(\lambda_1+\lambda_3)
+
(\lambda_2+\lambda_3)
+
\lambda_3
>
2\tau+\frac45.
\]

But \(\tau>1/5\), so
\[
2\tau+\frac45>1+\tau=s,
\]
contradiction.

### j=3, r=4

Again
\[
\tau>3/5.
\]

Use
\[
u=\lambda_1+\lambda_3.
\]

We have
\[
u>3/5>\tau-1/5.
\]

If \(u>\tau+1/5\), then also
\[
\lambda_2+\lambda_3>\tau+1/5,
\]
and
\[
s
\ge
(\lambda_1+\lambda_3)
+
(\lambda_2+\lambda_3)
>
2\tau+\frac25.
\]

Since
\[
\tau>3/5,
\]
the right side exceeds
\[
1+\tau=s,
\]
contradiction.

Therefore
\[
u\le\tau+1/5,
\]
so u lies in the required interval.

This completes the r>=4 proof.

## 7. Branchwise DLS consequence

We have proved:

\[
\boxed{
r\ge3,\quad
b_H(k)\ne0
\Longrightarrow
\exists\,T\subseteq\mathcal B:
\left|\sum_{x\in T}x-2\right|\le1/5.
}
\]

Including the outer H^2 factor gives
\[
\Delta_H\le1/5.
\]

Therefore
\[
\boxed{
T_{II,\ r\ge3}
\ll_\varepsilon
H^{6+1/10+\varepsilon}.
}
\]

Classification:
\`TYPEII_NONZERO_GE3_SUPPORT_H1_10\`.

## 8. Exactly two small factors

If
\[
k=rs,
\qquad
r,s\le H,
\qquad
rs>H,
\]
then
\[
b_H(k)=1-1-1=-1.
\]

This class can realize the older sharp factor geometry and is not covered by the 1/5 lemma.

There is an exact pointwise Vaughan cancellation on squarefree composite values, but:

\[
\boxed{
\text{pointwise coefficient cancellation}
\not\Rightarrow
\text{a bound for an arbitrarily restricted subfamily}.
}
\]

Restricting the first-Type-I partner to this factor pattern destroys the smooth unrestricted cofactor used in the proved low-Type-I B-process bound.

Therefore this two-factor class remains part of the official signed-multiscale frontier until a cancellation-preserving norm estimate is proved.

Permanent guard:
\`POINTWISE_VAUGHAN_CANCELLATION_NE_RESTRICTED_SUBFAMILY_BOUND\`.

## 9. Updated Type-II map

The support-aware Type-II sector is now stratified as:

1. proper prime-power e:
   CLOSED by sparsity;

2. rough prime-k / semiprime patterns:
   exact algebraic cancellation known, but analytic use requires signed recombination;

3. H-smooth squarefree k with >=3 prime factors and \(b_H(k)\ne0\):
   \[
   \boxed{H^{6+1/10+\varepsilon}};
   \]

4. exactly-two-small-factor k:
   remains the sharp cancellation-sensitive class.

Thus the genuinely difficult Type-II geometry is narrower than the previous all-smooth-composite H^(1/6) frontier.
