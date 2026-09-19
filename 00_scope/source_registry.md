# Audited Source Registry

외부 자료를 단순 인용하지 않고, 저장소에서 맡길 역할과 한계를 함께 기록한다.

## S001 — Clay Mathematics Institute: Riemann Hypothesis

- Type: `OFFICIAL_PROBLEM_SOURCE`
- Role: RH의 공식 문제 범위와 해결 대상 정의
- Main claim used here: 모든 비자명한 영점의 실수부가 1/2이라는 명제가 RH이다.
- Strength: 문제의 공식 범위를 정하는 최상위 기준 중 하나
- Limitation: 계산 알고리즘의 세부 기준이나 최신 연구 전체를 포괄하는 전문 데이터베이스는 아님
- Audit verdict: `ACCEPT_FOR_SCOPE`
- URL: https://www.claymath.org/millennium/Riemann-Hypothesis/

## S002 — Enrico Bombieri: Official Millennium Prize Problem Description

- Type: `OFFICIAL_PROBLEM_SOURCE`
- Role: 정밀한 문제 진술, 역사 및 수론적 맥락
- Strength: CMI 공식 문제 설명
- Limitation: 2000년 무렵 작성된 공식 문제 설명이므로 이후 수치기록과 최신 부분결과의 최신성 출처로 사용하지 않음
- Audit verdict: `ACCEPT_FOR_SCOPE_AND_CLASSICAL_CONTEXT`
- URL: https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf

## S003 — NIST DLMF §25.2

- Type: `STANDARD_REFERENCE`
- Role: 제타함수의 Dirichlet 급수 정의, 해석적 연속, Euler product 등
- Strength: 수식·정의에 대한 표준화된 참고자료이며 고전 문헌으로 출처를 역추적 가능
- Limitation: 모든 개별 정리의 원증명 논문을 대체하지 않음
- Audit verdict: `ACCEPT_FOR_FOUNDATIONAL_FORMULAS`
- URL: https://dlmf.nist.gov/25.2

## S004 — NIST DLMF §25.4

- Type: `STANDARD_REFERENCE`
- Role: 함수방정식과 Riemann xi 함수
- Main formula: xi(s)=xi(1-s)
- Audit verdict: `ACCEPT_FOR_FUNCTIONAL_EQUATION`
- URL: https://dlmf.nist.gov/25.4

## S005 — NIST DLMF §25.10

- Type: `STANDARD_REFERENCE`
- Role: 자명/비자명 영점, 임계띠, 대칭, Z(t) 정의, Riemann–Siegel 공식의 표준 개요
- Audit warning: 대칭성은 RH를 함의하지 않는다. 영점 집합이 대칭이라는 사실과 개별 영점이 대칭축 위에 있다는 명제는 구별한다.
- Audit verdict: `ACCEPT_FOR_ZERO_STRUCTURE`
- URL: https://dlmf.nist.gov/25.10

## S006 — NIST DLMF §25.18

- Type: `STANDARD_REFERENCE`
- Role: 제타함수 및 영점 계산 방법의 표준 개요
- Strength: Riemann–Siegel 등 계산도구의 문헌 연결
- Freshness warning: 영점 계산 현황에 관한 일부 서술은 2008년 시점을 명시한다. 따라서 2026년 현재의 최신 검증 범위 근거로 사용하지 않는다.
- Audit verdict: `ACCEPT_FOR_METHOD_REFERENCE_ONLY`
- URL: https://dlmf.nist.gov/25.18

## S007 — LMFDB Riemann zeta zeros source/completeness pages

- Type: `COMPUTATIONAL_DATASET`
- Role: 외부 대규모 영점 데이터의 교차검증 기준
- Reported data: 103,800,788,359 zeros in 0<t<=30,610,046,000; absolute precision ±2^-102; completeness reported as rigorously checked using a version of Turing's method.
- Critical audit note: 관련 LMFDB knowl 페이지의 review status가 `beta/awaiting review`로 표시된다. 따라서 데이터 자체의 원 계산 논문과 알고리즘을 별도로 확인해 신뢰성을 계층화해야 한다.
- Audit verdict: `ACCEPT_AS_EXTERNAL_DATA_WITH_PROVENANCE_CHECK_REQUIRED`
- URLs:
  - https://www.lmfdb.org/knowledge/show/rcs.source.zeros.zeta
  - https://www.lmfdb.org/knowledge/show/rcs.cande.zeros.zeta

