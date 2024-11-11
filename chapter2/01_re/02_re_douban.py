import re
import requests
import csv

# 爬取豆瓣电影的Top250

if __name__ == '__main__':

    url = 'https://movie.douban.com/top250'

    header = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5028.0 Safari/537.36'
    }

    # 预加载正则表达式
    # 部分电影的导演名字太长，所以导致无法显示演员的名字，所以将演员的匹配获取删除掉了
    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
                     r'.*?<p class="">(?P<director>.*?)<br>'
                     r'(?P<year>.*?)&nbsp;/&nbsp;(?P<where>.*?)&nbsp;/&nbsp;(?P<class>.*?)'
                     r'</p>.*?<span class="rating_num" property="v:average">(?P<score>.*?)'
                     r'</span>.*?<span property="v:best" content="10.0"></span>'
                     r'.*?<span>(?P<number>.*?)人评价</span>', re.S)

    f = open('02_douban_Top250.csv', mode='w', encoding='utf-8')
    csvwriter = csv.writer(f)

    for i in range(10):

        param = {
            'start' : 25 * i
        }
        response = requests.get(url, headers=header, params=param)

        page_content = response.text

        result = re.finditer(obj, page_content)

        for i in result:

            # print(i.group('name'))
            # print(i.group('director').strip())
            # print(i.group('actor'))
            # print(i.group('year').strip())
            # print(i.group('where'))
            # print(i.group('class').strip())
            # print(i.group('score').strip())
            # print(i.group('number'))

            dic = i.groupdict()

            # strip()方法将下列的key，删除字符串中的空字符，因为方法里面没有赋值变量
            dic['year'] = dic['year'].strip()
            dic['director'] = dic['director'].strip()
            dic['class'] = dic['class'].strip()
            dic['number'] = dic['number'].strip()

            csvwriter.writerow(dic.values())

    f.close()
    print('over!')