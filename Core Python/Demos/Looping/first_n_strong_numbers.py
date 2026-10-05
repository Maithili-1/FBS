n = int(input("Enter value of n : "))

count = 0
num = 1
while count<n:
    temp = num
    sum = 0
    while temp>0:
        d = temp%10
        temp//=10
        
        fact = 1
        for i in range(1,d+1):
            fact*=i
        sum+=fact
    if sum==num:
        print(num)
        count+=1
    num+=1