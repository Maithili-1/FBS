def reverse_num(num):
    rev = 0
    while num>0:
        d = num%10
        rev = rev*10+d
        num//=10
    return rev

n = int(input("Enter the value of n : "))
print(f"Reverse of {n} is {reverse_num(n)}.")