# Multiplicative formation data

이 디렉터리는 정수의 곱셈적 형성구조를 소수/합성수 이분법보다 세밀하게 기록하기 위한 실험 자료를 둔다.

## 현재 기준 범위

- 정수: `2 <= n <= 100`
- 요약표: `formation_summary_2_100.csv`
- 생성기: `scripts/compute_formation_structures.py`

## 재현

```bash
python scripts/compute_formation_structures.py
```

기본 실행은 다음 두 파일을 생성한다.

```text
data/formation/formation_summary_2_100.csv
data/formation/formation_detail_2_100.json
```

`formation_detail_2_100.json`은 모든 형성단어와 모든 비순서 이진 형성트리를 포함하는 파생 데이터이므로 현재 Git에는 중복 저장하지 않는다. 생성 규칙은 스크립트가 단일 기준이다.

기준 실행에서 얻은 SHA-256:

```text
formation_summary_2_100.csv
0aa0dc277bbbf09124d0916514abbec52e7d1011d8551e5c7266cf50ebda8e5f

formation_detail_2_100.json
22e7b73d8999f53d68bb104fcd48b00c99a74a1974924bd5c17f565efa756412
```

## 동치 규칙

### 1. 산술 기준

표준 소인수분해는 불변량 기준으로 유지한다.

예:

```text
12 = 2^2 * 3
```

### 2. 형성단어 `formation_word`

소인수를 순서대로 추출하는 경로를 보존한다.

`12`의 경우:

```text
(2, 2, 3)
(2, 3, 2)
(3, 2, 2)
```

같은 값의 수열은 한 번만 센다.

### 3. 비순서 형성트리 `unordered_factor_tree`

- 잎은 소수이다.
- 내부 노드는 두 자식의 곱이다.
- 좌우 자식 교환은 같은 것으로 본다.
- 괄호 구조가 다르면 다른 형성경로로 남긴다.

예를 들어 `12`에는 다음 두 구조가 남는다.

```text
((2*2)*3)
((2*3)*2)
```

### 4. 소수

소수는 비자명한 형성단어와 비자명한 형성트리를 `0`개로 기록한다. 이는 소수성을 재정의한 새로운 결과가 아니라 분석 기준이다.

## 요약 필드

- `omega`: 서로 다른 소인수 수 `ω(n)`
- `Omega`: 중복 포함 소인수 수 `Ω(n)`
- `tau`: 양의 약수 수 `τ(n)`
- `smallest_prime_factor`
- `largest_prime_factor`
- `nontrivial_factor_pair_count`
- `formation_word_count`
- `unordered_tree_count`
- `min_tree_depth`
- `max_tree_depth`

## 감사 원칙

형성단어의 순서나 트리의 괄호 구조는 표준 정수론에서 새로운 산술값을 만들지 않는다. 따라서 이 차이를 곧바로 새로운 수론적 불변량이라고 해석하지 않는다.

반대로 순서와 중간 결합정보를 너무 일찍 지우면 형성공리계/속성공리계에서 비교하려는 형성 경로 정보가 사라질 수 있으므로, 원시 형성자료와 산술 불변량을 병렬로 보존한다.
