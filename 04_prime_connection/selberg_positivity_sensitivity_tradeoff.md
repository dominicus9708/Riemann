# Selberg positivity–sensitivity tradeoff audit

Status: `EXACT STRUCTURAL BARRIER`

Let

\[
A(s):=-\frac{\zeta'(s)}{\zeta(s)}
=\sum_{n\ge1}\frac{\Lambda(n)}{n^s},\qquad \Re s>1.
\]

For a parameter \(c\ge0\), define

\[
F_c(s):=A(s)^2-cA'(s).
\]

## 1. Positive coefficients
Since

\[
A'(s)=-\sum_{n\ge1}\frac{\Lambda(n)\log n}{n^s},
\]

we have

\[
F_c(s)=\sum_{n\ge1}
\frac{(\Lambda*\Lambda)(n)+c\Lambda(n)\log n}{n^s}.
\]

Hence for every \(c\ge0\),

\[
\boxed{(\Lambda*\Lambda)(n)+c\Lambda(n)\log n\ge0.}
\]

This is an exact manifest-positivity family.

## 2. Pole at s=1
Near the pole of \(\zeta\),

\[
A(s)=\frac1{s-1}+O(1),\qquad
A'(s)=-\frac1{(s-1)^2}+O(1).
\]

Therefore

\[
\boxed{
F_c(s)=\frac{1+c}{(s-1)^2}+O((s-1)^{-1}).
}
\]

## 3. Sensitivity at a simple nontrivial zero
If \(\rho\) is a simple zero, then

\[
A(s)=-\frac1{s-\rho}+O(1),\qquad
A'(s)=\frac1{(s-\rho)^2}+O(1).
\]

Thus

\[
\boxed{
F_c(s)=\frac{1-c}{(s-\rho)^2}+O((s-\rho)^{-1}).
}
\]

The leading double-pole zero sensitivity is therefore exactly proportional to \(1-c\).

## 4. Selberg point c=1
At \(c=1\),

\[
F_1(s)=A(s)^2-A'(s)=\frac{\zeta''(s)}{\zeta(s)}.
\]

The Dirichlet coefficients are

\[
(\Lambda*\Lambda)(n)+\Lambda(n)\log n,
\]

which are the coefficients underlying Selberg's symmetry formula. This is precisely the point where the leading \((s-\rho)^{-2}\) singularity of every simple zero cancels.

Thus the same combination that yields the most elementary/traditional arithmetic tractability also suppresses the leading simple-zero detector.

## 5. Moving away from c=1
For \(c\ne1\), zero sensitivity is restored, but

\[
F_c(s)
=
\frac{\zeta''(s)}{\zeta(s)}+(1-c)A'(s).
\]

Hence one must control the separate zero-sensitive quantity

\[
A'(s)=-\sum_n\Lambda(n)\log n\,n^{-s}.
\]

On the summatory side this is exactly the precision that Selberg's special cancellation avoided.

Therefore the family exhibits the structural tradeoff

\[
\boxed{
\text{elementary Selberg tractability}\uparrow
\quad\Longleftrightarrow\quad
\text{leading simple-zero sensitivity}\downarrow.
}
\]

Classification:

- coefficient positivity for \(c\ge0\): `EXACT`;
- zero/pole Laurent coefficients: `EXACT`;
- c=1 Selberg cancellation: `EXACT`;
- using this family as a new RH proof shortcut: `CLOSED_AS_TRADEOFF`.

This should be treated as a new false-control rule: a positive quadratic Mangoldt identity can become easier precisely because it has cancelled the strongest simple-zero singularity.
