import requests

baidu ="https://www.baidu.com"

response = requests.get(baidu)


print(response)
print(response.status_code)
# print(response.content)
# print(response.text)
#
# print(response.encoding)
# print(response.content.decode('utf-8'))

# 设置解码子符集
response.encoding ='utf-8'
print(response.content)
# 用编码解码content
print(response.text)
