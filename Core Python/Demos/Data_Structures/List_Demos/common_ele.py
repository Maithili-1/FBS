li1 = [10, 20, 40, 70, 50, 100, 130, 150]
li2 = [10, 50, 30, 70, 130, 150, 60]
li = []
for i in li1:
    if i in li2:
        li.append(i)
print(li)