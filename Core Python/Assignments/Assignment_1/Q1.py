# WAP to calculate percentage of student based on marks of any 5 subjects.

s1 = int(input("Enter obtained marks of subject 1 : "))
s2 = int(input("Enter obtained marks of subject 2 : "))
s3 = int(input("Enter obtained marks of subject 3 : "))
s4 = int(input("Enter obtained marks of subject 4 : "))
s5 = int(input("Enter obtained marks of subject 5 : "))

total_obtained_marks = s1 + s2 + s3 + s4 + s5

percentage = (total_obtained_marks / 500) *100

print(f"Percentage of student based on 5 subjects is {percentage:.2f}%")
