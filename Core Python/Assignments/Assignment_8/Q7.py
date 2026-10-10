def sumOfDigits(num):
    sum = 0
    while num>0:
        d = num%10
        sum+=d
        num//=10
    return sum

n = int(input("Enter the value of n : "))
print(f"Sum of digits in {n} is {sumOfDigits(n)}.")