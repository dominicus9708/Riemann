# Möbius Hardy-Character Twist Barrier

## 목적

squarefree Boolean-group / Dirichlet-Hilbert bridge가 `L²`와 `Re(s)=1/2`를 자연스럽게 만든 뒤, 그 Hilbert/Hardy geometry 자체가 Möbius cancellation을 실제로 구별할 수 있는지 감사한다.

결론부터 말하면 **Haar/Hardy norm만으로는 Möbius 부호를 전혀 구별하지 못한다.**

---

## 1. positive squarefree polynomial과 Möbius polynomial

prime multi-index를 `alpha(n)`이라고 쓰자.

유한 cutoff `X`에 대해

\[
Q_X(z)
=
\sum_{\substack{n\le X\\\mu^2(n)=1}}z^{\alpha(n)}
\]

를 all-positive squarefree Bohr polynomial이라 하고

\[
P_X(z)
=
\sum_{n\le X}\mu(n)z^{\alpha(n)}
\]

를 Möbius polynomial이라 하자.

squarefree `n`에서는

\[
\mu(n)=(-1)^{\omega(n)}.
\]

따라서 모든 prime coordinate를 `-1` 회전시키면

\[
\boxed{
P_X(z_1,z_2,\ldots)
=
Q_X(-z_1,-z_2,\ldots).
}
\]

즉 Möbius 부호는 squarefree support 위의 **character twist / torus rotation**이다.

이 관점은 Hilberdink의 squarefree character group 및 Hedenmalm--Lindqvist--Seip의 character-twisted Dirichlet-series framework와 직접 연결된다.

---

## 2. 모든 Haar L^p norm이 동일하다

finite/infinite polytorus Haar measure를 `m`이라고 하자.

coordinatewise rotation

\[
R(z)=(-z_1,-z_2,\ldots)
\]

은 Haar measure preserving이다.

그러므로 모든 `0<p<infinity`에 대해

\[
\boxed{
\int|P_X(z)|^p\,dm(z)
=
\int|Q_X(z)|^p\,dm(z).
}
\]

즉

\[
\boxed{
\|P_X\|_{\mathscr H^p}
=
\|Q_X\|_{\mathscr H^p}.
}
\]

### 강한 감사결론

다음 종류의 정보는 Möbius와 all-positive squarefree coefficients를 구별하지 못한다.

- Haar `L²` energy,
- higher even moments,
- 일반 Haar `L^p` norm,
- character-torus global average,
- 그와 동치인 full vertical-limit norm.

따라서 이들만을 이용한 RH 증명 시도는 부호 cancellation의 핵심을 볼 수 없다.

---

## 3. vertical mean-square identity

유한 Dirichlet polynomial

\[
D_X(s)=\sum_{n\le X}\mu(n)n^{-s}
\]

에 대해 서로 다른 `log n` frequency의 직교성으로

\[
\boxed{
\lim_{T\to\infty}
\frac1{2T}\int_{-T}^T
|D_X(\sigma+it)|^2dt
=
\sum_{n\le X}\frac{\mu(n)^2}{n^{2\sigma}}.
}
\]

오른쪽은 Möbius **sign**을 완전히 잊고 squarefree support만 본다.

동일한 식은

\[
Q_X(s)=\sum_{n\le X}\mu(n)^2n^{-s}
\]

에도 성립하므로 두 polynomial의 vertical `L²` energy는 같다.

이것은 앞 절의 torus rotation invariance의 one-parameter vertical-flow 표현이다.

---

## 4. 1/2는 squarefree energy의 실제 critical exponent

squarefree Dirichlet identity

\[
\sum_{n\ge1}\frac{\mu(n)^2}{n^z}
=
\frac{\zeta(z)}{\zeta(2z)}
\]

에서

\[
E_X(\sigma)
=
\sum_{n\le X}\frac{\mu(n)^2}{n^{2\sigma}}
\]

를 생각하자.

### sigma > 1/2

\[
E_X(\sigma)
\to
\frac{\zeta(2\sigma)}{\zeta(4\sigma)}<\infty.
\]

### sigma = 1/2

squarefree density `6/pi²`에 의해

\[
\boxed{
E_X(1/2)
\sim
\frac6{\pi^2}\log X.
}
\]

### sigma < 1/2

partial summation으로

\[
E_X(\sigma)
\asymp
X^{1-2\sigma}
\]

규모가 된다.

따라서

\[
\boxed{
\sigma_c=1/2
}
\]

는 RH를 넣지 않고 **squarefree support의 Hilbert energy phase transition**으로 자연스럽게 나온다.

---

## 5. 이전 blind-spectrum 결과의 설명

이 저장소의 earlier blind Möbius shell spectrum에서는 empirical growth exponent가 `~1/2` 근처에 나타났지만, squarefree support에 random `±1` signs를 붙인 control에서도 같은 `~1/2`가 나타났다.

