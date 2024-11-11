from multiprocessing import Process


# 进程很大程度上写法与线程很类似，参考
# 方式1，直接写一个函数
def fun():
    for i in range(1000):
        print('进程1',i)


# 方式2，定义一个类
class myThread(Process):
    def run(self):
        for i in range(1000):
            print('进程2', i)


if __name__ == '__main__':

    # 函数的方式创建多进程
    p = Process(target=fun)
    p.start()
    p2 = Process(target=fun)
    p2.start()

    # class创建多进程
    p3 = myThread()
    p3.start()
    p4 = myThread()
    p4.start()