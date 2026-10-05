n = int(input("Enter the number : "))

num = n
reverse = 0
while(num > 0):
    d = num%10
    num//=10
    reverse = reverse*10 + d
if (n==reverse):
    print(f"{n} is palindrome.")
else:
    print(f"{n} is not palindrome.")