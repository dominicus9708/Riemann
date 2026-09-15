# Beurling integer rigidity and the 1/2 uncertainty floor

Status: literature-aligned synthesis + exact ordinary-system consequences.

## 1. [alpha,beta] uncertainty floor
For a Beurling generalized prime system with optimal exponents
\[
\psi_{\mathcal P}(x)=x+O_\varepsilon(x^{\alpha+\varepsilon}),\qquad
N_{\mathcal P}(x)=\rho x+O_\varepsilon(x^{\beta+\varepsilon}),
\]
Hilberdink proved
\[
\max\{\alpha,\beta\}\ge \tfrac12.
\]
Thus prime-side and integer-side regularity cannot both beat the square-root exponent.

For the ordinary integers,
\[
N(x)=\lfloor x\rfloor=x+O(1),
\]
so the integer exponent is \(\beta=0\). Hence every compatible optimal prime exponent satisfies
\[
\alpha\ge\tfrac12.
\]
Under RH one has \(\alpha=1/2\), so RH can be viewed as saturation of the Beurling regularity floor by the ordinary integer system.

## 2. Adding the Möbius exponent
Let
\[
M_{\mathcal P}(x)=O_\varepsilon(x^{\gamma+\varepsilon}).
\]
Neamah--Hilberdink proved that the two largest of \(\alpha,\beta,\gamma\) are equal and at least \(1/2\).

For the ordinary system \(\beta=0\), therefore
\[
\alpha=\gamma\ge\tfrac12.
\]
In the ordinary zeta case the common optimal exponent is the spectral abscissa \(\Theta=\sup\{\Re\rho:\zeta(\rho)=0\}\). Thus
\[
\mathrm{RH}\iff \alpha=\gamma=\Theta=\tfrac12.
\]
This unifies the Chebyshev-error and Mertens-error branches: they are not independent exponent problems once exact ordinary integer regularity is fixed.

## 3. Exact integer-completeness is strictly stronger than density
The condition \(N(x)=\lfloor x\rfloor\) as a counting function with multiplicity means that the generalized integer multiset is exactly \(\mathbb N\). Its irreducibles are therefore exactly the ordinary primes, so the generalized prime multiset must be the ordinary prime multiset.

By contrast, preserving only the residue/density \(N(x)\sim x\) leaves large deformation freedom. Hence the relevant hierarchy is

1. zero-divisor preservation in a half-plane;
2. residue / integer-density preservation;
3. finite Laurent-jet preservation at \(s=1\);
4. exact generalized-integer multiset equality.

Only the final level forces the ordinary primes exactly.

## 4. Methodological consequence
Integer-completeness explains why \(1/2\) is a lower regularity floor but does not prove the RH upper bound \(\alpha\le1/2\). Any successful argument still needs a saturation mechanism showing that the ordinary system achieves the universal lower floor rather than some larger exponent.

Classification: `BEURLING_UNCERTAINTY / EXACT_INTEGER_RIGIDITY`, not a proof of RH.
