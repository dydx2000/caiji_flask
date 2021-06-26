def twosum(nums,target):
    map1 = {}
    answers=[]
    for i in range(len(nums)):
        complement = target - nums[i]
        # print(map1.keys())
        if complement in map1.keys():
            answers.append ((map1[complement],i))
        else:
            map1[nums[i]]=i

    return answers

print(twosum([2,3,11,7],9))
print(twosum([2,3,11,7,4,2,3,1,3,4,5,523,32,4534,5534,23,5,3,545,23,8,9,54],16))
