def func_out():
    def func_in():
        print("I am func_in")

    return  func_in


f = func_out()
print(type(f))

f()