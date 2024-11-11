# -*- encoding:utf8 -*-

import requests
import os
# 爬取梨视频的视频，爬取的视频地址必须经过上一个地址才可以正确爬取
# 反反爬机制，可以加入防盗链（Referer溯源），爬取视频

# bug找了一天，终于找到了
# 原因是脑子里面混了浆糊，把视频的链接地址复制错了！！！

# 现在已经实现了梨视频的视频爬取
# 只需要提供原视频地址

if __name__ == '__main__':

    # 页面中想要下载的视频路径
    url = 'https://www.pearvideo.com/video_1760884'

    cont_id = url.split('_')[-1]
    # print(cont_id)

    # 源代码中视频的路径
    vedioStatus = 'https://www.pearvideo.com/videoStatus.jsp?contId={}&mrd=0.9365224186033843'.format(cont_id)
    # print('==============',vedioStatus)

    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5028.0 Safari/537.36',
        # 防盗链
        'Referer' : url
    }
    # 手动设定响应数据的编码格式

    res = requests.get(vedioStatus, headers=header)

    print(res)
    print(res.text)

    dict = res.json()

    # 获取到视频的url，但是url地址中的一部分得进行替换
    # python基本语法是获取videoInfo下面的videos再到下面的srcUrl(视频真正的下载地址)
    srcUrl = dict['videoInfo']['videos']['srcUrl']

    # 这个代码是原先的假地址中包含的一段信息
    systemTime = dict['systemTime']

    # 将假地址中的一段进行替换
    srcUrl = srcUrl.replace(systemTime, f'cont-{cont_id}')

    if not os.path.exists('./video'):
        os.makedirs('./video')

    # 下载视频
    # 视屏文件的写入不需要编码，with也不需要关闭
    with open('./video/'+ '刘畊宏.mp4',mode='wb') as f:
        f.write(requests.get(srcUrl).content)

    print('over!')
