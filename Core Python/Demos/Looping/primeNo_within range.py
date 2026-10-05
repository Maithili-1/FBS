start = int(input("enter start value of range : "))
stop = int(input("Enter end value of range : "))

for n in range(start, stop+1):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            print(n)