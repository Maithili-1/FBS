# WAP to find sum of the 3 digit number

num = int(input("Enter the number : "))

sum = 0
while(num>0):
    d = num%10
    sum+=d
    num//=10
print(sum)
    
    
# WAP to reverse the 3 digit number
num = int(input("\nEnter the number : "))
n = num

rev = 0
while(n>0):
    d = n%10
    rev = rev*10 + d 
    n//=10
print("\nOriginal number : ", num)
print("Reverse number : ",rev)