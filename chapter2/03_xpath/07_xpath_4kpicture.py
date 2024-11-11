import requests
from lxml import html
import os
import time
from concurrent.futures import ThreadPoolExecutor


def download_4kpic(url):

    header = {
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        'Accept-Encoding': 'utf-8'
    }

    try:
        response = requests.get(url, headers=header)
        response.raise_for_status()

        # 解决控制台输出的中文全是乱码的问题
        # 使用 response.content 而不是 response.text
        tree = html.fromstring(response.content)

        results = tree.xpath('/html/body/div[2]/div/div[3]/ul/li/a')

        if not os.path.exists('4kpic'):
            os.mkdir('4kpic')

        for res in results:
            link = res.xpath('./img/@src')
            filename = res.xpath('./img/@alt')
            filename = str(filename[0]).strip().replace(' ', '-')

            download_link = 'https://pic.netbian.com' + link[0]
            # print(download_link)
            # print(filename)

            response = requests.get(download_link)
            response = response.content

            with open('./4kpic/' + filename + '.jpg', mode='wb') as f:
                f.write(response)
            time.sleep(1)
            print('爬完一张辣~~~~')

    except Exception as e:
        print(f"下载出错：{str(e)}")


if __name__ == '__main__':

    urls = []

    for i in range(10, 50):
        url = 'https://pic.netbian.com/4kbeijing/index_' + str(i) + '.html'
        urls.append(url)

    max_threads = 100

    with ThreadPoolExecutor(max_threads) as executor:
        # 使用executor.submit()来处理每个URL
        futures = [executor.submit(download_4kpic, url) for url in urls]

    # 等待所有任务完成
    for future in futures:
        future.result()

