#WAP to find sum of 3-digit number.

num = int(input("Enter 3-digit number : "))

H = num//100
T = (num//10)%10
U = num%10

sum = H+T+U
print(f"Sum of 3-digit number {num} is {sum}.")