def movezeroes(nums):
    res0 = list()
    res1 = list()
    for num in nums:
        if num == 0:
            res0.append(num)
        else:
            res1.append(num)

    return res1 + res0


def movezeroes2(nums):
    for i in range(len(nums) - 1):
        if nums[i] != 0:
            break
        for j in range(i, len(nums) - 1):
            if nums[j] == 0:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    print(nums)


def movezeroes3(nums): #  如果不为０，j＋＋
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1

    for i in range(j, len(nums)):
        nums[i] = 0

    return nums


if __name__ == '__main__':
    print(movezeroes([0, 1, 0, 3, 12]))
    movezeroes2([0, 1, 0, 3, 12])
    print(movezeroes3([0, 1, 0, 3, 12]))
