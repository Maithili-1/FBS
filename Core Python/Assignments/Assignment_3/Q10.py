#WAP to check if person is eligible to marry or not(male age>=21 and female age>=18).

gender = input("Enter gender(M/F) : ")
age = int(input("Enter age : "))

if gender == 'M':
    if age>=21:
        print("Boy is eligible to marry.")
    else:
        print("Boy is not eligible to marry.")
else:
    if age>=18:
        print("Girl is eligible to marry.")
    else:
        print("Girl is not eligible to marry")