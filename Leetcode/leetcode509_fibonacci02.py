def fib(n):
    if n<=1:
        return n

    prev2 = 0
    prev1 = 1
    result =0
    for i in range(2, n+1):
        result = prev1 +prev2
        prev2 = prev1
        prev1 = result

    return result

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))