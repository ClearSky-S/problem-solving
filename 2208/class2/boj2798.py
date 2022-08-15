# bronze 2

n, m = map(int, input().split(" "))
lst = list(map(int, input().split(" ")))
lst.sort(reverse=True)
result = 0

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1, n):
            sum3 = lst[i] + lst[j] +lst[k]
            if sum3 > result and sum3 <= m:
                result = sum3

print(result)
