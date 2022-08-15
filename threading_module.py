import threading
import time
from threading import current_thread
"""
多线程用在IO操作多的时候，比如等待资源下载，等待文件读写，等待用户输入等
"""

def print_():
    print(current_thread().getName(), 'start')
    print('hello world')
    time.sleep(1)
    print(current_thread().getName(), 'end')


def out(func):
    def inner(*args, **kwargs):
        start = time.time()
        print(start)
        func(*args, **kwargs)
        end = time.time()
        print(end)
        print(start - end)

    return inner


@out
def main():
    for i in range(100):
        # print_()
        t = threading.Thread(target=print_)
        t.start()


if __name__ == '__main__':
    main()
