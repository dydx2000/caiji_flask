def func_out():
    rate = 6

    def transfer(dollar):
        return dollar * rate

    return transfer

f = func_out()
print(f(10))