# Formation Hilbert Bridge Audit

## 목적

현재 형성경로에서 `1/2`가 나타나는 이유를 두 단계로 분리한다.

1. squarefree prime-channel 구조가 왜 자연스럽게 `L^2`/Hilbert geometry를 갖는가?
2. 그 `L^2`가 Nyman–Beurling의 scale-space `L^2` 및 `Re(s)=1/2`와 비순환적으로 연결되는가?

핵심 원칙은 `RH가 1/2이므로 L^2를 선택`하지 않는 것이다.

---

## 1. finite squarefree Boolean group

첫 `m`개 prime을

\[
p_1<\cdots<p_m
\]

이라 하고

\[
P_m=\prod_{j=1}^m p_j
\]

라 하자.

squarefree divisor 집합

\[
G_m=D(P_m)
\]

은

\[
a\circ b=\frac{\operatorname{lcm}(a,b)}{\gcd(a,b)}
\]

아래

\[
\boxed{G_m\cong(\mathbb Z/2\mathbb Z)^m}
\]

인 finite abelian Boolean group이다.

이 구조와 Möbius가 character라는 사실은 Hilberdink (2014)의 직접적인 선행결과와 겹친다. 따라서 group observation 자체를 신규 정리로 주장하지 않는다.

bit vector

\[
\epsilon=(\epsilon_1,\ldots,\epsilon_m)\in\{0,1\}^m
\]

에

\[
d(\epsilon)=\prod_jp_j^{\epsilon_j}
\]

를 대응시키면 Möbius character는

\[
\boxed{
\chi_\mu(\epsilon)=(-1)^{\epsilon_1+\cdots+\epsilon_m}=\mu(d(\epsilon)).
}
\]

---

## 2. arithmetic cutoff는 weighted Boolean halfspace

cutoff `X`에 대해

\[
f_{X,m}(d)=\mathbf1_{d\le X}
\]

를 둔다.

bit coordinates에서는

\[
\boxed{
f_{X,m}(\epsilon)
=
\mathbf1_{\sum_j(\log p_j)\epsilon_j\le\log X}.
}
\]

즉 형성 cutoff는 임의 Boolean set이 아니라 positive weights `log p_j`를 가진 **weighted linear threshold / Boolean halfspace**이다.

prime-activation state는 정확히 Möbius character의 raw Fourier coefficient다.

\[
\boxed{
F_{p_m}(X)
=
\sum_{\substack{d\mid P_m\\d\le X}}\mu(d)
=
\sum_{d\in G_m}f_{X,m}(d)\chi_\mu(d).
}
\]

normalized Haar Fourier convention

\[
\widehat f(\chi)
=
2^{-m}\sum_{d\in G_m}f(d)\overline{\chi(d)}
\]

에서는

\[
F_{p_m}(X)=2^m\widehat f_{X,m}(\chi_\mu).
\]

따라서 `Möbius formation cancellation`을 finite Boolean Fourier coefficient로 정확히 재표현할 수 있다.

---

## 3. exact-zero primorial regime는 Haar 직교성

만약

\[
P_m\le X
\]

이면 모든 divisor `d|P_m`가 `d<=X`이므로

\[
f_{X,m}\equiv1.
\]

Möbius는 nonprincipal character이므로 Haar orthogonality에 의해

\[
\boxed{
F_{p_m}(X)=0.
}
\]

이것은 이전 prime-activation dynamics에서 관찰한

> primorial이 cutoff를 넘기 전에는 top-level state가 정확히 zero

라는 현상의 group-theoretic 설명이다.

`X=2^20`에서는

\[
2\cdot3\cdot5\cdot7\cdot11\cdot13\cdot17=510510<X,
\]

따라서 `p_m=17`까지 `F=0`이다.

다음 prime `19`에서 primorial이 `9,699,690>X`가 되고 boundary가 처음 group을 절단하면서

\[
F_{19}(X)=2
\]

가 된다.

---

## 4. 왜 L²가 자연스러운가

finite group에는 normalized Haar inner product

\[
\langle f,g\rangle
=
2^{-m}\sum_{d\in G_m}f(d)\overline{g(d)}
\]

가 canonical하게 존재한다.

characters는 이 inner product에서 orthonormal basis를 이룬다.

따라서

