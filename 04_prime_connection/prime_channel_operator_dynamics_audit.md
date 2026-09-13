# Prime-Channel Operator Dynamics Audit

## 목적

정적 formation descriptor가 prime-factor order statistics / smooth-number theory로 상당 부분 환원된 뒤, 사용자가 허용한 동역학 관점을 실제 수학적 상태전이로 도입한다.

목표는 임의의 물리적 시간이나 `c_info`를 붙이는 것이 아니라, prime channel이 하나씩 활성화될 때 Möbius formation state가 어떻게 변하는지를 정확한 연산자로 기술하고 이 동역학이 RH 난점을 단순화하는지 감사하는 것이다.

---

## 1. 정적 canonical path와 선행구조

squarefree

\[
n=p_1p_2\cdots p_k,
\qquad
p_1<\cdots<p_k
\]

에 대해

\[
a_j(n)=\frac{\log p_j}{\log n},
\qquad
\sum_ja_j=1
\]

을 두면 canonical cumulative path

\[
0\to a_1\to a_1+a_2\to\cdots\to1
\]

을 얻는다.

그러나 정렬된 `log p_j / log n` 벡터 자체는 고전적인 prime-factor order statistics와 직접 연결된다. random integer의 ordered log-prime-factor vector는 Poisson-Dirichlet law로 수렴하는 것이 알려져 있고, largest-prime/smoothness 방향은 Dickman/Buchstab 이론으로 깊게 연구되어 있다.

따라서 단순한

- largest step,
- smallest step,
- cumulative-path imbalance,
- log-prime gap,
- entropy/roughness

만으로 새 RH 경로를 주장하지 않는다.

주요 선행기준:

- Donnelly & Grimmett, *On the Asymptotic Distribution of Large Prime Factors*, JLMS 1993.
- Billingsley / Poisson-Dirichlet prime-factor law 계열.
- Dickman-de Bruijn smooth-number theory.
- Buchstab rough-number theory.

---

## 2. 정확한 prime-channel 동역학

함수 `f(x)`에 대해 dilation operator를

\[
(T_pf)(x)=f(\lfloor x/p\rfloor)
\]

라고 두고 prime-channel activation operator를

\[
\boxed{U_p=I-T_p}
\]

로 정의한다.

초기 상태를

\[
F_0(x)=1\qquad(x\ge1)
\]

로 두고 primes `p<=y`를 활성화하면

\[
\boxed{
F_y(x)
=\sum_{\substack{n\le x\\n\mid\prod_{p\le y}p}}\mu(n)
=\sum_{\substack{n\le x\\n\ \mathrm{squarefree}\\P^+(n)\le y}}\mu(n)
}
\]

이 정확히 성립한다.

prime `p`를 추가할 때

\[
\boxed{
F_p(x)=F_{p^-}(x)-F_{p^-}(\lfloor x/p\rfloor)
}
\]

이다.

따라서 이 단계의 `dynamics`는 비유가 아니라 정확한 finite-state transport/update law이다.

---

## 3. 동역학은 가환적이다

\[
T_pT_q=T_{pq}=T_qT_p
\]

이므로

\[
\boxed{U_pU_q=U_qU_p}.
\]

따라서 prime channel의 활성화 순서를 바꿔도 최종상태는 같다.

이것은 중요한 음성결과다.

형성단어 `(2,3,2)`와 `(3,2,2)`처럼 순서를 보존하는 별도 descriptor는 만들 수 있지만, **Möbius prime-channel operator 자체에는 비가환 holonomy나 path dependence가 없다.**

따라서 activation order 자체를 새 동역학 정보라고 해석하면 안 된다.

---

## 4. Mellin 모드에서의 완전 대각화

형식적으로 power mode

\[
f_s(x)=x^s
\]

를 보면

\[
T_pf_s=p^{-s}f_s
\]

이므로

\[
\boxed{
U_pf_s=(1-p^{-s})f_s.
}
\]

따라서 `p<=y` 전체 channel dynamics의 spectral multiplier는

\[
\boxed{
\prod_{p\le y}(1-p^{-s}).
}
\]

