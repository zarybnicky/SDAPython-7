from typing import List

# 4 = 2 * 2
# 9 = 3 * 3
# 27 = 3 * 3 * 3

# % (modulo, zbytek po dělení)
# 5 % 2 = 1

# n == 4:
# 4 % 2 = 0?
# => 2 is a prime factor of 4 == append to list of factors, 4 / 2 = 2
# => 2 % 2 = 0?
# => 2 is a prime factor of 2 == append to list of factors, 2 / 2 = 1
# => 2 / 2 == 1, můžeme skončit

primes = [2, 3, 5, 7, 11, 13, 17]


def get_prime_factors(n: int):
    factors = []
    for prime in primes:
        while n % prime == 0:
            factors.append(prime)
            n /= prime

    return factors


# <editor-fold defaultstate="collapsed" desc="Tests">
def test_prime_factors():
    assert sorted(get_prime_factors(1)) == []
    assert sorted(get_prime_factors(4)) == [2, 2]
    assert sorted(get_prime_factors(17)) == [17]
    assert sorted(get_prime_factors(27)) == [3, 3, 3]
# </editor-fold>
