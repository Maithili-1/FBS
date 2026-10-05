start = int(input("Enter start value of range : "))
end = int(input("Enter end value of range : "))

for num in range(start, end+1):
    temp = num
    length = 0
    while temp>0:
        length+=1
        temp//=10
    
    temp = num
    sum=0
    while temp>0:
        d = temp%10
        temp//=10
        
        mult = 1
        for i in range(length):
            mult*=d
        sum+=mult
    
    if sum==num:
        print(num)