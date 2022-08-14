# bronze 2
for i in range(int(input())):
    cnt_total = 0
    cnt = 0
    ox = input()
    if ox[0]=='O':
        cnt += 1
        cnt_total = cnt
    for i in range(1,len(ox)):
        if ox[i]=="X":
            cnt = 0
        else:
            if ox[i-1]=='X':
                cnt = 1
            else:
                cnt += 1
            cnt_total += cnt
    print(cnt_total)
