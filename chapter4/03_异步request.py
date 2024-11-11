import aiohttp

# 至关重要的模块！！！！
import asyncio

urls = [

]


async def download(url):
    # 发送请求，得到图片内容
    # 相当于request
    aiohttp.ClientSession()

    # 相当于request
    async with aiohttp.ClientSession as session:

        # resp 相当于 resp = request.get()
        async with session.get(url) as resp:

            with open('./img', mode='wb') as f:
                # 读取图片resp.content.read()
                # 读取文本resp.text()
                # 返回json resp.json()
                f.write(await resp.content.read())


async def main():
    tasks = []
    for url in urls:
        tasks.append(download(url))

    await asyncio.wait(tasks)


if __name__ == '__main__':

    asyncio.run(main())
