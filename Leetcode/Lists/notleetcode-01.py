def onesecond(nums):
    nums.sort()
    print(nums)
    start = 0
    end = len(nums)-1
    direction = "right"
    res=[]
    for i in nums:
        if start<=end:
            if direction=="right":
                res.append(nums[start])
                start+=1
                direction="left"
            else:
                res.append(nums[end])
                end-= 1
                direction = "right"
    return res

if __name__ == '__main__':
    print(onesecond([1, 2, 3, 4, 6, 4, 1, 3, 0, 8, 123, 2, 9]))
