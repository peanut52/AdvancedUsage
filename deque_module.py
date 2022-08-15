from collections import deque

l1 = [1,2,3,4]
q1 = deque(l1)
print(q1)
q1.append(7)
q1.appendleft(9)
print(q1)
print(q1.pop())
print(q1.popleft())
print(q1)