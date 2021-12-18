from typing import List

primes = [2, 3, 5, 7, 11, 13, 17]

def get_prime_factors(n: int) -> List[int]:
    result = []
    for prime in primes:
        while n % prime == 0:
            result.append(prime)
            n /= prime
    return result

get_prime_factors(12)


# <editor-fold defaultstate="collapsed" desc="Tests">
def test_prime_factors():
    assert sorted(get_prime_factors(1)) == []
    assert sorted(get_prime_factors(4)) == [2, 2]
    assert sorted(get_prime_factors(17)) == [17]
    assert sorted(get_prime_factors(27)) == [3, 3, 3]
# </editor-fold>
