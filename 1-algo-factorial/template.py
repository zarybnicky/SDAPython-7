
def factorial(n: int) -> int:
    n = 2
    factorial = 1

    for i in range(1, n + 1):
        factorial = fact * i


# <editor-fold defaultstate="collapsed" desc="Tests">
def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
# </editor-fold>
