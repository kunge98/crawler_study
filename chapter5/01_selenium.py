"""
概述：
    自动化测试工具
    可以打开浏览器，然后像人一样去操作浏览器
    程序员可以从selenium中直接提取网页上的各种信息
环境搭建：
    查pip install selenium
    在谷歌浏览器的 /帮助/关于Google Chrome 看浏览器的版本
    在https://npm.taobao.org/mirrors/chromedriver中下载win的驱动，
    只有32位的,也可以用，如果找不到完全对应的版本，可以向下兼容
"""

from selenium.webdriver import Chrome, Edge
from selenium import webdriver


if __name__ == '__main__':

    # # 创建浏览器对象
    # web = Edge()
    # # 打开一个网址
    # web.get('http://www.baidu.com/')
    # print(web.title)

    # 不自动关闭浏览器
    option = webdriver.EdgeOptions()
    option.add_experimental_option("detach", True)

    # 注意此处添加了chrome_options参数
    driver = webdriver.Edge(options=option)
    # driver.get('https://www.csdn.net/')
    driver.get('https://www.youtube.com/watch?v=FHHSum0ShiM')