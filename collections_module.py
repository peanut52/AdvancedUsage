from collections import namedtuple

# 表示people类有三个属性，分别是name age like
people = namedtuple('people', 'name age like')
rocky = people(name='rocky', age=16, like='python')
print(rocky._asdict())
