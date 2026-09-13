# Notation Baseline

이 문서는 저장소 전체에서 사용하는 표기를 고정한다.

## Complex variable

\[
s=\sigma+it,\qquad \sigma=\operatorname{Re}(s),\quad t=\operatorname{Im}(s).
\]

비자명한 영점은

\[
\rho=\beta+i\gamma
\]

로 쓴다. 여기서 \(\beta=\operatorname{Re}(\rho)\), \(\gamma=\operatorname{Im}(\rho)\).

## Critical geometry

- critical strip: \(0<\sigma<1\)
- critical line: \(\sigma=1/2\)
- trivial zeros: \(-2,-4,-6,\ldots\)

## Main functions

\[
\zeta(s)=\sum_{n=1}^{\infty}n^{-s}\qquad (\sigma>1)
\]

이며 다른 영역에서는 해석적 연속으로 정의한다.

Riemann xi 함수는

\[
\xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma\!\left(\frac{s}{2}\right)\zeta(s).
\]

함수방정식은

\[
\xi(s)=\xi(1-s).
\]

임계선 계산에는

\[
Z(t)=e^{i\vartheta(t)}\zeta\!\left(\frac12+it\right)
\]

를 사용한다. 실수 \(t\)에서 \(Z(t)\)는 실수값을 가지며 임계선상의 제타 영점과 같은 영점을 갖는다.

## Counting and prime functions

- \(N(T)\): \(0<\gamma\le T\)인 비자명한 영점을 중복도까지 세는 표준 영점계수 함수
- \(\Lambda(n)\): von Mangoldt 함수
- \(\psi(x)=\sum_{n\le x}\Lambda(n)\)
- \(\pi(x)\): \(x\) 이하 소수의 개수

## Data notation

양의 허수부를 갖는 임계선 영점을 오름차순으로

\[
\rho_n=\frac12+i\gamma_n
\]

이라 기록할 때

\[
\Delta_n=\gamma_{n+1}-\gamma_n
\]

을 raw gap으로 사용한다.

평균 밀도를 제거한 간격은 계산 단계에서 정의식을 명시하고 `normalized_gap`으로 저장한다. 서로 다른 정규화 관례를 혼용하지 않는다.

## Audit rule

표기가 같은 두 식이라도 정의역, 가지(branch), 극한방식, 영점 중복도 처리 방식이 다르면 같은 객체로 취급하지 않는다.
