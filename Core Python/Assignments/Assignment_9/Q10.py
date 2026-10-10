def reverseNum(n, rev=0):
    if n==0:
        return rev
    else:
        d = n%10
        rev = rev*10 + d
        return reverseNum(n//10, rev)

n = int(input("Enter the value of n : "))
print(f"Reverse of {n} is {reverseNum(n)}.")