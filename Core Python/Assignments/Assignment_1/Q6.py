# WAP to input two angles from user & find third angle of triangle.

a1 = int(input("Enter the 1st angle of triangle : "))
a2 = int(input("Enter the 2nd angle of triangle : "))

a3 = 180 - (a1+a2)
print("Third angle of triangle is ",a3)