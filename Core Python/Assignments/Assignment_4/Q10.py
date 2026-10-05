# check given number is perfect number or not

n = int(input("Enter the number : "))

sum = 0
for i in range(1, n//2+1):
    if( n%i == 0):
        sum+=i

if( n==sum):
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")