\[
\sum_{\chi\in\widehat G_m}|\widehat f(\chi)|^2
=
\|f\|_2^2
\]

이라는 Parseval/Plancherel identity가 성립한다.

이 점에서 `L^2`는 RH의 critical line을 맞추기 위해 외부에서 삽입한 것이 아니라

\[
\boxed{
\text{squarefree channel group}
\to
\text{characters}
\to
\text{Haar orthogonality}
\to
L^2
}
\]

로 내부에서 자연스럽게 생긴다.

다만 `L^p` spaces 자체도 정의할 수 있으므로, **L²가 논리적으로 유일하게 가능한 norm**이라는 뜻은 아니다.

L²가 특별한 이유는 Fourier transform이 같은 exponent의 공간으로 돌아오는 self-dual Plancherel geometry를 갖고, character spectrum을 정확한 orthogonal energy decomposition으로 만드는 점이다.

---

## 5. 첫 번째 장벽: channel Haar L² ≠ scale Lebesgue L²

map

\[
\ell(d)=\log d
\]

로 finite Haar measure를 real log-scale에 push forward하면

\[
\ell
=
\sum_{j=1}^m\epsilon_j\log p_j,
\qquad
\epsilon_j\sim\operatorname{Bernoulli}(1/2)
\]

의 분포가 된다.

평균과 분산은

\[
\mathbb E\ell
=
\frac12\sum_{p\le p_m}\log p,
\]

\[
\operatorname{Var}(\ell)
=
\frac14\sum_{p\le p_m}(\log p)^2.
\]

따라서 이것은 Lebesgue measure `dt`나 multiplicative Haar measure `dx/x`가 아니다. large `m`에서는 weighted Bernoulli-sum central-limit geometry가 나타난다.

### 판정

\[
\boxed{
L^2(G_m,\text{Haar})
\not\equiv
L^2(0,1,dx)
}
\]

을 단순 변수변환으로 주장할 수 없다.

따라서 Nyman–Beurling `L²`를 바로 얻었다고 말하면 안 된다.

---

## 6. 두 번째 다리: Dirichlet coefficient Hilbert space

squarefree support를 가진 Dirichlet series

\[
D_a(s)
=
\sum_{\mu^2(n)=1}a_n n^{-s}
\]

에 대해 coefficient norm

\[
\|a\|_2^2
=
\sum_{\mu^2(n)=1}|a_n|^2
\]

을 둔다.

Cauchy–Schwarz로 `sigma=Re(s)`일 때

\[
|D_a(s)|
\le
\|a\|_2
\left(
\sum_{\mu^2(n)=1}n^{-2\sigma}
\right)^{1/2}.
\]

squarefree Dirichlet series identity

\[
\sum_{\mu^2(n)=1}n^{-z}
=
\frac{\zeta(z)}{\zeta(2z)}
\]

를 쓰면

\[
\boxed{
|D_a(s)|
\le
\|a\|_2
\left(
\frac{\zeta(2\sigma)}{\zeta(4\sigma)}
\right)^{1/2},
\qquad \sigma>\frac12.
}
\]

따라서 squarefree `ell²` coefficient Hilbert space의 generic bounded point-evaluation half-plane은

\[
\boxed{\operatorname{Re}s>1/2}.
\]

이 `1/2`는 RH나 zero location을 넣지 않고 coefficient-counting/Plancherel geometry에서 발생한다.

### 매우 중요한 구분

이것은

> zeta의 nontrivial zeros가 Re(s)=1/2 위에 있다

는 명제가 아니다.

단지

> square-summable Dirichlet coefficient space의 natural point-evaluation boundary가 1/2이다

라는 별개의 functional-analytic 사실이다.

---

## 7. 강한 선행교차: Hedenmalm–Lindqvist–Seip

Hedenmalm, Lindqvist & Seip (Duke Math. J. 86, 1997)은

\[
\mathscr H^2
=
\left\{\sum_na_nn^{-s}:\sum_n|a_n|^2<\infty\right\}
\]

를 systematic하게 연구하고, 이를

- infinite-dimensional polydisc/polytorus의 Hardy `H²`,
- multiplicative character space,
- `L²(0,1)`의 dilated-function systems

와 직접 연결했다.

따라서

