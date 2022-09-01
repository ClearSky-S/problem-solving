# silver 5
def isPrime(a):
    if a==1:
        return False
    if a==2 or a==3:
        return True
    for i in range(2, int(a**0.5)+1):
        if a%i==0:
            return False
    return True
input()
cnt = 0
for n in map(int, input().split()):
    if isPrime(n):
        cnt += 1
print(cnt)
