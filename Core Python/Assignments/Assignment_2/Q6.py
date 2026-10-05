#WAP to calculate total salary of employees based on basic, da = 10% of basic, ta = 12% of basic, hra = 15% of basic.

basic = int(input("Enetr the salary of Employee : "))

#Dearness Allowance
da = basic * (10/100)
ta = basic * (12/100)
hra = basic * (15/100)

total_salary = basic + da + ta + hra
print("DA : ", da)
print("TA : ",ta)
print("HRA : ",hra)
print("Total salary of employee is ", total_salary)