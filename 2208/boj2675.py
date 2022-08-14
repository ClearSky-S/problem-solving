# bronze 2
N = int(input())
for i in range(N):
    r, s = input().split()
    r = int(r)
    ans = ""
    for c in s:
        ans += c*r
    print(ans)