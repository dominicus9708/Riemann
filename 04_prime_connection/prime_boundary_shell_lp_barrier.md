# Prime-Boundary Shell L^p Barrier

Date: 2026-09-15

## 목적

각 prime `p`에서 얻는 exact boundary identity를 임의의 signed linear combination으로 평균하면 Mertens cancellation을 더 작은 norm 문제로 바꿀 수 있는지 감사한다.

핵심 질문은 다음이다.

1. prime-boundary identities의 signed weights를 최적화해 coefficient vector의 L^p norm을 RH scale에 충분할 만큼 작게 만들 수 있는가?
2. Cauchy--Schwarz/Hölder 같은 norm inequality만으로 square-root cancellation을 얻을 수 있는가?

---

## 1. exact prime-boundary identity

prime `p`에 대해 squarefree multiples of `p`를 `pm`, `(m,p)=1`로 pair하면

\[
\boxed{
M(X)=\sum_{\substack{X/p<m\le X\\p\nmid m}}\mu(m).
}
\]

이는 exact identity다.

임의의 real weights `w_p`가

\[
\sum_{p\le X} w_p=1
\]

을 만족하면

\[
M(X)=\sum_{m\le X}\mu(m)c_w(m),
\]

where

\[
\boxed{
c_w(m)=\sum_{\substack{p\le X\\pm>X\\p\nmid m}}w_p.
}
\]

negative weights도 허용한다.

상태: `EXACT`.

---

## 2. prime-prime boundary matrix

prime rows `q\le X`, prime columns `p\le X`에 대해

\[
A_{q,p}=\mathbf 1_{\{pq>X,\ p\ne q\}}
\]

로 둔다.

그러면 prime input에서의 coefficient vector는

\[
(c_w(q))_{q\ \mathrm{prime}}=Aw.
\]

행렬 `A`는 symmetric이다.

---

## 3. exact dual certificate

\[
N_X=\pi(X)-\pi(X/2)
\]

라 하고 vector `v`를 prime columns에서

\[
v_p=
\begin{cases}
1/N_X,&p=2,\\
1/N_X,&X/2<p\le X,\\
0,&\text{otherwise}
\end{cases}
\]

로 둔다.

그러면 exact하게

\[
\boxed{Av=\mathbf 1.}
\]

### 확인

- `q=2`: `pq>X`를 만족하는 support primes는 정확히 `X/2<p\le X`인 `N_X`개다.
- `2<q\le X/2`: 모든 upper-half support prime이 `pq>X`를 만족하고 `p=2`는 만족하지 않으므로 다시 `N_X`개다.
- `q>X/2`: 모든 upper-half support prime이 들어오지만 `p=q` 하나가 빠지고, 대신 `p=2`가 `2q>X`로 들어오므로 다시 `N_X`개다.

따라서 모든 prime row에서 `(Av)_q=1`이다.

상태: `EXACT`.

---

## 4. L^2 lower bound

`sum_p w_p=1`이고 `A`가 symmetric이므로

\[
1=\mathbf1^T w=(Av)^Tw=(Aw)^Tv.
\]

Cauchy--Schwarz로

\[
1\le \|Aw\|_2\|v\|_2.
\]

그리고

\[
\|v\|_2=\frac{\sqrt{N_X+1}}{N_X}.
\]

따라서

\[
\boxed{
\|Aw\|_2\ge \frac{N_X}{\sqrt{N_X+1}}.
}
\]

즉 full coefficient vector에 대해서도

\[
\boxed{
\|c_w\|_2\ge \frac{N_X}{\sqrt{N_X+1}}.
}
\]

Prime Number Theorem로

\[
N_X\sim \frac{X}{2\log X},
\]

따라서

\[
\boxed{
\|c_w\|_2\gtrsim \sqrt{\frac{X}{2\log X}}.
}
\]

상태: exact finite lower bound + standard PNT asymptotic.

---

