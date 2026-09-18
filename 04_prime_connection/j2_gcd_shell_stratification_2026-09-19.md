# j=2 gcd-shell stratification and diagonal closure — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Context: j=2 sharp centered correlation with
  [
  d,d'asymp D=H^2,qquad p,p'asymp P=H^3,qquad |h|lesssim H.
  ]
- Result: the zero-shift sector is exactly diagonal and already target-sized; nonzero shifts split into primitive gcd shells with a universal H^2 short-box area and g^{-2} frame density.
- One-prime marginals remain closed uniformly after summing all gcd shells.
- Remaining open object: connected prime-pair covariance on the primitive shell family.
- Classification: `J2_GCD_SHELL_STRATIFICATION`.

## 1. Zero shift is exactly diagonal

Suppose
[
dp=d'p'
]
with
[
d,d'asymp H^2,qquad p,p'asymp H^3
]
and p,p' prime.

Because
[
p>d',qquad p'>d,
]
the prime p cannot divide d'. Thus p must divide p', so
[
p=p'.
]
Then
[
d=d'.
]

Hence:
[
oxed{
h=0quadLongrightarrowquad (d,p)=(d',p').
}
]

The zero-shift contribution is therefore the genuine diagonal
[
sum_{dasymp D}|alpha_d|^2
sum_{pasymp P}Lambda(p)^2 w(p/P)^2
ll_arepsilon
DP,H^arepsilon
=
H^{5+arepsilon}.
]

Thus the diagonal already lies exactly at the corrected normalized target.

Classification:
`J2_ZERO_SHIFT_DIAGONAL_CLOSED`.

## 2. GCD shell

