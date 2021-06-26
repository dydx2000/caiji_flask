count = 0


def bubble_sort(alist):
    global count
    n = len(alist)

    # print(n)

    for j in range(n - 1, 1, -1):
        # nonlocal change
        change = False
        for i in range(j):
            count += 1
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                # print(i)

                print(alist)
                change = True
        if not change:
            print(change)
            print("break")
            break

alist = [7, 1, 96, 5, 3, 6, 44, 22, 99, 11]
alist = [1,3,8,2,5,4,9,82,23,6,19,7]
# alist = [1,2,3,4,7,6,5]

bubble_sort(alist)
print(alist)
print(count)
