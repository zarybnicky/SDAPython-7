def factorial(n: int) -> int:
    factorial = 1
    if n < 0:
        print("Sorry, záporný čísla ne-e")
    elif n == 0:
        return 1
        print("Faktoriál 0 je 1")
    else:
        for i in range(1, n + 1):
            factorial = factorial * i
        print("Faktorial č.", n, "je", factorial)
        return factorial

factorial(7)
# <editor-fold defaultstate="collapsed" desc="Tests">
def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
# </editor-fold>
