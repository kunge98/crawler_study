import time
import requests
from bs4 import BeautifulSoup
import re
import os
from concurrent.futures import ThreadPoolExecutor
import random
import urllib3
import socket


def download_image():

    # urllib3.disable_warnings()

    # socket.setdefaulttimeout(20)


    # 想要爬取所有的网页，感觉还得加一个for
    # for i in range(1,40):
    #     if i == 1:
    #         url = 'https://www.ypfhk.com/you/index.html'
    #     else:
    #         url = 'https://www.ypfhk.com/you/index_'+ i +'.html'

    # 首页面的链接地址
    url = 'https://www.ypfhk.com/you/index_10.html'

    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47",
        # "Connection":"close"
    }

    resp = requests.get(url, headers=header)
    resp.encoding = 'utf-8'
    page_content = resp.text
    # print(page_content)


    # 每个人的链接需要加上一段，所以先要获取到后面的一段链接
    page_content = BeautifulSoup(page_content, 'lxml')
    ul = page_content.find_all('ul')[1]
    # print(ul)

    obj = re.compile(r'<li>.*?<a href="/you/(?P<link>.*?)"><span>.*?</span></a>.*?'
                     r'<a href=".*?.html"><h3>(?P<name>.*?)</h3></a>.*?</li>', re.S)

    result = re.finditer(obj, str(ul))
    # print(result)

    links = []
    names = []

    # 'https://www.ypfhk.com/you/ssyouya.html'
    for i in result:

        url2 = url.split('index')[0] + i.group('link')
        # 拿到每个人专属的网站链接
        links.append(url2)
        names.append(i.group('name'))
        # print(url2)

    # print(links)
    # print(names)

    for i in range(len(links)):
        resp2 = requests.get(links[i])

        resp2.encoding='utf-8'
        page_content2 = resp2.text
        # print(page_content2)

        page_content3 = BeautifulSoup(page_content2, 'lxml')
        result2 = page_content3.find('ul', class_='page_starphoto imgload').find_all('img')

        # 创建文件夹
        if not os.path.exists('./image/{}'.format(names[i])):
            os.makedirs('./image/{}'.format(names[i]))

        for j in result2:
            nam = j.get('alt')
            lin = j.get('src')

            lin = requests.get(url=lin)

            with open('./image/{}/{}.jpg'.format(names[i], nam), mode='wb') as f:
                f.write(lin.content)
                f.close()

            time.sleep(1)

        print('over！')


def download_image2():

    start_time = time.time()

    # with ThreadPoolExecutor(100) as t:
    #     for i in range(30):
    #         t.submit(download_image)
    # download_image()

    urllib3.disable_warnings()

    # socket.setdefaulttimeout(20)

    # 想要爬取所有的网页，感觉还得加一个for
    # for i in range(1,40):
    #     if i == 1:
    #         url = ''
    #     else:
    #         url = ''+ i +'.html'

    # 首页面的链接地址
    url = 'https://www.jpfhz.com/you/index.html'

    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47",
        # "Connection":"close"
    }

    resp = requests.get(url, headers=header)
    resp.encoding = 'utf-8'
    page_content = resp.text
    # print(page_content)

    # 每个人的链接需要加上一段，所以先要获取到后面的一段链接
    page_content = BeautifulSoup(page_content, 'lxml')
    ul = page_content.find_all('ul')[1]
    # print(ul)

    obj = re.compile(r'<li>.*?<a href="/you/(?P<sub_link>.*?)"><span>.*?</span></a>.*?'
                     r'<a href=".*?.html"><h3>(?P<person_name>.*?)</h3></a>.*?</li>', re.S)

    # 获取到每个人的半下载地址和每个人的姓名
    result = re.finditer(obj, str(ul))

    # 得到当前页面所有人的作品
    for i in result:
        # 得到不完整链接和人名
        # print(i.group('sub_link'))
        # print(i.group('person_name'))

        # 拿到每个人专属的网站链接
        #
        url2 = url.split('index')[0] + i.group('sub_link')
        # 张三
        person_name = i.group('person_name')

        resp2 = requests.get(url=url2, headers=header)
        resp2.encoding = 'utf-8'
        # 获取到每个人的作品
        page_content2 = resp2.text
        # print(page_content2)

        # 开始解析
        page_content2 = BeautifulSoup(page_content2, 'lxml')

        # 得到每个作品对应的img标签（里面包含着重要的src和alt）
        result2 = page_content2.find('ul', class_='page_starphoto imgload').find_all('img')

        # 创建文件夹，名字就是上面的 person_name
        if not os.path.exists('./image/{}'.format(person_name)):
            os.makedirs('./image/{}'.format(person_name))

        # 下载个人作品
        for j in result2:
            # 每5张休息10秒钟
            if(j%5 ==0):
                print('下完5张了，让我休息一下...')
                time.sleep(10)
            print('图片下载过程开始了....')
            # 得到具体的每张图片的下载地址和名称（用作给每张图片命名）
            works_number = j.get('alt')
            download_link = j.get('src')

            resp3 = requests.get(download_link, headers=header)

            with open('./image/{}/{}.jpg'.format(person_name, works_number), mode='wb') as f:
                f.write(resp3.content)
            resp3.close()
            print('图片下载完成，响应正在关闭...请等待3秒钟...')
            time.sleep(3)
        print('个人作品封面下载完成...请等待30秒钟...')
        time.sleep(30)

    end_time = time.time()

    print('总计用时', end_time-start_time)


if __name__ == '__main__':
    download_image2()

