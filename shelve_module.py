import shelve

s = shelve.open('test.db')
s['name'] = 'rocky'
s['like'] = 'python'
s['age'] = 23
s['content'] = {'first': 'good', 'second': 'well'}
s.close()

s = shelve.open('test.db')
name = s['name']
print(name)
