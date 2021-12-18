
def factorial(n: int) -> int:
    if n == 0:
        return 1
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

print(factorial(5))


# <editor-fold defaultstate="collapsed" desc="Tests">
def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
# </editor-fold>
