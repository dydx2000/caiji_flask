def sorts(arr):
    tempji = []
    tempou = []
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            tempji.append(arr[i])
            # print(arr)
        else:
            tempou.append(arr[i])
    return tempou + tempji


def sorts2(arr):
    j = 0
    # print(j)
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            for k in range(j, len(arr)):
                if arr[k] % 2 == 0:
                    arr[i], arr[k] = arr[k], arr[i]
                    # print(arr)
                    j = k
                    break
    return arr


def sorts3(arr):
    j = len(arr)-1
    for i in range(len(arr)):
        if i>=j:
            break
        if arr[i] % 2 == 1:
            for k in range(j, -1, -1):
                if arr[k] % 2 == 0:
                    arr[i], arr[k] = arr[k], arr[i]
                    j=k
                    break

    return arr


if __name__ == '__main__':
    # # print(1%2)
    print(sorts(arr=[3, 1, 5, 2, 6, 8, 4]))
    print(sorts2(arr=[3, 1, 5, 2, 6, 8, 4]))
    print(sorts3(arr=[3, 1, 5, 2, 6, 8, 4]))
