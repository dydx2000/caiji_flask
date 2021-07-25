
def isValid(s):
    dict1 ={"{":"}","(":")","[":"]"}

    stack  = []
    for i in range(len(s)):
        if s[i] in dict1.keys():
            stack.append(dict1[s[i]])
        else:
            if stack.pop() != s[i]:
                return False

    if len(stack)!=0:
        return False
    else:
        return True

print(isValid("({)}"))