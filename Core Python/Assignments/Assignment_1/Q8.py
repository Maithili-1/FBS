# WAP to convert days into years, weeks and days.

D = int(input("Enter number of days : "))

years = D//365
rdays = D % 365

weeks = rdays//7
days = rdays % 7

print(f"{D} days means {years} years, {weeks} weeks and {days} days.")
