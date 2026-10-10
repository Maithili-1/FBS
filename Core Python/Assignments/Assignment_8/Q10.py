def leap_year(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        print(f"{year} is leap year.")
    else:
        print(f"{year} is not a leap year.")
        
year = int(input("Enter the year : "))
leap_year(year)




# def num(n):
#     if n<=10:
#         print(n)
#         num(n+1)
# n = 1       
# num(n)


# def palindrome(n, rev=0):
#     if n>0:
#         d = n%10
#         rev = rev*10+d
#         return palindrome(n//10, rev)
#     else:
#         return rev

# n = int(input("Enter a number : "))
# if n==palindrome(n):
#     print(f"{n} is a palindrome number.")
# else:
#     print(f"{n} is not a palindrome number.")
        
        
def armstrong(n,count, sum=0):
    if n>0:
        d = n%10
        sum+=d**count
        return armstrong(n//10, count,sum)
    else:
        return sum
    
n = int(input("Enter a number : "))

temp = n
count=0
while(temp>0):
    count+=1
    temp//=10

if n==armstrong(n,count):
    print(f"{n} is a armstrong number.")
else:
    print(f"{n} is not a armstrong number.")
