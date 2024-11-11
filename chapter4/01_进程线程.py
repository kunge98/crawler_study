# 线程池和进程池的应用在斗图网的完善中，chapter2/02_bs4/03_bs4_picture

# 进程：资源单位
# 线程：执行单位
# 进程是一辆火车，线程是每一节车厢

# 引入线程
from threading import Thread

# 引入多线程
from multiprocessing import process

# 线程池：一次性开辟一些线程
# 进程池：
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def fn(name):
    for i in range(1000):
        print(name, i)


if __name__ == '__main__':

    # 创建了50个线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(fn, name=f"线程{i}")

    print("over!")