from typing import List

primes = [2, 3, 5, 7, 11, 13, 17]


def get_prime_factors(n: int) -> List[int]:
    factors = []
    for prime in primes:
        if n % prime != 0:
            continue
        else:
            while n % prime == 0:
                n = n // prime
                factors.append(prime)
    return factors


# <editor-fold defaultstate="collapsed" desc="Tests">
def test_prime_factors():
    assert sorted(get_prime_factors(1)) == []
    assert sorted(get_prime_factors(4)) == [2, 2]
    assert sorted(get_prime_factors(17)) == [17]
    assert sorted(get_prime_factors(27)) == [3, 3, 3]
# </editor-fold>
