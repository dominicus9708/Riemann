# Late-Stage Prime-Tail Compensation Audit

## 목적

prime-channel activation dynamics에서 `p>sqrt(X)` 구간이 큰 intermediate state를 최종 Mertens 값으로 되돌리는 late-stage compensation을 분석한다.

핵심 질문은 다음이다.

> 이 큰 보상이 RH 수준의 새로운 구조인가, 아니면 `s=1`의 prime-number-theorem 구조와 기존 largest-prime decomposition으로 이미 설명되는가?

---

## 1. 정확한 sqrt(X) 분해

\[
F_y(X)
=
\sum_{\substack{n\le X\\n\ \mathrm{squarefree}\\P^+(n)\le y}}
\mu(n)
\]

라고 하자.

`p>sqrt(X)`인 prime을 largest prime factor로 갖는 squarefree `n`은 유일하게

\[
n=pm,
\qquad
m\le X/p<\sqrt X<p
\]

로 쓰인다.

따라서 largest-prime restriction이 remainder `m`에서는 자동으로 사라지고

\[
\boxed{
M(X)
=
F_{\sqrt X}(X)
-
\sum_{\sqrt X<p\le X}
M\!\left(\left\lfloor\frac Xp\right\rfloor\right)
}
\]

이 정확히 성립한다.

prime-tail을

\[
T_X
=
\sum_{\sqrt X<p\le X}
M(\lfloor X/p\rfloor)
\]

라고 쓰면

\[
M(X)=F_{\sqrt X}(X)-T_X.
\]

이 항등식 자체에서 `F_sqrt`와 `T_X`의 높은 상관을 새로운 증거로 세면 안 된다. 둘의 차이가 정의상 `M(X)`이기 때문이다.

---

## 2. quotient kernel

\[
q=\left\lfloor\frac Xp\right\rfloor
\]

로 prime들을 묶으면 `q<sqrt(X)`이고

\[
T_X
=
\sum_{q<\sqrt X}w_X(q)M(q),
\]

여기서

\[
\boxed{
w_X(q)
=
\pi(X/q)-\pi(X/(q+1))
}
\]

이다 (`q<sqrt X` 범위에서는 해당 interval이 자동으로 `p>sqrt X`에 놓인다).

따라서 late-stage dynamics는 작은 scale의 Mertens profile을 prime-interval count kernel로 다시 조합하는 exact finite-scale operator이다.

---

## 3. Li/PNT common-mode kernel

exact `w_X(q)`를 prime number theorem의 continuous density로 바꾼 audit baseline을

\[
K_X
=
\sum_{q<\sqrt X}
M(q)
\left[
\operatorname{Li}(X/q)
-
\operatorname{Li}(X/(q+1))
\right]
\]

로 둔다.

이것은 증명 정의가 아니라 **known smooth prime-density component를 제거하기 위한 감사 기준**이다.

변수변환 `t=X/u`를 쓰면

\[
\operatorname{Li}(X/q)-\operatorname{Li}(X/(q+1))
=
X\int_q^{q+1}
\frac{du}{u^2(\log X-\log u)}.
\]

`q<sqrt X`에서는

\[
\frac{\log u}{\log X}<\frac12
\]

이므로 geometric expansion이 자연스럽다.

\[
K_X
=
\frac X{\log X}
\sum_{r\ge0}
\frac{B_r(\sqrt X)}{(\log X)^r},
\]

\[
B_r(Q)
=
\sum_{q<Q}
M(q)
\int_q^{q+1}
\frac{(\log u)^r}{u^2}\,du.
\]

---

## 4. 첫 smooth moment는 정확히 PNT cancellation

`r=0`에서는

\[
\int_q^{q+1}\frac{du}{u^2}
=
\frac1q-rac1{q+1}
=
\frac1{q(q+1)}.
\]

따라서 finite `Q`에서 정확히

\[
\boxed{
B_0(Q)
=
\sum_{q<Q}\frac{M(q)}{q(q+1)}
=
\sum_{n<Q}\frac{\mu(n)}n
-
\frac{M(Q-1)}Q
}
\]

이다.

`Q->infinity`에서

\[
\sum_{n\le Q}\frac{\mu(n)}n\to0
\]

은 prime number theorem과 같은 수준의 Möbius cancellation이다.

즉 naive하게 예상되는

\[
X/\log X
\]

크기의 common mode가 사라지는 첫 이유는 RH가 아니라 **PNT-level cancellation at s=1**이다.

---

## 5. 다음 moment와 s=1 expansion

일반적으로

\[
A_r(x)
=
\int_x^\infty\frac{(\log u)^r}{u^2}\,du
=
\frac{r!}{x}
\sum_{j=0}^r\frac{(\log x)^j}{j!}
\]

이면

