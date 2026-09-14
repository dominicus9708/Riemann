# Mertens Simplicial-Topology / Morse Barrier Audit

Date: 2026-09-15

## 목적

squarefree weighted Boolean halfspace

\[
\Delta_X
=
\left\{
S\subset\{p\le X:p\text{ prime}\}:
\prod_{p\in S}p\le X
\right\}
\]

의 alternating face count가 Mertens function과 동일하다는 관찰을 감사한다.

이 구조가 새로운 topology route인지, 이미 알려진 simplicial-complex formulation인지, 그리고 discrete Morse theory가 cancellation을 실제로 줄일 수 있는지를 검사한다.

---

## 1. exact Euler-characteristic representation

face `S`에 squarefree integer

\[
n_S=\prod_{p\in S}p
\]

를 대응시키면

\[
\mu(n_S)=(-1)^{|S|}.
\]

따라서 empty face를 포함한 alternating face sum은

\[
\sum_{S\in\Delta_X}(-1)^{|S|}=M(X).
\]

reduced Euler characteristic convention에서는

\[
\boxed{M(X)=-\widetilde\chi(\Delta_X).}
\]

상태: `EXACT`.

이 관찰은 신규가 아니다. Anders Björner (2011), *A cell complex in number theory*, Section 1에서 정확히 같은 simplicial complex와 Mertens Euler characteristic을 연구한다.

---

## 2. weighted-halfspace / quota-complex form

product cutoff는 log-coordinate에서

\[
\sum_{p\in S}\log p\le\log X
\]

이므로 `Delta_X`는 positive weights `w_p=log p`와 quota `q=log X`를 갖는 weighted quota/threshold complex다.

quota complexes 자체도 Pakianathan--Winfree (2011)에서 체계적으로 연구되며 number-theoretic examples 및 RH formulation까지 논의된다.

따라서 `prime log weights + quota complex`라는 명칭 자체의 신규성도 주장하지 않는다.

---

## 3. shifted-complex theorem

Björner는 prime vertices를 increasing order로 두면 `Delta_X`가 shifted complex임을 관찰한다.

실제로 face의 한 prime을 더 작은 prime으로 교체하면 product가 감소하므로 cutoff 안에 남는다.

shifted complex의 표준 theorem에 의해

\[
\boxed{\Delta_X\simeq\bigvee S^{d}}
\]

즉 wedge of spheres homotopy type를 갖는다.

따라서 static homotopy type 안에 임의의 복잡한 torsion이나 hidden attaching-map information이 남는 것은 아니다. 관련 정보는 dimension별 sphere multiplicities, 즉 Betti numbers로 닫힌다.

상태: `KNOWN_THEOREM`.

---

## 4. exact Betti formula

Björner Theorem 3.1:

\[
\boxed{
\beta_k(\Delta_X)
=
\sigma^{\rm odd}_{k+1}(X)
-
\sigma^{\rm odd}_{k+1}(X/2)
}
\]

여기서 `sigma_r^odd(Y)`는 `Y` 이하 odd squarefree integers 중 `omega=r`인 수의 개수다.

즉

\[
\beta_k
=
\#\left\{
X/2<n\le X:
 n\text{ odd, squarefree},\omega(n)=k+1
\right\}.
\]

Euler--Poincare로

\[
M(X)=\sum_{k\ge0}(-1)^{k-1}\beta_k(\Delta_X).
\]

따라서 exact하게

\[
\boxed{
M(X)
=
\sum_{\substack{X/2<n\le X\\2\nmid n}}
\mu(n).
}
\]

이것은 prime `2`를 toggle하여 `n`과 `2n`을 pair한 뒤 complete pairs를 cancellation하는 boundary identity와 정확히 같다.

즉 topology가 앞선 Boolean full-cube pairing을 독립적으로 강화하는 것이 아니라 기존 shifted-complex theorem으로 완성한다.

---

## 5. total Betti mass is linear

Björner는

\[
\boxed{
\sum_k\beta_k(\Delta_X)
=
\frac{2X}{\pi^2}+O(X^\theta)
\qquad(\theta>17/54)
}
\]

을 얻는다.

따라서 homological mass 자체는

\[
\asymp X
\]

이다.

RH가 요구하는 Euler characteristic scale

\[
|M(X)|\le X^{1/2+\varepsilon}
\]

와 비교하면 topology는 small number of homology generators를 만드는 것이 아니라 **linear many sphere generators 사이의 alternating cancellation**을 요구한다.

---

## 6. discrete Morse critical-cell barrier

어떤 discrete Morse function에서도 Morse inequalities에 의해 dimension `k`의 critical cells 수 `c_k`는

