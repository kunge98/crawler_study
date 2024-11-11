from lxml import etree
import requests

# 使用xpath爬取猪八戒网的信息，效果不是很理想，也没有生成csv文件(参照之前的代码可以写入csv中)
# 但是理解了xpath的语法即可
if __name__ == '__main__':

    url = 'https://fushun.zbj.com/search/f/?'

    header = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5028.0 Safari/537.36'
    }

    param = {
        'kw':'管理系统'
    }

    res = requests.get(url, headers=header, params=param)

    # print(res, type(res))

    # 加载html的源码
    html = etree.HTML(res.text)
    print(html)

    # 获取到想要的divs,div[1]表示所有的信息的合集，后面再接一个div表示获取父节点的所有子节点
    divs = html.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div')
    # print(divs)

    # 获取每个div的信息
    for div in divs:
        # print(div)
        # 使用相对路径,但是目前仅仅获取到了一个div的信息，现在是要获取到所有div的信息
        price = div.xpath('./div/div/a[2]/div[2]/div[1]/span[1]/text()')[0].strip('¥')
        amount = div.xpath('./div/div/a[2]/div[2]/div[1]/span[2]/text()')[0]
        name = '管理系统'.join(div.xpath('./div/div/a[2]/div[2]/div[2]/p/text()'))
        address = div.xpath('./div/div/a[1]/div[1]/div[1]/span/text()')[0]
        star = div.xpath('./div/div/a[1]/div[2]/span[2]/i[2]/test()')
        print(price)
        print(amount)
        print(name)
        print(address)
        print(star)



