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

## Source-use rule

어떤 자료도 `권위 있는 출처`라는 이유만으로 모든 종류의 주장에 사용하지 않는다. 범위, 정리, 계산기록, 최신성, 데이터 완전성은 서로 다른 검증축으로 관리한다.
