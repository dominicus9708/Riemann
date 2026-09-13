# Data Policy

대규모 영점 원자료를 저장소에 무작정 복제하지 않는다. 목적은 용량 경쟁이 아니라 재현성·교차검증·감사 가능성이다.

## Stored directly in Git

- 소규모 고정밀 기준 데이터
- 알려진 실패 사례와 음성 대조군
- 통계 요약
- 외부 데이터의 manifest/provenance
- 생성·검증 스크립트

## Generated locally

- first 1,000 / 10,000 / 100,000 zero tables
- gap and normalized-gap tables
- Gram scans
- high-T sampled windows

생성 파일은 동일한 스크립트와 환경으로 재현 가능해야 하며, 중요한 분석 결과만 요약본으로 commit한다.

## External large datasets

LMFDB/Platt 등의 대규모 자료는 원본 전체를 Git에 복제하지 않고 다음 메타데이터를 기록한다.

- source and paper
- dataset version/date
- range
- numerical precision
- completeness method
- extraction subset
- checksum when locally downloaded
- script version used for parsing

## Baseline currently committed

- `baseline/first_50_zeros.csv`
- `baseline/gram_failures_0_299.csv`

## Planned expansion gates

1. first 1,000 zeros — high precision + external cross-check
2. first 10,000 zeros — distribution summary
3. first 100,000 zeros — main low-height pattern corpus
4. separated high-T windows — test whether low-height patterns persist
5. certified finite subset — interval/Turing-style completeness experiment

## Audit rule

`generated`, `externally sourced`, `rigorously certified` data must never share the same status label merely because their numerical values agree.
