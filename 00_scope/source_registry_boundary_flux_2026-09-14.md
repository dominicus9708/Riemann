# Boundary-Flux / Parity Source Audit — 2026-09-14

This note extends the same evidence rules as `source_registry.md` and `source_registry_supplement_2026-09-14.md` for the connected-boundary-flux branch.

## S036 — D. R. Heath-Brown (1982), A parity problem from sieve theory

- Type: `PRIMARY_RESEARCH`.
- Journal: Mathematika 29(1), 1–6.
- DOI: `10.1112/S0025579300012109`.
- Role: classical sieve-theoretic parity obstruction context.
- Critical audit use: higher-order prime-divisibility / inclusion-exclusion observables do not automatically escape parity information loss merely by increasing combinatorial order.
- Limitation: not an RH theorem and not identical to the connected-boundary identity derived in this repository.
- Audit verdict: `ACCEPT_FOR_SIEVE_PARITY_BARRIER_CONTEXT`.

## S037 — Terence Tao (2007), Open question: The parity problem in sieve theory

- Type: `EXPOSITORY_BY_PRIMARY_RESEARCHER`.
- Source: What's new, 5 June 2007.
- Role: explicit modern exposition of why divisor-sum / Möbius-type sieve information is weak at distinguishing odd and even prime-factor parity, including the Liouville obstruction.
- Critical audit use: compare any claimed formation/divisibility improvement against the classical parity barrier before treating it as a new cancellation mechanism.
- Limitation: expository source; use Heath-Brown and standard sieve references for primary literature claims.
- Audit verdict: `ACCEPT_AS_PARITY_BARRIER_EXPOSITION`.

## S038 — M. Huxley & N. Watt (2018), Mertens sums requiring fewer values of the Möbius function

- Type: `PRIMARY_RESEARCH`.
- Journal: Chebyshevskii Sbornik 19(3), 20–34.
- Preprint: arXiv:1807.05890.
- Role: identities expressing `M(N^d)` and more general Möbius sums through lower-scale products / bilinear forms.
- Critical audit use: connected visibility-boundary flux also reduces exactly to lower-scale restricted Möbius pair sums, so decomposition into smaller-scale Möbius objects alone is not sufficient evidence of a new RH mechanism.
- Limitation: their identities are not asserted to be the same formula as this repository's Boolean connected difference.
- Audit verdict: `ACCEPT_FOR_MERTENS_RECURSION_AND_BILINEAR_CONTEXT`.

## S039 — O. Gorodetsky (2026), A Kubilius model for sieve-theoretic sequences

- Type: `PRIMARY_RESEARCH`.
- Journal: Analysis Mathematica (2026), published 14 August 2026.
- DOI: `10.1007/s10476-026-00178-w`.
- Role: modern total-variation version of the Kubilius probabilistic model for sieve-theoretic sequences with positive level of distribution.
- Critical audit use: independent prime-divisibility Bernoulli models are a standard probabilistic-number-theory baseline rather than a new formation assumption.
- Limitation: the exact CRT tensor-orthogonality calculation in this repository does not depend on Gorodetsky's theorem; this source is used only for modern model context and not as support for RH claims.
- Audit verdict: `ACCEPT_FOR_KUBILIUS_SIEVE_MODEL_CONTEXT`.

## Current audit consequence

The connected-boundary branch must demonstrate a structure that survives after known Möbius/inclusion-exclusion recursion is removed. A mere re-expression of the Mertens function, restricted Mertens sums, bilinear Möbius forms, or independent prime-divisibility tensor variance remains a representation/model change rather than independent RH progress.
