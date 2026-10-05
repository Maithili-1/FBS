# WAP to calculate selling price of book based on cost price and discount.

cost = int(input("Enter cost price of book : "))
D = float(input("Enter discount in % : "))

discount = (cost * D)/100
SP = cost - discount
print(f"Selling price is : {SP} Rs.")