def factorial(n: int) -> int:
        if n < 0:
            return 0
        elif n == 0 or n == 1:
            return 1
        else:
            fact = 1
            while (n > 1):
                fact *= n
                n -= 1
            return fact

    # Driver Code
    num = 5;
    print("Factorial of", num, "is",
          factorial(num))




# <editor-fold defaultstate="collapsed" desc="Tests">
def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
# </editor-fold>
