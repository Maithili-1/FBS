def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
    
def sum(n):
    if n==1:
        return 1
    else:
        return fact(n) + sum(n-1)

num = int(input("Enter the number : "))
print(f"Sum of series : {sum(num)}.")