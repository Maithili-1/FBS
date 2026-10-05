#WAP to enter P, T, R and calculate simple interest.

p = int(input("Enter the Principal amount: "))
t = int(input("Enter the Time in years: "))
r = int(input("Enter the Rate of interest in % per year: "))

SI = (p*t*r)/100
print("Simple Interest : ", SI)
