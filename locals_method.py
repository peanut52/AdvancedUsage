"""
locals()的作用是返回当前位置的局部变量
"""


def fun(like):
    name = 'rocky'
    print(locals())


if __name__ == '__main__':
    fun('python')
