# silver 5
lst = []
for i in range(int(input())):
    lst.append(tuple(map(int, input().split())))

lst.sort(key=lambda x: x[0]*1000000+x[1])
for element in lst:
    print(element[0], element[1])