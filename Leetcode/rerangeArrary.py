def arrange(list1):
    list1.sort()
    start = 0
    end = len(list1) - 1
    direction = "left"
    result = []

    while start <= end:
        if direction == "left":
            result.append(list1[start])
            start += 1
            direction = "right"

        else:
            result.append(list1[end])
            end -= 1
            direction = "left"
    print(result)
    return result


arrange([5, 8, 1, 4, 2, 9, 3, 7, 6,10])
arrange([1,2,3,4])
arrange([4,1])
arrange([4])
arrange([])
