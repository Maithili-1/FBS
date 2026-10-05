#WAP to input all sides of a triangle and check whether triangle is valid or not.

s1 = int(input("Enter 1st side of triangle : "))
s2 = int(input("Enter 2nd side of triangle : "))
s3 = int(input("Enter 3rd side of triangle : "))

if s1+s2 > s3 and s2+s3 > s1 and s1+s3 > s2:
    print("Triangle is valid.")
else:
    print("Triangle is invalid.")    