## 5. all L^r / Hölder barrier

`1\le r\le\infty`, `1/r+1/r'=1`에 대해

\[
1=(Aw)^Tv\le \|Aw\|_r\|v\|_{r'}.
\]

support size가 `N_X+1`, 각 nonzero entry가 `1/N_X`이므로

\[
\|v\|_{r'}=\frac{(N_X+1)^{1/r'}}{N_X}.
\]

따라서

\[
\boxed{
\|Aw\|_r\ge
\frac{N_X}{(N_X+1)^{1/r'}}.
}
\]

그리고

\[
\boxed{
\|c_w\|_r\ge
\frac{N_X}{(N_X+1)^{1/r'}}.
}
\]

asymptotically

\[
\|c_w\|_r\gtrsim N_X^{1/r}.
\]

---

## 6. consequence for norm-only Mertens bounds

Hölder를 직접 적용하면

\[
|M(X)|
\le
\|\mu\|_{r'}\|c_w\|_r.
\]

squarefree support density 때문에

\[
\|\mu\|_{r'}\asymp X^{1/r'}
\]

for finite `r'` (endpoint conventions included separately).

따라서 이 representation class에서 norm-only upper bound의 unavoidable floor는

\[
\boxed{
\|\mu\|_{r'}\|c_w\|_r
\gtrsim
\frac{X}{(\log X)^{1/r}}.
}
\]

모든 `r\ge1`에 대해 이는 적어도 order `X/\log X`이고, RH target

\[
X^{1/2+\varepsilon}
\]

보다 polynomially 크다.

중요: 이것은 `M(X)`의 lower bound가 아니다. **이 prime-boundary linear representation에 norm inequality를 적용해 얻는 upper-bound certificate 자체의 lower floor**다.

---

## 7. relation to finite numerical optimization

이전 numerical optimization에서 모든 prime-boundary weights를 허용하고 full squarefree coefficient vector의 L^2 norm을 최소화했을 때

| X | N_X | exact prime-only floor | numerical full optimum |
|---:|---:|---:|---:|
| 1024 | 75 | 8.6031 | 13.5413 |
| 2048 | 137 | 11.6622 | 19.2391 |
| 4096 | 255 | 15.9375 | 27.2073 |
| 8192 | 464 | 21.5175 | 38.5367 |

이었다.

full composite constraints는 실제 optimum을 더 높이지만, branch closure에는 prime-only exact floor만으로 충분하다.

---

## 8. branch verdict

### CLOSED

다음 class는 RH proof candidate에서 닫는다.

1. finitely or infinitely many prime-boundary identities의 real signed linear combination.
2. weights를 `mu` signs와 독립적으로 최적화한 뒤 L^2/Cauchy--Schwarz로 cancellation을 얻는 방법.
3. 더 일반적으로 fixed L^r/Hölder norm만으로 coefficient size를 줄여 RH scale을 얻는 방법.

### NOT CLOSED

이 정리는 다음을 배제하지 않는다.

1. coefficient와 Möbius sign 사이의 nonlinear deterministic coupling.
2. high-order products/interactions of boundary shells.
3. prime logarithmic weights와 slack를 동시에 사용하는 nonlinear observable.
4. norm이 아니라 sign/phase/ordering information을 직접 이용하는 inequality.

---

## 현재 의미

앞선 K-wise parity invisibility와 합치면

\[
\boxed{
\text{low-order marginals도 부족하고, linear boundary averaging도 부족하다.}
}
\]

따라서 남는 formation-side frontier는

\[
\boxed{
\text{high-order nonlinear prime-weighted incomplete-boundary geometry}
}
\]

이다.

## 상태

- prime-boundary identity: `EXACT`.
- dual certificate `Av=1`: `EXACT`.
- finite L^r norm floor: `EXACT`.
- PNT asymptotic scale: `STANDARD`.
- norm-only RH route in this class: `CLOSED`.
- RH: `OPEN`.
