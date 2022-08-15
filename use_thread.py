import time
from threading import Thread, Lock
from queue import Queue
from multiprocessing.pool import ThreadPool

"""单纯用函数的方式"""


def task(start, end):
    print(start)
    time.sleep(1)
    print(end)


def main1():
    for i in range(2):
        t = Thread(name='线程任务', target=task, args=(123, '结束',))
        t.start()
    print('主进程结束')


"""用类的方式"""


class MyThread(Thread):
    def __init__(self, end):
        super(MyThread, self).__init__()
        self.end = end

    def run(self) -> None:
        print(123)
        time.sleep(1)
        print(self.end)


def main2():
    for i in range(2):
        t = MyThread('子结束')
        t.start()
    print('主进程结束')


def main3():
    t_list = []
    for i in range(2):
        t = Thread(name='任务线程', target=task, args=(123, '结束',))
        t_list.append(t)
    for t in t_list:
        t.start()
        # for t in t_list:
        t.join()
    print('主线程结束')


def main4():
    """守护线程，非守护线程运行完毕，守护进程就结束"""
    t_list = []
    for i in range(2):
        t = Thread(name='任务线程', target=task, args=(123, '结束',))
        t.setDaemon(True) # 设置守护进程或线程这句话必须设置在start()之前
        t_list.append(t)
    for i in t_list:
        i.start()
    print('主线程结束，子线程就不在走了')


x = 0


def zi_with_no_lock():
    """线程数据共享，如果并不使用锁的话，会同时使用，得到数据会失真"""
    global x
    n = 1000000

    def incr(n):
        global x
        for i in range(n):
            x += 1

    def decr(n):
        global x
        for i in range(n):
            x -= 1

    t1 = Thread(target=incr, args=(n,))
    t2 = Thread(target=decr, args=(n,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(x)


def main5():
    """由于线程数据共享，所以容易乱套了，就要加互斥锁，此为没加锁乱套的现象"""
    zi_with_no_lock()
    zi_with_no_lock()
    zi_with_no_lock()


lock = Lock()


def zi_with_lock():
    """线程数据共享，修改数据的时候就使用锁"""
    global x
    n = 1000000

    def incr(n):
        global x
        for i in range(n):
            lock.acquire()
            x += 1
            lock.release()

    def decr(n):
        global x
        for i in range(n):
            lock.acquire()
            x -= 1
            lock.release()

    t1 = Thread(target=incr, args=(n,))
    t2 = Thread(target=decr, args=(n,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(x)


def queue_test():
    q = Queue(3)
    print('是否为空：', q.empty())
    q.put(1)
    q.put('abc')
    print('是否满了：', q.full())
    print('队列长度：', q.qsize())
    print(q.get())
    print(q.get())


class ThreadPool2():
    """使用线程池"""

    def __init__(self, n):
        self.queue = Queue()
        for i in range(n):
            Thread(target=self.worker).start()

    def worker(self):
        while True:
            func, args, kwargs = self.queue.get()
            func(*args, **kwargs)

    def apply_async(self, target, args=(), kwargs={}):
        """添加任务给队列"""
        self.queue.put((target, args, kwargs))


def main6():
    """由于线程数据共享，所以容易乱套了，就要加互斥锁，此为加锁"""
    zi_with_lock()
    zi_with_lock()
    zi_with_lock()


def poolTask(arg):
    print('start')
    time.sleep(1)
    print(arg)


def main7():
    t = ThreadPool2(2)
    for i in range(10):
        t.apply_async(poolTask, args=('结束',))


def main8():
    pool = ThreadPool(3)
    for i in range(10):
        pool.apply_async(poolTask, args=('xyz',))
    # join()前必须要close，这样就不允许提交任务了
    pool.close()
    pool.join()
    #     池的其他操作
    #
    # 操作一： close - 关闭提交通道，不允许再提交任务
    #
    # 操作二： terminate - 中止进程池，中止所有任务


if __name__ == '__main__':
    # main1()
    # main2()
    # main3()
    # main4()
    # main5()
    # main6()
    # queue_test()
    # main7()
    main8()
