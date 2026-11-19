data = [1,2,3,4,5,6,7,8,9,10]
#1st eg.
res = list(filter(lambda num : num*num, data))
print(res)

#2nd eg.
res = list(filter(lambda n: n%2==0, data))
print(res)