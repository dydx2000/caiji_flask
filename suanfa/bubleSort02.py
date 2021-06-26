count = 0


def bubble_sort(alist):
    global count
    n = len(alist)

    # print(n)

    for j in range(n-1):
        # print(j)
        for i in range(n-1-j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                # print(i)
                print(alist)
                count += 1


alist = [7, 1, 10, 5, 3, 6, 44, 22, 99, 11]

bubble_sort(alist)
print(count)
