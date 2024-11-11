# encoding=utf-8
from bs4 import BeautifulSoup
import requests
import time
import os

# 使用线程池加快爬取速度
from concurrent.futures import ThreadPoolExecutor

# 使用bs4爬取斗图王的图
# 1.通过主页面代码，提取主页面的表情包及href
# 2.获取到每张图片的src
# 3.下载图片


def download_pic(url, num):
    # url = 'http://www.bbsnet.com/doutu'

    # for i in range(8):
        # 01234567

    urll = url + '/page/' + str(num+2)

    header = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5028.0 Safari/537.36'
    }

    res = requests.get(urll, headers=header)

    page_content = res.text

    # print(page_content)

    soup = BeautifulSoup(page_content, 'lxml')

    # print(soup)

    # 得到一个列表对象
    li1 = soup.find('div', class_='mainleft').find_all('a', class_='zoom')

    # print(len(li1))
    # print(li1)

    # 对列表进行遍历循环取出，每个链接
    # 直接通过get方法拿到列表中每个的href值，从而获取到每个表情包的链接
    for i in li1:

        # print(i.get('href'))

        # 通过href来下载每张表情包
        sub_link = i.get('href')
        resp = requests.get(sub_link, headers=header)
        sub_page_content = resp.text

        sub_page = BeautifulSoup(sub_page_content, 'lxml')

        # 因为这个链接中又包含了30张图片，拿到的div变量还是一个列表
        div = sub_page.find('div', attrs={'id':'post_content'}).find_all('img')

        # print('---------',div)

        # 所以再次对div进行训练取出每一个src即可得到link
        for j in div:
            # print(j.get('src'))
            # 每张图片的link
            src = j.get('src')

            # 修改每张图的名字
            file_name = j.get('src').split('/')[-1]

            # 通过requests请求打开这个link
            img_src = requests.get(src)

            # 获取到内容，当然在这个地方是字节的形式
            respon = img_src.content

            with open('./img/' + file_name, mode='wb') as f:
                f.write(respon)
            time.sleep(1)

    f.close()
    print('over！')


if __name__ == '__main__':

    # 判断文件夹是否存在
    if not os.path.exists('./img'):
        os.makedirs('./img')

    url = 'http://www.bbsnet.com/doutu'

    # 创建100个线程池，进行爬取
    with ThreadPoolExecutor(100) as t:

        for i in range(8):

            t.submit(download_pic, url=url, num=i)