\[
\ell^2\text{ coefficients}
\to
\text{Dirichlet }H^2
\to
L^2\text{ dilation}
\]

이라는 bridge 자체는 선행연구에 존재한다.

우리 formation route가 새로울 수 있는 지점은 이 bridge의 존재가 아니라

1. squarefree Boolean subgroup,
2. Möbius parity character,
3. arithmetic threshold `d<=X`,
4. finite prime-activation dynamics

을 한꺼번에 놓았을 때 **어떤 추가 finite-boundary inequality가 생기는가**뿐이다.

---

## 8. Parseval만으로는 턱없이 약하다

`N_{X,m}`을 허용상태 수

\[
N_{X,m}=\#\{d\mid P_m:d\le X\}
\]

라 하자.

`f`가 indicator이므로

\[
\|f\|_2^2=N_{X,m}/2^m.
\]

Parseval에서 한 coefficient에 대한 generic bound는

\[
|\widehat f(\chi_\mu)|
\le
\sqrt{N_{X,m}/2^m},
\]

따라서 raw Möbius coefficient에는

\[
\boxed{
|F_{p_m}(X)|
\le
\sqrt{2^mN_{X,m}}.
}
\]

`X=2^20`, `m=20`, `p_m=71`에서

\[
N_{X,m}=9444,
\qquad
F_{p_m}(X)=-34.
\]

Parseval ratio

\[
\frac{|F|}{\sqrt{2^mN}}
\approx3.42\times10^{-4}
\]

이다.

즉 실제 cancellation은 generic Hilbert bound보다 훨씬 강하다.

최종 `m=pi(X)`로 가면 group size `2^m` 자체가 막대하므로 generic Parseval bound는 더 쓸모없어진다.

### 판정

canonical `L²`의 존재는 `왜 quadratic geometry인가`를 설명하지만

\[
M(X)=O_\varepsilon(X^{1/2+\varepsilon})
\]

을 자동으로 주지 않는다.

---

## 9. full Boolean Fourier spectrum 진단

`X=2^20`, `m=20`의 weighted halfspace 전체 Walsh spectrum을 직접 계산했다.

raw top-degree parity coefficient는

\[
\widehat f_{\rm raw}([20])=-34.
\]

전체 Fourier energy에서 이 coefficient 하나가 차지하는 비율은

\[
\boxed{1.17\times10^{-7}}
\]

정도이다.

반면 degree 1--4의 energy mass가 매우 크다.

이것은 top parity coefficient가 작은 방향임을 보여주지만, **일반 halfspace Fourier theory도 high-degree suppression을 연구하므로 prime-specific law라고 해석하지 않는다.**

실제로 weights `log p_j`를 양의 random perturbation으로 바꾸고 허용상태 수를 같게 맞춘 단순 null에서도 top parity coefficient의 소형화가 흔히 재현된다.

따라서 `high-degree Fourier coefficient가 작다` 자체는 RH 증거가 아니다.

---

## 10. finite-difference 동일성

log cutoff를 `L=log X`, weights를 `w_j=log p_j`라 쓰면

\[
F_m(L)
=
\sum_{\epsilon\in\{0,1\}^m}
(-1)^{|\epsilon|}
\mathbf1_{\sum_jw_j\epsilon_j\le L}.
\]

Heaviside function `H(L)=1_{L>=0}`에 shift operator

\[
(\tau_wH)(L)=H(L-w)
\]

를 두면

\[
\boxed{
F_m(L)
=
\prod_{j=1}^m(I-\tau_{w_j})H(L).
}
\]

즉

- Boolean top parity Fourier coefficient,
- prime-channel activation dynamics,
- commuting finite-difference operators

는 같은 객체의 세 표현이다.

Laplace/Mellin mode에서 multiplier는 다시

\[
\prod_{j=1}^m(1-p_j^{-s}).
\]

따라서 이 표현만 spectral continuation하면 다시 partial `1/zeta(s)`로 순환한다.

---

## 11. Nyman–Beurling과의 현재 거리

Nyman–Beurling–Báez-Duarte 계열은

\[
\zeta(s)\ne0\ \text{for }\Re s>1/p
\]

와 특정 fractional-part dilation span의 `L^p` closure를 연결한다.

`p=2`가 RH critical half-plane과 맞는다.

현재 formation route에서는

