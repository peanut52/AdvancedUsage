import inspect


def check_admin(func):
    def wrapper(*args, **kwargs):
        # 使用inspect是为了调用的时候，如果参数没写具体是username=。。。的时候，也能认出是username
        func_arg = inspect.getcallargs(func, *args, **kwargs)
        if func_arg.get('username') != 'admin':
            raise Exception('This user do not have permission')
        return func(*args, **kwargs)

    return wrapper


# 比如说我想使用装饰器每次打印出函数名
def outer(func):
    def wrapper(*args, **kwargs):
        print('start', func.__name__)
        a = func(*args, **kwargs)
        print('end')
        return a

    return wrapper

@outer
def go():
    print('123')

if __name__ == '__main__':
    go()