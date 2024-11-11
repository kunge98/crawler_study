import os
import time
from lxml import etree
from selenium import webdriver
from concurrent.futures import ThreadPoolExecutor


def download_novel(url):
    driver = webdriver.Edge()
    # driver.implicitly_wait(5)

    driver.get(url)

    while driver.execute_script("return document.readyState") != "complete":
        time.sleep(1)

    text = driver.page_source
    # print(text)

    # 加载html的源码
    html = etree.HTML(text)

    # 获取网页中的小说标题
    chapter = html.xpath('/html/body/div[1]/div[4]/div/div[2]/h1/text()')
    # print(str(chapter[0]).strip())

    # 获取网页中的小说内容
    contents = html.xpath('/html/body/div[1]/div[4]/div/div[3]/text()')

    if not os.path.exists('./novel2'):
        os.mkdir('./novel2')
    # folder = './novel'

    with open('./novel2/' + str(chapter[0]).strip() + '.txt', 'w') as file:
        for res in contents:
            print(str(res).strip())
            file.write(str(res).strip())
    file.close()
    print('success！')


if __name__ == '__main__':

    urls = []
    # 斗破苍穹的链接索引5785-7410
    for i in range(5785, 6295):
        url = 'https://www.ibiquges.org/7/7877/359' + str(i) + '.html'
        urls.append(url)
    # print(len(urls), urls)

    # 单线程
    # for url in urls:
    #     download_novel(url)

    # 您使用了executor.map()来映射download_novel函数到一组URL，但是在这里，您意图对每个URL调用download_novel，
    # 但实际上，executor.map()的工作方式是将download_novel函数并行应用于所有URL。
    # 这导致了Selenium不停地打开多个网页，因为每个线程都在尝试打开所有的URL。
    # 错误代码：
    # with ThreadPoolExecutor(max_threads) as executor:
    #     for url in urls:
    #         executor.map(download_novel, urls)

    max_threads = 5
    with ThreadPoolExecutor(max_threads) as executor:
        # 使用executor.submit()来处理每个URL
        futures = [executor.submit(download_novel, url) for url in urls]

    # 等待所有任务完成
    for future in futures:
        future.result()
