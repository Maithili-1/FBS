#WAP to swap 2 numbers using third variable.

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))

print(f"Numbers before swapping : a = {a} and b = {b}.")

temp = a
a=b
b=temp

print(f"Numbers after swapping : a = {a} and b = {b}.")