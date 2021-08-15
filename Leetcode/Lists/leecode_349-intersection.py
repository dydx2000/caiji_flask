def intersection(array1, array2):
    set1 = set(array1)
    set2 = set(array2)
    res = list()
    for num in set1:
        if num in set2:
            res.append(num)
    return res


if __name__ == '__main__':
    print(intersection([1, 2, 2, 1], [2, 2]))
    print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
