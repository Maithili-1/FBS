#WAP to calculate profit or loss.

cp = int(input("Enter the Cost Price : "))
sp = int(input("Enter the Selling Price : "))

if(sp > cp):
    profit = sp-cp
    print("Profit : ",profit)
elif(cp > sp):
    loss = cp-sp
    print("Loss : ",loss)
else:
    print("No profit, No loss")