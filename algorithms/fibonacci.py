def fibonacci_list(n):
    fibNumbers = [0, 1]
    l, r = 0, 1 
    
    for _ in range(n - 1):
        fibNumbers.append(fibNumbers[l] + fibNumbers[r])
        l+= 1
        r+=1

    return fibNumbers[r]


def fibonacci(n): # No List approach
    a, b = 0, 1

    for _ in range(n):
        temp = a
        a = b
        b = temp + b        

    return a

def fibonacci_recursive(n):
    if n <= 1:
        return n
    
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_recursive_memoization(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n
    
    memo[n] = fibonacci_recursive_memoization(n-1, memo) + fibonacci_recursive_memoization(n-2, memo) 
    return memo[n]

print(fibonacci(6))
print(fibonacci_list(6))
print(fibonacci_recursive(6))
print(fibonacci_recursive_memoization(6))
