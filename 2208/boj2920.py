# bronze 22
asc = list(range(1,9))
des = asc[:]
des.reverse()

lst = list(map(int, input().split(' ')))
if lst == asc:
    print("ascending")
elif lst == des:
    print("descending")
else:
    print("mixed")
