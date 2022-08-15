# bronze 2
for i in range(int(input())):
    h, w, n  = map(int, input().split())
    a = (n-1)%h +1
    b = (n+h-1)//h
    print(str(a)+ ("0" if b <10 else"") + str(b))