`y->infinity`, `Re(s)>1`에서는 바로

\[
\frac1{\zeta(s)}
\]

이다.

### 판정

translation/scale-invariant linear dynamics를 Mellin/Fourier 방식으로 분석하면 정확히 기존 Euler product로 대각화된다.

따라서 이 선형 dynamics의 spectrum만으로 `Re(s)=1/2`를 다시 도출하면

\[
\text{prime-channel dynamics}
\to1/\zeta(s)
\to\text{RH}
\]

라는 순환 가능성이 높다.

---

## 5. exact-zero 구간과 hidden profile

`P(y)=prod_{p<=y}p`를 primorial이라고 하자.

만약

\[
P(y)\le X
\]

이면 `P(y)`의 모든 squarefree divisor가 `<=X`에 포함되므로

\[
\boxed{
F_y(X)=\sum_{d\mid P(y)}\mu(d)=0
}
\]

이다.

예를 들어

\[
X=2^{20}=1,048,576
\]

에서

\[
2\cdot3\cdot5\cdot7\cdot11\cdot13\cdot17
=510,510<X
\]

이므로 `p=17`까지 top-level state는 정확히 zero이다.

그 다음 prime `19`를 넣으면

\[
F_{19}(X)
=-F_{17}(\lfloor X/19\rfloor)
=2.
\]

즉 `F_y(X)=0`이라는 scalar 값만으로는 상태가 소멸한 것이 아니다. smaller-scale profile

\[
x'\mapsto F_y(x')
\]

가 hidden state로 남아 다음 scale update를 결정한다.

따라서 top-level scalar만 추적하면 dynamics는 Markov-closed가 아니다. 완전상태는 scale profile 전체이다.

---

## 6. 중간상태 amplification

`X=2^10,...,2^20`에서 activation trajectory를 전수계산했다.

대표적으로 `X=2^20`:

\[
M(X)=257,
\]

하지만

\[
\max_y|F_y(X)|=38,892.
\]

관측 최대점은 `y≈X/3` 부근이었다.

더 중요한 것은 최대점 여부와 무관한 정확한 관계다.

`p>X/2`인 prime은 해당 scale에서 singleton `p`만 새로 만들므로 각 prime의 increment는 `-1`이다. 따라서

\[
\boxed{
F_{X/2}(X)
=M(X)+\pi(X)-\pi(X/2).
}
\]

`X=2^20`에서는

\[
\pi(X)-\pi(X/2)=38,635
\]

이므로

\[
F_{X/2}(X)=257+38,635=38,892.
\]

한편

\[
\sqrt X=1,024.
\]

따라서 실제 dynamics는 RH-scale보다 훨씬 큰 intermediate excursion을 거친 뒤 최종 `M(X)`으로 재상쇄된다.

### 결과

\[
\boxed{
\text{모든 intermediate state를 }O(X^{1/2+\varepsilon})\text{로 제어하는 방식은 불가능하다.}
}
\]

필요한 것은 trajectory stability가 아니라 **late-stage signed compensation**이다.

이 결과는 앞서 발견한 `(X/2,X]` large-prime singleton matching barrier와 같은 구조를 dynamics에서 다시 확인한 것이다.

전체 수치는

```text
data/formation/prime_channel_operator_dynamics_dyadic_20.csv
```

에 기록한다.

---

## 7. canonical largest-prime formation tree

각 squarefree `n>1`에 대해

\[
\operatorname{par}(n)=\frac{n}{P^+(n)}
\]

을 부모로 둔다.

그러면 prime factors를 increasing order로 추가하는 canonical formation tree가 생기며 각 노드는 부모를 정확히 하나 갖는다.

`X` 이하의 induced tree에서 node `m`의 relative alternating subtree residual을

\[
R_X(m)
=\sum_{d:\,md\le X\atop P^-(d)>P^+(m)}\mu(d)
\]

라고 두면

\[
\boxed{
R_X(m)=1-\sum_{c\in\mathrm{child}(m)}R_X(c)
}
\]

이고 root에서는

