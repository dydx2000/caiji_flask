import time

start_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001):
        c = 1000-b-a
        if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
            print("a: ", a, "b", b,"c", c)
end_time = time.time()

print("所花费时间:", end_time - start_time)
