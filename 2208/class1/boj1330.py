# boj1330.py
# bronze 5
# 22 08 13

a, b = map(int,input().split(' '))
if a>b:
    print(">")
elif a<b:
    print("<")
else:
    print("==")