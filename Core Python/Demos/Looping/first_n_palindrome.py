n = int(input("Enter value of n : "))

count = 0
num = 1
while count<n:
    temp = num
    reverse = 0
    while(temp>0):
        d = temp%10
        temp//=10
        reverse = reverse*10 + d
    if reverse == num:
        print(num)
        count+=1
    num+=1