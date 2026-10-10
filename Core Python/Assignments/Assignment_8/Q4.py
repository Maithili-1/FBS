def sumOfOdd(n):
    sum = 0
    for i in range(1,n+1):
        if i%2!=0:
            sum+=i
    print(f"Sum of Odd numbers between 1 to {n} is {sum}.")
    
n = int(input("Enter the value of n : "))
sumOfOdd(n)