# WAP to find roots of quadratic equation.
import math

a = int(input("Enter the coefficient of x^2 : "))
b = int(input("Enter the coefficient of x : "))
c = int(input("Enter the constant : "))

D = b**2 - 4*a*c

if D>0:
    r1 = (-b + math.sqrt(D))/(2*a)
    r2 = (-b - math.sqrt(D))/(2*a)
    print("The roots are real & different numbers and these are : ")
    print(f"Root 1 : {r1:.2f}")
    print(f"Root 2 : {r2:.2f}")
elif D==0:
    r1 = r2 = -b/2*a
    print("The roots are real & equal and these are: ")
    print(f"Root 1 = Root2 : {r1:.2f}")
else:
    r1 = (-b + math.sqrt(D))/(2*a)
    r2 = (-b - math.sqrt(D))/(2*a)
    print("The roots are complex numbers and these are :")
    print(f"Root 1 : {r1:.2f}")
    print(f"Root 2 : {r2:.2f}")