import requests

baidu ="https://www.baidu.com"

response = requests.get(baidu)


print(response.headers)

# 请求对头部信息
print(response.request.headers)

