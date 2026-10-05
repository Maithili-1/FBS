def sumOfSeries(n):
    if n<=0:
        return 0
    else:
        return n + sumOfSeries(n-1)

n=5  
res = sumOfSeries(n)
print(res)