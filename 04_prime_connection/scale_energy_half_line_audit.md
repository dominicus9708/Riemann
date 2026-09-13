# Scale-Energy and the Emergence of Re(s)=1/2

## 목적

prime-channel dynamics에서 `1/2`를 사전에 넣지 않았는데도 scale normalization 자체에서 `Re(s)=1/2`가 나올 수 있는지 감사한다.

이 결과가 산술적으로 특별한지, 아니면 함수공간을 `L^2`로 선택한 일반적 결과인지 구분한다.

---

## 1. dilation의 L^r scaling

연속 scale dilation을

\[
(T_af)(x)=f(x/a),
\qquad a>1
\]

라고 하자.

Lebesgue counting measure `dx`에 대해

\[
\|T_af\|_{L^r(dx)}^r
=
\int_0^\infty|f(x/a)|^r\,dx
=
a\|f\|_r^r.
\]

따라서

\[
\boxed{
\|T_af\|_r=a^{1/r}\|f\|_r
}
\]

이고 normalized dilation

\[
\boxed{
D_{a,r}=a^{-1/r}T_a
}
\]

는 scale-isometry이다.

---

## 2. Mellin mode

Mellin character를

\[
f_s(x)=x^{-s}
\]

라고 두면

\[
T_af_s=a^s f_s.
\]

따라서 normalized dilation은

\[
D_{a,r}f_s
=a^{s-1/r}f_s.
\]

고유값의 modulus가 1이 되는 선은

\[
\boxed{
\Re s=\frac1r
}
\]

이다.

특히 quadratic/Hilbert energy를 사용하면 `r=2`이므로

\[
\boxed{
\Re s=\frac12
}
\]

가 사전입력 없이 나온다.

---

## 3. discrete prime-channel operator와의 관계

정수 scale profile에서

\[
(T_pf)(x)=f(\lfloor x/p\rfloor)
\]

을 사용하면 boundary effect를 제외하고 각 작은-scale 값이 대략 `p`번 복제되므로

\[
\|T_pf\|_2^2
\approx
p\|f\|_2^2.
\]

따라서

\[
p^{-1/2}T_p
\]

가 discrete counting-measure에서 자연스러운 approximate isometry이다.

이것은 prime-channel dynamics에서 `1/2`가 Hilbert normalization exponent로 나타나는 정확한 이유를 준다.

---

## 4. 그러나 이것은 RH 신호가 아니다

동일 계산을 `L^1`에서 하면

\[
\Re s=1,
\]

`L^4`에서 하면

\[
\Re s=1/4
\]

이 나온다.

따라서

\[
\boxed{
1/2\text{는 arithmetic data만이 아니라 quadratic norm 선택에 의해 결정된다.}
}
\]

즉 `L^2`를 선택한 이유가 별도로 정당화되지 않으면 `1/2`의 출현을 RH 증거로 세면 안 된다.

`L^2`는 inner product, orthogonality, Plancherel, self-adjoint spectral theory를 사용할 수 있다는 점에서 특별하지만 이것은 함수해석적 특별성이지 곧바로 zeta-zero의 특별성이 아니다.

---

## 5. Nyman-Beurling 교차검증

이 방향은 고전적인 Nyman-Beurling 접근과 직접 겹친다.

Nyman-Beurling criterion은 RH를 특정 dilation-generated 함수들의 `L^2` closure 문제로 표현한다.

관련 연구에서는 Mellin transform이 `L^2(0,1)`을

\[
\Re s>1/2
\]

의 Hardy space로 unitary하게 옮기는 구조를 명시적으로 사용한다.

Báez-Duarte의 strong criterion도 integer dilations와 `L^2` closure를 이용하여 RH와 동치인 근사문제로 만든다.

따라서

\[
\text{scale dynamics}
\to L^2
\to \Re s=1/2
\]

경로 자체는 새로운 증명전략이라고 볼 수 없다.

---

## 6. 감사 판정

### 의미 있는 점

1. `1/2`가 왜 scale/Hilbert dynamics에서 자연스러운지 독립적으로 설명한다.
2. `1/2`를 숫자로 직접 넣지 않고 normalization exponent로 회복할 수 있다.
3. prime-channel operator의 dilation 성격과 functional-analytic RH approaches 사이의 정확한 다리를 제공한다.

### 제한

1. `L^r` 선택에 따라 `1/r`로 움직인다.
2. `L^2`를 선택하는 순간 Nyman-Beurling/Hardy-space 계열과 강하게 겹친다.
3. 따라서 이 `1/2` 출현을 독립 RH 증거로 계산하지 않는다.

### 결론

\[
\boxed{
\Re s=1/2\text{의 scale-energy 출현은 설명적 가치가 있으나 증명적 독립성은 없다.}
}
\]

현재 새 경로가 되려면 `L^2`를 사전 선택하지 않아도 **정수 형성동역학 자체가 quadratic energy를 유일하게 강제**하거나, Nyman-Beurling과 다른 finite-boundary inequality를 제공해야 한다.
