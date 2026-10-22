n = int(input("Enter the value of n : "))

total_salary = 0
for i in range(1, n+1):
    basic_sal = int(input("Enter sbasic salary of employee : "))
    
    if basic_sal<20000:
        da = (basic_sal * (10/100))
        ta = (basic_sal * (12/100))
        hra = (basic_sal * (15/100))
    else:
        da = (basic_sal * (15/100))
        ta = (basic_sal * (18/100))
        hra = (basic_sal * (20/100))
    
    sal = basic_sal+da+ta+hra
    total_salary+=sal
    
    print(f"Total salary of employee {i} = {sal}.")
    
print(f"\nTotal salary of all employees = {total_salary}.")