\[
B_r(Q)
=
\sum_{n<Q}\mu(n)A_r(n)
-M(Q-1)A_r(Q).
\]

무한범위의 formal/asymptotic coefficient들은

\[
\frac1{\zeta(s)}
=(s-1)-\gamma(s-1)^2+\cdots
\]

의 `s=1` Taylor data에 의해 정해진다.

첫 두 nonzero coefficient는

\[
B_0(\infty)=0,
\qquad
B_1(\infty)=-1,
\]

\[
B_2(\infty)=-2(1+\gamma).
\]

따라서 smooth tail의 처음 두 비자명 항은

\[
\boxed{
K_X
\approx
-rac{X}{\log^2X}
-rac{2(1+\gamma)X}{\log^3X}
+\cdots
}
\]

이다.

여기서 `gamma`는 Euler-Mascheroni constant이다.

중요: 이 전개는 **critical line data가 아니라 zeta의 pole `s=1` 주변 데이터**이다.

---

## 6. 수치 감사

`X=2^10,...,2^20`의 exact data를

```text
data/mertens/late_stage_compensation_dyadic_20.csv
```

에 기록했다.

대표적으로

\[
X=2^{20}=1,048,576
\]

에서

\[
M(X)=257,
\]

\[
F_{\sqrt X}(X)=-6605,
\qquad
T_X=-6862.
\]

따라서 두 큰 항의 차이만

\[
257
\]

남는다.

Li/PNT kernel은

\[
K_X\approx-6746.20.
\]

그리고 `s=1` 첫 항만 쓰면

\[
-rac X{\log^2X}
\approx-5456.18,
\]

두 번째 moment까지 포함하면

\[
-rac X{\log^2X}
-rac{2(1+\gamma)X}{\log^3X}
\approx-6697.71.
\]

exact prime-tail `-6862`와 비교하면 두 moment만으로 이미 거대한 late-stage mass의 대부분을 설명한다.

---

## 7. 해석

이번 dynamics에서 보였던 현상을 세 층으로 나누면:

### A. `X/log X` 후보 주성분

\[
B_0\to0
\]

때문에 제거된다.

이는

\[
\sum\mu(n)/n\to0
\]

이라는 PNT-level structure이다.

### B. 실제 dominant smooth tail

첫 nonzero term은 대략

\[
-X/\log^2X
\]

이고 다음 correction들도 `s=1` Taylor/Stieltjes data에서 나온다.

### C. 최종 residual mismatch

실제 `M(X)`는

\[
M(X)
=
[F_{\sqrt X}(X)-K_X]
-
[T_X-K_X]
\]

로 쓸 수 있다.

단, 같은 `K_X`를 양쪽에서 뺀 이 식 자체는 항등식이므로 residual의 작음만 보고 새 구조라 주장하면 안 된다.

RH 수준의 난점은 결국 두 finite-boundary error 사이의 signed mismatch를 균일하게 제어하는 데 남는다.

---

## 8. 기존 연구와의 관계

largest/smallest prime factor로 Möbius sum을 분해하는 방법은 Alladi의 duality 및 largest-prime-factor Möbius sum 문헌과 직접 연결된다.

또 `M(N^d)`를 작은 Möbius 값들의 multilinear form으로 압축하는 Huxley-Watt identity도 같은 hyperbola/decomposition 계열의 강한 선행기준이다.

Hildebrand는 greatest-prime-factor 제한을 둔 multiplicative-function sums를 uniform하게 연구했다.

따라서 sqrt split 자체를 새 정리로 주장하지 않는다.

---

## 9. 현재 판정

### 양성

- dynamics의 late-stage mass를 exact quotient kernel로 압축했다.
- `X/log X` 규모가 왜 사라지는지 finite Abel-summation identity로 분해했다.
- 실제 dominant common mode가 `s=1`, 즉 PNT/pole structure라는 것을 수치와 식 모두에서 확인했다.

### 음성

- large intermediate compensation 자체는 RH 특유 신호가 아니다.
- smooth main hierarchy는 `s=1` 데이터에서 이미 나온다.
- residual을 zeta-zero explicit formula로 분석하면 다시 RH/zero structure로 순환할 가능성이 높다.
- triangle inequality로 tail을 항별 제어하면 `X/log X` 수준 손실이 돌아온다.

### 결론

\[
\boxed{
\text{late-stage compensation의 큰 부분은 PNT common mode이고, RH 난점은 그보다 작은 residual mismatch에 남는다.}
}
\]

따라서 이 dynamics도 그 자체로 간단한 증명은 아니다.

다음 후보는 `K_X` 같은 smooth baseline을 사전에 선택하지 않고도 finite-boundary residual의 **구조적 에너지/직교성**을 제어할 수 있는지를 보는 것이다.