## S008 — NIST DLMF §25.16

- Type: `STANDARD_REFERENCE`
- Role: Chebyshev psi 함수, 제타 영점과 소수분포의 연결, RH 동치 오차식
- Main result used here: RH iff psi(x)=x+O(x^(1/2+epsilon)) for every epsilon>0.
- Strength: 표준 정의와 동치명제를 명확하게 분리해 제공
- Audit warning: 명시적 공식의 영점 합은 합산 순서/극한 규약을 요구한다. 유한 영점 합을 그대로 정확식으로 사용하지 않는다.
- Audit verdict: `ACCEPT_FOR_PRIME_ZERO_CONNECTION`
- URL: https://dlmf.nist.gov/25.16

## S009 — David J. Platt (2017), Isolating some non-trivial zeros of zeta

- Type: `PRIMARY_RESEARCH`
- Journal: Mathematics of Computation 86 (2017), 2449–2467
- DOI: 10.1090/mcom/3198
- Role: 엄밀한 제타 계산과 영점 고립, 대규모 유한범위 인증의 원 계산 근거
- Reported scope: imaginary part <= 30,610,046,000; absolute precision ±2^-102
- Strength: peer-reviewed primary computation paper
- Audit limitation: 유한 높이 검증이며 전역 RH 증명이 아님. 재현 구현이 동일한 엄밀성을 갖기 위해서는 interval/error enclosure와 completeness proof를 별도로 구현해야 함.
- Audit verdict: `ACCEPT_AS_PRIMARY_RIGOROUS_COMPUTATION_SOURCE`

## S010 — Platt & Trudgian (2021), The Riemann hypothesis is true up to 3·10^12

- Type: `PRIMARY_RESEARCH`
- Journal: Bulletin of the London Mathematical Society 53 (2021), 792–797
- DOI: 10.1112/blms.12460
- Role: 현대적인 엄밀 유한높이 RH 검증 기준
- Reported claim: interval arithmetic로 0<gamma<=3×10^12의 모든 비자명 영점이 beta=1/2이며 해당 범위의 영점이 simple임을 검증
- Strength: peer-reviewed, 유한범위가 명시된 엄밀 계산 주장
- Audit limitation: finite-height theorem/computation; global RH로 외삽 금지
- Audit verdict: `ACCEPT_AS_FINITE_RIGOROUS_VERIFICATION`

## S011 — Chirre (2021), Large oscillations of the argument of the Riemann zeta-function

- Type: `PRIMARY_RESEARCH`
- Journal: Bulletin of the London Mathematical Society
- Role: 현대 문헌에서의 Riemann–von Mangoldt 공식 표기와 S(t) 정의 교차검증
- Audit note: 논문의 주정리는 별도 가정을 사용할 수 있으므로, 여기서는 도입부의 표준 무조건적 zero-counting formula만 기준으로 사용한다.
- Audit verdict: `ACCEPT_FOR_STANDARD_ZERO_COUNT_FORMULA`

## S012 — Bertil Nyman (1950), On the One-Dimensional Translation Group and Semi-Group in Certain Function Spaces

- Type: `PRIMARY_CLASSICAL_SOURCE`
- Form: Uppsala doctoral thesis
- Role: RH를 실변수 함수공간의 closure 문제로 옮기는 Nyman–Beurling 계보의 출발점
- Audit limitation: `L^2`/closure reformulation은 RH와 동치인 새 표현이지 RH의 무조건적 증명이 아님.
- Audit verdict: `ACCEPT_FOR_NYMAN_BEURLING_ORIGIN`

## S013 — Arne Beurling (1955), A Closure Problem Related to the Riemann Zeta-Function

- Type: `PRIMARY_CLASSICAL_SOURCE`
- Journal: Proceedings of the National Academy of Sciences 41 (1955), 312–314
- Role: Nyman의 closure 접근을 `L^p`로 일반화. zero-free half-plane `Re(s)>1/p`와 특정 fractional-part dilation span의 `L^p` 조밀성을 연결.
- Critical audit use: `p=2 -> 1/2`가 Hilbert-space 선택과 연결된다는 고전적 기준.
- Audit limitation: 왜 산술구조가 `p=2`를 선택해야 하는지를 독립적으로 증명하는 결과는 아님.
- Audit verdict: `ACCEPT_FOR_LP_CLOSURE_CRITERION`

