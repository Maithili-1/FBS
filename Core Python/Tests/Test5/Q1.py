D = [2000, 500, 200, 100, 50, 20, 10, 5]

amt = int(input("Enter the amount : "))
min_notes = 0

for i in D :
    count = amt//i
    if count > 0:
        print(f"{i} : {count}")
        min_notes += count
        amt %= i
        
print("Minimum number of notes =", min_notes)

if amt > 0:
    print("Remaining amount =", amt)