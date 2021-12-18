from typing import List

primes = [2, 3, 5, 7, 11, 13, 17]

def get_prime_factors(n: int) -> List[int]:
    lst = []
    for prime in primes:
        while n % prime == 0:
            lst.append(prime)
            n /= prime
    return lst

print(get_prime_factors(27))

# <editor-fold defaultstate="collapsed" desc="Tests">
def test_prime_factors():
    assert sorted(get_prime_factors(1)) == []
    assert sorted(get_prime_factors(4)) == [2, 2]
    assert sorted(get_prime_factors(17)) == [17]
    assert sorted(get_prime_factors(27)) == [3, 3, 3]
# </editor-fold>
