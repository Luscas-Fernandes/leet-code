def factorial_recursive(n):
    if n <= 1:
        return 1
    
    return n * factorial_recursive(n - 1)

def factorial(n):
    result = 1

    for i in range(n, 0, -1):
        result *= i
    
    return result
""" 
print(factorial_recursive(1))
print(factorial_recursive(5)) """
print(factorial(5))