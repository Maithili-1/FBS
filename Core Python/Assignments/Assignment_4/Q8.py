# Numbers divisible by 7 and multiple of 5 in a given range

n = int(input("Enter the value of n(range) : "))

print("Following are the numbers that are divisible by 7 and multiple of 5 in a given range : ")
for i in range(1, n+1):
    if ( i%7==0 and i%5==0):
        print(i)