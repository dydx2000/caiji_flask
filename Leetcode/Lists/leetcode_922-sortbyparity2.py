def sortArrayByParity2(arr):
    # print(len(arr))

    if len(arr)%2!=0:
        return
    res = []

    dic_odd ={}
    dic_even ={}

    for i in range(len(arr)):
        if i % 2 == 0:

            if arr[i] % 2 == 0:
                res.append(arr[i])
            else:
                res.append(0)
                dic_odd[i]=arr[i]


        else:

            if arr[i] % 2 != 0:
                res.append(arr[i])
            else:
                res.append(0)
                dic_even[i] = arr[i]

    # print(dic_odd)
    # print(dic_even)

    i=0
    even_values = list(dic_even.values()) #偶数
    # print(even_values)
    for j in dic_odd.keys():
        res[j]=even_values[i]
        i+=1

    i=0
    odd_values = list(dic_odd.values()) # 奇数
    # print(odd_values)

    for j in dic_even.keys():
        res[j]=odd_values[i]
        i+=1

    return res

def sortArrayByParity(arr):
    pointer=1
    for i in range(0,len(arr),2):
        if arr[i]%2==1:
            for j in range(pointer,len(arr),2):
                if arr[j]%2==0:
                    pointer=j
                    arr[i],arr[j]=arr[j],arr[i]
                    break
    return arr




if __name__ == '__main__':
    print(sortArrayByParity2([1,2,3,4,5,6]))
    print(sortArrayByParity([18,2,3,4,5,7]))
    print("*888888888888888********************")
    print(sortArrayByParity([1,2,3,4,5,6]))
    print(sortArrayByParity2([18,2,3,4,5,7]))


    # dic1= {1:2,2:5,4:2,6:0,9:11}
    # print(type(list((dic1.keys()))))

