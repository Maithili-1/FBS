start = int(input("Enter start value of range : "))
end = int(input("Enter end value of range : "))

for num in range(start, end+1):
    n = num
    reverse = 0
    while(n>0):
        d = n%10
        n//=10
        reverse = reverse*10 + d
    if reverse==num:
        print(num)