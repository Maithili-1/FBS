x = int(input("enter the value of x : "))
n = int(input("Enter number of terms : "))

sum = 0
for i in range(1,n+1):
    term = (x**i)/(2*i-1)
    
    if(i%2==0):
        sum -= term
    else:
        sum+=term
print("Sum of series : ", sum)