"""Finite verification of the Chebyshev event-energy identities.

Default cutoff is intentionally modest. Increase X if desired.
This script verifies algebraic equality between
  H = integral_2^x(theta(t)-t)dt + 0.5(theta(x)-x)^2
and
  H = 0.5 theta(x)^2 - sum_{p<=x} p log p + 2
at prime cutoffs, and records the prime-event jump formula.
"""

import math

X = 1_000_000

is_prime = bytearray(b"\x01") * (X + 1)
is_prime[0:2] = b"\x00\x00"
for p in range(2, int(X**0.5) + 1):
    if is_prime[p]:
        start = p * p
        is_prime[start:X+1:p] = b"\x00" * (((X - start) // p) + 1)

primes = [p for p in range(2, X + 1) if is_prime[p]]

theta = math.log(2.0)
weighted = 2.0 * math.log(2.0)
E = theta - 2.0
I = 0.0
prev = 2
H_prev = 0.5 * theta * theta - weighted + 2.0

max_identity_error = 0.0
max_jump_error = 0.0
max_H_after_3 = -float("inf")
argmax_H = None

for p in primes[1:]:
    gap = p - prev

    # Integrate the linear segment E(t)=E(prev+)-(t-prev).
    I += E * gap - 0.5 * gap * gap

    L = math.log(p)
    E_before = E - gap
    E = E_before + L
    theta += L
    weighted += p * L

    H_dynamic = I + 0.5 * E * E
    H_prime_sum = 0.5 * theta * theta - weighted + 2.0
    max_identity_error = max(max_identity_error, abs(H_dynamic - H_prime_sum))

    jump_actual = H_prime_sum - H_prev
    jump_formula = L * (E - 0.5 * L)
    max_jump_error = max(max_jump_error, abs(jump_actual - jump_formula))

    if p >= 3 and H_prime_sum > max_H_after_3:
        max_H_after_3 = H_prime_sum
        argmax_H = p

    H_prev = H_prime_sum
    prev = p

print(f"X={X}")
print(f"prime count={len(primes)}")
print(f"max identity error={max_identity_error:.6e}")
print(f"max jump error={max_jump_error:.6e}")
print(f"max H for prime p>=3: H({argmax_H})={max_H_after_3:.12f}")
print("finite inequality verified" if max_H_after_3 < 0 else "finite inequality FAILED")
