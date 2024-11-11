import requests
import re
import csv

# 爬取小说网站的三国演义
# 找了半天bug，原来是网站本身就是个垃圾网站
# 确实是爬取的三国演义，进去每章节显示却是 旧五代史，每部小说都是这样，代码只能这样了

if __name__ == '__main__':

    url='https://www.shicimingju.com/book/sanguoyanyi.html'

    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5028.0 Safari/537.36'
    }

    response1 = requests.get(url, headers=header)

    # 获取初次页面的内容
    page_content1 = response1.content.decode('utf-8', 'ignore').replace(u'\xa9', 'u')

    # 获取到了页面内容，找到相关的链接地址
    # print(page_content)

    # 书写re规则
    obj1 = re.compile(r'<li><a href="/book/sanguoyanyi/(?P<link>.*?)">(?P<every_name>.*?)</a></li>', re.S)

    obj2 = re.compile(r'史书典籍.*?<div class="chapter_content">(?P<content>.*?)</div>', re.S)

    # 写入文件中
    f = open('04_re_novel1.csv', mode='w', encoding='utf-8')
    csvwriter = csv.writer(f)

    result1 = re.finditer(obj1, page_content1)

    for i in result1:
        # print(i.group('every_name'))
        # print(i.group('link'))
        complete_url = url.split('.html')[0]+'/'+i.group('link')

        # 获取到了完整的url地址
        print(complete_url)

        response2 = requests.get(complete_url, headers=header)

        page_content2 = response2.content.decode('utf-8', 'ignore').replace(u'\xa9', 'u').replace(u'\ue3d7', 'u')
        # print('page2',page_content2)

        result2 = re.finditer(obj2, page_content2)
        for i in result2:
            # print(i.group('content').encode('').strip())

            # 以字典的形式保存
            dic = i.groupdict()
            dic['content'] = dic['content'].strip()

            csvwriter.writerow(dic.values())

    f.close()
    print('over!')