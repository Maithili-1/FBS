#Factorial of a number
n = int(input("Enter value of n : "))

fact = 1
for i in range(1,n+1):
    fact*=i
print(f"Factorial of number {n} is {fact}.")