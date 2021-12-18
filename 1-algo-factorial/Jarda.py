# BY JARDA
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# <editor-fold defaultstate="collapsed" desc="Tests">
def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
# </editor-fold>
