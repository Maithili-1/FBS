n = int(input("Enter number of students : "))
li= []

for i in range(n):
    name = input(f"Enter name of the student {i+1} : ")
    li.append(name)
    
print(li)
