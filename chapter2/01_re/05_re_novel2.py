import requests
import re
import csv

# 爬取小说网站的斗破苍穹

if __name__ == '__main__':

    url = 'https://www.ibiquges.org/7/7877/3595785.html'

    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60'
    }

    response = requests.get(url, headers=header)

    # 获取初次页面的内容
    page_content = response.content.decode('utf-8', 'ignore').replace(u'\xa9', 'u')

    # 获取到了页面内容，找到相关的链接地址
    # print(page_content)

    # 书写re规则
    # obj = re.compile(r'<li><a href="/book/sanguoyanyi/(?P<link>.*?)">(?P<every_name>.*?)</a></li>', re.S)
    obj = re.compile(r'<div class="bookname"><h1>(?P<chapter>.*?)"></h1></div>'
                     r'.*?&nbsp;&nbsp;&nbsp;(?P<content>.*?)<br>', re.S)

    # # 写入文件中
    # f = open('04_re_novel1.csv', mode='w', encoding='utf-8')
    # csvwriter = csv.writer(f)
    #
    result1 = re.finditer(obj, page_content)
    # print(result1)
    #
    for i in result1:
        print(i.group('chapter'))
        print(i.group('content'))
    #     complete_url = url.split('.html')[0]+'/'+i.group('link')
    #
    #     # 获取到了完整的url地址
    #     print(complete_url)
    #
    #     response2 = requests.get(complete_url, headers=header)
    #
    #     page_content2 = response2.content.decode('utf-8', 'ignore').replace(u'\xa9', 'u').replace(u'\ue3d7', 'u')
    #     # print('page2',page_content2)
    #
    #     result2 = re.finditer(obj2, page_content2)
    #     for i in result2:
    #         # print(i.group('content').encode('').strip())
    #
    #         # 以字典的形式保存
    #         dic = i.groupdict()
    #         dic['content'] = dic['content'].strip()
    #
    #         csvwriter.writerow(dic.values())
    #
    # f.close()
    # print('over!')