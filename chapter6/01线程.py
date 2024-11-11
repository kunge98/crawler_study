from threading import Thread
# 多线程和多进程,工业开发是必备

# 方式1，直接写一个函数
def fun(name):
    for i in range(1000):
        print('子线程1',i)

# 方式2，定义一个类
class myThread(Thread):
    def run(self):
        for i in range(1000):
            print('子线程2',i)


if __name__ == '__main__':
    # 创建方式1
    # 多线程，后面不是fun(),不带括号，args传入的参数必须是tuple，如果只有一个参数，后面必须逗号
    t = Thread(target=fun, args=('周杰伦',))
    # 开始执行多线程，只是可以开始执行，具体执行由CPU决定
    t.start()
    t2 = Thread(target=fun, args=('林俊杰',))
    # 开始执行多线程，只是可以开始执行，具体执行由CPU决定
    t2.start()

    # 创建方式2,直接创建新对象就可以
    t3 = myThread()
    t3.start()
    t4 = myThread()
    t4.start()
