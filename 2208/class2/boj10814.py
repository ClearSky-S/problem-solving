# silver 5
lst = [{"total":input()} for i in range(int(input()))]

for element in lst:
    element["age"] = int(element["total"].split()[0])
    element["name"] = element["total"].split()[1]

# lst.sort(key=lambda x: "%3s%100s" %(x["age"], x["name"]))
lst.sort(key= lambda x:x["age"])

for element in lst:
    print(element["total"])