# silver 4
import sys
sys.stdin.readline()
a = sys.stdin.readline().split()
# set 탐색의 시간 복잡도는 O(1)이다
a = set(a)
sys.stdin.readline()
b = sys.stdin.readline().split()

for element in b:
    if element in a:
        print(1)
    else:
        print(0)
