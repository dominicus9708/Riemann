# Double-Möbius reciprocal bilinear literature-gap audit — 2026-09-18

## Status
- Riemann hypothesis: OPEN.
- Target: critical Vaughan-edge bilinear reciprocal sum with Möbius coefficients in both variables.
- Literature search status: no theorem was identified that directly exploits both Möbius coefficient sequences for the real reciprocal monomial phase strongly enough to reach the present target.
- This is a literature-status statement, not a novelty claim.

## 1. Critical target

At the extreme edge
[
D=K,qquad nasymp1,qquad
Masymp K^{1/4},qquad
Lasymp K^{3/4},
]
the exact Vaughan-edge identity gives
[
b_d=mu(d)
]
on the shortest factor block, so the Type-II model becomes
[
oxed{
T_{m edge}
=
sum_{dasymp K^{1/4}}mu(d)
sum_{wasymp K^{3/4}}mu(w)
e!left(A(dw)^{-1/2}ight).
}
]

The relaxed low-outer-index target is of scale
[
oxed{|T_{m edge}|ll_arepsilon K^{3/4+arepsilon}.}
]

## 2. Known generic monomial technology

Robert--Sargos and related double-large-sieve / real-monomial estimates apply to the phase class, but treat coefficient sequences essentially as arbitrary bounded sequences.

The project audit already showed that this architecture does not reach the target exponent in the critical block. More recent generic bilinear monomial estimates improve the arbitrary-coefficient exponent but still remain above (3/4) at the critical reciprocal scaling.

Therefore a successful direct Type-II theorem must preserve additional arithmetic information rather than merely sharpen unsigned spacing.

## 3. Möbius exponential-sum literature checked

The search included literature on:
- one-variable Möbius exponential sums;
- exponential sums with general multiplicative coefficients;
- nonlinear Möbius orthogonality in short intervals;
- bilinear exponential sums with arbitrary coefficients;
- Möbius correlations and truncated Möbius functions;
- recent large-value / Dirichlet-polynomial results.

The sources found are useful benchmarks, but none gives a direct theorem of the form
[
sum_{msim M}mu(m)sum_{nsim N}mu(n)
e(Fm^{-1/2}n^{-1/2})
]
with the power saving required here.

In particular:
- single-variable linear/nonlinear Möbius estimates do not automatically transfer through local Taylor linearization because translation destroys multiplicativity;
- arbitrary-coefficient bilinear estimates lose the Möbius structure;
- correlation results for truncated Möbius functions do not directly control full Möbius parity in the present parameter range.

Classification:
[
oxed{	exttt{DOUBLE_MOBIUS_RECIPROCAL_BILINEAR_DIRECT_THEOREM_NOT_IDENTIFIED}.}
]

## 4. Audit warning

Do not convert the absence of an identified theorem into a novelty claim.

A valid novelty statement would require a systematic bibliographic review of:
- Type-I/II estimates with multiplicative coefficients,
- exponent-pair methods for reciprocal monomials,
- bilinear forms with Möbius/Liouville coefficients,
- shifted-convolution methods,
- long mollifier and long Dirichlet-polynomial literature.

For the working proof search, however, it is reasonable to treat this as an unresolved coefficient-sensitive module.

## 5. Next exact structural audit

Before attempting to prove a new bilinear theorem, exploit the special edge scale
[
V=K^{1/4},qquad
wasymp K^{3/4}.
]

A squarefree (w) can contain only a bounded number of prime factors larger than (V). The next audit should separate
[
w=a,quad w=pa,quad w=pqa
]
with all prime factors of (a) at most (V), and determine whether this bounded large-prime tail produces a genuine simplification or is merely a finite-depth Buchstab/Heath--Brown re-expression of the same parity barrier.
