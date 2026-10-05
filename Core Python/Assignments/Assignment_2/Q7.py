#WAP to find sum of 3-digit number.

num = int(input("Enter the 3-digit number : "))
n = num

d1 = num % 10
num = num//10

d2 = num % 10
num = num//10

d3 = num % 10
num = num //10

sum = d1 + d2 + d3
print(f"Sum of 3-digit number {n} is {sum}.")
