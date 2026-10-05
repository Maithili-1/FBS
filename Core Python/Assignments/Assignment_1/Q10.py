# WAP to calculate area of equilateral traingle.

import math

side = int(input("Enter the sode of the equilateral traingle : "))
area = (math.sqrt(3)/4) * (side**2)
print(f"Area of Equilateral Triangle is : {area:.2f}")