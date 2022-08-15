"""使用进程和进程池"""
import os
import time
from multiprocessing import Process


def main1():
    res = os.getpid()
    print(res)
    # 获取父进程
    print(os.getppid())


def func():
    print(f'{os.getpid()}子进程，{os.getppid()}父进程')


def func2(n):
    for i in range(1, n + 1):
        print(f'{os.getpid()}子进程，{os.getppid()}父进程')


def main2():
    """创建带有参数的进程"""
    n = 5
    p = Process(target=func2, args=(n,))
    p.start()
    for i in range(1, n + 1):
        print('*' * i)


def func3(i):
    print(i)


def main3():
    """这些进程不是接力跑，而是同时跑"""
    lst = []
    for i in range(10):
        p = Process(target=func3, args=(i,))
        p.start()
        lst.append(p)
    for i in lst:
        i.join()
    print('主进程')


def func4():
    print('start')
    time.sleep(1)
    print('end')


def main4():
    """守护主进程"""
    p = Process(target=func4)
    p.daemon = True
    p.start()
    print('主进程结束')


def func51():
    cnt = 1
    while True:
        print('*' * cnt)
        time.sleep(0.1)
        cnt += 1


def func52():
    print('start')
    time.sleep(3)
    print('end')


def main5():
    p1 = Process(target=func51)
    p2 = Process(target=func52)
    p1.daemon = True
    p1.start()
    p2.start()
    print('主进程结束')


"""监控保活"""


def func61():
    while True:
        print('报告自己的状态，i am alive')
        time.sleep(1)


def func62():
    while True:
        try:
            print('我是1号服务器，数据分析中')
        except:
            break


def main6():
    p1 = Process(target=func61)
    p2 = Process(target=func62)
    p1.daemon = True
    p1.start()
    p2.start()
    p2.join()
    print('当前服务器异常')


if __name__ == '__main__':
    # main1()
    # main2()
    """多个进程直接数据不共享"""
    # main3()
    # main4()
    # main5()
    main6()