# Formation Symmetry Selection Audit

## 목적

현재까지 서로 따로 발견된

- Möbius phase `theta=pi`,
- Hilbert exponent `p=2`,
- Dirichlet point-evaluation boundary `Re(s)=1/2`

가 RH 목표를 사전에 넣지 않고 formation structure 내부에서 어느 정도까지 **canonical하게 선택되는지** 정리한다.

이 문서는 RH 증명을 주장하지 않는다. 목표는 선택의 비임의성을 감사하는 것이다.

---

## 1. binary prime channels

squarefree formation state는 prime-channel activation vector

\[
\epsilon=(\epsilon_1,\ldots,\epsilon_m),
\qquad
\epsilon_j\in\{0,1\}
\]

로 표현된다.

symmetric-difference composition 아래

\[
G_m\cong(\mathbb Z/2\mathbb Z)^m.
\]

각 generator `e_j`는 involution이다.

\[
e_j+e_j=0.
\]

이 Boolean group 자체와 Möbius가 character라는 사실은 Hilberdink (2014)의 선행구조와 겹친다.

---

## 2. equal-channel phase family 중 genuine character는 두 개뿐

formation phase scan에서 사용한 equal-channel weight를

\[
a_\theta(\epsilon)
=e^{i\theta|\epsilon|}
\]

라고 하자.

이것이 `G_m`의 group character가 되려면 generator involution을 보존해야 한다.

\[
\chi(e_j)^2=\chi(0)=1.
\]

모든 channel에 같은 phase를 부여했으므로

\[
\chi(e_j)=e^{i\theta}
\]

이고

\[
e^{2i\theta}=1.
\]

따라서

\[
\boxed{
\theta\equiv0\ \text{or}\ \pi\pmod{2\pi}.
}
\]

### theta=0

\[
\chi_0(\epsilon)=1
\]

trivial character다.

### theta=pi

\[
\chi_\pi(\epsilon)=(-1)^{|\epsilon|}.
\]

squarefree integer `n`에서는

\[
\boxed{
\chi_\pi(n)=(-1)^{\omega(n)}=\mu(n).
}
\]

따라서 earlier continuous phase scan에서 `theta=pi`가 예외점으로 나온 사실은, 적어도 algebraic level에서는 `pi`가 genuine nontrivial Boolean character가 되는 유일한 equal-channel phase라는 설명을 갖는다.

generic `theta`는 squarefree symmetric-difference group의 character가 아니다.

---

## 3. prime-label permutation symmetry도 Möbius를 선택한다

character group 역시

\[
\widehat G_m\cong(\mathbb Z/2\mathbb Z)^m
\]

이다.

character를 vector

\[
a=(a_1,\ldots,a_m),\quad a_j\in\{0,1\}
\]

로 쓰면

\[
\chi_a(\epsilon)=(-1)^{a\cdot\epsilon}.
\]

prime labels를 모든 permutation으로 바꾸는 symmetric group `S_m` 작용 아래 invariant character가 되려면 vector `a`의 모든 coordinate가 같아야 한다.

따라서 fixed characters는

\[
a=(0,\ldots,0)
\]

과

\[
a=(1,\ldots,1)
\]

뿐이다.

즉

\[
\boxed{
\text{prime-label permutation invariant characters}
=
\{\text{trivial},\ \mu\}.
}
\]

비자명한 쪽을 요구하면 Möbius parity character가 유일하다.

### 감사주의

실제 arithmetic cutoff는 weights `log p` 때문에 prime labels를 동등하게 취급하지 않는다.

따라서 이 symmetry는 **observable/character 선택의 canonicality**를 설명하지 cutoff measure의 symmetry를 의미하지 않는다.

---

## 4. 왜 p=2가 특별한가

finite Boolean group에는 normalized Haar Fourier transform이 있다.

일반 `L^p` norm도 정의할 수 있지만 Fourier transform이 같은 exponent의 norm으로 exact self-dual isometry가 되는 것은 Plancherel case

\[
\boxed{p=2}
\]

이다.

즉 다음 세 요구를 동시에 둔다면 quadratic Hilbert geometry가 자연스럽다.

1. group translation invariance,
2. character decomposition,
3. state-space와 spectrum-space 사이 exact norm self-duality.

그 결과

\[
\|f\|_2^2
=
\sum_\chi|\widehat f(\chi)|^2
\]

가 된다.

이는 `RH가 1/2이므로 L²를 선택`하는 논리와 다르다.

### 단, 유일성 범위

`L^p` 분석 자체를 금지하는 것은 아니다. `p=2`가 선택되는 것은 **Plancherel self-duality를 요구했을 때**이다.

