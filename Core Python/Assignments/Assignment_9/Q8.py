def prime(n, i=2):
    if n<=1:
        return 0
    if i<=n//2:
        if n%i==0:
            return 0
        else:
            return prime(n, i+1)
    else:
        return 1
        
n = int(input("Enter the number : "))
if prime(n)!=0:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
        