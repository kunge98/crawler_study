import requests

if __name__ == '__main__':

    # 进入https://fanyi.baidu.com首页中
    # 英文状态下，随便输入单词查询
    # F12找到sug，并复制其url

    url = 'https://fanyi.baidu.com/sug'

    s = input('输入想要翻译的单词')

    data={
        'kw':s
    }

    # post请求，传入data数据
    res = requests.post(url, data=data)

    print(res)
    print(res.text)

    # json文件显示（字典显示）
    print(res.json())

    # 访问记得关闭
    res.close()