## S014 — Luis Báez-Duarte (1999), A Class of Invariant Unitary Operators

- Type: `PRIMARY_RESEARCH`
- Journal: Advances in Mathematics 144(1) (1999), 1–12
- DOI: 10.1006/aima.1998.1801
- Role: `L^2((0,∞),dx)`의 dilation operator와 invariant unitary operator를 Nyman–Beurling Hilbert closure 문제와 연결.
- Audit verdict: `ACCEPT_FOR_DILATION_HILBERT_OPERATOR_CONTEXT`

## S015 — Luis Báez-Duarte (2002), New Versions of the Nyman-Beurling Criterion for the Riemann Hypothesis

- Type: `PRIMARY_RESEARCH`
- Journal: International Journal of Mathematics and Mathematical Sciences 31(7) (2002), 387–406
- DOI: 10.1155/S0161171202013248
- Role: 일반 `L^p`에서 zero-free boundary `Re(s)>1/p`, Möbius/Mertens norm, Nyman–Beurling 근사를 직접 연결.
- Critical audit use: `1/p` 경계는 `L^p` 선택 전반의 구조임을 확인.
- Audit verdict: `ACCEPT_FOR_LP_MOBIUS_NB_CONNECTION`

## S016 — Luis Báez-Duarte (2003), A Strengthening of the Nyman-Beurling Criterion for the Riemann Hypothesis

- Type: `PRIMARY_RESEARCH`
- Journal: Rendiconti Lincei, Matematica e Applicazioni 14 (2003), 5–11
- Preprint: arXiv:math/0202141
- Role: 연속 dilation family보다 작은 정수 dilation family만으로도 RH와 동치인 closure criterion을 구성.
- Audit limitation: 정수 dilation으로 산술화되지만 criterion의 참을 무조건적으로 증명한 것은 아님.
- Audit verdict: `ACCEPT_FOR_INTEGER_DILATION_CRITERION`

## S017 — Báez-Duarte, Balazard, Landreau & Saias (2000), Notes sur la fonction ζ de Riemann, 3

- Type: `PRIMARY_RESEARCH`
- Journal: Advances in Mathematics 149(1) (2000), 130–144
- DOI: 10.1006/aima.1999.1861
- Role: Nyman–Beurling approximation distance의 정량적 분석과 영점 정보의 연결.
- Audit verdict: `ACCEPT_FOR_QUANTITATIVE_NB_DISTANCE`

## S018 — Jean-François Burnol (2002), A Lower Bound in an Approximation Problem Involving the Zeros of the Riemann Zeta Function

- Type: `PRIMARY_RESEARCH`
- Journal: Advances in Mathematics 170(1) (2002), 56–70
- DOI: 10.1006/aima.2001.2066
- Role: Nyman–Beurling approximation lower bound를 강화하고, 제타 영점과 연결된 Hilbert-space vectors를 구성. Hilbert–Pólya 관점과도 연결.
- Audit limitation: RH 증명이 아니라 approximation obstruction/zero geometry 분석.
- Audit verdict: `ACCEPT_FOR_NB_ZERO_HILBERT_GEOMETRY`

## S019 — Titus Hilberdink (2014), The Group of Squarefree Integers

- Type: `PRIMARY_RESEARCH`
- Journal: Linear Algebra and its Applications 457 (2014), 383–399
- DOI: 10.1016/j.laa.2014.05.037
- Role: squarefree integers가 `m∘n=lcm(m,n)/gcd(m,n)` 아래 Boolean abelian group을 이루며 Möbius 함수가 그 character 중 하나임을 명시. 유한 divisor subgroup의 character/Fourier 구조를 연구.
- Critical audit use: formation prime-channel symmetric difference와 Möbius parity character의 선행기준.
- Audit verdict: `ACCEPT_FOR_SQUAREFREE_BOOLEAN_GROUP`

## S020 — Hedenmalm, Lindqvist & Seip (1997), A Hilbert Space of Dirichlet Series and Systems of Dilated Functions in L²(0,1)

