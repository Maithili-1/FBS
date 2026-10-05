#WAP to swap 2 numbers without using third variable.

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))

print(f"Numbers before swapping : a = {a} and b = {b}.")
a = a+b
b = a-b
a = a-b
print(f"Numbers after swapping : a = {a} and b = {b}.")