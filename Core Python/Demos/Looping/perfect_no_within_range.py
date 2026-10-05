start = int(input("Enter start value of range : "))
end = int(input("Enter end value of range : "))

for num in range(start, end+1):
    sum = 0
    for i in range(1, num//2+1):
        if num%i==0:
            sum+=i
    if sum==num:
        print(num)