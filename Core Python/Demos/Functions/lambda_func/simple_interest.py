SI = lambda p,t,r: (p*t*r)/100

p = int(input("Enter the principal amount : "))
t = int(input("Enter time : "))
r = int(input("Enter rate of interest(%) : "))

res = SI(p,t,r)
print(res)