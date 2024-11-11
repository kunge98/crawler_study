"""
视频爬取思路：
    1.在页面源代码中找到 iframe（我爬取的网站首先就没有）
    2.从 iframe找到 m3u8文件的下载地址
    3.下载第一层m3u8文件 --> 下载第二层m3u8文件（视频存放路径）
    4.下载视频
    5.下载秘钥，进行解密操作
    6.合并所有的ts文件，生成mp4
案例总结：
    视频的片段成功爬取下来了
    代码没有怎么写，感觉有点没必要了，
    主要就是获取到网页中的 m3u8文件，然而在网页中抓包也可以获取到这个文件，
    通过第一层的 m3u8文件可以找到第二层的 m3u8文件，所以可以在网页中直接获取
    到第二层的 m3u8文件，这些在代码中可以直接省略
    但是要是将来要爬取大量的视频，这些代码是必须的，
未完成：
    多线程的代码没有加入
    视频后期的合成
    还有一个加密解密的问题，没有参与，爬取的视频没有涉及到加解密的问题
秘钥的获取：
    根据up的演示，秘钥存在于m3u8文件中，而且地址链接与视频播放地址有关系
    在页面的抓包工具中的preview也可以看到秘钥（是一个字符串）
解密：
    需要安装特定的解密库
    pip install
    from Crypto.Cipher import AES（加密方式是AES）
爬视频推荐流程：
    个人使用的话，下载量小的话，可以直接在网页中获取到最终的 m3u8文件，直接下载就行了
    没必要特别精通，了解爬起方法爬下来就行了！
"""
import os
import requests
import re
from bs4 import BeautifulSoup

if __name__ == '__main__':

    # url = 'http://halihali4.com/tv/73362/'
    #
    # # http://halihali4.com
    # s = url.split('/tv')[0]
    #
    # headers = {
    #     "":""
    # }
    #
    # resp = requests.get(url)
    #
    # resp.encoding = 'utf-8'
    # page_content = resp.text
    #
    # # print(page_content)
    #
    # # 获取页面中的27集的播放地址
    # page = BeautifulSoup(page_content, 'lxml')
    # # print(page)
    #
    # # 书写bs4表达式
    # ul = page.find('ul', id="ul_playlist_1")
    # # print(ul)
    #
    # lis_a = ul.find_all('a')
    # # print(lis_a)
    #
    # # 拿到了每一集的播放地址
    # for a in lis_a:
    #     url = a.get('href')
    #     url = s + url
    #     print(url)

    # http://halihali4.com/tv/73362/27.html
    # url2 = 'http://halihali4.com/tv/73362/27.html'
    # resp2 = requests.get(url2)
    # resp2.encoding = 'utf-8'
    # print(resp2.text)

    # n = 1
    # with open('./video/火影忍者.m3u8', mode='r', encoding='utf-8') as f:
    #     for line in f:
    #         # 去掉文件中的空格内容
    #         line = line.strip()
    #         # 如果这一行是#开始
    #         if line.startswith("#"):
    #             continue
    #
    #         # 5.下载视频片段
    #         resp3 = requests.get(line)
    #         f = open(f"./video/火影/{n}.ts", mode='wb')
    #         f.write(resp3.content)
    #         f.close()
    #         resp3.close()
    #         n += 1
    #         print(f'已经完成{n}了')



    # 合成视频
    lis = []

    with open('./video/1.m3u8', mode='r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('#'):
                continue
            line = line.strip()
            lis.append(f"./video/2/{line}")

    s = ' '.join(lis)
    os.system(f"copy /b {s} > movie.mp4")


