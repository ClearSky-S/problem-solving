# silver 5
def key(a):
    return " "*(50-len(a))+a
    """
    cnt = 0
    for i in range(len(a)):
        cnt+= (100**(len(a)-i-1)) * ord(a[i])
    return (10**100)*len(a)+ cnt
    """
lst = []

for i in range(int(input())):
    s = input()
    if s in lst:
        continue
    lst.append(s)

lst = sorted(lst, key=key)

for element in lst:
    print(element)
    