\[
\boxed{R_X(1)=M(X)}.
\]

여기서 `P^-(1)=infinity` convention을 쓴다.

---

## 8. tree residual의 문헌 교차검증

위 residual은 새로운 산술함수가 아니다.

\[
R_X(m)
=
\sum_{\substack{d\le X/m\\P^-(d)>P^+(m)}}\mu(d)
\]

이므로 **Möbius function restricted to rough integers**의 summatory function이다.

Krishnaswami Alladi는 1982년 JNT 논문 *Asymptotic estimates of sums involving the Moebius function*에서

\[
M(x,y)=\sum_{n\le x,\,p(n)>y}\mu(n)
\]

(`p(n)` = smallest prime factor)을 직접 연구했다. largest-prime restricted Möbius sums도 후속 논문에서 연구되었다.

따라서 canonical tree language는 계산/감사에는 유용하지만 object 자체를 새 것으로 주장하지 않는다.

---

## 9. remaining-depth 변수

node `m`에서

\[
u(m;X)
=\frac{\log(X/m)}{\log P^+(m)}
\]

를 정의하면, 앞으로 추가할 수 있는 prime-channel 수의 거친 상한을 준다.

- `u<1`: child가 없으므로 `R=1`.
- `1<=u<2`: 추가 prime은 많아야 하나이므로
  \[
  R=1-\{\pi(X/m)-\pi(P^+(m))\}.
  \]
- `2<=u<3`: prime-pair descendants까지 들어간다.
- 더 큰 `u`: higher formation layers가 순차적으로 열린다.

이는 signed Buchstab/inclusion-exclusion cascade에 해당한다.

`X=2^20`에서 internal non-root node를 `floor(u)`별로 집계한 결과는

```text
data/formation/canonical_tree_residual_summary_2pow20.csv
```

에 기록한다.

---

## 10. 이번 dynamics 감사의 판정

### 확인된 양성 구조

1. prime activation은 정확한 linear transport operator로 표현된다.
2. scalar zero 뒤에도 scale-profile memory가 남는다는 hidden-state 구조가 명확하다.
3. canonical largest-prime tree는 unique-parent dynamics를 제공한다.
4. final Mertens cancellation이 매우 큰 intermediate mass를 상쇄한 결과임을 정량화할 수 있다.

### 닫힌 단순경로

1. activation order 자체: operators commute하므로 추가 path information 없음.
2. Mellin spectral dynamics: exact partial `1/zeta`로 환원.
3. uniform small-state/stability proof: `F_{X/2}(X)`가 이미 `X/log X` scale로 큼.
4. largest-prime tree residual 자체: Alladi의 rough Möbius sums와 기존 sieve/Buchstab 구조로 연결.

---

## 11. 다음에 남는 비순환 후보

현재 dynamics가 새 RH 경로가 되려면 linear commuting operator 자체가 아니라 다음 중 하나가 필요하다.

1. **late-stage compensation law**
   - 큰 `X/log X` intermediate excursion이 왜 final `M(X)`에서 강하게 제거되는지,
   - known zeta-zero data를 입력하지 않고 유한 scale relation으로 제어.

2. **non-translation-invariant energy / correlation**
   - Mellin mode에서 단순 `1/zeta`로 대각화되지 않는 canonical finite-boundary quantity,
   - arbitrary centering이나 `1/2` 사전입력 금지.

3. **cross-scale profile constraint**
   - `F_y(X)` 한 점이 아니라 `F_y(x')` 전체 profile 사이의 deterministic relation,
   - standard rough/smooth Möbius estimate로 이미 알려진 부분을 제거한 residual만 사용.

4. **ordered/hierarchical data beyond counts**
   - squarefree에서 `|W|=k!`, `|T|=(2k-3)!!`처럼 `omega`로 환원되는 개수는 제외,
   - 실제 prime labels와 partial products를 쓰되 Poisson-Dirichlet/Buchstab statistics로 환원되는지 먼저 감사.

현재 단계에서는 1번 `late-stage compensation`의 finite-scale 구조를 가장 우선한다.
