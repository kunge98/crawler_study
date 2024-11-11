import requests


if __name__ == '__main__':

    # 和视频中代码一样，可能就是网站改进了反爬机制

    query = input('你想搜什么内容')

    url = f'https://www.sogou.com/web?query={query}'

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5028.0 Safari/537.36'
    }

    # get的请求方式
    res = requests.get(url, headers=header)
    print(res)
    print(res.text)

    # 访问记得关闭
    res.close()

