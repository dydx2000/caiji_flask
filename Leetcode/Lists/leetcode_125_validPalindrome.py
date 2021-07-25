import re


def validPalindrome(string1):
    # string1 = remove(string1)
    # string1 = re.sub("[\W_]+","",string1)
    # string1 = "".join(re.findall(r'[a-zA-Z0-9]',string1))
    string1 = re.sub("[\W_]+", "", string1)

    string1 = string1.lower()

    if len(string1) <= 2:
        return True
    left = 0
    right = len(string1) - 1
    while left < right:
        if string1[left] != string1[right]:
            # print(string1[left])
            # print(string1[right])

            # print("not equal")
            return False
        left += 1
        right -= 1
    return True


print(validPalindrome("A m_an, a plan,  a_ kcka nal: Panama"))
print(validPalindrome("ak"))
