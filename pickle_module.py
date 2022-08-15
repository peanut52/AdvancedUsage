import pickle

"""
序列化
"""
integer = [1, 2, 3, 4, 5]
f = open('test.dat', 'wb')
pickle.dump(integer, f)
f.close()

"""反序列化"""
it = pickle.load(open('test.dat', 'rb'))
print(it)
