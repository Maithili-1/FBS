def sumOfPrime(n):
    sum = 0
    for num in range(2,n+1):
        for i in range(2,num//2+1):
            if num%i==0:
                break
        else:
            sum+=num
    return sum

n = int(input("Enter the value of n : "))
print(f"Sum of all prime numbers between 1 to {n} is {sumOfPrime(n)}.")