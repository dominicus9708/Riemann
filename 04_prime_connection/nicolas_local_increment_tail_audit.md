# Nicolas local increment and tail-sign audit

Status: exact local identities + asymptotic threshold + method audit.

Let p_k be the k-th prime, N_k=prod_{j<=k} p_j, and theta_k=theta(p_k)=sum_{j<=k} log p_j. Define the logarithmic Nicolas defect

G_k := log(N_k/phi(N_k)) - gamma - log log theta_k.

Nicolas' criterion is RH iff G_k>0 for every k>=1.

## 1. Exact one-prime increment

For p=p_k, t=theta(p^-)=theta_{k-1}, L=log p,

Delta_p G_N := G_k-G_{k-1}
= log(p/(p-1)) - log( log(t+L) / log t ).

For fixed p this is strictly increasing in t, since log(t+L)/log t is strictly decreasing in t.

Therefore there is a unique threshold t_p^* solving

t_p^* + log p = (t_p^*)^{p/(p-1)},

and

Delta_p G_N > 0  iff  theta(p^-)>t_p^*.

Writing u_p := theta(p)-p and u_p^*:=t_p^*+log p-p gives

Delta_p G_N>0 iff u_p>u_p^*.

A large-p expansion gives

u_p^* = (log p)^2/[2(log p+1)] + O((log p)^3/p)
      = (1/2)log p - 1/2 + O(1/log p).

Thus the local direction of the Nicolas defect is controlled by whether the Chebyshev error theta(p)-p exceeds a threshold asymptotic to (1/2)log p.

More explicitly, if u=theta(p)-p=o(p), L=log p, then

Delta_p G_N
= [ (1+1/L)u - L/2 ]/p^2
+ O( (u^2 + L^2|u| + L^3)/(p^3 min(1,L)) ).

The exact threshold statement is primary; the expansion is only diagnostic.

## 2. Exact tail-sign representation

By the prime number theorem and Mertens product theorem, G_k -> 0. Hence telescoping gives

G_k = - sum_{j>k} Delta_{p_j} G_N.

Therefore Nicolas' criterion can be restated as

RH iff every future increment tail is negative:

sum_{j>k} Delta_{p_j} G_N < 0   for all k.

This is an exact re-encoding, not a proof.

## 3. Finite monotonic range and why monotonicity cannot be the proof

Platt-Trudgian proved theta(x)<x for 2<x<1.39e17. Since u_p^*>0 for large p, this forces Delta_p G_N<0 throughout that verified range (apart from trivial small-domain bookkeeping). Thus the Nicolas defect is locally decreasing across primes on an enormous initial interval.

However theta(x)-x is known to change sign, so eventual global monotonicity cannot be the mechanism behind Nicolas/RH. Any proof that tries to establish Delta_p G_N<=0 for all sufficiently large p is aiming at a false strengthening.

## 4. Prime-square baseline

Use

psi(x)=theta(x)+theta(x^{1/2})+theta(x^{1/3})+...

so

theta(x)-x = [psi(x)-x] - theta(sqrt x) - theta(x^{1/3}) - ... .

The dominant deterministic negative component is -sqrt x from the prime-square layer. In the tail transform for G_N this produces the positive Nicolas baseline of order

2/(sqrt x log x),

while the psi(x)-x component carries the zero-sensitive oscillation. This is the local-increment version of Nicolas' known 2+W(x) asymptotic.

Consequently, a crude pointwise bound on |psi(x)-x| followed by triangle inequality is structurally too weak: even an RH-sized bound O(sqrt x log^2 x) gives a weighted tail much larger than the 1/(sqrt x log x) positive baseline. The criterion needs cancellation in the zero-sensitive component, not only pointwise PNT error control.

## 5. Audit verdict

- one-prime increment formula: EXACT.
- local threshold u_p^*: EXACT definition; asymptotic ~0.5 log p.
- all-tail negativity criterion: EXACT / EQUIVALENT REENCODING.
- eventual monotone-decrease route: CLOSED; theta-x changes sign.
- pointwise-PNT-error + triangle inequality route: TOO WEAK.
- remaining Nicolas content: weighted future cancellation of the Chebyshev/psi residual.

This closes the idea that the Robin-Nicolas corridor can be proved by a local monotonicity argument. The open part is intrinsically a long-range signed tail problem.