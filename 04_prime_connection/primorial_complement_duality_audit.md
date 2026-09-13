# Primorial Complement Duality Audit

## 목적

finite squarefree Boolean group에서 divisor complement

\[
d\longleftrightarrow \frac{P_m}{d}
\]

가 arithmetic cutoff와 Möbius parity sum에 주는 정확한 대칭을 분리한다.

이 구조에서 normalized log-cutoff `1/2`가 다시 나타나지만, 이를 RH critical line과 혼동하지 않는 것이 핵심이다.

---

## 1. 설정

첫 `m`개 prime의 primorial을

\[
P_m=\prod_{j=1}^m p_j
\]

라고 하자.

유한 prime-activation sum을

\[
F_m^{\le}(X)
=
\sum_{\substack{d\mid P_m\\d\le X}}\mu(d)
\]

로 둔다.

`m>=1`이면

\[
\sum_{d\mid P_m}\mu(d)=0.
\]

---

## 2. exact complement identity

`d|P_m`에 대해

\[
e=P_m/d
\]

를 두면

\[
\mu(d)
=
(-1)^m\mu(e),
\]

왜냐하면 `d`와 `e`의 활성 prime-channel 수가 합쳐서 정확히 `m`이기 때문이다.

또

\[
d>X
\iff
e<P_m/X.
\]

전체 Möbius divisor sum이 zero이므로

\[
F_m^{\le}(X)
=-\sum_{\substack{d\mid P_m\\d>X}}\mu(d).
\]

complement를 적용하면

\[
\boxed{
F_m^{\le}(X)
=
(-1)^{m+1}
\sum_{\substack{e\mid P_m\\e<P_m/X}}
\mu(e).
}
\]

left-continuous notation

\[
F_m^<(Y)=\sum_{\substack{d\mid P_m\\d<Y}}\mu(d)
\]

을 쓰면

\[
\boxed{
F_m^{\le}(X)=(-1)^{m+1}F_m^<(P_m/X).
}
\]

---

## 3. normalized log coordinate의 1/2

\[
u=\frac{\log X}{\log P_m}
\]

를 두면 complement map은

\[
X\longmapsto P_m/X
\]

이므로

\[
\boxed{u\longmapsto1-u}.
\]

고정점은

\[
\boxed{u=1/2}.
\]

즉

\[
X=\sqrt{P_m}
\]

가 finite Boolean threshold의 정확한 중앙이다.

### parity effect

`P_m`은 `m>=1`에서 squarefree non-square이므로 divisor가 정확히 `sqrt(P_m)`일 수 없다.

따라서 중앙에서는 `F_m^<=F_m^<`이고

\[
F_m(\sqrt{P_m})
=(-1)^{m+1}F_m(\sqrt{P_m}).
\]

`m`이 even이면

\[
\boxed{F_m(\sqrt{P_m})=0.}
\]

`m`이 odd이면 이 대칭만으로 zero를 강제하지 않는다.

### 감사 판정

이 `1/2`는 **normalized log-product complement symmetry의 중앙점**이다.

따라서 RH critical line `Re(s)=1/2`의 증거로 세지 않는다.

---

## 4. first primorial crossing은 small Mertens value로 정확히 환원

`m=m_0(X)`를

\[
P_{m-1}\le X<P_m
\]

을 만족하는 첫 crossing index라 하자.

그러면

\[
\frac{P_m}{X}\le p_m.
\]

따라서

\[
e<P_m/X
\]

인 모든 positive integer `e`는 prime factor가 `p_m`보다 작고, squarefree `e`라면 자동으로 `P_{m-1}`의 divisor이다.

그러므로 complement sum의 divisor restriction이 사라지고

\[
\boxed{
F_m^{\le}(X)
=
(-1)^{m+1}
M\!\left(\left\lceil\frac{P_m}{X}\right\rceil-1\right).
}
\]

즉 **primorial이 cutoff를 처음 넘는 순간의 formation boundary state는 작은-scale ordinary Mertens value와 정확히 같다.**

이것은 finite complement identity의 직접 corollary이며 신규 정리 주장은 하지 않는다.

---

## 5. dyadic exact verification

`X=2^10,...,2^24`에서 전부 직접 검증했다.

대표값:

