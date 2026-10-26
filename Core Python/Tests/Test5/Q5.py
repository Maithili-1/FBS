li1 = [10, 20, 40, 70, 50, 100, 130, 150]
li2 = [10, 50, 30, 70, 130, 150, 60]
union_li = []

li3 = li1.copy()
li3.extend(li2)

for ele in li3:
    if ele not in union_li:
        union_li.append(ele)

print(f"List 1 : {li1}\nList 2 : {li2}\nUnion of List1 and List2 :- {union_li}")