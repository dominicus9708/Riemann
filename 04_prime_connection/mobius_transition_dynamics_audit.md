# Möbius Additive-Transition Dynamics Audit

## 목적

prime-channel activation dynamics

\[
U_p=I-T_p
\]

는 서로 commute하므로 activation order 자체가 새 정보를 만들지 않는다.

따라서 실제로 순서가 중요한 방향으로 정수축 전이

\[
n\longrightarrow n+h
\]

를 검사한다.

이 단계의 목표는 shifted Möbius correlation에서 간단한 결정론적 전이법칙이 나타나는지 확인하는 것이다.

---

## 1. support 전이의 정확한 제약

소수 `p`가 `n`과 `n+h`를 동시에 나누면

\[
p\mid h.
\]

따라서

\[
\operatorname{supp}(n)\cap\operatorname{supp}(n+h)
\subseteq\operatorname{supp}(h).
\]

특히 `h=1`이면

\[
\gcd(n,n+1)=1
\]

이므로 두 정수의 prime-channel support는 완전히 disjoint하다.

이 점에서 additive transition은 한 정수 내부의 commuting multiplicative channel dynamics와 성격이 다르다.

---

## 2. shifted correlation

\[
C_X(h)
=
\sum_{n\le X-h}\mu(n)\mu(n+h)
\]

를 계산한다.

`X=2^20=1,048,576`에서 `h=1`:

\[
C_X(1)=605.
\]

두 항이 모두 nonzero인 squarefree pair의 수는

\[
338,299
\]

이므로 conditional mean은

\[
\frac{605}{338,299}
\approx1.788\times10^{-3}
\]

이고 random-sign square-root scale로 표준화하면

\[
\frac{605}{\sqrt{338,299}}
\approx1.0402.
\]

따라서 현재 범위에서 adjacent transition은 뚜렷한 저차 상관을 보이지 않는다.

---

## 3. h=1 transition table

zero state를 제외한 sign transition count는

```text
(+,+) = 84,820
(+,-) = 84,392
(-,+) = 84,455
(-,-) = 84,632
```

정도이며 독립성 chi-square 진단값은 약

\[
1.08
\]

이다.

따라서 `n -> n+1`의 prime support가 완전히 교체됨에도 Möbius sign transition에서는 단순한 deterministic bias가 나타나지 않는다.

---

## 4. shift 1..64 scan

`1<=h<=64`를 동일하게 계산했다.

전체 결과:

```text
data/mertens/mobius_shift_correlations_2pow20_h64.csv
```

가장 큰 standardized absolute deviation은

\[
h=60,
\qquad
C_X(60)=-1898,
\qquad
|z|\approx2.6645.
\]

64개의 shift를 동시에 검사한다는 점을 고려하면 이것은 독립 Gaussian heuristic의 최대편차 규모

\[
\sqrt{2\log64}\approx2.88
\]

보다도 작다.

이 비교는 엄밀한 p-value가 아니라 multiple-testing scale audit이다.

### 판정

현재 범위에서 특정 작은 shift가 예외적으로 강한 Möbius correlation을 가진다는 증거는 없다.

---

## 5. dyadic h=1 stability

`X=2^10,...,2^20`에서 `C_X(1)/sqrt(support)`는

```text
-0.549, -0.351, +0.467, -0.175, +0.027,
-0.622, -0.928, -1.634, -1.730, -0.221, +1.040
```

정도로 움직인다.

즉 한 방향으로 수렴하는 고정된 adjacent bias는 관찰되지 않는다.

전체 자료:

```text
data/mertens/mobius_adjacent_correlation_dyadic_20.csv
```

---

## 6. Chowla barrier

고정된 서로 다른 shift들에 대한

\[
\sum_{n\le X}
\mu(n+h_1)\cdots\mu(n+h_k)
=o(X)
\]

형태의 명제는 Chowla conjecture 계열이다.

특히 two-point unweighted fixed-shift correlation을 충분히 강하게 제어하는 것은 고전적으로 깊은 문제다.

Tao의 logarithmically averaged two-point Chowla theorem 등 중요한 부분결과가 있으나, 현재 필요한 uniform ordinary-sum bound를 자동으로 제공하지 않는다.

따라서 additive dynamics가 Euler product로 즉시 대각화되지 않는다는 장점은 있지만, 난점이 사라지는 것이 아니라 **Möbius correlation/parity problem**으로 이동한다.

---

## 7. M(X)와 모든 shift correlation의 정확한 관계

\[
M(X)=\sum_{n\le X}\mu(n)
\]

이므로

\[
\boxed{
M(X)^2
=
\sum_{n\le X}\mu(n)^2
+2\sum_{h=1}^{X-1}
\sum_{n\le X-h}\mu(n)\mu(n+h)
}
\]

이다.

즉

\[
M(X)^2=Q(X)+2\sum_{h=1}^{X-1}C_X(h),
\]

여기서 `Q(X)`는 squarefree count이다.

따라서 RH-scale

\[
M(X)=O_\varepsilon(X^{1/2+\varepsilon})
\]

은 전체 shifted-correlation mass에 매우 강한 aggregate cancellation이 있다는 명제와 연결된다.

그러나 fixed small `h` 몇 개의 작은 상관만으로는 이를 닫을 수 없다.

van der Corput / differencing을 이용하면 finite range의 averaged correlation으로 `M(X)`를 제어할 수 있지만, 필요한 uniform signed cancellation이 바로 핵심 난점이다.

---

## 8. 동역학적 판정

### 양성

1. `n -> n+h`는 prime-channel support를 실제로 재구성하므로 multiplicative activation보다 진짜 ordered dynamics에 가깝다.
2. `h=1`에서 support가 완전히 disjoint하다는 강한 구조가 있다.
3. all-shifts identity는 `M(X)`를 transition correlations의 총합과 정확히 연결한다.

### 음성

1. `h<=64`, `X<=2^20`에서 간단한 저차 correlation signal이 없다.
2. 이를 엄밀하게 밀면 Chowla/Elliott-type 난점으로 들어간다.
3. 따라서 현재 형태의 additive dynamics는 RH 문제를 단순화했다고 볼 수 없다.

### 결론

additive transition dynamics는 **보조 감사축**으로 유지하되 주 증명 후보에서는 내린다.

다음 주 후보는 shifted correlation이 아니라 prime-activation trajectory의

\[
\boxed{
\text{late-stage compensation}
}
\]

이다.

구체적으로

\[
F_{\sqrt X}(X)
\]

라는 큰 intermediate state가 `p>sqrt(X)` prime tail에 의해 거의 정확히 제거되어 최종 `M(X)`가 되는 finite-scale relation을 분석한다.

이 관계가 단순 Alladi/Buchstab/Heath-Brown identity의 재표현인지 먼저 감사한 뒤, 남는 finite-boundary residual만 후보로 유지한다.
