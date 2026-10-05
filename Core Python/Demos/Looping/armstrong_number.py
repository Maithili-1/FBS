num = int(input("Enter the number : "))

temp = num
length = 0
while temp>0:
    length+=1
    temp//=10
    
n = num
sum = 0
while n>0:
    d = n%10
    n//=10
    mult=1
    for i in range(length):
        mult*=d
    sum+=mult

if sum==num:
    print(f"{num} is an armstrong number.")
else:
    print(f"{num} is not a armstrong number.")