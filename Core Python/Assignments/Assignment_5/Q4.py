start = int(input("Enter starting number of range : "))
end = int(input("Enter ending number of range : "))

print(f"\nFollowing are the armstrong numbers in range {start} to {end} :-")
for n in range(start, end+1):
    temp = n
    count = 0
    while temp>0:
        count+=1
        temp//=10
    
    num = n
    sum = 0
    while(num>0):
        d = num % 10
        mult=1
        for i in range(count):
            mult*=d
        sum+=mult
        num //=10
    if ( n == sum):
        print(n)