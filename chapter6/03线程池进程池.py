# 导入线程池
from concurrent.futures import ThreadPoolExecutor
# 导入进程池
from concurrent.futures import ProcessPoolExecutor

# 线程池：一次性开辟多少个线程，用户直接给线程池提交任务
# 线程任务的调度交给线程池完成
# 可以看出写起来比单个线程好用


def fun(name):
    for i in range(1000):
        print(name, i)


if __name__ == '__main__':

    # 使用线程池来执行任务
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(fun, name=f'线程{i}')

    print('线程任务全部执行完毕')

    # 使用进程池来执行任务
    with ProcessPoolExecutor(50) as t:
        for i in range(100):
            t.submit(fun, name=f'进程{i}')

    print('进程任务全部执行完毕')