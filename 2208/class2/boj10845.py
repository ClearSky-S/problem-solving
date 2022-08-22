# silver 4
from collections import deque
import sys
queue = deque()

for line in sys.stdin.readlines():
    command = line.split()
    if command[0] == "push":
        queue.append(int(command[1]))
    elif command[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            x = queue.popleft()
            queue.appendleft(x)
            print(x)
    elif command[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            x = queue.pop()
            queue.append(x)
            print(x)