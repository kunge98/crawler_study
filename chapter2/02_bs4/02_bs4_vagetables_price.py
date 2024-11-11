import requests
from bs4 import BeautifulSoup
import re
import csv

# 有一个非常阴间的bug：
# 编码问题反反复复报错，用代码行的方法可以有效解决
# 新的问题又出来了，BeautifulSoup创造出来的对象却不能使用find和find_all
# 删掉replace，bs对象可以成功使用find和find_all但是却又报gbk的错误
# 现在就是恶心循环了，解决一个bug，另一个就报错
# 水平还没有那么高，果断放弃，去做下一个实例

# 解决了，将pycharm的编码改为utf-8

# 程序成功爬取到了蔬菜的价格，但是还是水平不够导致了蔬菜与价格之间有空格，最终生成的csv文件也是特别难看。
if __name__ == '__main__':

    url = 'http://www.xinsinong.com/price/list-2211.html'

    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5028.0 Safari/537.36'
    }

    response = requests.get(url, headers=header)
    # page_content = response.content.decode('utf-8', 'ignore').replace(u'\xa9', 'u').replace(u'\xa0', 'u')
    page_content = response.text

    # 1.解析数据
    page = BeautifulSoup(page_content, 'lxml')

    # print(page)

    # 书写bs4解析表达式

    # 当前网页中有多项符合要求，但是目标在第一个，所以直接使用find方法找到第一个即可
    div1 = page.find('div', attrs={
        'class':'qbox_body',
    })

    # print(div1)

    li1 = div1.find_all('li', attrs={
        'style':'float:left;width:25%'
    })

    print(li1)

    obj1 = re.compile(r'.*?">(?P<name_price>.*?)<font color=".*?</li>', re.S)

    result = re.finditer(pattern=obj1, string=str(li1))
    # print(result)

    f = open('./vegetable_price.csv', mode='w', encoding='utf-8')

    csvwriter = csv.writer(f)

    for i in result:

        dict = i.groupdict()
        dict['name_price'] = dict['name_price'].split('>')[-1].strip()
        csvwriter.writerow(dict.values())

    f.close()
    print('over!')