- Type: `PRIMARY_RESEARCH`
- Journal: Duke Mathematical Journal 86(1) (1997), 1–37
- DOI: 10.1215/S0012-7094-97-08601-4
- Role: square-summable coefficients의 Dirichlet-series Hilbert space `H²`를 도입하고, 무한차원 polydisc/polytorus의 Hardy `H²`, character space, `L²(0,1)` dilation systems를 직접 연결.
- Critical audit use: `ell² coefficient -> Dirichlet series -> dilation L²`가 이미 존재하는 강한 선행 다리임을 확인.
- Audit limitation: Möbius coefficient sequence 자체는 무한 `ell²`에 속하지 않으며, 이 Hilbert geometry만으로 RH를 증명하지 않음.
- Audit verdict: `ACCEPT_FOR_DIRICHLET_HILBERT_BRIDGE`

## S021 — Defant, García, Maestre & Sevilla-Peris (2019), Hardy Spaces of Dirichlet Series / Bohr’s Problem in Hardy Spaces

- Type: `MODERN_MONOGRAPH_REFERENCE`
- Work: Dirichlet Series and Holomorphic Functions in High Dimensions, Cambridge University Press
- Chapter DOI: 10.1017/9781108691611.013 and 10.1017/9781108691611.014
- Role: Bohr transform를 통한 Dirichlet series와 infinite polytorus Hardy spaces의 현대적 정리. `H²`가 square-summable coefficient space와 일치함을 표준화하며 Hardy-space abscissa 문제에서 `1/2` 경계를 설명.
- Audit verdict: `ACCEPT_FOR_MODERN_HARDY_DIRICHLET_REFERENCE`

## S022 — Anders Björner (2011), A Cell Complex in Number Theory

- Type: `PRIMARY_RESEARCH`
- Journal: Advances in Applied Mathematics 46 (2011), 71–85
- DOI: 10.1016/j.aam.2010.09.007
- Role: squarefree integers `<=n` ordered by divisibility를 simplicial complex로 보고 Euler characteristic/Mertens function, Betti numbers, wedge-of-spheres 구조를 연구.
- Critical audit use: weighted prime-product threshold complex가 이미 직접적인 RH/topological literature에 속함을 확인.
- Audit limitation: topology/Betti information만으로 Mertens square-root bound를 주지 않음.
- Audit verdict: `ACCEPT_FOR_NUMBER_THEORETIC_THRESHOLD_COMPLEX`

## S023 — Jonathan Pakianathan & Troy Winfree (2013), Threshold Complexes and Connections to Number Theory

- Type: `PRIMARY_RESEARCH`
- Journal: Turkish Journal of Mathematics 37(3) (2013)
- DOI: 10.3906/mat-1112-14
- Role: scalar-weight quota/threshold complexes와 quota 변화에 따른 topology를 연구하고 PNT, RH 등 수론문제를 위상적 formulation으로 연결.
- Critical audit use: `sum log p_j epsilon_j <= log X` 형식의 formation cutoff가 일반 threshold/quota-complex 이론과 겹침을 확인.
- Audit limitation: threshold-complex reformulation 자체는 RH 증명이 아님.
- Audit verdict: `ACCEPT_FOR_THRESHOLD_QUOTA_CONTEXT`

## S024 — Anders Björner & Martin Tancer (2009), Combinatorial Alexander Duality — A Short and Elementary Proof

- Type: `PRIMARY_RESEARCH`
- Journal: Discrete & Computational Geometry 42 (2009), 586–593
- DOI: 10.1007/s00454-008-9102-x
- Role: finite Boolean ground set에서 `X*={A:V\A notin X}` 형태의 complement-based Alexander duality를 정식화.
- Critical audit use: primorial divisor complement `d <-> P_m/d`가 일반 Boolean complement duality의 산술 실현임을 판별하는 기준.
- Audit verdict: `ACCEPT_FOR_COMPLEMENT_ALEXANDER_DUALITY`


## S025 — Todd Cochrane & Zhiyong Shi (2010), The congruence x1 x2 ≡ x3 x4 (mod m) and mean values of character sums