For nonzero h, write
[
g=(d,d'),qquad
d=ga,qquad
d'=gb,qquad
(a,b)=1.
]

Necessarily
[
gmid h.
]

Write
[
h=gk.
]

Then
[
oxed{
ap-bp'=k.
}
]

Since
[
|h|lesssim H,
]
a nonzero shell satisfies
[
oxed{1le glesssim H,qquad |k|lesssim H/g.}
]

The small factors have length
[
a,basymp D/g=H^2/g.
]

## 3. Primitive coprimality after removing g

For k nonzero,
[
(ap,bp')=1.
]

Indeed:
- ((a,b)=1);
- (p>b), so (p
mid b);
- (p'>a), so (p'
mid a);
- if (p=p'), then
  [
  p(a-b)=k,
  ]
  impossible for nonzero (|k|<p).

Therefore every nonzero gcd shell reduces to a genuinely primitive determinant equation after g is removed.

For squarefree Möbius support, g,a,b are pairwise coprime and
[
mu(d)mu(d')
=
mu(ga)mu(gb)
=
mu(g)^2mu(a)mu(b)
=
oxed{mu(a)mu(b)}.
]

Thus the common gcd contributes no random sign:
[
oxed{	ext{the g-shell weight is sign-coherent in g}.}
]

Permanent guard:
`COMMON_GCD_DOES_NOT_SUPPLY_MOBIUS_CANCELLATION`.

## 4. Exact shell parametrization

For fixed coprime a,b, choose (ar amod b) and set
[
t_{a,b}=rac{aar a-1}{b}.
]

Then
[
p=kar a+bell,
qquad
p'=aell+t_{a,b}k.
]

Now
[
basymp H^2/g,
qquad
pasymp H^3,
]
so
[
oxed{ellasymp P/basymp gH.}
]

Combined with
[
|k|lesssim H/g,
]
the short parameter rectangle has area
[
oxed{
(H/g)(gH)=H^2,
}
]
independent of g.

The coefficient matrix remains unimodular:
[
det
egin{pmatrix}
b&ar a\
a&t_{a,b}
end{pmatrix}
=-1.
]

Therefore the local singular-series factor is still exactly 1 in every primitive gcd shell.

## 5. Frame density

The number of a,b frames in a fixed g-shell is schematically
[
(D/g)^2
=
rac{H^4}{g^2}.
]

Each frame contains H^2 short lattice points before primality/centering.

Hence the raw shell mass is
[
oxed{
rac{H^6}{g^2}.
}
]

If the connected prime-pair discrepancy is square-root-sized in each short rectangle, the error per frame is H, so the natural shell target becomes
[
oxed{
rac{H^5}{g^2}.
}
]

Summing over g gives
[
sum_{gle H}rac{H^5}{g^2}
ll H^5.
]

Thus a uniform square-root frame estimate is automatically summable over all gcd shells.

Classification:
`GCD_SHELL_SQUARE_ROOT_TARGET_SUMMABLE`.

## 6. Farey resolution in a g-shell

From
[
ap-bp'=k
]
we have
[
left|
rac ab-rac{p'}p
ight|
=
rac{|k|}{bp}.
]

Using
[
|k|lesssim H/g,qquad
basymp H^2/g,qquad
pasymp H^3,
]
gives
[
oxed{
left|a/b-p'/pight|
lesssim
H^{-4},
}
]
independent of g.

But the natural Farey spacing for denominators
[
Q_g:=H^2/g
]
is
[
Q_g^{-2}
=
g^2H^{-4}.
]

Therefore:
- g=1 is exactly Farey-critical;
- g>1 is over-resolved relative to the natural denominator spacing by a factor g^2.

This does not by itself close the connected covariance, because the ell-range grows by g and keeps the short-box area H^2 fixed.

Permanent guard:
`GCD_FAREY_OVERRESOLUTION_NOT_AUTOMATIC_SAVING`.

## 7. One-prime marginal closure uniformly in g

For fixed g, the ratio-multiplicity character polynomial has:
[
Q_g=D/g=H^2/g,
qquad
N_g=(D/g)(H/g)=P/g^2.
]

The character large sieve gives
[
mathcal E_C(g)
ll_arepsilon
rac{N_g+Q_g^2}{Q_g}N_g H^arepsilon.
]

Since
[
Q_g^2/N_g=H,
]
the (Q_g^2) term dominates uniformly, giving
[
oxed{
mathcal E_C(g)
ll_arepsilon
rac{H^5}{g^3}H^arepsilon.
}
]

For the prime AP discrepancy of length P,
[
mathcal E_P(g)
ll_arepsilon
rac{P+Q_g^2}{Q_g}P H^arepsilon.
]

If
[
gle H^{1/2},
]
then (Q_g^2ge P), so
[
mathcal E_P(g)
ll_arepsilon
rac{H^5}{g}H^arepsilon.
]

Cauchy therefore gives the one-prime marginal shell
[
oxed{
mathcal L_1(g)
ll_arepsilon
rac{H^5}{g^2}H^arepsilon
qquad(gle H^{1/2}).
}
]

If
[
g>H^{1/2},
]
then (P>Q_g^2), so
[
mathcal E_P(g)
ll_arepsilon
gH^4 H^arepsilon,
]
and hence
[
oxed{
mathcal L_1(g)
ll_arepsilon
rac{H^{9/2}}{g}H^arepsilon.
}
]

Summing:
[
sum_{gle H^{1/2}}rac{H^5}{g^2}
+
sum_{H^{1/2}<gle H}rac{H^{9/2}}g
ll_arepsilon
H^{5+arepsilon}.
]

Thus the one-prime marginal closure survives the complete gcd decomposition.

Classification:
`J2_ALL_GCD_ONE_PRIME_MARGINALS_CLOSED`.

## 8. Refined remaining target

After:
- exact zero-shift diagonal closure;
- outer-d factorability reduction;
- principal-density removal;
- all one-prime marginal closures;
- gcd-shell decomposition;

the remaining problem is only
[
oxed{
sum_{gle H}
mathcal C_{m conn}(g)
ll_arepsilon
H^{5+arepsilon},
}
]
where (mathcal C_{m conn}(g)) is the connected covariance over
[
a,basymp H^2/g,qquad
kasymp H/g,qquad
ellasymp gH,
]
with the unimodular pair
[
L_1=bell+ar a k,
qquad
L_2=aell+t_{a,b}k.
]

A sufficient shell-wise target is
[
oxed{
mathcal C_{m conn}(g)
ll_arepsilon
H^{5+arepsilon}/g^2.
}
]

The g=1 shell is simultaneously:
- largest in frame count;
- exactly Farey-critical;
- the original H x H determinant-shell geometry.

It is therefore the correct first connected-covariance stress test, although failure/success there alone does not constitute a proof for every g-shell.
