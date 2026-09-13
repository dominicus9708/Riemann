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
- Role: 자명/비자명 영점, 임계띠, 대칭, Z(t) 정의
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

## Source-use rule

어떤 자료도 `권위 있는 출처`라는 이유만으로 모든 종류의 주장에 사용하지 않는다. 범위, 정리, 계산기록, 최신성, 데이터 완전성은 서로 다른 검증축으로 관리한다.
