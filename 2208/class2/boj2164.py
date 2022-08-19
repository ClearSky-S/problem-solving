# silver 4
from collections import deque

n = int(input())
lst = list(range(n,0,-1))
lst = deque(lst)
while len(lst)>1:
    lst.pop()
    if len(lst)==1:
        break
    lst.appendleft(lst.pop())

print(lst[0])