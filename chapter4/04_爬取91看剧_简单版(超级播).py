"""
科普：爬取视频
会将一个视频拆分成各种切片，记录在一个文件中
而这个文件就是m3u8，里面最少包含了视频的播放顺序、视频的存放路径等等
找到m3u8文件（各种手段）
通过m3u8下载所有的ts文件
通过各种手段（不仅是编程），把ts文件合并为一个mp4文件

案例抓取91看剧视频步骤：
1.拿到首页面的html页面源代码
2.从源代码中提取到m3u8的url
3.下载m3u8
4.读取m3u8文件，下载视频
5.合并视频
"""

import requests
import time
import re
import os

if __name__ == '__main__':


    # 播放源一定要选 超级播 里面的视频并且是可以包房的，不然根本爬取不到url
    url = 'https://91kanju2.com/vod-play/750-1-2.html'

    header = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5057.3 Safari/537.36"
    }

    # 请求的第一次说连接有问题，使用下面的while连接之后还是出现问题，又切换回现在的代码就好了
    resp = requests.get(url, headers=header)

    print(resp.text)

    # while True:
    #     try:
    #         response = requests.get(url, headers=header, timeout=(30, 50), verify=False)
    #         break
    #     except:
    #         print("Connection refused by the server..")
    #         print("Let me sleep for 5 seconds")
    #         print("ZZzzzz...")
    #         time.sleep(5)
    #         print("Was a nice sleep, now let me continue...")
    #         continue

    # 书写寻找页面中m3u8的正则表达式
    obj = re.compile(r"url: '(?P<url>.*?)',", re.S)

    # 提取页面中m3u8的url地址
    m3u8_url = obj.search(resp.text).group('url')

    # https://m3api.awenhao.com/index.php?note=kkRcd7fkehm9zyqpawr4n&raw=1&n.m3u8
    print(m3u8_url)

    # 3.下载m3u8文件
    if not os.path.exists('./video'):
        os.makedirs('./video')

    resp2 = requests.get(m3u8_url, headers=header)
    with open('./video/白夜追凶.m3u8', mode='wb') as f:
        f.write(resp2.content)

    resp2.close()
    # print('over!')

    # 4.解析m3u8文件
    n = 1
    with open('./video/白夜追凶.m3u8', mode='r', encoding='utf-8') as f:
        for line in f:
            # 去掉文件中的空格内容
            line = line.strip()
            # 如果这一行是#开始
            if line.startswith("#"):
                continue

            # 5.下载视频片段
            resp3 = requests.get(line)
            f = open(f"./video/v/{n}.ts", mode='wb')
            f.write(resp3.content)
            f.close()
            resp3.close()
            n += 1
            print(f'已经完成{n}了')





