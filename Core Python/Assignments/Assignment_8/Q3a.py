def sumOfSeries(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    print(f"Sum of series upto {n} is {sum}.")
    
n = int(input("Enter the value of n : "))
sumOfSeries(n)