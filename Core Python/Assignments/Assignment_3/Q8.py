#WAP to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the same. If user enters the same number then show him success message otherwise failed. (Something like captcha).

import random

id = input("Enter User ID : ")
password = input("Enter Password : ")

if id == "maithili" and password == "maithu123":
    captcha = random.randint(1000,9999)
    print("Captcha : ", captcha)
    entered_captcha = int(input("Enter the captcha : "))
    if captcha == entered_captcha:
        print("Success.")
    else:
        print("Failed.")
else:
    print("Inorrect User ID and Password.")