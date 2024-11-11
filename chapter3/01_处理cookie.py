# 有一些网站（淘宝）必须登录之后才可以看到自己想要得到数据，必须要处理cookie，完成之后就是request的常规操作爬取数据
# 登录  -->  cookie
# 带着cookie去请求url
# 可以使用session进行请求，session可以认为是一连串的请求，在这个过程中cookie不会丢失

# 处理session共有两种方式
# 1.session常规途径获取cookie
# 2.在F12下面可以知道对应的cookie值，可以直接在请求的时候复制cookie值
# 但是现在问题，无论哪种方法我都无法成功
# bug在第二天解决，第一种方法成功解决，
# 原因：session.post（）之后赋值给了其他变量，导致后面再调用session的时候，出现bug

import requests

if __name__ == '__main__':

    # 方法1 处理cookie
    session = requests.session()

    url = 'https://passport.17k.com/ck/user/login'

    data = {
        'loginName':'15314233351',
        'password':'wangzk12345'
    }

    # 这个地方赋值会导致后面报错
    session.post(url, data=data)

    # 获取到了cookie
    # print(session.post(url, data=data).text)
    # print(session.post(url, data=data).cookies)

    res2 = session.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919')
    # print(res2)
    # print(res2.text)
    print(res2.json())

    # 方法2，直接复制浏览器中的cookie，使用request.get()
    # cookie = 'GUID=848e2ede-56e7-40f6-8b6a-f5e56f06aa8f; sajssdk_2015_cross_new_user=1; c_channel=0; c_csc=web; sensorsdata2015jssdkcross={"distinct_id":"848e2ede-56e7-40f6-8b6a-f5e56f06aa8f","$device_id":"180917e25831fe-0dbfcd6d5d5d6a-19721c27-2073600-180917e25841446","props":{"$latest_traffic_source_type":"直接流量","$latest_referrer":"","$latest_referrer_host":"","$latest_search_keyword":"未取到值_直接打开"},"first_id":"848e2ede-56e7-40f6-8b6a-f5e56f06aa8f"}'
    # cookie = cookie.encode('utf-8').decode('latin-1')
    # res3 = requests.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919', headers = {
    #     'Cookie':cookie
    # })
    # print(res3.json())
