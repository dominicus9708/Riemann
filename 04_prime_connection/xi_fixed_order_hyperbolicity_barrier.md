# Xi fixed-order hyperbolicity barrier

Status: `EXACT LITERATURE BARRIER + NEW AUDIT RULE`.

## 1. Pólya–Jensen criterion
Let the Riemann Xi-function have central Taylor/moment coefficients \(\gamma(n)\), and define

\[
J^{d,n}(X)=\sum_{j=0}^{d}{d\choose j}\gamma(n+j)X^j.
\]

The Pólya–Jensen criterion identifies RH with hyperbolicity of the full Jensen family (equivalently Xi belonging to the Laguerre–Pólya class).

The logical quantifier is global: all relevant degrees and shifts must be controlled, not one fixed derivative order.

## 2. Fixed-degree false control
Griffin–Ono–Rolen–Zagier proved unconditionally that for every fixed degree \(d\), \(J^{d,n}\) is hyperbolic for all sufficiently large \(n\). The normalized polynomials enter a Hermite asymptotic regime.

Therefore

\[
\boxed{\text{fixed }d\text{ + large }n\text{ hyperbolicity is not RH-specific}.}
\]

This is the Xi-side analogue of the fixed-order Möbius moment barrier.

## 3. Even unbounded verified degree can be a false control
Define

\[
D_*(n):=\max\{D:\ J^{d,n}\text{ is hyperbolic for every }1\le d\le D\}
\]

whenever the initial block is defined.

Since each fixed \(D\) is eventually hyperbolic, for every finite \(D\) there exists \(N_D\) such that \(D_*(n)\ge D\) for all \(n\ge N_D\). Hence

\[
\boxed{D_*(n)\to\infty}
\]

follows unconditionally from fixed-degree eventual hyperbolicity.

Consequently a numerical or analytic observation that the number of verified Jensen degrees increases without bound with shift is still not sufficient evidence for RH. The missing ingredient is uniform control of the joint \((d,n)\) regime / finite exceptional region.

## 4. Kernel concavity is also finite-order information
The Xi Fourier kernel is known to satisfy several nontrivial positivity/concavity inequalities. In 2026 Planat–Solé proved the Csordas–Dimitrov second-level concavity conjecture, which implies associated double Turán inequalities. The authors explicitly make no RH claim.

This is consistent with the hierarchy:

- log-concavity / ordinary Turán: low-order Laguerre/PF information;
- double Turán / second-level concavity: a stronger but still finite layer;
- Laguerre–Pólya / Jensen hyperbolicity: all-order real-rootedness structure.

A fixed finite set of such kernel inequalities should therefore be treated as a necessary/partial layer, not as a completed RH mechanism.

## 5. New audit rules
`FIXED_JENSEN_DEGREE_FALSE_CONTROL`:
If a proposed Xi/Jensen argument proves hyperbolicity only for a fixed degree (even for all sufficiently large shifts), classify it as already compatible with unconditional Hermite asymptotics.

`UNBOUNDED_DEGREE_FALSE_CONTROL`:
Showing only that a verified degree cutoff \(D_*(n)\to\infty\) is also insufficient; this follows qualitatively from the fixed-degree theorem.

`FINITE_LAGUERRE_LEVEL_FALSE_CONTROL`:
Any finite-order Turán/Laguerre/kernel-concavity hierarchy must be separated from the all-order Laguerre–Pólya condition before being treated as RH-specific.

## 6. Live frontier
The live Jensen/Xi question is not another fixed derivative inequality. It is a uniform growing-order problem:

\[
\boxed{\text{control the joint }(d,n)\text{ regime that is not covered by fixed-}d\text{ Hermite asymptotics}.}
\]

Equivalently, identify a deterministic structure that propagates full real-rootedness through the remaining exceptional region without assuming the zero geometry itself.

Literature anchors:
- Griffin, Ono, Rolen, Zagier (2019), Jensen polynomials for the Riemann zeta function and other sequences.
- Griffin, Ono, Rolen, Thorner, Tripp, Wagner (2022), Jensen polynomials for the Riemann xi-function.
- Planat, Solé (2026), Second-Level Concavity of the Riemann Xi Kernel.
