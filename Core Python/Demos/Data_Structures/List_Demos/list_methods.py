li = [10, 20, 30, 40, 50, 60 ,70, 80, 90, 100, 40]

#1)  append(value)
li.append(110)
print(li)

#2) clear()
li.clear()
print(li)

li = [10, 20, 30, 40, 50, 60 ,70, 80, 90, 100, 40]
#3) copy()
li2 = li.copy()  #Copy only upper layer not the deep copies
print(li2)

#4) count(value)
print(li.count(40))

#5) extend(iterable)
li.extend([120,130])
print(li)

#6) index(value)
print(li.index(40))

#7) insert(index, value)
li.insert(5, 150)
print(li)

#8) pop(index)
li.pop()
li.pop(0)
print(li)

#9) remove(value)
li.remove(150)
print(li)

#10) reverse()
li.reverse()
print(li)

#11) sort()
li.sort()
print(li)

li.sort(reverse=True)
print(li)
