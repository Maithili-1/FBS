#WAP to accept an interger amount from user and tell minimum number of notes needed for representing that amount.

amount = int(input("Enter an integer amount : "))
amt = amount

notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
count = 0
for note in notes:
    count +=  amt//note
    amt = amt % note
    
    if amt==0:
        break
    
print(f"For {amount} Rs, minimum {count} notes are required.")