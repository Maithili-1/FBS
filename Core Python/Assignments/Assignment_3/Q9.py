#WAP to input 5 subjects marks from user and display grade(e.g First Class, Second Class...)

s1 = int(input("Enter marks of 1st subject : "))
s2 = int(input("Enter marks of 2nd subject : "))
s3 = int(input("Enter marks of 3rd subject : "))
s4 = int(input("Enter marks of 4th subject : "))
s5 = int(input("Enter marks of 5th subject : "))

per = (s1+s2+s3+s4+s5/500) * 100

if per > 60 :
    print("First Class")
elif per > 50:
    print("Second Class")
elif per > 35:
    print("Pass")
else:
    print("Fail")