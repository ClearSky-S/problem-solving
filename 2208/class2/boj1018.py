MAX_CNT= 100

n, m = map(int, input().split())

def compare_2D(a, b):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if a[i][j] != b[i][j]:
                cnt += 1
    return cnt


def print_2D(lst):
    print("")
    for row in lst:
        for element in row:
            print(element, end=" ")
        print("")

arr = [0 for j in range(n)]

for i in range(n):
    arr[i] = [c for c in input()]

white_board = [["W" if (i+j)%2==0 else "B" for j in range(8)] for i in range(8)]
black_board = [["W" if (i+j)%2==1 else "B" for j in range(8)] for i in range(8)]


result1 = MAX_CNT
result2 = MAX_CNT
for i in range(n-7):
    for j in range(m-7):
        arr1 = [[arr[i+i2][j+j2] for j2 in range(8)] for i2 in range(8)]

        tmp1 = compare_2D(arr1,white_board)
        if tmp1 < result1:
            result1 = tmp1
        tmp2 = compare_2D(arr1,black_board)
        if tmp2 < result2:
            result2 = tmp2

print(min(result1, result2))
