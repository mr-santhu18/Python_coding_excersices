# recursive function

def fibonacci(n):
    if n<=0:
        return 0
    elif n== 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
print(fibonacci(3)) # 0 1 1 2

# 0 1 1 2 3 5 8 13 21 

# direct recursion

def factorial(n):
    if n ==1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5)) # 1x2x3x4x5