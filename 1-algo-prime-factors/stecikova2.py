from typing import List
import math

primes = [2, 3, 5, 7, 11, 13, 17]

# Below function will print the
# all prime factor of given number
def get_prime_factors(num):
    # Using the while loop, we will print the number of two's that divide n
    while num % 2 == 0:
        print(2, )
        num = num / 2

    for i in range(3, int(math.sqrt(num)) + 1, 2):

        # while i divides n , print i ad divide n
        while num % i == 0:
            print(i, )
            num = num / i
    if num > 2:
        print(num)
    # calling function


num = 250
get_prime_factors(num)

# def get_prime_factors(n: int) -> List[int]:
#     return []


# <editor-fold defaultstate="collapsed" desc="Tests">
def test_prime_factors():
    assert sorted(get_prime_factors(1)) == []
    assert sorted(get_prime_factors(4)) == [2, 2]
    assert sorted(get_prime_factors(17)) == [17]
    assert sorted(get_prime_factors(27)) == [3, 3, 3]
# </editor-fold>