- Type: `PRIMARY_RESEARCH`
- Journal: Journal of Number Theory 130(3) (2010), 767–785
- Role: arbitrary-modulus product-congruence collision counts and fourth-moment character-sum control; used as an unweighted/support-level cross-check for ratio-residue multiplicity.
- Critical audit use: for rectangular boxes, the centered product-congruence count has a square-root-of-box-volume error up to (m^{o(1)})-type factors, matching the natural (DH) scale in the j=2 support model.
- Limitation: interval/indicator support theorem; it does not by itself handle the actual signed Möbius coefficient. The weighted project estimate is instead closed by character product-collapse plus the large sieve.
- Audit verdict: `ACCEPT_FOR_UNWEIGHTED_PRODUCT_CONGRUENCE_CROSSCHECK`

## S026 — Alexandru Pascadi (2025), Smooth numbers in arithmetic progressions to large moduli

- Type: `PRIMARY_RESEARCH`
- Journal: Compositio Mathematica 161(8) (2025), 1923–1974
- DOI: 10.1112/S0010437X2500747X
- Role: modern Linnik-dispersion / Poisson / Kloosterman template beyond the square-root modulus barrier.
- Critical audit use: Remark 8.3 records that introducing the post-Poisson dual shift costs one full factor (H) under the trivial bound, motivating removal of bad index pairs before Poisson.
- Relevance here: the current j=2 variance front independently has exactly one missing factor (H); therefore completion order and bad-pair elimination are compared against this proof architecture.
- Limitation: smooth-number coefficients and parameter geometry differ from the present Möbius-weighted connected prime-pair covariance. No black-box transfer is allowed.
- Audit verdict: `ACCEPT_FOR_DISPERSION_ARCHITECTURE_NOT_DIRECT_CLOSURE`

## S027 — Zongkun Zheng (2025), Primes in simultaneous arithmetic progressions

- Type: `PRIMARY_PREPRINT`
- arXiv: 2512.22798
- Role: mean-value distribution of primes constrained by two simultaneous arithmetic progressions, using spectral Kloosterman estimates and q-van der-Corput methods.
- Critical audit use: comparison source for moving-residue / simultaneous-congruence structures that arise after the j=2 determinant-shell reduction.
- Limitation: theorem hypotheses, factorable weights and parameter ranges must be matched exactly; it is not counted as a closure theorem for the unimodular connected covariance.
- Audit verdict: `ACCEPT_FOR_SIMULTANEOUS_AP_COMPARISON_EXACT_MAP_REQUIRED`

## S028 — Alexandru Pascadi (2026), Non-Abelian Amplification and Bilinear Forms with Kloosterman Sums

- Type: `PRIMARY_RESEARCH`
- Journal: Geometric and Functional Analysis 36 (2026), 1174–1243
- DOI: 10.1007/s00039-026-00746-0
- Role: bilinear Type-II Kloosterman sums for composite moduli via non-abelian Fourier analysis and amplification.
- Reported scope: nontrivial bounds for essentially all composite moduli beyond the Pólya–Vinogradov range; at square-root summation length, products of two comparably-sized primes admit a (c^{-1/12}) saving.
- Relevance here: candidate comparison theorem after a rigorous Vaughan/Heath–Brown and completion step produces an exact Kloosterman bilinear form.
- Limitation: near-prime and modulus-factorization dependence is material. Do not transfer the saving before the exact transformed modulus and two sequence lengths are identified.
- Audit verdict: `ACCEPT_AS_KLOOSTERMAN_INPUT_CANDIDATE_EXACT_PARAMETER_MAP_REQUIRED`

## S029 — Valentin Blomer & Alexandru Pascadi (2026), Bilinear forms with Kloosterman sums via quadratic characters

- Type: `PRIMARY_PREPRINT`
- arXiv: 2607.24311
- Role: new bilinear Kloosterman bounds valid for all moduli.
- Reported critical-range result: when the summation length is the square root of the modulus, a (c^{-1/32}) saving over the trivial bound is obtained.
- Relevance here: possible future input if the connected j=2 covariance is transformed into the exact fixed-modulus bilinear Kloosterman geometry of the theorem.
- Limitation: the present project has not yet derived that exact transformed form. Any exponent comparison before parameter matching is only heuristic.
- Audit verdict: `ACCEPT_AS_CURRENT_KLOOSTERMAN_BENCHMARK_EXACT_PARAMETER_MAP_REQUIRED`


