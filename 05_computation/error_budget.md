# Numerical Error and Certification Budget

수치 결과를 `패턴 관찰`, `회귀검사`, `엄밀한 유한범위 검증`으로 혼동하지 않기 위한 오차 예산이다.

## 1. Error classes

### E1 — Arithmetic rounding
유한 정밀도 실수/복소수 연산의 반올림 오차.

Required metadata:
- working precision
- output precision
- rounding/interval mode if available

### E2 — Function-evaluation error
`zeta(s)`, `Z(t)`, `theta(t)`, Gamma 등 특수함수 평가 알고리즘의 근사/절단 오차.

A small residual `abs(zeta(rho))` is evidence that a point is near a numerical root, but is not by itself a certified root enclosure.

### E3 — Root-location error
근 찾기 알고리즘이 반환한 근의 위치 오차.

Required distinction:
- approximate root
- bracketed root
- interval-certified unique root

### E4 — Sampling miss
`Z(t)`를 이산 샘플링할 때 샘플 사이의 영점을 놓치는 오류.

Sign changes alone cannot certify completeness; even-multiplicity zeros may not change sign.

### E5 — Global completeness error
임계선에서 찾은 근의 목록이 임계띠 전체의 모든 영점을 포함한다고 잘못 가정하는 오류.

Mitigation requires an independent zero count, e.g. argument-principle/Turing-type machinery.

### E6 — Indexing error
`nth critical-line zero`와 `nth nontrivial zero in the strip`를 동일시하는 오류.

This is especially relevant to APIs such as Wolfram `ZetaZero[k]`, documented as enumerating zeros on the critical line.

### E7 — Asymptotic remainder error
Riemann–Siegel, Riemann–von Mangoldt, explicit formula 등에서 `O(...)` 또는 절단항을 실제 유한 오차상계처럼 사용하는 오류.

A big-O expression is not a usable certified bound until its constant/range are explicit enough for the calculation.

### E8 — Cancellation / loss of significance
큰 항들의 차나 진동합에서 유효자릿수가 손실될 수 있다.

Required response:
- increase working precision;
- compare independent formulations;
- use interval/enclosure arithmetic for certification.

### E9 — Summation-order error
조건수렴 또는 대칭 극한이 필요한 영점 합을 임의 순서의 유한합으로 해석하는 오류.

The explicit formula's zero sum must carry its prescribed limiting convention.

### E10 — Data provenance / parsing error
외부 테이블의 정확도, 색인, 부호, 정규화, 버전, 파서가 잘못 연결되는 오류.

Required metadata:
- source URL/publication
- stated precision
- index convention
- extracted range
- checksum when raw file is locally retained

## 2. Evidence classes

### Class A — exploratory
보통의 부동소수점/다중정밀도 계산. 패턴 탐색과 구현 회귀에 사용.

### Class B — independently cross-checked
서로 다른 구현/외부 데이터가 허용 오차 내에서 일치. 구현 오류 가능성을 낮추지만 수학적 완전성을 자동 보장하지 않음.

### Class C — locally interval-certified
개별 함수값/근이 rigorous enclosure 안에 존재함을 보증.

### Class D — range-complete certification
interval-certified root isolation + independent total zero count를 결합하여 특정 유한 높이까지 누락이 없음을 보증.

### Class E — global proof
유한 계산 상한을 제거하는 수학적 논증. Class D를 아무리 높여도 자동으로 Class E가 되지 않는다.

## 3. Current repository status

- first 50 zeros: Class A
- first 1,000 direct run + Odlyzko/Wolfram sample comparison: Class B
- Gram-law failure fixtures: Class A/B pattern audit fixtures
- Platt 2017 / Platt–Trudgian 2021 external results: externally sourced Class D claims, accepted through peer-reviewed primary literature
- repository's own Class C/D implementation: not yet implemented

## 4. Certification gate

어떤 계산 결과를 `NUMERICAL_RIGOROUS`로 자체 승격하려면 최소한 다음이 필요하다.

1. interval/enclosure arithmetic;
2. each candidate root has a rigorous bracket/enclosure;
3. uniqueness or multiplicity handling is explicit;
4. total zero count in the strip is independently bounded/countable;
5. count agrees with certified critical-line roots;
6. all endpoint conventions are fixed;
7. code/version/precision metadata are reproducible.

## 5. Literature audit

Platt (2017) and Platt & Trudgian (2021) are used as examples of the distinction between ordinary high-precision computation and finite-range rigorous verification. We do not infer that reproducing their output values with ordinary floating point reproduces their proof-level guarantees.
