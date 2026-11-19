from functools import reduce

data = [1,2,3,4,5,6,7,8,9,10]

res = reduce(lambda x, y : x+y, data)
print(res)