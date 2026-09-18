# j=2 ratio-character large-sieve closure of one-prime marginals — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Context: sharp j=2 determinant shell
[
ap-bp'=k,
qquad
D=H^2,quad P=H^3,quad S=DP=H^5.
]
- Result: the residue-multiplicity fluctuation, including the actual real Möbius/divisor-bounded outer coefficient, is already at the exact S-scale after averaging over moduli.
- The corresponding one-prime arithmetic-progression marginal is also S-scale.
- Therefore all linear/one-body pieces of the unimodular prime-pair expansion close by the ordinary character large sieve.
- Remaining object: the genuinely connected two-prime covariance in the same unimodular frame.
- Classification: `J2_ONE_PRIME_MARGINALS_LARGE_SIEVE_CLOSED`.

## 1. Residue multiplicity

For (basymp D), define on the reduced residue group
[
C_b(r)
:=
sum_{substack{aasymp D, kasymp H\(ak,b)=1\kar aequiv rpmod b}}
alpha_aeta_k,
]
where
- (alpha_a) is the inherited real Möbius/divisor-bounded coefficient;
- (eta_k) is a bounded smooth shift coefficient.

Let
[
ar C_b
:=
rac1{arphi(b)}
left(sum_{substack{aasymp D\(a,b)=1}}alpha_aight)
left(sum_{substack{kasymp H\(k,b)=1}}eta_kight).
]

This is exactly the principal-character component.

## 2. Character Parseval

Fourier inversion on ((mathbb Z/bmathbb Z)^	imes) gives
[
sum_{rin(mathbb Z/bmathbb Z)^	imes}
|C_b(r)-ar C_b|^2
=
rac1{arphi(b)}
sum_{chi
echi_0}
|A_b(chi)|^2 |K_b(chi)|^2,
]
up to harmless conjugation conventions, with
[
A_b(chi)=sum_{aasymp D}alpha_achi(a),
qquad
K_b(chi)=sum_{kasymp H}eta_kchi(k).
]

Because the coefficients are real,
[
|A_b(chi)|=|A_b(archi)|,
qquad
|K_b(chi)|=|K_b(archi)|.
]

Hence
[
|A_b(chi)|^2|K_b(chi)|^2
=
left|
sum_n c_nchi(n)
ight|^2,
]
where
[
c_n
=
sum_{substack{ak=n\aasymp D, kasymp H}}
alpha_aeta_k.
]

Thus the apparently ratio-type multiplicity problem is converted to an ordinary product Dirichlet polynomial.

Classification:
`RATIO_CHARACTER_PRODUCT_COLLAPSE`.

## 3. Length and coefficient norm

The product polynomial has length
[
Nasymp DH=P=H^3.
]

For divisor-bounded (alpha_a) and bounded (eta_k),
[
|c_n|ll 	au(n)^{O(1)},
]
and therefore
[
sum_n |c_n|^2
ll_arepsilon
P^{1+arepsilon}.
]

## 4. Dyadic character large sieve

For (basymp D), the standard large sieve for Dirichlet characters, with the usual harmless loss for induced characters, gives
[
sum_{basymp D}
rac{b}{arphi(b)}
sum_{chimod b}^{*}
left|
sum_n c_nchi(n)
ight|^2
ll_arepsilon
(P+D^2)P^{1+arepsilon}.
]

Passing from primitive to all characters costs only divisor/logarithmic factors in the present (H^arepsilon) bookkeeping.

Since (basymp D),
[
rac1{arphi(b)}
asymp
rac1Drac{b}{arphi(b)}.
]

Therefore
[
sum_{basymp D}
sum_{r}^{*}
|C_b(r)-ar C_b|^2
ll_arepsilon
rac{P+D^2}{D}P^{1+arepsilon}.
]

At the sharp scale
[
D=H^2,qquad P=H^3,
]
we have (D^2=H^4>P), hence
[
oxed{
sum_{basymp D}
sum_r^{*}
|C_b(r)-ar C_b|^2
ll_arepsilon
DP,H^arepsilon
=
H^{5+arepsilon}
=
S^{1+arepsilon}.
}
]

This is exactly the corrected normalized residual scale.

