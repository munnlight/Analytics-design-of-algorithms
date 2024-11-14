def fib( n, memo):
    if n < 2:
         return n
    return fib(n - 1, memo) + fib(n - 2, memo)

n = 1
memo = [0] * n
memo[1] = 1

print(fib(n, memo))