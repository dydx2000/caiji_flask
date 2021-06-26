print("格式化的内容是 |%020.2s|" %'hello')
print("格式化的内容是 |%+20s|" %'hello')
print("格式化的内容是 |%-20s|" %'hello')
print("格式化的内容是 |%-20s|" % 4345)

print("==================================")

template = "格式化的数字是: |%+10d|"
print(template % 13)
print(template % +13)
print(template % -13)


print("==================================   ")

template = "格式化的数字是: |%010d|"
print(template % 13)
print(template % +13)
print(template % -13)

# 浮点数
print("++++++++++++++++++")
template ="格式化的数字是 |%20.2f|"  #四舍五入
print(template %123455.1231432)
print(template %123455.1)