# 代理可以快速的下载大量的数据
# 不推荐，自己玩玩的话没必要
# 这个还涉及到法律的问题，毕竟翻墙违法

import requests

if __name__ == '__main__':

    url = 'https://www.baidu.com'

    # 代码实现代理本质就是
    # 拿到代理的那个ip后，写在字典的value里面
    # 示例代理ip：218.608.83:3129
    proxies = {
        'https':'https://代理ip',
        'http':'http://代理ip'
    }

    res = requests.get(url, proxies=proxies)

    print(res)
