# Source Registry — Topology / K-wise Parity Audit — 2026-09-15

This supplement follows the evidence rules in `source_registry.md`.

## S039 — Anders Björner (2011), A cell complex in number theory

- Type: `PRIMARY_RESEARCH`.
- arXiv: `1101.5704`.
- Published DOI: `10.1016/j.aam.2010.09.007`.
- Exact roles used in repository:
  - squarefree integers `<=n` ordered by divisibility form a simplicial complex `Delta_n`;
  - `M(n)=- reduced Euler characteristic(Delta_n)`;
  - `Delta_n` is shifted and has homotopy type of a wedge of spheres;
  - `beta_k(Delta_n)=sigma_{k+1}^{odd}(n)-sigma_{k+1}^{odd}(n/2)`;
  - total Betti number is `2n/pi^2 + O(n^theta)` for every `theta>17/54`.
- Critical audit use: closes novelty of the Mertens Euler-characteristic formulation and gives a linear homological-mass barrier to critical-cell-count strategies.
- Limitation: paper explicitly notes that these Betti estimates do not yield new control on Mertens growth.
- Verdict: `ACCEPT_AS_PRIMARY_STATIC_TOPOLOGY_SOURCE`.

## S040 — Jonathan Pakianathan & Troy Winfree (2011/2013), quota / threshold complexes

- Type: `PRIMARY_RESEARCH`.
- arXiv: `1104.4324`.
- Journal version: *Threshold complexes and connections to number theory*, Turkish Journal of Mathematics 37 (2013).
- Exact theorem used:
  - a scalar quota complex is homotopy equivalent to a bouquet of spheres;
  - with minimum-weight vertex `v0`, one `s`-sphere occurs for each `s`-face `F` not containing `v0` with `q-w(v0) <= w(F) < q`.
- Prime-log specialization:
  - `w(p)=log p`, minimum vertex `2`, `w0=log 2`;
  - shell faces are odd squarefree `m` in the multiplicative window `X/2 < m <= X`;
  - natural persistence birth/death window is `m -> 2m`, hence logarithmic lifetime `log 2`.
- Critical audit use: closes novelty of quota-complex/persistent-homology reinterpretations and shows persistence lifetime itself is deterministic rather than a new RH spectrum.
- Verdict: `ACCEPT_AS_PRIMARY_QUOTA_TOPOLOGY_SOURCE`.

## S041 — Itai Benjamini, Ori Gurel-Gurevich & Ron Peled (2012), On K-wise Independent Distributions and Boolean Functions

- Type: `PRIMARY_RESEARCH / PROBABILITY_CS_CONTEXT`.
- arXiv: `1201.3261`.
- Role: classical context for k-wise independent distributions, Boolean functions and the discrete moment problem.
- Repository specialization:
  - uniform even-parity and uniform odd-parity distributions on `K+1` bits agree on every `K`-coordinate marginal but have opposite global parity.
  - This exact specialization is elementary and re-derived in repository; the paper is cited for the broader established k-wise-independence framework, not as the source of every displayed identity.
- Critical audit use: prevents novelty claims for low-order label indistinguishability and connects arithmetic prime-channel parity to a known information-theoretic phenomenon.
- Verdict: `ACCEPT_AS_KWISE_CONTEXT`.

## S042 — D. R. Heath-Brown (1982), A parity problem from sieve theory

- Type: `PRIMARY_RESEARCH`.
- Journal: Mathematika 29(1), 1–6.
- DOI: `10.1112/S0025579300012109`.
- Role: classical sieve parity-problem context.
- Critical audit use: arithmetic boundary/full-cube decompositions that still depend on detecting prime-factor parity must be compared against the sieve parity barrier.
- Verdict: `ACCEPT_AS_SIEVE_PARITY_CONTEXT`.

## Current consequence

The following are now treated as prior/reencoding classes rather than independent RH mechanisms:

1. Mertens as static simplicial Euler characteristic.
2. Shifted-complex / wedge-of-spheres homotopy formulation.
3. Scalar quota/threshold-complex formulation with prime logarithmic weights.
4. Persistence-lifetime statistics of the natural scalar filtration.
5. Generic low-order/K-wise Boolean-channel statistics that omit the full parity character.

Any surviving candidate must exploit additional deterministic arithmetic structure of the incomplete weighted-halfspace boundary rather than merely changing mathematical language.
