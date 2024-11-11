# 这个难度较大
# 爬取网易云音乐的热评

# 1.找到未加密的参数
# 2.加密，得按照网易的来
# 3.请求到网易拿到评论解析

import requests

if __name__ == '__main__':

    url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='

    
