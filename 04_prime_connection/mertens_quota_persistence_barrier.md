# Mertens Quota-Complex Persistence Barrier

Date: 2026-09-15

## 목적

static simplicial topology가 Björner의 shifted-complex theory로 완전히 닫힌 뒤, filtration

\[
\Delta_X\subseteq\Delta_Y\qquad(X\le Y)
\]

의 persistent homology가 추가 arithmetic information을 제공하는지 감사한다.

---

## 1. log-prime quota complex

prime vertex `p`에 weight

\[
w(p)=\log p
\]

를 주고 quota

\[
q=\log X
\]

를 두면

\[
\prod_{p\in S}p<X
\iff
\sum_{p\in S}\log p<\log X.
\]

endpoint convention `<=` vs `<`를 제외하면 Mertens simplicial complex는 scalar-valued quota/threshold complex다.

minimum-weight vertex는 `p=2`이고

\[
w_0=\log2.
\]

---

## 2. quota-complex sphere theorem

Pakianathan--Winfree의 scalar quota-complex theorem에 따르면, minimum-weight vertex `v_0`를 포함하지 않는 face `F` 중

\[
q-w_0\le w(F)<q
\]

인 각각에 대해 dimension `dim F`인 sphere가 wedge decomposition에 하나씩 대응한다.

prime-log weights에서는 `F`가 odd squarefree integer

\[
m=\prod_{p\in F}p
\]

에 대응하므로 condition은

\[
\log X-\log2\le\log m<\log X,
\]

즉

\[
\boxed{X/2\le m<X.}
\]

이는 Björner의 exact Betti formula와 동일하다.

상태: `KNOWN_THEOREM / EXACT_SPECIALIZATION`.

---

## 3. natural persistent interval

odd squarefree face `F` with product `m`를 고정한다.

- quota가 `q=log m`를 넘을 때 `F`가 complex에 들어온다.
- `F cup {2}`의 weight는 `log(2m)`이다.
- `F cup {2}`가 들어오기 전에는 quota theorem의 shell sphere가 존재한다.
- quota가 `log(2m)`를 넘으면 minimum vertex `2`가 붙은 cone simplex가 들어오며 해당 shell sphere가 채워진다.

따라서 strict/weak endpoint convention을 무시하면 natural persistence interval은

\[
\boxed{
[\log m,\log(2m))
}
\]

이고 homological dimension은

\[
\boxed{
\omega(m)-1.
}
\]

multiplicative X-coordinate에서는

\[
\boxed{[m,2m)}.
\]

모든 such bars의 logarithmic lifetime은 정확히

\[
\boxed{\log2}.
\]

따라서 persistence length 자체는 prime-specific spectrum을 만들지 않는다.

---

## 4. Betti occupancy check

fixed `X`에서 active bars는 정확히

\[
m\le X<2m,
\]

즉

\[
X/2<m\le X
\]

인 odd squarefree `m`들이다.

따라서 dimension `k`의 active-bar count는

\[
\#\{X/2<m\le X:
 m\text{ odd squarefree},\omega(m)=k+1\},
\]

which is exactly

\[
\beta_k(\Delta_X).
\]

즉 barcode occupancy가 Björner Betti formula를 pointwise 재현한다.

---

## 5. persistence carries re-encoded arithmetic data

barcode에서 각 bar는

\[
(m,\omega(m)-1)
\]

를 기록하고 death point는 deterministic하게 `2m`이다.

따라서 이 natural scalar filtration의 persistence는 essentially

\[
\boxed{
\text{odd squarefree integer locations}
+
\omega\text{ labels}
}
\]

의 재부호화다.

새 independent cancellation law는 자동으로 생기지 않는다.

특히 Mertens function은 time `X`에서 active bars의 dimension parity alternating sum이다.

---

## 6. no persistence-lifetime discriminator

모든 bars가 same log lifetime `log 2`를 가지므로

- unusually long bars,
- lifetime tail,
- persistence scale selection,
- lifetime-based spectral gap

같은 standard TDA statistic으로 Mertens cancellation을 분리할 수 없다.

남는 nontrivial information은

1. bar birth locations `log m`,
2. homological dimensions `omega(m)-1`,
3. 이 둘의 signed correlation

뿐이다.

이는 다시 odd squarefree dyadic parity problem이다.

---

## 7. relation to RH

Euler characteristic at `X` is active bars의 dimension-parity signed count:

\[
M(X)
=
\sum_{\text{active bars at }X}
(-1)^{\dim+1}.
\]

따라서 RH는 이 barcode에서 bar **수명**을 bound하는 문제가 아니라

\[
\boxed{
\text{same-lifetime bars의 dimension parity cancellation}
}
\]

문제로 남는다.

static topology에서 linear Betti mass가 남았던 것과 동일한 obstruction이다.

---

## 8. verdict

### closed

- persistent homology를 도입하면 새로운 lifetime scale이 나타난다는 기대.
- long-persistence class를 찾아 RH-critical structure를 고른다는 경로.
- barcode length distribution alone으로 Euler cancellation을 제어하는 경로.

### retained

birth-position/dimension joint structure는 arithmetic information을 그대로 보존하므로 분석대상으로는 사용할 수 있다.

그러나 이를 사용할 경우 반드시 odd-squarefree layer / weighted-halfspace boundary와 동치인지 감사해야 한다.

## 상태

- quota specialization: `KNOWN_EXACT`.
- natural bar `[log m, log(2m))`: `EXACT_FROM_QUOTA_SHELL_STRUCTURE`.
- equal lifetime `log 2`: `EXACT`.
- persistence as independent RH mechanism: `CLOSED_AS_REENCODING`.
- RH: `OPEN`.

## 선행문헌

- Jonathan Pakianathan & Troy Winfree, *Threshold complexes and connections to number theory*, Turkish Journal of Mathematics 37 (2013), scalar quota-complex wedge theorem.
- Jonathan Pakianathan & Troy Winfree (2011), *Quota Complexes, Persistant Homology and the Goldbach Conjecture*, arXiv:1104.4324.
- Anders Björner (2011), *A cell complex in number theory*, arXiv:1101.5704.
