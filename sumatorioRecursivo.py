def sumatorio(x):
    if x > 0:
        return x + sumatorio(x - 1)
    else:
        return 0

print(sumatorio(100))

def factorial(x):
    if x > 0:
        return x * factorial(x - 1)
    else:
        return 1
    
print(factorial(5))