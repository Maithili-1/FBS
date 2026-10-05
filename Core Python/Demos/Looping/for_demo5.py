n = int(input("Enter value of n to calculate factorial : "))

fact = 1
for i in range(1,n+1):
    fact*=i
    print(fact)
print(f"Factorial of {n} is : {fact}")