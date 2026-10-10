def countDigits(n):
    count=0
    while n>0:
        count+=1
        n//=10
    return count

def armstrongSum(n,count):
    sum = 0
    while n>0:
        d = n%10
        sum+=d**count
        n//=10
    return sum

def checkArmstrong(n):
    if n==armstrongSum(n,countDigits(n)):
        print(f"{n} is an armstrong number.")
    else:
        print(f"{n} is not an armstrong number.")

num = int(input("Enter the number : "))
checkArmstrong(num)