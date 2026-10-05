start = int(input("Enter start value of range : "))
end = int(input("Enter end value of range : "))

for num in range(start, end+1):
    n = num
    sum = 0
    while n>0:
        d = n%10
        n//=10
        
        fact = 1
        for i in range(1,d+1):
            fact*=i
        sum+=fact
    if sum==num:
        print(num)