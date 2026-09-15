# Event-energy block majorization audit

Status: exact generic identities + bounded-locality obstruction from known Chebyshev oscillations. No RH proof claim.

Let

H(x)=1/2 theta(x)^2 - sum_{p<=x} p log p + 2.

For prime cutoffs a<b define

L := theta(b)-theta(a),

pbar_log := [sum_{a<p<=b} p log p]/L.

Then exactly

H(b)-H(a)
= L[(theta(a)+theta(b))/2 - pbar_log].

Thus a block loses energy iff

pbar_log > [theta(a)+theta(b)]/2.

This is the exact log-weighted centroid formulation.

## 1. Generic step-function false control

The half coefficient is not RH-specific. For any increasing step function

A(x)=sum_{x_j<=x} w_j

with discrepancy E_A(x)=A(x)-x, define

H_A(x)=int E_A(t)dt + 1/2 E_A(x)^2.

Between events E_A'=-1 and the integral derivative is E_A, hence H_A'=0. At event x_j,

Delta H_A = w_j(E_A(x_j)-w_j/2).

For any event block with total mass W=A(b)-A(a) and weighted event centroid

xbar_w = sum x_j w_j / W,

Delta H_A = W[(A(a)+A(b))/2-xbar_w].

Therefore the `1/2`, midpoint and centroid geometry are universal completion-of-square consequences of sawtooth drift. They are not evidence for the zeta critical line.

Permanent classification: `EVENT_ENERGY_HALF_FALSE_CONTROL`.

## 2. Prime-gap form

Let consecutive primes in a block be p_{m+1},...,p_n, write

l_j=log p_j,

g_j=p_j-p_{j-1},

u_j=theta(p_j)-p_j,

and L=sum l_j. Then

u_j=u_{j-1}-g_j+l_j.

The block energy can also be written

Delta H
=u_m L + L^2/2 - sum_{j=m+1}^n g_j [sum_{r=j}^n l_r].

Thus large early gaps have more damping leverage than equally large late gaps. Any gap-order proof would have to control this future-log-mass weighted gap sum.

## 3. Bounded-locality obstruction

Littlewood proved

psi(x)-x = Omega_+(sqrt(x) log log log x).

Known elementary/explicit estimates give

0 <= psi(x)-theta(x) << sqrt(x).

Hence

theta(x)-x = Omega_+(sqrt(x) log log log x).

Taking the largest prime p_n<=x along such a positive sequence gives

u_n:=theta(p_n)-p_n
>= c sqrt(p_n) log log log p_n

for some c>0 along an unbounded sequence.

Going backwards one prime,

u_{j-1}
= u_j + (p_j-p_{j-1}) - log p_j
>= u_j - log p_n.

Therefore for every integer r>=0,

u_{n-r}
>= u_n - r log p_n.

Choose, for example,

R_n=floor[u_n/(4 log p_n)].

Then for all 0<=r<=R_n and sufficiently large n,

u_{n-r} >= 3u_n/4 >> log p_n >= (1/2)log p_{n-r}.

Hence every prime event in this entire consecutive run has

Delta H_{p_{n-r}}>0.

Moreover

R_n >> sqrt(p_n) log log log p_n / log p_n -> infinity.

### Consequence

No rule that partitions or compensates the event-energy using a uniformly bounded number K of adjacent prime events can make every block nonpositive. For every fixed K there exist arbitrarily large runs of more than K consecutive positive energy injections.

This closes all fixed-locality pairing/triple/K-block strategies.

A viable deterministic grouping, if it exists, must have a block length growing with scale or must carry a long-range negative reserve across arbitrarily long positive runs.

## 4. Relation to the RH mechanism

Under RH the global energy has a negative prime-square reserve of order x^(3/2), whereas the local injection sign is controlled by theta(p)-p - (1/2)log p. The existence of arbitrarily long positive runs is therefore compatible with RH: local monotonicity is neither necessary nor expected.

The remaining question is genuinely global:

Can a scale-growing block rule or reserve inequality force cumulative H to remain negative without importing an RH-equivalent estimate for theta/psi?

## 5. Audit verdict

- block centroid identity: EXACT.
- half-midpoint geometry: GENERIC FALSE CONTROL, not RH-specific.
- fixed-K local grouping: CLOSED by theta-x Omega_+ oscillations.
- scale-growing grouping / global reserve: OPEN.

This sharpens `METHOD-OPEN-04/05`: the block size cannot remain bounded.