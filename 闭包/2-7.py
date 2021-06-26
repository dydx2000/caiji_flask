origin =0

def creator(start):
    def gogo(step):
        nonlocal start
        target = start + step
        start = target
        return target
    return gogo

f =creator(origin)

print(f(2))
print(f(3))
print(f(6))