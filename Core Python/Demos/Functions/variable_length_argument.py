def add(*data):
    print(type(data))
    sum = 0
    for i in data:
        sum+=i
    return sum

res = add(10,20,30,40,50,60,70,80,90,100)
print(res)