#WAP to reverse 3-digit number.

num = int(input("Enter the 3-digit number : "))
H = num//100
T = (num//10)%10
U = num%10

reverse = (U*100)+(T*10)+H
print(f"{num} afer reversing : {reverse}")