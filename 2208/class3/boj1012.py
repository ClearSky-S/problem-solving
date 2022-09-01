# silver 2
def print2D(array):
    for row in array:
        print(row)
    print()
# print("-------------")
for i in range(int(input())):
    M, N, K = map(int, input().split())
    cnt = 0
    farm = []
    for i in range(N):
        farm.append([0 for i in range(M)])
    for i in range(K):
        a, b = map(int, input().split())
        farm[b][a] = 1
    # print2D(farm)
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:
                cnt += 1
                stack = [(i,j)]
                while stack:
                    a, b = stack.pop()
                    if farm[a][b] == 1:
                        farm[a][b] = 2
                        for (x,y) in (-1,0), (0,1), (1,0), (0,-1):
                            if a+y>-1 and a+y<N:
                                if b+x>-1 and b+x<M:
                                    stack.append((a+y,b+x))
                # print2D(farm)
    print(cnt)

    # print2D(farm)