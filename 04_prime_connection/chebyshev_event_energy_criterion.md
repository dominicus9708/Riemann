# Chebyshev event-energy criterion

Status: exact derived RH equivalence, obtained from Johnston's integral criterion plus explicit RH bounds. Novelty not claimed; exact-form prior-art search remains incomplete.

Let

E(x):=\vartheta(x)-x,

I(x):=\int_2^x (\vartheta(t)-t)\,dt,

and define the event energy

\mathcal H(x):=I(x)+\frac12E(x)^2.

## 1. Exact conservation between primes

On every open interval containing no prime,

E'(x)=-1,
I'(x)=E(x),

hence

\mathcal H'(x)=I'(x)+E(x)E'(x)=E(x)-E(x)=0.

Thus H is exactly constant between prime events.

At a prime p, theta jumps by L=log p while I is continuous. With u_p=theta(p)-p,

\Delta_p \mathcal H
=\frac12[u_p^2-(u_p-L)^2]
=L\left(u_p-\frac L2\right).

Therefore

\boxed{\Delta_p\mathcal H>0\iff \vartheta(p)-p>\frac12\log p.}

This is extremely close to the Nicolas local-increment threshold

u_p^*=\frac12\log p-\frac12+o(1)

found in `nicolas_local_increment_tail_audit.md`.

## 2. Exact prime-sum collapse

Since

\int_2^x\vartheta(t)dt
=\sum_{p\le x}(x-p)\log p,

we have

I(x)
=x\vartheta(x)-\sum_{p\le x}p\log p-\frac{x^2}{2}+2.

Adding one half of E(x)^2 cancels every explicit x term:

\boxed{
\mathcal H(x)
=\frac12\vartheta(x)^2
-\sum_{p\le x}p\log p
+2.
}

The conservation law between primes is therefore also immediate from the fact that the right-hand side changes only when a prime enters.

## 3. RH implies H(x)<0 for all x>=3

Johnston proves under RH that for x>=3000

|\int_2^x(\psi(t)-t)dt| <= 0.08 x^{3/2}.

His unconditional Lemma 2.3 gives for t>=121

\vartheta(t)<\psi(t)-0.98\sqrt t.

Since psi-theta>=0 below 121 as well,

I(x)
<=0.08x^{3/2}-0.98\int_{121}^x\sqrt t\,dt
= -\frac{43}{75}x^{3/2}+\frac{49}{75}121^{3/2}

for x>=3000 under RH.

Schoenfeld's RH bound gives for x>=599

|E(x)|<\frac1{8\pi}\sqrt x\log^2x,

hence

\frac12E(x)^2
<\frac{x\log^4x}{128\pi^2}.

Therefore for x>=3000,

\frac{\mathcal H(x)}{x^{3/2}}
<
-\frac{43}{75}
+\frac{49\,121^{3/2}}{75x^{3/2}}
+\frac{\log^4x}{128\pi^2\sqrt x}.

At x=3000 the right side is about -0.50865. Both positive correction terms decrease for x>=3000; for the logarithmic term this follows because d(log^4 x / sqrt x)/dx<0 once log x>8, and log 3000>8. Hence H(x)<0 for all x>=3000 under RH.

For 3<=x<=3000, the rigorous verified inequality theta(x)<x is vastly stronger than needed. We have H(3)<0, H is constant between primes, and each prime jump is negative because u_p<0<L/2. Hence H(x)<0 throughout this finite interval.

Thus

RH => H(x)<0 for all x>=3.

## 4. Converse

If H(x)<0 for all x>=3, then

I(x)=H(x)-\frac12E(x)^2<0

for x>=3. For 2<x<3, theta(t)=log 2 and I(x)<0 directly. Johnston's theorem therefore gives RH.

Hence

\boxed{
RH
\iff
\mathcal H(x)<0\quad\text{for every }x\ge3.
}

## 5. Purely discrete prime inequality

Because H is constant between primes, it is enough to test prime cutoffs. The criterion becomes

\boxed{
RH
\iff
2\sum_{q\le p} q\log q
>
\vartheta(p)^2+4
\quad\text{for every prime }p\ge3.
}

Equivalently, with p_k the k-th prime and theta_k=sum_{j<=k} log p_j,

2\sum_{j<=k}p_j\log p_j > theta_k^2+4

for all k>=2.

This is a quadratic inequality between two prime-weighted moments. It uses no zeros in its statement.

## 6. Event recursion

At consecutive primes p_k<p_{k+1}, if u_k=theta(p_k)-p_k, then

u_{k+1}=u_k-(p_{k+1}-p_k)+\log p_{k+1}.

Meanwhile

H_{k+1}-H_k
=\log p_{k+1}\left(u_{k+1}-\frac12\log p_{k+1}\right).

Thus the RH criterion is a cumulative event-energy condition: positive injections are allowed, but total energy must never return to zero after p=3.

## 7. Relation to Nicolas local dynamics

Nicolas' one-prime defect increases when

u_p>\frac12\log p-\frac12+o(1),

while H increases exactly when

u_p>\frac12\log p.

Therefore both criteria react to essentially the same Chebyshev excursion threshold. The energy form removes continuous drift exactly; Nicolas uses the log-log Mertens-product geometry and begins reacting about 1/2 earlier in u_p.

This is a structural bridge, not an independent proof.

## 8. Audit verdict

- conservation between prime events: EXACT.
- prime jump formula: EXACT.
- prime-sum collapse: EXACT.
- RH equivalence H<0 for x>=3: DERIVED EXACT EQUIVALENCE using Johnston + Schoenfeld + verified theta<x range.
- discrete quadratic prime criterion: DERIVED EXACT EQUIVALENCE.
- novelty: UNRESOLVED; no novelty claim. Initial phrase search did not locate this exact quadratic form.

The next useful question is not whether H is monotone (it cannot be expected to remain so once theta-x changes sign), but whether the event increments admit a deterministic grouping/majorization that prevents cumulative energy from returning to zero.