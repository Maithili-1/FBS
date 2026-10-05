# WAP to convert distance given in feet and inches into meter and centimeter.

f = int(input("Enter distance in feet : "))
i = int(input("Enter distance in inch : "))

cm = ((f * 12) + i) * 2.54
m = cm/100

print(f"{f} feet and {i} inches = {m:.4f} m.")
print(f"{f} feet and {i} inches = {cm:.4f} cm.")