n = int(input("Enter the value of n : "))

count = 0
num = 1

while(count<n):
    sum = 0
    for i in range(1, num//2+1):
        if num%i==0:
            sum+=i
    if sum==num:
        print(num)
        count+=1
    num+=1