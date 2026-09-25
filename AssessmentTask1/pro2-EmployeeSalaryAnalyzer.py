#accept : Employee name  Basic salary  Experience 

employee_name = input ("Enter the Employee Name : ")
employee_basic_salary = float(input("Enter the Employee's Salary : "))
employee_experience = int(input("Enter the no of years experience (eg : 1 or 4 ) : "))

#Calculate HRA 
#hra = 40% of Basic Salary
hra = employee_basic_salary * 0.4

#Calculate DA 
#DA = 10% of Basic Salary
da = employee_basic_salary * 0.1


#Bonus based on experience 
if employee_experience >= 5 :
    bouns = employee_basic_salary * 0.2 
else : 
    bouns = 0

#Calculate Gross salary 
gross_salary = employee_basic_salary + hra + da +bouns

#display the result 
print("\n")
print("Salary calculator")
print(f"Employee Name : {employee_name}")
print("*****************************************************")

print(f"Basic Salary                 {employee_basic_salary}/month")
print(f"HRA                          {hra}/month")
print(f"DA                           {da}/month")
print("------------------------------------------------------------")
print(f"Gross Salary                     {gross_salary}/month")

print(f"Bouns                        {bouns}/year")