Permanent rule:
`RATIO_MULTIPLICITY_L2_IS_ALREADY_S_SCALE`.

## 5. Prime AP discrepancy has the same scale

Let
[
E_b(r)
:=
sum_{substack{pasymp P\pequiv rpmod b}}
Lambda(p)w(p/P)
-
rac1{arphi(b)}
sum_{substack{nasymp P\(n,b)=1}}
Lambda(n)w(n/P).
]

Character Parseval gives
[
sum_r^{*}|E_b(r)|^2
=
rac1{arphi(b)}
sum_{chi
echi_0}
|P_b(chi)|^2.
]

Applying the same dyadic character large sieve to the length-P sequence
[
Lambda(n)w(n/P),
]
with
[
sum_{nasymp P}Lambda(n)^2|w(n/P)|^2
ll Plog P,
]
yields
[
oxed{
sum_{basymp D}sum_r^{*}|E_b(r)|^2
ll_arepsilon
DP,H^arepsilon
=
H^{5+arepsilon}.
}
]

This is the dyadic Barban--Davenport--Halberstam scale appropriate to (D=P^{2/3}>sqrt P).

Classification:
`J2_PRIME_AP_L2_AT_S_SCALE`.

## 6. Linear marginal closure

The first one-prime marginal has the form
[
mathcal L_1
=
sum_{basymp D}alpha_b
sum_r^{*}
(C_b(r)-ar C_b),E_b(r),
]
up to smooth dyadic factors.

Cauchy--Schwarz and the two preceding L2 bounds give
[
|mathcal L_1|
ll_arepsilon
H^{5+arepsilon}
=
S^{1+arepsilon}.
]

The symmetric second marginal is identical after exchanging the two sides.

Therefore:
[
oxed{
	ext{all one-prime / linear marginal terms close at the exact normalized target.}
}
]

No pointwise prime-AP theorem at modulus (P^{2/3}) is required.

This sharpens the earlier `J2_PRIME_AP_TWO_THIRDS_BARRIER` statement:
- the (P^{2/3}) modulus is a barrier only for a pointwise/supremum treatment;
- after preserving the full residue/modulus L2 average, the linear marginal is already closed by the classical large sieve.

Permanent correction:
`POINTWISE_P23_BARRIER_DOES_NOT_APPLY_TO_L2_MARGINAL`.

## 7. What remains

Write schematically
[
Lambda(L_1)Lambda(L_2)-1
=
(Lambda(L_1)-1)(Lambda(L_2)-1)
+
(Lambda(L_1)-1)
+
(Lambda(L_2)-1),
]
with the constant (1) replaced by the appropriate smooth local density in the rigorous version.

The last two terms are the one-prime marginals just closed.

Hence the only new arithmetic object is the connected covariance
[
oxed{
mathcal C_{m conn}
=
sum_{a,basymp D}
alpha_aalpha_b
sum_{k,ellasymp H}
(Lambda(L_1)-ho_1)
(Lambda(L_2)-ho_2)
}
]
for
[
L_1=bell+ar a k,
qquad
L_2=aell+t_{a,b}k,
qquad
det
egin{pmatrix}
b&ar a\
a&t_{a,b}
end{pmatrix}
=-1.
]

The target remains
[
oxed{
mathcal C_{m conn}
ll_arepsilon
H^{5+arepsilon}.
}
]

Thus j=2 is no longer a general prime-AP distribution problem. It is specifically an averaged connected prime-pair covariance problem over near-cusp unimodular frames.

Classification:
`J2_CONNECTED_UNIMODULAR_PRIME_PAIR_COVARIANCE_OPEN`.

## 8. Dispersion-order lesson

Recent beyond-square-root dispersion proofs provide a useful structural warning: applying Poisson/completion before removing bad index-pair structure can introduce an extra shift sum whose trivial bound costs one full factor H.

The present project has independently identified exactly one missing H at variance level.

Therefore the next step should preserve the connected pair structure before completion:
1. remove/close principal and one-body modes first;
2. identify degenerate/bad pair subfamilies by gcd and near-diagonal structure;
3. only then apply Vaughan/Heath--Brown and Poisson/Kloosterman completion to the connected piece.

Permanent rule:
`CONNECTED_PAIR_BEFORE_POISSON`.
