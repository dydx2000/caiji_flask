import requests

baidu = "https://www.baidu.com/s"

session = requests.session()
response = requests.get(baidu)
response = session.get(baidu)

print(response.headers)

# 请求对头部信息   
print(response.request.headers)

headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/53"
                  "7.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
}

params = {
    "wd": "自动化测试"
}

response = requests.get(baidu, params=params, headers=headers)
response = requests.get(baidu, params=params)

response.encoding = 'utf-8'
with open('temp_wd.html', 'wb') as f:
    f.write(response.content)
