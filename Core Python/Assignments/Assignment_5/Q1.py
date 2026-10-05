id = "Maithili"
password = "Mathu1#"

for i in range(3):
    userid = input("\nEnter User ID : ")
    psw = input("Enter password : ")

    if (userid==id or psw==password):
        print("\nLogin successful!.")
        break
    else:
        print("Incorrect User Id and Password.")
else:
    print("\nLogin Failed. Your 3 attempts are over.")