def sep_digits(n):
    if n==0:
        return 0
    else:
        d = n%10
        print(d)
        sep_digits(n//10)

n = int(input("Enter a number : "))
num = n
print(f"Digits in {num} are : ")
sep_digits(n)