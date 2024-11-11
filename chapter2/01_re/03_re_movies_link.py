# encoding=utf-8
# 获取盗版电影的电影下载地址

# 一直报错，意思是超过了最大连接次数
# HTTPSConnectionPool(host='dytt89.coom', port=443): Max retries exceeded with

import requests
import time


if __name__ == '__main__':

    url = 'https://baijiahao.baidu.com/s?id=1731640428833032435'

    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5028.0 Safari/537.36',
        'Connection':'Close'
    }
    # requests.adapters.DEFAULT_RETRIES = 5

    # 盗版电影网站，关闭安全验证
    time.sleep(1)
    res = requests.get(url, headers=header)

    print(res.content.decode(encoding='utf-8'))

    res.close()