| X | crossing m | p_m | P_m/X | strict cutoff | F_m(X) | predicted |
|---:|---:|---:|---:|---:|---:|---:|
| 1,024 | 5 | 11 | 2.2559 | 2 | 0 | 0 |
| 4,096 | 6 | 13 | 7.3315 | 7 | 2 | 2 |
| 32,768 | 7 | 17 | 15.5795 | 15 | -1 | -1 |
| 1,048,576 | 8 | 19 | 9.2503 | 9 | 2 | 2 |
| 4,194,304 | 8 | 19 | 2.3126 | 2 | 0 | 0 |
| 16,777,216 | 9 | 23 | 13.2974 | 13 | -3 | -3 |

전체 `15/15` cutoff에서 exact match다.

자료:

```text
data/formation/primorial_first_crossing_duality_2pow10_24.csv
```

---

## 6. central-symmetry 증명 후보 감사

중앙 zero를 쓰려면 `m`이 even이고

\[
P_m\approx X^2
\]

여야 한다.

하지만 even primorial index는 두 prime씩 건너뛰므로

\[
\frac{P_{m+2}}{P_m}=p_{m+1}p_{m+2}.
\]

즉 multiplicative grid가 촘촘하지 않다.

`X=2^10,...,2^24`에서 `P_m`이 `X^2`에 가장 가까운 even `m`을 고르면

\[
P_m/X^2
\]

가 대략

\[
0.026\ \text{to}\ 27
\]

사이로 크게 움직인다.

따라서 임의 `X`에서 exact center에 근접한 even primorial을 uniform하게 선택할 수 없다.

전체 자료:

```text
data/formation/primorial_even_center_audit_2pow10_24.csv
```

### 두 번째 장벽

설령 intermediate `F_m(X)`가 중앙 대칭 때문에 작더라도

\[
F_m(X)\ne M(X)
\]

이다.

`m` 이후 `p_m<p<=X`의 prime channels를 더 활성화해야 최종 Mertens 값이 된다.

이 tail은 이미 Buchstab/Alladi/prime-tail dynamics 계열의 어려운 cancellation을 다시 포함한다.

따라서

\[
\boxed{
\text{primorial central symmetry alone does not close RH.}
}
\]

---

## 7. threshold/Alexander duality와의 관계

formation cutoff

\[
\sum_{j=1}^m(\log p_j)\epsilon_j\le\log X
\]

는 scalar-weight quota/threshold complex다.

Boolean set complement는 total weight

\[
\log P_m-\log X
\]

를 만드는 일반 complement duality 구조다.

따라서

- complement involution,
- normalized quota center `1/2`,
- complement-based dual complex

자체는 일반 threshold/Alexander-duality 문헌과 겹친다.

Björner의 number-theoretic complex 및 Pakianathan--Winfree의 quota-complex 연구는 이 방향의 직접 선행기준이다.

---

## 8. 현재 의미

### 양성

1. formation boundary state에 exact scale-reflection identity가 있다.
2. first primorial crossing은 작은-scale Mertens value로 exact renormalization된다.
3. normalized log coordinate의 `1/2`가 Boolean complement symmetry에서 target-free로 나타난다.
4. earlier exact-zero regime와 first nonzero boundary state를 하나의 complement picture로 통합한다.

### 음성

1. `u=1/2`는 generic complement center이며 RH line과 동일시할 수 없다.
2. even primorial grid가 너무 성기다.
3. first-crossing reduction은 매우 작은 Mertens argument만 주어 초기 boundary를 설명할 뿐 final `M(X)`를 닫지 않는다.
4. 후속 prime activation tail에 원래 난점이 남는다.

### 남은 질문

complement identity를 **한 번만** 쓰는 대신 activation tail 전체에 반복 적용했을 때,

\[
X\mapsto P_m/X
\]

scale reflection들이 유한한 renormalization tree를 만들며 그 전체 signed boundary를 deterministic하게 제어할 수 있는가?

단, 이것이 Buchstab/Heath--Brown/Alladi recursion을 다른 표기로 다시 쓰는지 먼저 감사해야 한다.

---

## 재현자료

```text
scripts/audit_primorial_complement_duality.py
data/formation/primorial_first_crossing_duality_2pow10_24.csv
data/formation/primorial_even_center_audit_2pow10_24.csv
```

## 선행문헌

- Anders Björner (2011), *A Cell Complex in Number Theory*, Adv. Appl. Math. 46, 71--85, DOI 10.1016/j.aam.2010.09.007.
- Jonathan Pakianathan & Troy Winfree (2013), *Threshold Complexes and Connections to Number Theory*, Turkish J. Math. 37(3), DOI 10.3906/mat-1112-14.
- Anders Björner & Martin Tancer (2009), *Combinatorial Alexander Duality -- A Short and Elementary Proof*, Discrete Comput. Geom. 42, 586--593, DOI 10.1007/s00454-008-9102-x.
