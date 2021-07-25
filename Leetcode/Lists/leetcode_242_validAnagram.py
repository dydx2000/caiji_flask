def validAnagram(s1, s2):
    if len(s1)!= len(s2):
        return False

    dic1 = dict()
    for letter in s1:
        if letter in dic1.keys():
            dic1[letter] += 1
        else:
            dic1[letter] = 1

    print(dic1)

    for letter in s2:
        if letter not in dic1.keys():
            print("These i an error letter")
            return False

        dic1[letter] -= 1

    print(dic1)

    for i in dic1.values():
        if i != 0:
            return False
    return True

s1 = "rabbit"
s2 = "rbbait"

print(validAnagram(s1, s2))
