def reverse_num(n, rev=0):
    if n>0:
        d = n%10
        rev = rev*10+d
        return reverse_num(n//10,rev)
    else:
        return rev

n = int(input("Enter the number : "))
print(f"Reverse of {n} is {reverse_num(n)}.")