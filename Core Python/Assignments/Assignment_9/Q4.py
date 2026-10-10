def sumOfSeries(n):
    if n>0:
        return n+sumOfSeries(n-1)
    else:
        return 0
    
n = int(input("Enter a number : "))
print(f"Sum of series upto {n} is {sumOfSeries(n)}.")