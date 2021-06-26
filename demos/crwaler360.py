
import requests

if __name__ == '__main__':
    keyword = "123sad"
    keyword = input("请输入你想搜索的内容")
    try:
		#添加headers防止被最简单的反爬虫阻止，在chrome按F12后点击Network中一个下滑查看
        headers = {
            'Connection': 'Keep-Alive',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'User-Agent': 'Mozilla/6.1 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Host': 'www.so.com',
            'Referer': 'https://www.so.com'
        }
        page = 1
        #GET参数列表
        kv = {'q': keyword, 'ie': 'utf-8', 'pn': page}

        # requests.ReadTimeout(60)
        r = requests.get("http://www.so.com/s", headers=headers,
                         params=kv)
        print('url:'+r.request.url)
        r.raise_for_status()
        html = r.text
        print(html)
    except requests.HTTPError as a:
        print(a)
        print("爬取失败")
    except:
        print('失败')

