# boj1789.py
# silver 5
# 22 08 13

def getSum(i):
    return i*(i+1)/2

s = int(input())
for n in range(1, 100000):
    if getSum(n)<=s and s<getSum(n+1):
        break
print(n)
