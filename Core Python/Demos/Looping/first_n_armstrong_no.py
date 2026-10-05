n = int(input("Enter value of n : "))

count = 0
num = 1

while count<n:
    temp = num
    length = 0    
    while temp>0:
        length+=1
        temp//=10
        
    temp = num
    sum = 0
    while temp>0:
        d = temp%10
        temp//=10
        
        mult = 1
        for i in range(length):
            mult*=d
        sum+=mult
    
    if sum==num:
        print(num)
        count+=1
    num+=1