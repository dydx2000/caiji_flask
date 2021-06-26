template = "格式化的内容是: {}"
print(template.format("hello"))


print("{0:+<20.3s} {1} {0}".format("1232323",2232323))
print("{1:+>20,.3f} {1} {0}".format("1232323",2232323.0))
print("{0:+^20.3s} {1} {0}".format("1232323",2232323))


print('|{:^d}|{:^d}|'.format(13,-13))

# index
print("{name} {age:010.3f} {gender}".format(name='john',age=19,gender='male'))
name='john'
age=19
gender='male'

print(f"我是{name.capitalize()}")