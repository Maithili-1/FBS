def palindrome(n):
    rev = 0
    num = n
    while(n>0):
        d = n%10
        rev = rev*10+d
        n//=10
    if num==rev: 
        print(f"{num} is a palindrome number.")
    else:
        print(f"{num} is not a palindrome number.")

num = int(input("Enter the value of n : "))
palindrome(num)