\[
c_k\ge\beta_k.
\]

따라서

\[
\boxed{
\sum_k c_k
\ge
\sum_k\beta_k
=
\frac{2X}{\pi^2}+o(X).
}
\]

즉 discrete Morse matching으로 거의 모든 faces를 pair해서

\[
O(X^{1/2+\varepsilon})
\]

개의 critical cells만 남긴 뒤 Euler characteristic를 bound하려는 전략은 구조적으로 불가능하다.

critical-cell count 자체는 반드시 linear scale이다.

따라서 topology route가 RH-scale에 도달하려면 critical cell **개수**가 아니라 dimensions/signs 사이의 cancellation을 다시 제어해야 한다.

그 문제는 원래 Möbius parity cancellation과 동형이다.

상태: `EXACT_TOPOLOGICAL_BARRIER` given standard Morse inequalities + Björner Betti asymptotic.

---

## 7. finite X=2^24 audit

기존 squarefree layer counts와

\[
\sigma_k^{odd}(X)
=
\sigma_k(X)-\sigma_{k-1}(X/2)+\sigma_{k-2}(X/4)-\cdots
\]

를 사용하여 Betti numbers를 재현했다.

`X=2^24=16,777,216`에서

\[
(\beta_0,\ldots,\beta_6)
=
(513708,
1252181,
1107615,
442966,
78422,
4848,
39).
\]

총합은

\[
\boxed{3,399,779}
\]

이고

\[
\frac{2X}{\pi^2}
\approx3,399,774.7667.
\]

반면 Euler alternating sum은

\[
-513708
+1252181
-1107615
+442966
-78422
+4848
-39
=
\boxed{211}
=M(2^{24}).
\]

따라서 finite data에서도

\[
3.4\times10^6
\quad\longrightarrow\quad
211
\]

의 homological parity cancellation이 직접 보인다.

상태: `NUMERICAL_REPRODUCTION_OF_EXACT_FORMULA`.

---

## 8. topology does not create an independent RH observable

static complex `Delta_X`에 대해

- f-vector = squarefree `omega` layer counts,
- Betti vector = odd upper-half squarefree layer counts,
- Euler characteristic = Mertens function,
- homotopy type = wedge of spheres

가 모두 explicit하게 연결된다.

따라서 ordinary static homotopy invariants를 추가하는 것만으로는 새 independent spectral information이 생기지 않는다.

Björner 자신도 individual/total Betti estimates가 Euler-characteristic growth에 새로운 통제를 주지 못한다고 지적한다.

---

## 9. possible but unproven escape routes

다음은 static topology와 구분해야 한다.

1. filtration maps `Delta_X -> Delta_Y` 자체의 persistent data,
2. arithmetic labels/weights를 유지한 non-topological chain operators,
3. weighted Laplacian spectra with information beyond homotopy type,
4. boundary-support dynamics as `X` crosses individual squarefree products.

그러나 quota-complex persistent homology도 기존 문헌이 있으므로 선행감사 없이 신규성 주장하지 않는다.

또 Euler characteristic를 계산하는 데 필요한 signed cancellation이 nonzero Laplacian spectrum으로 자동 이전된다고 가정해서도 안 된다.

---

## 10. branch verdict

### closed

- `M(X)`를 Euler characteristic로 재해석하는 것 자체.
- shifted/weighted threshold complex임을 이용해 wedge-of-spheres를 얻는 것 자체.
- discrete Morse matching으로 only `O(sqrt X)` critical cells를 남기는 전략.
- total Betti bound만으로 Euler cancellation을 얻는 전략.

### retained as conceptual organization

Topology는 다음 사실을 매우 투명하게 만든다.

\[
\boxed{
\text{RH difficulty}
=
\text{linear homological mass의 dimension-parity cancellation}
}
\]

이는 low-order moment / K-wise label invisibility barrier와 같은 방향이다.

## 상태

- Mertens Euler characteristic: `KNOWN_EXACT`.
- shifted/wedge-of-spheres: `KNOWN_THEOREM`.
- Betti formula: `KNOWN_EXACT`.
- total Betti linear asymptotic: `KNOWN_THEOREM`.
- critical-cell lower bound: `EXACT_CONSEQUENCE`.
- independent RH progress: `NOT_ESTABLISHED`.
- RH: `OPEN`.

## 선행문헌

- Anders Björner (2011), *A cell complex in number theory*, arXiv:1101.5704.
- Jonathan Pakianathan & Troy Winfree (2011), *Quota Complexes, Persistant Homology and the Goldbach Conjecture*, arXiv:1104.4324.
