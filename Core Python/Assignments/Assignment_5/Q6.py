n = int(input("Enter the value of n : "))

count = 0
num = 2

while count<n:
    for i in range(2,num//2+1):
        if num%i == 0:
            break
    else:
        count+=1
        print(num)
    num+=1