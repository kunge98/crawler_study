# 三种数据解析
# re解析(正则表达式)、bs4解析、xpath解析（较为流行）
# 三种解析方式可以混合使用

# .     代表除换行符之外的任意字符
# d     代表匹配数字
# w     匹配字母数字下划线
# *     重复0次或更多次
# ？    重复0次或1次
# +     重复1次或多次
# .*?   惰性匹配（尽可能少的匹配字符）
# .*    贪婪匹配（尽可能多的匹配字符）

import re

if __name__ == '__main__':

    # # 返回列表，不常用
    lis = re.findall(r'\d+', '我的电话是15314233351，爸爸电话是13969923958')
    # print(lis)
    #
    # # 全文匹配，找到第一个就返回了
    sear = re.search(r'\d+', '我的电话是15314233351，爸爸电话是13969923958')
    # print(sear)
    # print(sear.group())
    #
    # # 从头开始匹配，开始不匹配就不匹配了
    mat = re.match(r'\d+', '我的电话是15314233351，爸爸电话是13969923958')
    # # 返回none
    # print(mat)
    #
    # # 效率最高且最常用
    itr = re.finditer(r'\d+', '我的电话是15314233351，爸爸电话是13969923958')
    # for i in itr:
    #     print(i)
    #     print(i.group())
    #

    # 预加载正则,可以反复使用
    # obj = re.compile(r'\d+')
    #
    # it = re.finditer(pattern=obj, string='我的电话是15314233351，爸爸电话是13969923958')
    # for i in it:
    #     print(i.group())

    # 模拟网页中爬取到的字符串
    str = """
            <div class='jay'><span id='1'>ResNet</span></div>
            <div class='jj'><span id='2'>VGG</span></div>
            <div class='he'><span id='3'>GoogleNet</span></div>
            <div class='king'><span id='4'>UNet</span></div>
            <div class='wzk'><span id='5'>EfficientNetV2</span></div>
            <div class='abc'><span id='5'>YOLOv5</span></div>
            <div class='pool'><span id='5'>BigData</span></div>
    """

    # re.S 功能可以让 . 匹配换行符
    # (?P<分组名字>正则式)   可以进一步提取正则表达式中匹配的内容
    obj = re.compile(r"<div class='(?P<cls>.*?)'><span id='\d'>(?P<content>.*?)</span></div>", re.S)

    result = re.finditer(obj, string=str)
    # print(result)
    for i in result:
        print(i.group('cls'))
        print(i.group('content'))