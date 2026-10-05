#WAP to enter P, T, R and calculate compount interest.

p = int(input("Enter the Principal amount: "))
t = int(input("Enter the Time in years: "))
r = int(input("Enter the Rate of interest in % per year: "))

amount = p*(1+r/100)**t

CI = amount - p
print("Compound Interest : ", CI)