def sumOfExpo(n):
    sum = 0
    for i in range(1,n+1):
        sum+=i*i
    return sum

n  = int(input("Enter the value of n : "))
print(f"Sum of exponential series is {sumOfExpo(n)}.")