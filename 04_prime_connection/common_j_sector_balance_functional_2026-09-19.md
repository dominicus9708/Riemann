# Common sector balance functional for (j=0,1,2,3) — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Purpose: unify all bounded-large-prime sectors before full closure.
- Main result: every standard two-product DLS estimate is governed by a single subset-balance functional (Delta).
- This is a bookkeeping/theorem-reduction formula, not an RH proof.
- Classification: `COMMON_J_SECTOR_BALANCE_FUNCTIONAL`.

## 1. General sector

At the Vaughan edge write
[
w=aprod_{i=1}^{j}p_i,
qquad 0le jle3,
]
where
- (dasymp V) is the outer Möbius variable;
- (a) is squarefree and (V)-smooth;
- (p_i>V) are the large-prime factors;
- (wasymp V^3).

Factor the smooth part as
[
a=prod_{ell=1}^{m}q_ell.
]

When useful, factor (d) as well; otherwise keep it atomic.

Associate to every retained atomic factor (r) the scale exponent
[
e(r):=log_V r.
]

Thus:
- an atomic (d)-block has exponent (1+o(1));
- every smooth prime (q_ellle V) has exponent (0<lambda_ellle1);
- every large prime has exponent (eta_ige1).

The full reciprocal argument has size
[
d,aprod_i p_iasymp V^4,
]
hence
[
oxed{sum_{einmathcal E_j}e=4+o(1)}
]
for the exponent multiset (mathcal E_j).

## 2. Balance functional

Define
[
oxed{
Delta(mathcal E_j)
:=
min_{Ssubseteqmathcal E_j}
left|
sum_{ein S}e-2
ight|.
}
]

Choose a minimizing subset (S), and let
[
R=V^{2+delta},
qquad
S_2=V^{2-delta},
qquad
|delta|=Delta(mathcal E_j)+o(1)
]
be the two product lengths.

The reciprocal phase
[
e!left(A(rs)^{-1/2}ight),
qquad Aasymp V^4,
]
normalizes to
[
e(Xu(r)v(s)),
qquad Xasymp V^2.
]

## 3. Standard DLS consequence

Assume that after smooth/Mellin separation the two collapsed product coefficients satisfy divisor-type second moments
[
sum_{rasymp R}|A_r|^2ll_arepsilon R V^arepsilon,
qquad
sum_{sasymp S_2}|B_s|^2ll_arepsilon S_2 V^arepsilon.
]

The normalized frequency spacings have cell width (X^{-1}asymp V^{-2}).

A product range (V^{2+delta}) has spacing multiplicity
[
ll 1+V^delta,
]
while its complementary range has multiplicity
[
ll1+V^{-delta}.
]

Thus the Bombieri--Iwaniec DLS gives
[
|T_j|^2
ll_arepsilon
V^2
cdot V^4
cdot
(1+V^delta)(1+V^{-delta})
V^arepsilon.
]

Therefore
[
oxed{
T_j
ll_arepsilon
V^{3+Delta(mathcal E_j)/2+arepsilon}.
}
]

This is the common two-product formula.

## 4. Closure criterion

Within this class of arguments:

- if
[
Delta(mathcal E_j)=o(1),
]
then the sector closes at
[
V^{3+arepsilon};
]

- if
[
Delta(mathcal E_j)gedelta_0>0
]
for an admissible family, standard two-product DLS necessarily loses at least
[
V^{delta_0/2}.
]

Hence (Delta) separates:
1. sectors already closed by product balance;
2. sectors that need genuinely additional arithmetic/multilinear input.

## 5. (j=3)

The dyadic support forces
[
a=1,
qquad
p_1,p_2,p_3asymp V.
]

Thus
[
mathcal E_3={1,1,1,1}+o(1).
]

Choosing any two factors gives
[
oxed{Delta_3=0+o(1)}.
]

Therefore
[
T_3ll_arepsilon V^{3+arepsilon}.
]

Status: CLOSED.

## 6. (j=2)

Write
[
aasymp V^alpha,
qquad
pasymp V^eta,
qquad
qasymp V^gamma,
]
where
[
0lealphale1,
qquad
1leetalegamma,
qquad
alpha+eta+gamma=3.
]

The cross partition (dpmid aq) has imbalance
[
eta-1.
]

Hence
[
Delta_2leeta-1
lerac{1-alpha}{2}.
]

At the balanced-prime configuration
[
eta=gamma=rac{3-alpha}{2},
]
even splitting the whole smooth residual (a) cannot move a single large-prime group to exponent (2), because
[
2-eta=rac{1+alpha}{2}>alpha
qquad(alpha<1).
]

Therefore this family attains
[
oxed{
Delta_2=rac{1-alpha}{2}.
}
]

Thus the sharp two-product estimate is
[
oxed{
T_2
ll_arepsilon
V^{3+(1-alpha)/4+arepsilon}.
}
]

At (alpha=1), (Delta_2=0): CLOSED endpoint.

For (alpha<1): OPEN beyond standard two-product DLS.

## 7. (j=1): long-prime flank

Write
[
aasymp V^alpha,
qquad
pasymp V^{3-alpha}.
]

For
[
0lealpha<1,
]
the large prime exponent is
[
3-alpha>2.
]

