#WAP to check if given 3-digit number is a palindrome or not.

num = int(input("\nEnter the number : "))
n = num

rev = 0
while(n>0):
    d = n%10
    rev = rev*10 + d 
    n//=10
print("\nOriginal number : ", num)
print("Reverse number : ",rev)
if num==rev:
    print(f"{num} is palindrome.")