#Method 1
data = [1,2,3,4,5,6,7,8,9,10]
def sq(n):
    return n*n
sqr = map(sq, data)
res = list(sqr)
print(res)


#Method 2
res = list(map(lambda n : n*n, data))
print(res)