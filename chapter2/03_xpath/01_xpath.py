# xpath是xml文档中搜索内容的一门语言
# html是xml的一个子集
# xpath可以直接通过每个标签（节点）来搜索，节点之间存在父子节点、兄弟节点的关系

from lxml import html, etree
import requests

# 小tricks：查看源代码之后，点击element出现的源代码，右键可以复制xpath

if __name__ == '__main__':

    # 解析xml文件
    # xml = ''
    # tree = etree.XML(xml)

    # 加载html文件
    tree = etree.parse('02_xpath.html')
    # res = tree.xpath('/html')

    # print(res)

    # 使用获取标签里面的内容 text()
    # res2 = tree.xpath('/html/body/ul/li/a/text()')
    # print(res2)
    #
    # xpath获取的索引是从1开始的！
    # res3 = tree.xpath('/html/body/ul/li[1]/a/text()')
    # print(res3)
    #
    # # 筛选a标签中href为x的标签
    # res4 = tree.xpath('/html/body/ol/li/a[@href="x"]/text()')
    # print(res4)
    #
    # 获取li下面的所有内容
    res5 = tree.xpath('/html/body/ol/li')
    # print(res5)
    for li in res5:
        print(li)
        # 这个是第二次查找，为相对查找
        # res6 = li.xpath('./a/')
        # print(res6)
    #     # 获取标签中的属性值,不需要 "[]",但是需要加“/”
    #     # 要是筛选属性值和属性值为多少的话需要加 “[]”,不需要加“/”
        res7 = li.xpath('./a/@href')
        print(res7)

    # * 代表通配符，代表任意的名字，（ul/ol两个标签）
    # res8 = tree.xpath('/html/body/*/li/a/text()')
    # print(res8)

    # // 中间放了两个杠，代表后代
    # res9 = tree.xpath('/html/body/ul//li/a/text()')
    # print(res9)

    # # 这两种写法都可以获取到文本内容，一个是根据索引获取，一个是根据类名获取
    # res10 = tree.xpath('/html/body/div[@class="job"]/text()')
    # res11 = tree.xpath('/html/body/div[1]/text()')
    # print(res10)
    # print(res11)



