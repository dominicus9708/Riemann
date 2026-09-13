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

## Supplement rule

이 supplement의 source도 본 registry와 동일하게 역할별로만 사용한다. 특히 random-model theorem, computational identity, equivalent criterion을 RH의 무조건적 증명으로 승격하지 않는다.