---

## 5. squarefree Dirichlet H²에서 1/2가 선택된다

squarefree-support coefficient Hilbert space

\[
\mathscr H^2_{sf}
=
\left\{
\sum_{\mu^2(n)=1}a_nn^{-s}
:\sum|a_n|^2<\infty
\right\}
\]

를 본다.

point evaluation kernel norm은

\[
K(\sigma)
=
\sum_{\mu^2(n)=1}n^{-2\sigma}
=
\frac{\zeta(2\sigma)}{\zeta(4\sigma)}.
\]

따라서 generic bounded point evaluation은 정확히

\[
\boxed{
\operatorname{Re}s>1/2
}
\]

에서 가능하고 `1/2`에서 kernel이 발산한다.

이 `1/2`는 zeta zero location을 입력한 것이 아니라 squarefree coefficient density와 quadratic norm에서 발생한다.

---

## 6. target-free structural chain

현재까지 다음 chain은 RH를 사전에 넣지 않고 구성된다.

\[
\boxed{
\begin{aligned}
&\text{independent binary prime channels}\\
&\Downarrow\\
&G_m=(\mathbb Z/2)^m\\
&\Downarrow\\
&\text{unique nontrivial channel-symmetric character }\mu\\
&\Downarrow\\
&\text{Haar character analysis / Plancherel self-duality}\\
&\Downarrow\\
&L^2\\
&\Downarrow\\
&\text{squarefree Dirichlet }\mathscr H^2\text{ point-evaluation boundary}\\
&\Downarrow\\
&\operatorname{Re}s=1/2.
\end{aligned}
}
\]

이 chain은

- `mu`를 왜 사용하는가,
- `L²`가 왜 자연스러운가,
- `1/2`가 왜 functional-analytic boundary로 나오는가

를 하나의 formation-symmetry language에서 설명한다.

---

## 7. 그러나 이것은 RH가 아니다

RH에 필요한 것은

\[
\zeta(\rho)=0,
\quad0<\Re\rho<1
\implies
\Re\rho=1/2.
\]

위 chain은 zero location을 강제하지 않는다.

특히 `mobius_hardy_twist_barrier.md`에서 확인했듯 Haar/Hardy global norm은 Möbius twist와 positive squarefree polynomial을 동일하게 본다.

따라서 빠진 화살표는

\[
\boxed{
\text{canonical }(\mu,L^2,1/2)
\not\Rightarrow
\text{all nontrivial zeta zeros lie there}
}
\]

이다.

---

## 8. 현재 가장 정확한 OPEN question

formation route가 독립적인 RH 경로가 되려면 다음을 보여야 한다.

> arithmetic cutoff
> \[
> \prod p^{\epsilon_p}\le X
> \]
> 가 canonical Möbius character의 boundary evaluation을 generic squarefree-Hilbert scale보다 크게 증폭시키지 않는다는 deterministic inequality를 증명할 수 있는가?

Fourier language로는

\[
M(X)
=
\widehat{1_{A_X}}(\chi_\mu)_{\rm raw},
\]

\[
A_X
=
\left\{\epsilon:\sum_p(\log p)\epsilon_p\le\log X\right\}.
\]

Parseval에서 character 평균 RMS는

\[
\left(
\frac1{|G|}\sum_\chi
|\widehat{1_{A_X}}(\chi)_{\rm raw}|^2
\right)^{1/2}
=
\sqrt{|A_X|}.
\]

최종 range에서

\[
|A_X|=Q(X)\asymp X,
\]

이므로 typical character scale은

\[
\asymp\sqrt X.
\]

RH는 이 관점에서

> **특정 canonical character `mu`가 Fourier RMS scale보다 subpolynomial factor 이상으로 exceptional하지 않다**

는 방향으로 읽을 수 있다.

이것은 정확한 증명 동치로 사용하기 전 추가 정식화가 필요하지만, 다음 계산/부등식 탐색의 가장 좁은 목표로 사용한다.

---

## 선행감사

- Hilberdink (2014): squarefree group과 Möbius character는 선행.
- Hedenmalm--Lindqvist--Seip (1997): square-summable Dirichlet Hilbert space, character space, dilation `L²` bridge는 선행.
- Nyman--Beurling--Báez-Duarte: `L^p` closure와 `Re(s)>1/p`, 특히 `p=2` RH criterion은 선행.

따라서 novelty claim은 하지 않는다. 현재 의미는 이 세 선행축을 formation-channel audit에서 하나의 선택 사슬로 정렬하고, 정확히 어느 화살표가 아직 증명되지 않았는지 분리한 데 있다.
