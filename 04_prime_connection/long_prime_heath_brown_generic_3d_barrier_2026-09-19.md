# Long-prime flank: Heath--Brown / generic 3D monomial barrier — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Context: (j=1) long-prime flank (0le alpha<1), after the product-balanced transition (alpha=1) was closed.
- Candidate tested: replace the prime indicator by (Lambda), apply a fixed-depth Heath--Brown identity, dyadically decompose, and use known generic three-dimensional monomial exponential-sum bounds on the resulting multilinear blocks.
- Conclusion: this candidate does **not** automatically close the flank. A concrete admissible block at (alpha=0) remains polynomially above the required (V^3) scale.
- Classification: `HEATH_BROWN_PLUS_GENERIC_3D_NOT_ENOUGH`.

## 1. Prime replacement is legal at the edge

In the (j=1) sector, the large variable (p) is prime. Replacing the prime indicator by (Lambda(p)/log p) changes only harmless logarithmic factors.

Prime powers introduced by extending to (Lambda(n)) are lower order in the long-prime flank. If
[
P=V^{3-alpha},
]
then prime powers contribute at most (P^{1/2+o(1)}) values. Multiplying by the outer (r=da) range (V^{1+alpha}) gives
[
V^{1+alpha}P^{1/2}
=
V^{5/2+alpha/2}
le V^3,
]
with strict power saving for (alpha<1).

Thus the (Lambda)-replacement is acceptable for this audit.

## 2. Heath--Brown identity

For fixed (k), one usable form is
[
Lambda(n)
=
sum_{j=1}^{k}
(-1)^{j+1}inom{k}{j}
sum_{substack{
n=m_1cdots m_j n_1cdots n_j\
m_ile 2P^{1/k}
}}
mu(m_1)cdotsmu(m_j)log n_1.
]

After dyadic decomposition:
- each Möbius variable (m_i) is short, at most (P^{1/k});
- the (n_i) variables are not individually forced to be short.

Therefore increasing (k) does not by itself guarantee that the full list of variables can be partitioned into two products of size (V^{2+O(arepsilon)}).

Permanent guard:
`HB_DEPTH_NOT_AUTOMATIC_PRODUCT_BALANCE`.

## 3. Concrete obstruction at (alpha=0)

Take the extreme long-prime endpoint
[
alpha=0.
]

Then
[
r=daasymp V,
qquad
Pasymp V^3.
]

An admissible Heath--Brown dyadic configuration has two smooth (1)-type variables of lengths
[
n_1asymp n_2asymp V^{3/2},
]
while the truncated Möbius variables lie in unit/small dyadic ranges.

The resulting essential three-variable phase block has lengths
[
H=V,qquad
M=N=V^{3/2},
]
with total product
[
HMN=V^4.
]

The reciprocal-square-root phase has normalized monomial amplitude
[
Xasymp V^2.
]

Logarithmic and divisor-bounded coefficients are harmless at (V^arepsilon) level.

## 4. Robert--Sargos generic 3D theorem

A standard Robert--Sargos / Fouvry--Iwaniec type three-dimensional monomial bound has the form
[
S_0(H,M,N)
ll_arepsilon
(HMN)^{1+arepsilon}
left[
left(rac{X}{HMN^2}ight)^{1/4}
+
(HM)^{-1/4}
+
N^{-1/2}
+
X^{-1/2}
ight]
]
after choosing the distinguished (N)-variable appropriately.

For
[
H=V,qquad M=N=V^{3/2},qquad X=V^2,
]
the four savings are
[
V^{-7/8},qquad
V^{-5/8},qquad
V^{-3/4},qquad
V^{-1}.
]

The dominant term is
[
V^{-5/8}.
]

Hence
[
oxed{
S_0
ll_arepsilon
V^{4-5/8+arepsilon}
=
V^{27/8+arepsilon}.
}
]

The required edge scale is
[
V^{3+arepsilon}=V^{24/8+arepsilon}.
]

Thus the generic theorem misses by
[
oxed{V^{3/8}}.
]

Choosing the (V)-length variable as the distinguished (N)-variable is worse, so this is not an artifact of a poor permutation.

## 5. Interpretation

This calculation rules out the implication
[
	ext{high-depth Heath--Brown decomposition}
+
	ext{generic 3D monomial theorem}
Longrightarrow
	ext{automatic closure of the long-prime flank}.
]

The obstruction is a genuine multilinear configuration rather than the previously closed self-dual two-product transition.

However this does **not** prove that the long-prime flank is as hard as a new prime theorem. There remain at least three structures not used by the generic 3D estimate:

1. cancellation between different Heath--Brown identity terms;
2. special Möbius/log coefficient structure rather than arbitrary bounded coefficients;
3. the pre-existing outer coefficient (A_r), whose divisor/convolution structure may interact with the HB variables before absolute values are taken.

## 6. Updated long-prime frontier

The active question is now narrower:

[
oxed{
	ext{Can the HB decomposition be recombined before termwise absolute estimation
so that the }V^{3/8}	ext{ representative gap disappears?}
}
]

A second possibility is to use a genuinely coefficient-sensitive multilinear estimate rather than the generic Robert--Sargos theorem.

Permanent classifications:
- `HB_DEPTH_NOT_AUTOMATIC_PRODUCT_BALANCE`.
- `GENERIC_3D_MONOMIAL_V38_GAP`.
- `HB_CROSS_TERM_RECOMBINATION_OPEN`.

## References
- D. R. Heath-Brown, generalized Vaughan/Heath--Brown identity.
- O. Robert and P. Sargos, *Three-dimensional exponential sums with monomials*, J. Reine Angew. Math. 591 (2006), 1--20.
