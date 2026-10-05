# Number is Armstrong number or not

n = int(input("Enter a number : "))

temp = n
count = 0
while temp>0:
    count+=1
    temp//=10

num = n
sum = 0
while(n>0):
    d = n%10
    sum += d**count
    n//=10

if sum==num:
    print(f"{num} is a armstrong number.")
else:
    print(f"{num} is not a armstrong number.")