\[
\text{squarefree Boolean group}
\to
\text{Haar-Plancherel }L^2
\to
\text{Dirichlet coefficient }\mathscr H^2
\to
\Re s>1/2
\]

까지는 RH를 넣지 않고 설명할 수 있다.

하지만

\[
\boxed{
\text{이 Hilbert boundary가 왜 }1/\zeta(s)\text{의 모든 nontrivial singular geometry를 강제하는가}
}
\]

는 아직 전혀 증명되지 않았다.

이 마지막 화살표를 기존 NB criterion이나 zeta-zero 정보를 사용해 채우면 순환이다.

---

## 12. 현재 판정

### 확인된 양성결과

1. squarefree prime-channel 상태공간은 canonical Boolean group이며 Möbius는 parity character다.
2. prime-activation sum은 arithmetic threshold indicator의 exact parity Fourier coefficient다.
3. primorial exact-zero 구간은 Haar character orthogonality로 설명된다.
4. `L²`는 channel Fourier/Plancherel geometry에서 RH와 독립적으로 자연스럽게 등장한다.
5. squarefree Dirichlet `ell²` point-evaluation boundary도 정확히 `Re(s)=1/2`다.
6. Hedenmalm–Lindqvist–Seip 이론이 coefficient `H²`와 actual dilation `L²` 사이의 강한 선행 bridge를 제공한다.

### 닫힌/경고 경로

1. `L²가 나왔다 -> RH`는 성립하지 않는다.
2. channel Haar measure를 log scale로 단순 push-forward해서 Nyman `L²`를 얻을 수 없다.
3. Parseval/Cauchy-Schwarz generic bound는 Mertens cancellation에 지나치게 약하다.
4. full spectrum의 top-degree suppression은 generic Boolean halfspace 현상일 수 있다.
5. finite-difference spectrum을 무한화하면 다시 Euler product / `1/zeta`로 돌아간다.

### 남은 핵심 질문

\[
\boxed{
\text{arithmetic weighted halfspace boundary가
Möbius parity character와 가지는 추가 구조가
일반 halfspace보다 강한 deterministic cancellation을 강제하는가?}
}
\]

그리고 그 구조가 있다면

- `1/zeta` analytic continuation,
- known zeta zeros,
- Nyman–Beurling closure criterion

을 다시 가정하지 않고 증명되어야 한다.

---

## 재현자료

```text
scripts/audit_formation_hilbert_bridge.py
data/formation/boolean_hilbert_bridge_2pow20.csv
data/formation/boolean_halfspace_fourier_degree_2pow20_m20.csv
```

---

## 선행문헌

- B. Nyman (1950), *On the One-Dimensional Translation Group and Semi-Group in Certain Function Spaces*.
- A. Beurling (1955), *A Closure Problem Related to the Riemann Zeta-Function*, PNAS 41, 312–314.
- L. Báez-Duarte (1999), *A Class of Invariant Unitary Operators*, Adv. Math. 144, 1–12, DOI 10.1006/aima.1998.1801.
- L. Báez-Duarte (2002), *New Versions of the Nyman-Beurling Criterion for the Riemann Hypothesis*, IJMMS 31, 387–406, DOI 10.1155/S0161171202013248.
- L. Báez-Duarte (2003), *A Strengthening of the Nyman-Beurling Criterion for the Riemann Hypothesis*, Rend. Lincei 14, 5–11.
- L. Báez-Duarte, M. Balazard, B. Landreau, E. Saias (2000), *Notes sur la fonction zeta de Riemann, 3*, Adv. Math. 149, 130–144, DOI 10.1006/aima.1999.1861.
- J.-F. Burnol (2002), *A Lower Bound in an Approximation Problem Involving the Zeros of the Riemann Zeta Function*, Adv. Math. 170, 56–70, DOI 10.1006/aima.2001.2066.
- T. Hilberdink (2014), *The Group of Squarefree Integers*, Linear Algebra Appl. 457, 383–399, DOI 10.1016/j.laa.2014.05.037.
- H. Hedenmalm, P. Lindqvist, K. Seip (1997), *A Hilbert Space of Dirichlet Series and Systems of Dilated Functions in L²(0,1)*, Duke Math. J. 86, 1–37, DOI 10.1215/S0012-7094-97-08601-4.
