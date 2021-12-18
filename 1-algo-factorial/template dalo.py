#dalibor hriadel


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24




def recur_factorial(n):  
       if n == 1:  
           return n  
       else:  
           return n*recur_factorial(n-1)  
   
num = int(input("Enter a number: "))  
    
if num < 0:  
    print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
    print("The factorial of 0 is 1")  
else:  
    print("The factorial of",num,"is",recur_factorial(num))  