

# buffer = [0, 1]
def fib(x):
    if x == 0:
        return 0

    elif x == 1:
        return 1

    buffer = [0,1]
    def memoize(number):
        try:
            return buffer[number]
        except:
            buffer[number] = memoize(number-1)  + memoize(number-2)
            return buffer[number]

    return memoize(x)

# print("0:", fib(0))
# print("1:", fib(1))
# print("2:", fib(2))
# print("3", fib(3))

print(fib(3))
print(fib(4))
print(fib(6))
print(fib(7))
print(fib(8))
print(fib(9))
print(fib(10))
print(fib(11))
print(fib(12))
# print(fib(15))
# print(fib(20))