이번 identity는 그 이유를 설명한다.

`L²` growth에서는 sign이 사라지고 support density만 남으므로

\[
\text{actual Möbius}
\quad\text{and}\quad
\text{random squarefree signs}
\]

이 같은 square-root critical scaling을 보이는 것이 자연스럽다.

따라서

\[
\boxed{
1/2\text{ energy emergence는 RH evidence가 아니라 squarefree-Hilbert baseline이다.}
}
\]

---

## 6. pointwise에서는 차이가 극단적이다

all-one torus point에서

\[
Q_X(1,1,\ldots)
=
\sum_{n\le X}\mu(n)^2
=Q(X)
\sim\frac6{\pi^2}X.
\]

반면

\[
P_X(1,1,\ldots)
=
M(X).
\]

rotation identity로 쓰면

\[
\boxed{
M(X)
=
Q_X(-1,-1,\ldots).
}
\]

즉 같은 positive squarefree polynomial을

- `(+1,+1,...)`에서 평가하면 `~0.6079 X`,
- `(-1,-1,...)`에서 평가하면 Mertens cancellation

이 된다.

Haar average에서는 두 점의 차이를 볼 수 없지만 특정 boundary evaluation에서는 차이가 최대화된다.

### 핵심 재표현

\[
\boxed{
\text{RH의 어려움은 global Hilbert energy가 아니라
특정 arithmetic boundary phase에서의 pointwise discrepancy 제어다.}
}
\]

---

## 7. 왜 point evaluation에서 다시 1/2가 나타나는가

squarefree `ell²` Dirichlet-Hilbert space의 evaluation vector는

\[
z_p=p^{-s}.
\]

Bohr/polytorus 관점에서 bounded point evaluation을 위해 필요한 kernel norm은

\[
\prod_p(1+|p^{-s}|^2)
=
\prod_p(1+p^{-2\sigma})
=
\frac{\zeta(2\sigma)}{\zeta(4\sigma)}.
\]

이는 정확히

\[
\sigma>1/2
\]

에서 유한하다.

즉 `1/2`는

1. coefficient square-summability,
2. character/Haar Plancherel,
3. Dirichlet point evaluation

사이에서 반복해서 같은 functional-analytic boundary로 나온다.

그러나 boundary point itself는 generic `H²` norm으로 uniform하게 제어되지 않는다.

---

## 8. higher moment도 탈출구가 아니다

integer `k>=1`에 대해 vertical `2k`-moment를 전개하면 resonance condition은

\[
n_1\cdots n_k=m_1\cdots m_k.
\]

모든 index가 squarefree support에 있으면

\[
\prod_i\mu(n_i)\prod_j\mu(m_j)
=(-1)^{\sum_i\Omega(n_i)+\sum_j\Omega(m_j)}=1,
\]

왜냐하면 product equality 때문에 두 `Omega` 합이 같기 때문이다.

따라서 모든 even vertical moment 역시 sign pattern을 잃는다.

더 일반적으로 이는 앞의 torus-rotation norm invariance의 특수한 전개일 뿐이다.

---

## 9. 현재 장벽

### 닫힌 경로

\[
\text{canonical }L²
\to
\text{global energy/moments}
\to
RH
\]

는 현재 형태로는 닫는다.

이유: global Haar/Hardy norm은 Möbius twist와 positive squarefree polynomial을 정확히 같은 크기로 본다.

### 살아 있는 경로

필요한 것은 Haar symmetry를 **산술적으로 정당한 방식으로 깨는 observable**이다.

후보는 다음 조건을 만족해야 한다.

1. 특정 phase `(-1,-1,...)`를 RH를 알고 사후선택하지 않을 것.
2. finite cutoff `prod p^epsilon <= X`에서 그 phase가 formation parity로 canonical하게 선택됨을 사용할 것.
3. global norm이 아니라 boundary evaluation 또는 boundary flux를 제어할 것.
4. 제어과정이 `1/zeta`, known zero data, Nyman-Beurling criterion을 다시 가정하지 않을 것.

현재 formation phase scan에서 `theta=pi`가 blind minimum으로 나온 사실은 1--2와 관련되지만, random-sign / generic square-root baseline을 넘는 deterministic pointwise bound는 아직 없다.

---

## 선행기준

- T. Hilberdink (2014), *The Group of Squarefree Integers*, Linear Algebra Appl. 457, 383--399.
- H. Hedenmalm, P. Lindqvist, K. Seip (1997), *A Hilbert Space of Dirichlet Series and Systems of Dilated Functions in L²(0,1)*, Duke Math. J. 86, 1--37.
- Nyman--Beurling--Báez-Duarte literature listed in `00_scope/source_registry.md`.
