def armstrong(n, count, sum=0):
    if n>0:
        d = n%10
        sum+=d**count
        return armstrong(n//10, count, sum)
    else:
        return sum

n = int(input("Enter the number : "))

temp=n
count=0
while temp>0:
    count+=1
    temp//=10
    
if n==armstrong(n,count):
    print(f"{n} is a armstrong number.")
else:
    print(f"{n} is not a armstrong number.")