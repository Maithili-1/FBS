# WAP to find area and circumference of circle.
import math

r = int(input("Enter the radius of circle : "))
area = math.pi * (r**2)
c = 2 * math.pi* r

print(f"Area of circle is {area:.2f}.")
print(f"Circumference of circle is {c:.2f}")