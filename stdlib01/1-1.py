import os

# 系统相关内容
print(os.name)
print(os.environ)

for i in os.environ:
    print(i)
print(os.sep)
print(os.pathsep)


# os.mkdir("stdemo")
# os.rmdir("stdemo")
print(os.getcwd())