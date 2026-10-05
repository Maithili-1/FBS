gender = input("Enter gender(M/F) : ")
age = int(input("Enter age : "))

if (gender == 'M'):
    if (age >= 21 ):
        print("Boy is eligible for marriage.")
    else:  
        print("Boy is not eligible for marriage.")
else:
    if (age >= 18 ):
            print("Girl is eligible for marriage.")
    else:  
            print("Girl is not eligible for marriage.")
