import sys
"""
类中为什么要使用__slots__?
创建百万级实例如何节省内存？
使用slot，不用再存储成字典，减少大量消耗
"""
class User1:
    def __init__(self, id, name, sex, status):
        self.id = id
        self.name = name
        self.sex = sex
        self.status = status


class User2:
    __slots__ = ['id', 'name', 'sex', 'status']

    def __init__(self, id, name, sex, status):
        self.id = id
        self.name = name
        self.sex = sex
        self.status = status


if __name__ == '__main__':
    u1 = User1('01', 'rocky', '男', 1)
    u2 = User2('02', 'leey', '男', 1)
    u1_dir = u1.__dir__()
    u2_dir = u2.__dir__()
    print(u1_dir)
    print(u2_dir)
    print(set(u1_dir) - set(u2_dir))
    # 结果是弱引用和字典，如果不加入__slots__，在不使用弱引用的时候，字典成为最大的内存消耗者，因此，使用__slots__可以省空间
    print(u1.__dict__)
    print(sys.getsizeof(u1.__dict__))
