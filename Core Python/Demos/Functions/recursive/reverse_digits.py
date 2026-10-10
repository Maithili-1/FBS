def reverse_digits(n, rev=0):
    if n==0:
        return rev
    else:
        d = n%10
        rev = rev*10 + d
        return reverse_digits(n//10, rev)
        

n = int(input("Enter a number : "))
res = reverse_digits(n)
print(res)