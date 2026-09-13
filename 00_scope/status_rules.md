# Evidence and Audit Status Rules

외부 문헌, 계산, 새 식, 증명 시도는 아래 상태를 명시한다.

## 1. Mathematical status

- `THEOREM_ESTABLISHED`: 표준 문헌에서 무조건적으로 확립된 정리
- `THEOREM_CONDITIONAL`: 명시된 가정 아래에서만 성립
- `EQUIVALENT_TO_RH`: RH와 논리적으로 동치
- `NECESSARY_FOR_RH`: RH의 필요조건
- `SUFFICIENT_FOR_RH`: RH의 충분조건
- `NUMERICAL_RIGOROUS`: 엄밀한 오차/완전성 검증을 포함한 유한 계산 결과
- `NUMERICAL_EXPERIMENTAL`: 수치 실험이나 패턴 관찰
- `HEURISTIC`: 증명되지 않은 모델/직관
- `CONJECTURE`: 미증명 명제
- `CLAIM_UNVERIFIED`: 검토 전 주장
- `REFUTED_OR_INVALID`: 반례 또는 논리 오류가 확인된 주장

## 2. Source status

- `PRIMARY_HISTORICAL`: 원 논문/역사 자료
- `PRIMARY_RESEARCH`: 연구 논문
- `STANDARD_REFERENCE`: 교과서·DLMF 등 표준 참고문헌
- `OFFICIAL_PROBLEM_SOURCE`: CMI 등 공식 문제 정의
- `COMPUTATIONAL_DATASET`: 계산 데이터셋
- `RECENT_PREPRINT`: 최신 프리프린트; 검증 상태 별도 표기

## 3. Audit dimensions

각 자료에 대해 최소한 다음을 기록한다.

1. `claim`: 무엇을 실제로 주장하는가
2. `assumptions`: 숨은 가정 포함 전제
3. `domain`: 식과 정리의 정확한 정의역
4. `dependency`: 어떤 정리/계산에 의존하는가
5. `proof_scope`: 전체/부분/비율/유한범위 중 무엇인가
6. `numerical_scope`: 계산 범위, 정밀도, 오차 경계
7. `freshness`: 최신 현황 인용에 사용 가능한가
8. `independence`: RH 또는 RH 동치명제를 전제로 하는가
9. `failure_modes`: 오용 시 발생 가능한 오류
10. `reproducibility`: 제3자가 재현 가능한가

## 4. Hard rejection tests

다음 중 하나라도 해당하면 RH 증명 단계로 승격하지 않는다.

- 유한한 수치 검증을 `모든 영점`으로 일반화
- 함수방정식의 대칭성을 `모든 영점이 대칭축 위`라는 결론으로 오인
- RH를 전제로 한 정리나 RH 동치명제를 무증명 전제로 사용
- Dirichlet 급수의 수렴영역을 벗어나 같은 급수를 그대로 사용
- 무한합·적분·미분·극한 순서 교환을 조건 없이 수행
- 모든 영점이 단순영점임을 무증명으로 가정
- big-O 또는 점근식을 정확한 항등식처럼 사용
- 수치 오차/영점 누락 검증 없이 그래프나 근사값을 증명으로 사용

## 5. Literature freshness rule

하나의 자료가 모든 종류의 주장에 동일한 권위를 갖는다고 간주하지 않는다.

예: DLMF의 제타함수 정의와 함수방정식은 표준 공식의 강한 기준이지만, 오래된 문구가 포함된 계산 현황 설명은 2026년 현재의 `최신 검증 범위` 근거로 사용하지 않는다.

## 6. Promotion rule

새 결과는

`CLAIM_UNVERIFIED → NUMERICAL_EXPERIMENTAL/HEURISTIC → lemma candidate → independently checked lemma → theorem candidate`

순으로 관리한다. 단계 상승은 증거가 추가될 때만 허용하며, 실패한 시도도 삭제보다 감사 기록으로 남긴다.
