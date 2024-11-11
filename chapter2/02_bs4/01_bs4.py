import requests
from bs4 import BeautifulSoup

# bs4 的用法

if __name__ == '__main__':

    url = ''

    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5028.0 Safari/537.36'
    }

    response = requests.get(url, headers=header)

    # 1.解析数据
    # 把页面源代码交给bs进行处理，生成bs对象
    # 'html.parser'为指定html为解析器
    page = BeautifulSoup(response.text, 'html.parser')
    print(page)

    # 2.从bs对象中查找对象
    # find（只找出第一个）、find_all
    # find(标签, 属性=值)
    # find_all(标签, 属性=值)

    # 两种写法是一样的
    # 1.为了避免和python中的class冲突，在find函数中class可以加上一个下划线
    # 2.使用字典的表现形式，里面可以塞很多键值对
    table = page.find('table', class_='1')
    tabl2 = page.find('table', attrs={
        'class':'1'
    })

    # 在table1和table2中还可以继续嵌套两种搜索
