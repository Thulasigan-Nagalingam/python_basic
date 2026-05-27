salary=float(input("Enter your Basic Salary:"))

if (salary>100000):
    tax=salary*0.05
elif (salary>80000):
    tax=salary*0.03
else:
    tax=00

net_salary=salary-tax    
    
print("Salary Details")
print("----------------------------")
print(f"Basic Salary  : Rs.{salary:,.2f}")
print(f"Tax           : Rs.{tax:,.2f}")
print(f"Net Salary    : Rs.{net_salary:,.2f}")

