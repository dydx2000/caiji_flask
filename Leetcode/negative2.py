def negetive(list1):
    j = len(list1) - 1

    for i in range(len(list1) -1, -1, -1):
        # print("list i: ", list1[i])
        # print("list1 j: ", list1[j])
        if list1[i] > 0:
            # print("list i: ",list1[i])
            # print("list1 j: ",list1[j])
            if list1[j] < 0 and i != j:
                list1[i], list1[j] = list1[j], list1[i]

            j -= 1

    return list1


a = negetive([1, 3, 4, 3, -5, -7, -9, 2, 44, 34, -87, 23, 23])
print(a)
b = negetive([12, 11, -13, -5, 6, -7, 5, -3, -6])
print(b)
