import requests


if __name__ == '__main__':

    url = 'https://movie.douban.com/j/search_subjects?'

    # 反爬小手段
    header={
        "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5028.0 Safari/537.36'
    }

    # url里面的参数过多，将url中问号后面的内容全部写到param中，所以重新封装参数
    param = {
        'type': 'tv',
        'tag': '热门',
        'page_limit': 100,
        'page_start': 100
    }

    res = requests.get(url, params=param, headers=header)

    print(res.text)
    print(res.json())

    # 访问记得关闭
    res.close()