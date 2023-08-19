#Author: Gustavo Fernandez
print('Serie de Fibonacci en Phyton')

def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n - 1) + fib(n - 2)

print(fib(10))