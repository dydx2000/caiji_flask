import random

print(random.randint(1,100))
print(random.random())

print(random.randrange(1,101,2))

print(random.uniform(11.1,16.8))


# 非数字类型的随机抽样
targetList =['a','b','c','d','e','f','g']

print(random.choice(targetList))
random.shuffle(targetList)
print(targetList)


print(random.sample(targetList,4))

import string
x = string.ascii_letters
print(x)
y = string.digits
print(y)

print(string.hexdigits)

print(string.punctuation)

a = set(range(1,11))
print(a)

x,y,z =1,2,3

x,y,z = map(str,range(3))

print(x,y,z)
print(type(x))