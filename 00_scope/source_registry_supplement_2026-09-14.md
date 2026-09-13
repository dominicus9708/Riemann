# Audited Source Registry — Supplement 2026-09-14

`00_scope/source_registry.md`의 S024 이후 추가된 선행문헌을 임시 누적한다. 이후 정기 정리 시 본 registry에 병합한다.

## S025 — Harald Andrés Helfgott & Lola Thompson (2023), Summing μ(n): a Faster Elementary Algorithm

- Type: `PRIMARY_RESEARCH`
- Journal: Research in Number Theory 9 (2023), article 6
- DOI: 10.1007/s40993-022-00408-8
- Role: Mertens function `M(x)` 계산을 위한 현대 elementary algorithm 및 Möbius용 Heath–Brown identity의 직접 사용.
- Critical audit use: formation/complement recursion을 multi-factor decomposition으로 확장하면 기존 Vaughan/Heath–Brown 계열과 겹치는지 판별하는 기준.
- Reported complexity: elementary computation of `M(x)` with exponent `x^(3/5)` up to logarithmic factors.
- Audit limitation: 계산 알고리즘 개선이며 RH square-root bound 증명이 아님.
- Audit verdict: `ACCEPT_FOR_MERTENS_DECOMPOSITION_AND_ALGORITHM_CONTEXT`

## S026 — Andrew Granville & K. Soundararajan (2003), Decay of Mean Values of Multiplicative Functions

- Type: `PRIMARY_RESEARCH`
- Journal: Canadian Journal of Mathematics 55(6), 1191–1230
- DOI: 10.4153/CJM-2003-047-0
- Role: Halász mean-value theorem을 multiplicative function과 `n^{it}` 사이의 prime-weighted distance로 정량화.
- Main audit object:
  `D(f,n^{it};x)^2 = sum_{p<=x} (1-Re(f(p)p^{-it}))/p`.
- Critical audit use: prime-by-prime character mismatch alone가 설명할 수 있는 cancellation scale의 한계 측정.
- Audit verdict: `ACCEPT_FOR_PRETENTIOUS_MEAN_VALUE_BASELINE`

## S027 — Andrew Granville & K. Soundararajan (2008), Pretentious Multiplicative Functions and an Inequality for the Zeta-Function

- Type: `PRIMARY_RESEARCH/EXPOSITORY_RESEARCH`
- In: Anatomy of Integers, CRM Proceedings & Lecture Notes 46 (2008), 179–189
- Role: multiplicative functions의 `pretentious distance`를 체계화하고 zeta-function 및 고전 수론 결과를 같은 언어로 재해석.
- Critical audit use: Möbius all-minus prime character가 어떤 simpler model을 흉내내는지/흉내내지 않는지 formation-character 관점과 비교.
- Audit verdict: `ACCEPT_FOR_PRETENTIOUS_FRAMEWORK`

## S028 — Granville, Harper & Soundararajan (2019), A New Proof of Halász’s Theorem, and Its Consequences

- Type: `PRIMARY_RESEARCH`
- Journal: Compositio Mathematica 155(1), 126–163
- DOI: 10.1112/S0010437X18007522
- Role: Halász theorem의 유연한 현대적 증명과 quantitative consequences.
- Critical audit use: nonpretentiousness가 mean cancellation을 주지만 일반 theorem이 square-root RH scale을 자동으로 주지는 않는다는 기준.
- Audit verdict: `ACCEPT_FOR_MODERN_HALASZ_REFERENCE`

## S029 — Adam J. Harper (2020), Moments of Random Multiplicative Functions, I

- Type: `PRIMARY_RESEARCH`
- Journal: Forum of Mathematics, Pi 8 (2020), e1
- DOI: 10.1017/fmp.2019.7
- Role: Rademacher/Steinhaus random multiplicative sums의 low moments와 critical multiplicative chaos.
- Main result used in audit: first absolute moment is of order `sqrt(x)/(log log x)^(1/4)`.
- Critical audit use: character RMS `sqrt(Q(x))`를 typical absolute size와 혼동하지 않기 위한 random baseline.
- Audit verdict: `ACCEPT_FOR_RANDOM_CHARACTER_LOW_MOMENT_BASELINE`

