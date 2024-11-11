import requests
from lxml import html
import os
import time
from concurrent.futures import ThreadPoolExecutor


def download_video(url):

    header = {
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=header)
        response.raise_for_status()

        tree = html.fromstring(response.text)
        # /html/body/div[1]/div[1]/div/div/div[4]/div[1]/div/section/article[7]/div/a/div[2]

        # 视频的界面只是图片，需要获取到当前的视频图片的地址，地址换成视频就可以进行下载了

        results = tree.xpath('/html/body/div[1]/div[1]/div/div/div[4]/div[1]/div/section/article')

        if not os.path.exists('video2'):
            os.mkdir('video2')

        # https://pic.jpfhz.com/d/file/202008/81f794113fa99ccf92a741dcadd16c26.jpg
        for res in results:

            # 图片的下载链接
            data_link = res.xpath('./div/a/div[1]/picture/img/@src')
            download_path = "https:" + str(data_link[0])

            # 图片名字
            data_src = res.xpath('./div/a/div[1]/picture/img/@alt')
            filename = data_src[0].split('视频下')[0].split(' ')
            filename = ''.join(filename)

            # 视频的初始下载链接
            video_link = res.xpath('./div/a/div[1]/picture/source[2]/@data-srcset')
            # print(video_link)

            med_name, video_old_name = str(video_link[0]).split('/snapshot/')[0], str(video_link[0]).split('/snapshot/')[-1]  # //gossv.cfp.cn/videos   VCG42N1500744125
            # print(med_name, video_old_name)

            # 最终的链接形式为：https:  //gossv.cfp.cn/videos  /mts_videos/medium/  VCG42N1500744125  .mp4
            video_link = 'https:' + med_name + '/mts_videos/medium/' + video_old_name.split('_')[0] + '.mp4'

            print(filename)
            # print(video_link)

            # 拿到视频的下载路径
            img_src = requests.get(video_link, headers=header)
            # print(img_src)

            with open('./video2/' + filename + '.mp4', mode='wb') as f:
                f.write(img_src.content)
            time.sleep(1)
            print('爬完辣~~~~')
        print('over！')

    except Exception as e:
        print(f"下载出错：{str(e)}")


if __name__ == '__main__':

    urls = []

    x = input("使用拼音的形式，输入你想要搜的视频：")

    for i in range(2, 10):
        url = 'https://www.vcg.com/creative-video-search/' + str(x) + '/?page=' + str(i)
        urls.append(url)
    # https: // gossv.cfp.cn / videos / mts_videos / medium / VCG2224161816.mp4
    # print(urls)

    max_threads = 100

    with ThreadPoolExecutor(max_threads) as executor:
        for url in urls:
            executor.map(download_video, urls)
