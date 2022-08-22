# silver 4
n = int(input())
lst = list(map(int, input().split(' ')))
dictionary = {}
for element in lst:
    try:
        dictionary[element] += 1
    except KeyError:
        dictionary[element] = 1
    
m = int(input())
lst_target = list(map(int, input().split(' ')))
lst_result = []
for element in lst_target:
    try:
        lst_result.append(dictionary[element])
    except KeyError:
        lst_result.append(0)


print(" ".join(map(str,lst_result)))