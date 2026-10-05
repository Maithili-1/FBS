#WAP to check whether the triangle is equilateral, isosceles or scalene triangle.

s1 = int(input("Enter 1st side of triangle : "))
s2 = int(input("Enter 2nd side of triangle : "))
s3 = int(input("Enter 3rd side of triangle : "))

if (s1==s2==s3):
    print("Triangle is Equilateral.")
elif (s1==s2 or s2==s3 or s1==s3):
    print("Triangle is Isosceles.")
else:
    print("Triangle is Scalene.")