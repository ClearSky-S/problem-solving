# silver 4
for i in range(int(input())):
    lst = input()
    cnt = 0
    for c in lst:
        if c =='(':
            cnt += 1
        if c ==')':
            if cnt == 0:
                cnt = -1
                break
            cnt -= 1
    if cnt == 0:
        print("YES")
    else:
        print("NO")