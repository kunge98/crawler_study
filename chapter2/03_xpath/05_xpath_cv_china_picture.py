import requests
from lxml import html
import os
import time
from concurrent.futures import ThreadPoolExecutor


def download_pic(url):
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=header)
        response.raise_for_status()

        tree = html.fromstring(response.text)
        results = tree.xpath('/html/body/div[1]/section/div/div[2]/section/div[4]/section/div/figure/a')

        if not os.path.exists('CV_china2'):
            os.mkdir('CV_china2')

        for res in results:
            alt = res.xpath('./img/@alt')
            filename = alt[0].split('图片下')[0].split(' ')
            filename = ''.join(filename)
            print(filename)

            data_src = res.xpath('./img/@data-src')
            download_path = "https:" + str(data_src[0])

            img_src = requests.get(download_path)

            response = img_src.content

            with open('./CV_china2/' + filename + '.jpg', mode='wb') as f:
                f.write(response)
            time.sleep(1)
            print('爬完一张辣~~~~')
        print('over！')
    except Exception as e:
        print(f"下载出错：{str(e)}")


if __name__ == '__main__':
    urls = []
    x = input("使用拼音的形式，输入你想要搜的图片：")
    for i in range(2, 30):
        url = 'https://www.vcg.com/creative-image/' + str(x) + '/?page=' + str(i)
        urls.append(url)

    max_threads = 100

    # with ThreadPoolExecutor(max_threads) as executor:
    #     for url in urls:
    #         executor.map(download_pic, urls)

    with ThreadPoolExecutor(max_threads) as executor:
        # 使用executor.submit()来处理每个URL
        futures = [executor.submit(download_pic, url) for url in urls]

    # 等待所有任务完成
    for future in futures:
        future.result()
