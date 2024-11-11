# 协程：当程序遇见io操作的时候，可以选择切换到其他操作上
# 压榨cpu，不让cpu空闲
# 多任务异步操作
# 一切都是在单线程的前提下

import asyncio
import time


async def fun1():
    print('hello,world')
    await asyncio.sleep(2)
    print('hello,world')


async def fun2():
    print('hello,kkk')
    await asyncio.sleep(3)
    print('hello,kkk')


async def fun3():
    print('hello,giao')
    await asyncio.sleep(1)
    print('hello,giao')


async def fun4():
    print('hello,MJ')
    await asyncio.sleep(3)
    print('hello,MJ')


async def main():

    f1 = fun1()
    f2 = fun2()
    f3 = fun3()
    f4 = fun4()
    # py3.7的写法
    tasks = [f1, f2, f3, f4]

    # py3.8以后版本的写法
    # tasks = [
    #     asyncio.create_task(f1),
    #     asyncio.create_task(f2),
    #     asyncio.create_task(f3),
    #     asyncio.create_task(f4),
    # ]

    t1 = time.time()

    await asyncio.wait(tasks)

    t2 = time.time()

    print(t2-t1)


if __name__ == '__main__':

    # 推荐:写一个异步的main，在外面run，在异步main中使用await
    asyncio.run(main())