## S030 — Adam J. Harper (2023), Almost Sure Large Fluctuations of Random Multiplicative Functions

- Type: `PRIMARY_RESEARCH`
- Journal: International Mathematics Research Notices 2023(3), 2095–2138
- DOI: 10.1093/imrn/rnab299
- Role: Rademacher/Steinhaus random multiplicative sums가 almost surely `sqrt(x)`보다 큰 fluctuation을 무한히 자주 보임을 증명.
- Critical audit use: random multiplicative model을 deterministic Möbius proof로 직접 이전할 수 없음을 강화.
- Audit verdict: `ACCEPT_FOR_RANDOM_CHARACTER_LARGE_FLUCTUATION_BASELINE`

## S031 — Florian K. Richter (2021), A New Elementary Proof of the Prime Number Theorem

- Type: `PRIMARY_RESEARCH`
- Journal: Bulletin of the London Mathematical Society 53 (2021), 1365–1375
- DOI: 10.1112/blms.12503
- Role: `Omega(n)`의 additive shift-invariance를 이용해 PNT를 도출하는 새로운 elementary proof.
- Main structural result used in audit: bounded `g`에 대해 평균적으로 `g(Omega(n)+1)`과 `g(Omega(n))`의 차이가 사라지는 shift-invariance.
- Critical audit use: weighted-prime Boolean threshold의 parity decorrelation이 PNT 수준에서 기존 연구와 연결됨을 확인.
- Audit limitation: RH 수준 `M(x)=O_epsilon(x^(1/2+epsilon))` 정량상계를 주는 논문은 아님.
- Audit verdict: `ACCEPT_FOR_PNT_PARITY_DECORRELATION_CONTEXT`

## S032 — Yuval Peres, Noise Stability of Weighted Majority

- Type: `PRIMARY_RESEARCH`
- Preprint: arXiv:math/0412377; later published as a book chapter.
- Role: arbitrary weighted majority/halfspace의 noise sensitivity를 `O(sqrt(epsilon))` 수준으로 제어.
- Critical audit use: 일반 Boolean-halfspace Fourier tail/noise bounds가 arithmetic rare-event threshold의 RH-scale top parity coefficient를 자동으로 제어하지 못함을 비교하는 기준.
- Audit verdict: `ACCEPT_FOR_GENERIC_WEIGHTED_MAJORITY_NOISE_BOUND`

## S033 — Diakonikolas, Jaiswal, Servedio, Tan & Wan (2012), On the Distribution of the Fourier Spectrum of Halfspaces

- Type: `PRIMARY_RESEARCH`
- Preprint: arXiv:1202.6680
- Role: Boolean halfspace의 Fourier spectrum이 저차/특정 구조에 집중되는 정량결과를 연구.
- Critical audit use: 일반 halfspace spectral concentration과 arithmetic weighted-halfspace endpoint parity coefficient를 구별하는 기준.
- Audit limitation: `log p` weights와 threshold `log X`의 극희박 영역에서 RH square-root cancellation을 함의하지 않음.
- Audit verdict: `ACCEPT_FOR_GENERIC_HALFSPACE_FOURIER_BASELINE`

## S034 — Gil Kalai (2020), Expository Commentary on Richter's PNT Proof

- Type: `EXPOSITORY_COMMENTARY`
- Role: weights `log p_j`와 threshold `log X`인 weighted-majority Boolean function에서 최고차 parity Fourier coefficient를 PNT와 연결하는 해설적 관점을 명시.
- Critical audit use: `2^m fhat([m])=M(X)` 및 density 대비 top-coefficient decorrelation이라는 표현이 선행 해설에 이미 존재함을 확인.
- Limitation: primary theorem source가 아니므로 Richter의 원논문 및 표준 PNT/Mertens 동치와 함께만 사용.
- Audit verdict: `ACCEPT_AS_COMMENTARY_NOT_PRIMARY_EVIDENCE`

## Supplement rule

이 supplement의 source도 본 registry와 동일하게 역할별로만 사용한다. 특히 random-model theorem, computational identity, equivalent criterion을 RH의 무조건적 증명으로 승격하지 않는다.