## S030 — Rachita Guria (2024), An asymptotic formula with power-saving error term for counting prime solutions to a binary additive problem

- Type: `PRIMARY_RESEARCH`
- Preprint: arXiv:2410.10856
- Role: the closest direct determinant-equation prior art to the current j=2 connected shell.
- Main theorem used for audit: for (ad-pb=r), one arbitrary coefficient (alpha(a)=O(a^arepsilon)), one prime variable (p), and the other two variables unrestricted/smoothed, Guria obtains an asymptotic with error
  [
  O_arepsilon!left(X^{7/4+arepsilon}+|r|^{1/5}X^{31/20+arepsilon}ight).
  ]
  Choosing the arbitrary coefficient as a prime indicator gives a two-prime determinant count with the same power-saving error.
- Method: smooth the unrestricted variables, Poisson summation, then average Kloosterman fractions over the prime variable.
- Critical limitation for this project: our sharp j=2 shell has **two** small arithmetic coefficients (Möbius/prime-like) and **two** large prime variables, with anisotropic lengths (H^2,H^2,H^3,H^3). Guria's theorem does not provide this four-arithmetic-variable weighted estimate as a black box.
- Audit verdict: `ACCEPT_AS_CLOSEST_DETERMINANT_POSITIVE_CONTROL_NOT_DIRECT_CLOSURE`
- URL: https://arxiv.org/abs/2410.10856

## S031 — Natalie Evans (2022/2023), Correlations of almost primes

