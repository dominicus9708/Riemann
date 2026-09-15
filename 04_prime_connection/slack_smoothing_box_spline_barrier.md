# Slack Smoothing and Prime-Log Box-Spline Barrier

Date: 2026-09-15

## 1. total-slack-only observables

For squarefree n<=X, total logarithmic slack is

\[
\mathcal S_X(n)=\log(X/n).
\]

For a kernel phi on [0,infinity), define

\[
R_\phi(X)=\sum_{n\le X}\mu(n)\phi(\log(X/n)).
\]

Let

\[
\Phi(s)=\int_0^\infty \phi(u)e^{-su}\,du.
\]

Where interchange is justified,

\[
\int_1^\infty R_\phi(X)X^{-s-1}\,dX
=\sum_n\mu(n)n^{-s}\Phi(s)
=\boxed{\frac{\Phi(s)}{\zeta(s)}}.
\]

Thus a nonlinear-looking observable that depends only on scalar slack is simply a multiplicative smoothing of the reciprocal zeta Dirichlet series.

### polynomial slack

For

\[
R_k(X)=\frac1{k!}\sum_{n\le X}\mu(n)\log^k(X/n),
\]

we have `Phi(s)=s^{-(k+1)}`, hence exactly

\[
\boxed{
\frac1{\zeta(s)}
=s^{k+1}\int_1^\infty R_k(X)X^{-s-1}\,dX.
}
\]

Therefore proving `R_k(X)=O_epsilon(X^{1/2+epsilon})` for every epsilon is another reciprocal-zeta/RH criterion, not an easier scalar-boundary problem. This sits in the classical Riesz/Hardy--Littlewood smoothing family.

Verdict: `TOTAL-SLACK-ONLY -> MELLIN REENCODING`.

---

## 2. first-order addable prime-log mass

Define

\[
A_X(n)=\sum_{\substack{p\nmid n\\np\le X}}\log p.
\]

Then

\[
\sum_{n\le X}\mu(n)A_X(n)
=\sum_{p\le X}\log p
 \sum_{\substack{n\le X/p\\p\nmid n}}\mu(n).
\]

For

\[
S_p(Y)=\sum_{\substack{n\le Y\\p\nmid n}}\mu(n),
\]

one has

\[
M(Y)=S_p(Y)-S_p(Y/p),
\]

so

\[
S_p(Y)=\sum_{j\ge0}M(Y/p^j).
\]

Consequently

\[
\sum_{n\le X}\mu(n)A_X(n)
=\sum_{p^j\le X}\log p\,M(X/p^j)
=\sum_{q\le X}\Lambda(q)M(X/q).
\]

Since

\[
\mu*\Lambda=-\mu\log,
\]

we get the exact identity

\[
\boxed{
\sum_{n\le X}\mu(n)A_X(n)
=-\sum_{n\le X}\mu(n)\log n.
}
\]

Thus first-order prime-log boundary coupling is the `s`-derivative of reciprocal-zeta data.

Verdict: `FIRST PRIME-LOG COUPLING -> DERIVATIVE REENCODING`.

---

## 3. positive box-spline representation

Fix Y>=X, let primes p<=Y have weights

\[
w_p=\log p,
\]

and define interval functions

\[
g_p=\mathbf1_{[0,w_p]}.
\]

Let

\[
B_Y=g_{p_1}*\cdots*g_{p_m},
\qquad m=\pi(Y).
\]

Then `B_Y` is nonnegative and log-concave as a convolution of interval indicators.

Distributionally,

\[
Dg_p=\delta_0-\delta_{w_p},
\]

hence

\[
\boxed{
D^mB_Y
=\sum_{S\subseteq\{p\le Y\}}
(-1)^{|S|}\delta_{\sum_{p\in S}\log p}.
}
\]

Taking the right-continuous cumulative distribution,

\[
\boxed{
D^{m-1}B_Y(\log X+)
=M(X)
}
\qquad(Y\ge X).
\]

So Möbius parity is exactly an ultra-high derivative of a positive convolution density.

### Laplace transform

Since

\[
\mathcal L g_p(s)=\frac{1-p^{-s}}s,
\]

we obtain

\[
\boxed{
\mathcal L B_Y(s)
=s^{-m}\prod_{p\le Y}(1-p^{-s}).
}
\]

Hence the box-spline is precisely the finite Euler product in positive-convolution coordinates.

Positivity/log-concavity has not removed the problem; it has moved it to derivative order `m-1`.

---

## 4. finite-Euler-product L2 identity

Let

\[
P_Y(s)=\prod_{p\le Y}(1-p^{-s})
=\sum_{d\mid P_Y}\mu(d)d^{-s},
\]

and

\[
A_Y(u)=\sum_{\substack{d\mid P_Y\\d\le u}}\mu(d).
\]

Using

\[
\int_{-\infty}^{\infty}
\frac{e^{-it\log(d/e)}}{1/4+t^2}\,dt
=2\pi e^{-|\log(d/e)|/2},
\]

we obtain exactly

\[
\boxed{
\int_{-\infty}^{\infty}
\frac{|P_Y(1/2+it)|^2}{1/4+t^2}\,dt
=2\pi\int_1^\infty\frac{A_Y(u)^2}{u^2}\,du.
}
\]

For `u<=Y`, every squarefree integer <=u uses only primes <=Y, so

\[
A_Y(u)=M(u).
\]

Therefore

\[
\boxed{
\int_{-\infty}^{\infty}
\frac{|P_Y(1/2+it)|^2}{1/4+t^2}\,dt
\ge
2\pi\int_1^Y\frac{M(u)^2}{u^2}\,du.
}
\]

Thus using the fact that the finite Euler product is entire does not evade the critical difficulty: a useful critical-line L2 bound already contains the weak-Mertens mean-square problem.

Verdict: `FINITE-EULER L2 -> WEAK-MERTENS BARRIER`.

---

## 5. overall verdict

Closed as independent proof mechanisms:

1. scalar total-slack kernels;
2. first-order addable prime-log mass;
3. positivity/log-concavity of the prime-log box spline;
4. critical-line L2 norm of the finite Euler product.

A surviving nonlinear boundary observable must therefore retain genuinely multivariate prime-label geometry and cannot collapse to a function of `log(X/n)` alone or to a global norm of the finite Euler product.
