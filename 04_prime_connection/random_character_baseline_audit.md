# Random Character Baseline Audit

## 목적

formation symmetry 관점에서 Möbius는 squarefree Boolean group의 canonical nontrivial symmetric character다.

이를 random prime-sign characters와 비교하여

\[
\sqrt{Q(X)}
\]

scale의 정확한 의미를 정리하고, `random baseline`을 RH evidence로 오해하지 않도록 한다.

---

## 1. Rademacher multiplicative character ensemble

각 prime에 독립 Rademacher sign

\[
\chi(p)\in\{-1,+1\}
\]

을 주고 squarefree integer에

\[
f_\chi(n)=\mu(n)^2\prod_{p\mid n}\chi(p)
\]

를 정의한다.

이는 squarefree Boolean group의 random character와 같다.

partial sum을

\[
S_\chi(X)=\sum_{n\le X}f_\chi(n)
\]

라고 한다.

Möbius는 special deterministic corner

\[
\chi(p)=-1\quad\forall p
\]

에 해당한다.

---

## 2. exact second moment / Parseval

character orthogonality 때문에 squarefree `n,m`에 대해

\[
\mathbb E_\chi[f_\chi(n)f_\chi(m)]
=
\mathbf1_{n=m}.
\]

따라서 정확히

\[
\boxed{
\mathbb E_\chi|S_\chi(X)|^2
=
Q(X)
=
\sum_{n\le X}\mu(n)^2.
}
\]

즉 ensemble RMS는

\[
\boxed{
\operatorname{RMS}(S_\chi(X))=\sqrt{Q(X)}\asymp\sqrt X.
}
\]

이 identity는 finite-group Parseval과 같은 사실이다.

---

## 3. RMS를 typical absolute size와 동일시하면 안 된다

Adam Harper의 random multiplicative function 결과에 따르면 Rademacher/Steinhaus model에서 low moments는 단순 Gaussian square-root model과 다르다.

특히

\[
\mathbb E|S_\chi(X)|
\asymp
\frac{\sqrt X}{(\log\log X)^{1/4}}
\]

이다.

따라서

\[
\sqrt{Q(X)}
\]

를 `typical absolute magnitude`라고 부르지 않고 **character RMS scale**이라고 부른다.

또 random multiplicative partial sums에는 almost-sure large fluctuations와 critical multiplicative-chaos structure가 존재한다.

---

## 4. Möbius와 random model의 정확한 차이

random model:

\[
\chi(p)\text{ independent random signs}.
\]

Möbius:

\[
\boxed{
\chi_\mu(p)=-1\quad\text{for every prime }p.
}
\]

즉 Möbius는 random ensemble의 `typical sample`로 주어진 것이 아니라 prime-label permutation symmetry에 고정된 deterministic corner다.

따라서 random multiplicative function theorem을 Möbius에 그대로 이전할 수 없다.

### RH-scale reading

고전적 동치

\[
RH\iff M(X)=O_\varepsilon(X^{1/2+\varepsilon})
\]

를 character language로 보면,

> canonical all-minus character의 arithmetic-cutoff Fourier coefficient가 character RMS `sqrt(X)`보다 polynomially 큰 amplification을 갖지 않는다.

라고 읽을 수 있다.

이것은 해석적 재표현이며 그 자체가 증명은 아니다.

---

## 5. random control의 역할

random prime-sign controls는 다음에만 사용한다.

- generic multiplicative-character fluctuation scale 확인,
- `1/2`가 random square-root baseline에서도 나오는지 확인,
- actual Möbius statistic이 random ensemble에서 truly exceptional한지 진단.

다음에는 사용하지 않는다.

- random theorem을 deterministic Möbius theorem으로 외삽,
- finite Monte-Carlo tail을 RH probability로 해석,
- random cancellation 자체를 arithmetic proof로 대체.

---

## 선행문헌

- Adam J. Harper, *Moments of random multiplicative functions, I: Low moments, better than squareroot cancellation, and critical multiplicative chaos*, Forum of Mathematics, Pi 8 (2020), e1, DOI 10.1017/fmp.2019.7.
- Adam J. Harper, *Almost sure large fluctuations of random multiplicative functions*, International Mathematics Research Notices 2023(3), 2095--2138, DOI 10.1093/imrn/rnab299.
- Harper, Nikeghbali & Radziwill, *A Note on Helson's Conjecture on Moments of Random Multiplicative Functions*.
- Marco Aymone et al. literature on Rademacher random multiplicative functions as Möbius models.

## 현재 판정

random-character theory strengthens the audit baseline but does not close the deterministic all-minus corner.

남은 arithmetic question remains:

\[
\boxed{
\text{why does the prime-weighted cutoff keep the canonical Möbius character within an }X^{o(1)}\text{ factor of square-root scale?}
}
\]
