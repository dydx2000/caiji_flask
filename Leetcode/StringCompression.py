str1 = input("请输入要圧缩的单词：　")
sum = 1
result = ""
length = len(str1)
print(length)
for i in range(0, length):
    if i < length - 1:
        # print("round %s" % i)

        if str1[i] == str1[i + 1]:
            sum += 1
        else:
            result = result + str1[i] + str(sum)
            print(result)
            sum = 1
    else:

        # print("round %s" % i)

        if str1[i] != str1[i - 1]:
            sum = 1
            result = result + str1[i] + str(sum)

        if str1[i] == str1[i - 1]:
            result = result + str1[i-1] + str(sum)

print(result)