Any subset containing (p) has exponent at least (3-alpha), hence lies at distance at least
[
1-alpha
]
above (2).

Any subset excluding (p) is contained in the product (da), whose total exponent is
[
1+alpha<2,
]
again at distance at least
[
1-alpha.
]

Therefore, even after fully factorizing (d) and (a),
[
oxed{
Delta_{1,-}=1-alpha.
}
]

This is an exact structural barrier for **all two-product partitions**.

Hence
[
oxed{
T_{1,-}
ll_arepsilon
V^{3+(1-alpha)/2+arepsilon}
}
]
is the best possible scale from standard two-product DLS alone.

At (alpha=0), the loss is (V^{1/2}).

This proves that the long-prime flank genuinely requires more than product repartition.

## 8. (j=1): transition

At
[
alpha=1,
qquad
pasymp V^2,
]
we have
[
Delta_1=0.
]

Status: CLOSED.

## 9. (j=1): long-smooth flank

For
[
1<alphale2,
]
the large prime exponent (3-alpha<2).

Keep (d) atomic and write
[
a=prod q_i,
qquad
lambda_i=log_Vq_i,
qquad
sumlambda_i=alpha.
]

For a divisor (bmid a) with exponent
[
t=log_Vb,
]
the partition
[
dbmid p(a/b)
]
has imbalance
[
|t-1|.
]

Thus define the smooth subset discrepancy
[
sigma(a;V)
=
min_{bmid a}
left|log_Vb-1ight|.
]

Then
[
oxed{
Delta_{1,+}lesigma(a;V).
}
]

The elementary subset lemma gives uniformly
[
sigma(a;V)lerac13+o(1).
]

This is sharp for
[
a=q_1q_2,qquad q_iasymp V^{2/3},
qquad alpha=rac43,
]
with atomic (d), for which
[
sigma=rac13+o(1).
]

Hence the uniform two-product barrier is
[
oxed{
T_{1,+}
ll_arepsilon
V^{3+1/6+arepsilon},
}
]
and (V^{1/6}) is sharp within this class.

## 10. (j=0): pure smooth-Möbius sector

Now
[
aasymp V^3,
qquad
a=prod q_i,
qquad
0<lambda_i=log_Vq_ile1,
qquad
sum_ilambda_i=3+o(1).
]

With atomic (d), a partition (dbmid a/b) again has imbalance
[
|t-1|,
qquad t=log_Vb.
]

Hence
[
Delta_0le
min_{bmid a}
|log_Vb-1|.
]

### Sharp (1/4) subset lemma

For positive numbers
[
0<lambda_ile1,
qquad
sum_ilambda_i=3,
]
there is always a subset with sum in
[
oxed{[3/4,5/4]}.
]

Proof by contradiction:
- suppose no subset sum lies in ([3/4,5/4]);
- then every individual (lambda_i<3/4);
- choose a subset of maximal sum (s<3/4);
- every unused (lambda) must satisfy (s+lambda>5/4), so (lambda>5/4-s>1/2);
- the unused total is (3-s>9/4), so at least four unused elements are present;
- every pair of unused elements has sum (>1), and since the forbidden interval contains ([1,5/4]), every such pair must actually exceed (5/4);
- four unused elements then have total (>5/2), implying (s<1/2);
- but then each unused element is (>5/4-s>3/4), contradicting the first step.

Therefore
[
oxed{Delta_0le1/4+o(1)}.
]

The bound is sharp for
[
a=q_1q_2q_3q_4,
qquad
q_iasymp V^{3/4},
]
with atomic (d), where the nearest subset exponents to (1) are (3/4) and (3/2).

Thus standard two-product DLS gives the sharp uniform bound
[
oxed{
T_0
ll_arepsilon
V^{3+1/8+arepsilon}.
}
]

The remaining (V^{1/8}) is a genuine two-product partition barrier.

## 11. Unified sector table

The common balance functional yields:

[
egin{array}{c|c|c}
	ext{sector}&Delta	ext{ barrier}&	ext{DLS loss}\
hline
j=3&0&1\
j=2, alpha=1&0&1\
j=2, alpha<1&(1-alpha)/2&V^{(1-alpha)/4}\
j=1, alpha<1&1-alpha&V^{(1-alpha)/2}\
j=1, alpha=1&0&1\
j=1, alpha>1&le1/3	ext{ sharp uniformly}&V^{1/6}\
j=0&le1/4	ext{ sharp uniformly}&V^{1/8}
end{array}
]

## 12. Interpretation

The (j)-classification is not fundamentally four unrelated problems.

All standard two-product DLS behavior is controlled by the single combinatorial quantity
[
oxed{Delta(mathcal E_j)}.
]

The real analytic/arithmetic work begins exactly where (Delta>0).

This suggests the final common theorem should eventually have the form
[
T_j
=
T_j^{m balanced}
+
T_j^{m residual},
]
where the balanced part is controlled universally by the (Delta)-formula and the residual theorem supplies precisely the missing factor
[
V^{-Delta/2}.
]

That is the natural target for a post-closure common formula.

Permanent rules:
- `COMMON_BALANCE_FUNCTIONAL_FIRST`.
- `RESIDUAL_SAVING_MUST_MATCH_DELTA_OVER_2`.
