# Möbius Layer Generating-Polynomial Root Criterion Audit

Date: 2026-09-15

## 목적

squarefree prime-factor layer generating polynomial

\[
G_X(z)=\sum_{n\le X}\mu(n)^2 z^{\omega(n)}
      =\sum_{r\ge0}A_r(X)z^r
\]

에서 parity point `z=-1` 근처의 실근이 Mertens cancellation을 새로운 방식으로 부호화하는지 감사한다.

핵심 질문:

1. `z=-1` 근처의 실근이 충분히 큰 X에서 실제로 존재하고 유일한가?
2. 그 root displacement가 `M(X)`와 어떤 정량관계를 갖는가?
3. root convergence rate가 RH와 동치인 criterion을 주는가?
4. 이것이 증명 진전인지, Selberg--Delange/Mertens의 재부호화인지 구분한다.

---

## 1. exact identities at z=-1

squarefree n에서는 `mu(n)=(-1)^omega(n)`이므로

\[
\boxed{G_X(-1)=M(X).}
\]

또한

\[
G_X'(-1)
=\sum_{n\le X}\mu(n)^2\omega(n)(-1)^{\omega(n)-1}
=-\sum_{n\le X}\mu(n)\omega(n).
\]

따라서

\[
\boxed{G_X'(-1)=-M_\omega(X)}.
\]

마찬가지로

\[
G_X''(-1)
=\sum_{n\le X}\mu(n)\omega(n)(\omega(n)-1)
=M_{\omega^2}(X)-M_\omega(X).
\]

상태: `EXACT`.

---

## 2. Selberg--Delange derivative asymptotics

Dirichlet generating family은

\[
F(s,z)=\sum_{n\ge1}\frac{\mu(n)^2 z^{\omega(n)}}{n^s}
=\prod_p(1+zp^{-s})
=\zeta(s)^z H(s,z),
\]

where

\[
H(s,z)=\prod_p(1+zp^{-s})(1-p^{-s})^z.
\]

near `z=-1`, `H(1,-1)=1` and

\[
\frac1{\Gamma(z)}=-(z+1)+O((z+1)^2).
\]

Standard quantitative Selberg--Delange, equivalently Tenenbaum's expansion quoted/proved in the Alladi--Johnson / Alladi--Sengupta line, yields

\[
\sum_{n\le X}\mu(n)\omega(n)
=\frac{X}{\log^2X}
+O\!\left(\frac{X}{\log^3X}\right),
\]

and

\[
\sum_{n\le X}\mu(n)\omega(n)^2
=-\frac{2X\log\log X}{\log^2X}
+O\!\left(\frac{X}{\log^2X}\right).
\]

Hence

\[
\boxed{
G_X'(-1)
=-\frac{X}{\log^2X}
\left(1+O\left(\frac1{\log X}\right)\right)
}
\]

and

\[
\boxed{
G_X''(-1)
=O\!\left(\frac{X\log\log X}{\log^2X}\right).
}
\]

Uniform Selberg--Delange on a shrinking real neighborhood `|z+1|=o(1/log log X)` gives the corresponding local bound

\[
\sup_{|z+1|\le \eta_X}|G_X''(z)|
\ll \frac{X\log\log X}{\log^2X}
\]

whenever `eta_X log log X -> 0`.

상태: first/second derivative asymptotics `KNOWN / STANDARD SELBERG--DELANGE`; local use audited here.

---

## 3. unconditional root existence near -1

Let

\[
a_X:=\frac{M(X)\log^2X}{X}.
\]

The classical zero-free-region bound for the Mertens function gives

\[
M(X)\ll X\exp\{-c(\log X)^{3/5}(\log\log X)^{-1/5}\},
\]

so in particular

\[
a_X\log\log X\to0.
\]

If `M(X)=0`, then `z=-1` is already a root.

Assume `M(X) != 0`. Taylor expansion for `h` in a neighborhood of size `O(|a_X|)` gives

\[
G_X(-1+h)
=M(X)+hG_X'(-1)
+O\!\left(h^2\frac{X\log\log X}{\log^2X}\right).
\]

At `h=2a_X`,

\[
M(X)+2a_XG_X'(-1)
=-M(X)+o(M(X)),
\]

while the quadratic remainder divided by `|M(X)|` is

\[
O\!\left(\frac{|M(X)|\log^2X\log\log X}{X}\right)=o(1).
\]

Therefore `G_X(-1)` and `G_X(-1+2a_X)` have opposite signs for all sufficiently large X.

By the intermediate value theorem there is a real root between them.

Furthermore the same local second-derivative control gives

\[
G_X'(z)
=-\frac{X}{\log^2X}(1+o(1))<0
\]

throughout this interval, so the root is unique there.

Thus there exists a distinguished real root `rho_X` near -1 for all sufficiently large X.

상태: `EXACT CONSEQUENCE OF STANDARD ASYMPTOTICS`.

---

## 4. root displacement asymptotic

At `G_X(rho_X)=0`, Taylor expansion gives

\[
0=M(X)+(\rho_X+1)G_X'(-1)
+O\!\left((\rho_X+1)^2\frac{X\log\log X}{\log^2X}\right).
\]

The quadratic term is `o(M(X))`, hence

\[
\rho_X+1
=-\frac{M(X)}{G_X'(-1)}(1+o(1)).
\]

Using the first-derivative asymptotic,

\[
\boxed{
\rho_X+1
=\frac{M(X)\log^2X}{X}(1+o(1)).
}
\]

Consequences:

- sign(`rho_X+1`) eventually equals sign(`M(X)`);
- `rho_X=-1` exactly when `M(X)=0`;
- the near-`-1` root carries essentially the same endpoint information as Mertens, rescaled by `log^2 X / X`.

This explains the previously observed parity-phase resolution scale `log^2 X / sqrt(X)`.

---

## 5. RH-equivalent root convergence criterion

The classical Mertens formulation of RH is

\[
\mathrm{RH}
\iff
M(X)=O_\varepsilon(X^{1/2+\varepsilon})
\quad\text{for every }\varepsilon>0.
\]

Combining it with the root displacement asymptotic gives

\[
\mathrm{RH}
\iff
\rho_X+1
=O_\varepsilon(X^{-1/2+\varepsilon}\log^2X)
\quad\forall\varepsilon>0.
\]

Since powers of `log X` are absorbed by arbitrarily small powers of X, this is equivalently

\[
\boxed{
\mathrm{RH}
\iff
|\rho_X+1|=O_\varepsilon(X^{-1/2+\varepsilon})
\quad\forall\varepsilon>0.
}
\]

This is an RH criterion / reparameterization, **not a proof of RH**.

---

## 6. finite dyadic audit

Using exact layer counts in

`data/formation/mobius_layer_counts_dyadic_24.csv`, roots of `G_X` were computed.

Important correction: full real-rootedness does **not** persist. Nonreal root pairs already occur at some relatively small cutoffs, including `X=2^12`.

The relevant object is only the distinguished real root nearest `-1` once that local branch is present.

Selected values:

| X | M(X) | rho_X+1 | Newton `-M/G'(-1)` | ratio |
|---:|---:|---:|---:|---:|
| 2^15 | 26 | 0.041029 | 0.043845 | 0.9358 |
| 2^16 | 14 | 0.015692 | 0.016260 | 0.9651 |
| 2^17 | -20 | -0.015667 | -0.014993 | 1.0450 |
| 2^18 | 24 | 0.009533 | 0.009764 | 0.9763 |
| 2^19 | -125 | -0.036910 | -0.032765 | 1.1265 |
| 2^20 | 257 | 0.029466 | 0.031518 | 0.9349 |
| 2^21 | -362 | -0.034799 | -0.030893 | 1.1264 |
| 2^22 | 228 | 0.009212 | 0.009440 | 0.9759 |
| 2^23 | -10 | -0.0002397101 | -0.0002395449 | 1.00069 |
| 2^24 | 211 | 0.0027405446 | 0.0027621991 | 0.99216 |

The exact Newton predictor using the actual derivative is already very accurate; the simpler asymptotic `M log^2 X / X` converges more slowly because `G'_X(-1)/( -X/log^2 X)` is still about 1.26 at `2^24`.

Status: `NUMERICAL CONSISTENCY CHECK ONLY`.

---

## 7. prior-art audit

The ingredients are classical / known:

- Selberg--Delange asymptotics for `sum mu^2(n) z^omega(n)` are uniform on compact z-sets.
- the zero of `1/Gamma(z)` at `z=-1` explains why the generic `s=1` main term vanishes at the Möbius parity point.
- Tenenbaum / Alladi--Johnson / Alladi--Sengupta give quantitative asymptotics for `sum mu(n) omega(n)^k`, including the derivative information used above.

A targeted literature search did **not** locate a paper explicitly formulating RH as the convergence rate of the distinguished real zero of the finite polynomial `G_X(z)` toward `-1`.

This absence is not a novelty proof. The criterion should be treated as a derived reformulation until a broader bibliographic audit is completed.

---

## 8. verdict

### new useful structure

The near-`-1` zero gives a clean finite algebraic coordinate for Mertens cancellation:

\[
\boxed{
\rho_X+1\sim M(X)\log^2X/X.
}
\]

It also turns the earlier phase-resolution observation into an actual root-displacement statement.

### limitation

The criterion is asymptotically equivalent to the classical Mertens RH criterion. It does not reduce the analytic difficulty by itself.

Therefore current status:

- local root existence / uniqueness: `DERIVED THEOREM FROM STANDARD SELBERG--DELANGE + MERTENS ZERO-FREE BOUND`;
- root displacement: `DERIVED ASYMPTOTIC`;
- RH root-rate criterion: `EQUIVALENT REFORMULATION`;
- independent proof progress: `NOT ESTABLISHED`;
- possible novelty of formulation: `UNRESOLVED / NO CLAIM`.

## next question

The only reason to retain this branch is if the root `rho_X` obeys an **algebraic monotonicity, interlacing, or contraction law across X** that is not already equivalent to Mertens cancellation.

Next audit should therefore test root motion at every squarefree activation, not merely dyadic cutoffs, and compare it against the exact update

\[
G_X(z)=G_{X-1}(z)+\mu(X)^2z^{\omega(X)}.
\]

If root motion simply differentiates to `Delta M(X)` under the local formula, close the branch as reencoding.
