# Check if given number is strong number

n = int(input("Enter a number : "))

num = n
sum=0
while(n>0):
    d = n%10
    
    fact = 1
    for i in range(1,d+1):
        fact *=i
    sum+=fact
    
    n //= 10
    
if (sum == num):
    print(f"{num} is a strong number.")
else:
    print(f"{num} is not a strong number.")