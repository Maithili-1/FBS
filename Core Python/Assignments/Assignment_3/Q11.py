# WAP accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

ticket = float(input("Enter ticket amount per person : "))

total = 0
for i in range(5):
    age = int(input("Enter age : "))
    
    if age < 12 :
        amount = ticket - (ticket*30/100)
    elif age > 59:
        amount = ticket - (ticket*50/100)
    else:
        amount = ticket
    
    total += amount

print("Total ticket amount : ", total)