def sumOfDigits(n):
    if n>0:
        d = n%10
        return d+sumOfDigits(n//10)
    else:
        return 0

num = int(input("Enter the number : "))
print(f"Sum of digits in {num} = {sumOfDigits(num)}.")