- Type: `PRIMARY_RESEARCH`
- Journal: Mathematical Proceedings of the Cambridge Philosophical Society 174(2), 301–344
- DOI: 10.1017/S0305004122000251
- Role: direct comparison for correlations (n,n+h) when both are products of two primes.
- Main relevant facts:
  - restricted-factor (E_2') correlations admit Hardy–Littlewood-type asymptotics for almost all shifts down to polylogarithmic (H);
  - general (E_2)-(E_2) correlations admit such asymptotics for almost all (|h|le H) when (Hge exp((log X)^{1-arepsilon})).
- Relevance: our (S=H_0^5), shift length (H_0=S^{1/5}) lies comfortably inside the general theorem's shift range.
- Critical limitation: an almost-all-shift asymptotic with logarithmic exceptional/error savings does not by itself imply the project’s normalized centered aggregate target (O(S)), which requires recovering a full polynomial factor (H_0^{-1}) from a raw (H_0S) scale.
- Audit verdict: `ACCEPT_FOR_E2_CORRELATION_COMPARISON_NOT_VARIANCE_CLOSURE`
- URL: https://doi.org/10.1017/S0305004122000251

## S032 — A. J. Irving (2014), Average Bounds for Kloosterman Sums Over Primes

- Type: `PRIMARY_RESEARCH`
- Role: prime Kloosterman-fraction estimate used by Guria after Poisson summation.
- Relevant bound:
  [
  sum_{qsim Q}left|sum_{substack{ple X\(p,q)=1}}e(aar p/q)ight|
  ll_arepsilon
  left(1+rac{a}{XQ}ight)^{1/2}
  left(Q^{1/2}X^{11/8}+Q^{7/6}X^{2/3}ight)(aQ)^arepsilon
  ]
  in the stated range (Q^{4/3}ge Xge Q^{1/2}).
- Audit verdict: `ACCEPT_FOR_PRIME_KLOOSTERMAN_FRACTION_BENCHMARK`
- URL: https://arxiv.org/abs/1301.6372

## S033 — Sandro Bettin & Vorrapan Chandee (2018), Trilinear forms with Kloosterman fractions

- Type: `PRIMARY_RESEARCH`
- Journal: Advances in Mathematics 328 (2018), 1234–1262
- DOI: 10.1016/j.aim.2018.01.026
- Role: arbitrary-coefficient trilinear Kloosterman-fraction benchmark and determinant-equation application.
- Critical audit use: supplies a permissive black-box benchmark after a hypothetical legal smoothing/Poisson step. It does not automatically handle two Möbius-weighted small variables and two prime variables simultaneously.
- Audit verdict: `ACCEPT_FOR_GENERIC_FRACTION_BENCHMARK_NOT_DIRECT_CLOSURE`

## S034 — Amos Nevo (2008), On matrices with (almost) prime entries, lattice points and ergodic theorems

- Type: `RESEARCH_WORKSHOP_NOTE`
- Role: severity guard for fixed-determinant all-prime (2	imes2) matrix problems.
- Reported status: infinitude of (2	imes2) prime-entry matrices of determinant 2 is posed as open; the note compares it with twin-prime-type difficulty.
- Critical audit use: if a proposed j=2 reduction silently demands a pointwise theorem for four prime entries at fixed determinant, classify that route as stronger than the intended averaged centered problem rather than treating it as routine.
- Limitation: workshop report, used only as a problem-status/severity guard, not as an analytic input theorem.
- Audit verdict: `ACCEPT_FOR_FOUR_PRIME_FIXED_DETERMINANT_SEVERITY_GUARD`


## S035 — Encyclopedia of Mathematics, Vaughan identity

- Type: `STANDARD_REFERENCE`
- Role: exact sign/support convention for the Vaughan decomposition used in the j=2 branch-coupling audit.
- Formula used: for n>v,
  [
  Lambda(n)
  =
  sum_{dr=n, dle u}mu(d)log r
  -
  sum_{kr=n, kle uv}a(k)
  -
  sum_{ek=n, e>v, k>u}Lambda(e)b(k),
  ]
  with
  [
  b(k)=sum_{dmid k, dle u}mu(d).
  ]
- Critical audit use: confirms that the Type-II term is the negative k>H tail of the same factorable convolution obtained from the first two branches.
- Audit verdict: `ACCEPT_FOR_EXACT_VAUGHAN_SIGN_AND_SUPPORT`
- URL: https://encyclopediaofmath.org/wiki/Vaughan_identity

## S036 — James Maynard, Primes in Arithmetic Progressions to Large Moduli II: Well-Factorable Estimates

- Type: `PRIMARY_RESEARCH`
- Journal: Memoirs of the American Mathematical Society
- DOI: 10.1090/memo/1543
- Role: comparison architecture for preserving factorability of sieve weights inside dispersion estimates rather than taking branchwise absolute values.
- Reported result: mean-value estimates for primes in arithmetic progressions to moduli up to x^(3/5-epsilon) with suitably well-factorable weights.
- Relevance here: motivates the current `J2_WELL_FACTORABLE_TAIL_DISPERSION_MAP` as an architecture comparison.
- Limitation: arithmetic-progression geometry and theorem hypotheses differ from the present reciprocal monomial phase; no black-box transfer is claimed.
- Audit verdict: `ACCEPT_FOR_WELL_FACTORABLE_DISPERSION_ARCHITECTURE_NOT_DIRECT_CLOSURE`


## S037 — Olivier Robert & Patrick Sargos (2006), Three-dimensional exponential sums with monomials

- Type: \`PRIMARY_RESEARCH\`
- Journal: Journal für die reine und angewandte Mathematik 591 (2006), 1–20
- DOI: 10.1515/CRELLE.2006.012
- Role: generic real three-dimensional monomial exponential-sum benchmark with arbitrary bounded coefficients.
- Main audit use: the theorem's functional class includes the reciprocal exponent pattern relevant to the j=2 sharp block after relabeling.
- Sharp-scale comparison used here:
  \[
  H_1=H^2,\quad M=N=H^3,\quad X=H^4.
  \]
  In the best direct permutation, the generic bound is of scale
  \[
  H^{27/4+\varepsilon}=H^{6+3/4+\varepsilon},
  \]
  while the j=2 target is \(H^{6+\varepsilon}\).
- Critical interpretation: the smooth phase itself has an H^6 three-dimensional stationary-phase benchmark; the H^(3/4) gap measures loss in a theorem robust to generic arithmetic coefficients, not insufficient phase curvature.
- Audit verdict: \`ACCEPT_FOR_GENERIC_3D_ARITHMETIC_COEFFICIENT_BENCHMARK_NOT_CLOSURE\`
- URL: https://doi.org/10.1515/CRELLE.2006.012

## Source-use rule

어떤 자료도 `권위 있는 출처`라는 이유만으로 모든 종류의 주장에 사용하지 않는다. 범위, 정리, 계산기록, 최신성, 데이터 완전성은 서로 다른 검증축으로 관리한다.
