n = int(input("Enter number of students : "))

total_per = 0
for i in range(1,n+1):
    print(f"\nEnter marks of student-{i} :- ")
    
    sum = 0
    for j in range(1,6):
        marks = int(input(f"Enter marks of subject {j} : "))
        sum+=marks
        
    percentage = (sum / 500) * 100
    print(f"\nPercentage of student {i} = {percentage}%.")
    total_per += percentage

avg = total_per/n
print(f"\nAverage percentage of {n} students is {avg}%.")