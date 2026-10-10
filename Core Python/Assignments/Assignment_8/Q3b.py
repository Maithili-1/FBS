def sumOfFact(n):
    sum = 0
    fact = 1
    for i in range(1,n+1):
        fact*=i 
        sum+=fact
    return sum

n = int(input("Enter the value of n : "))
print(f"Sum of factorial series is {sumOfFact(n)}.")