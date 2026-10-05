n = int(input("Enter number of passengers : "))
ticket_cost = int(input("Enter per person ticket cost(Rs) : "))

total_cost = 0
for i in range(1,n+1):
    age = int(input(f"Enter age of passenger {i} : "))
    
    if age<12:
        ticket = ticket_cost - (ticket_cost * (30/100))
    elif age>59:
        ticket = ticket_cost - (ticket_cost * (50/100))
    else:
        ticket = ticket_cost
    total_cost += ticket

print(f"Total amount of ticket to travel {n} passengers = {total_cost} Rs.")