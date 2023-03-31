# Write a program that takes input of someone's basic salary and benefits, 
# adds them to find the gross salary then uses  the gross salary to find the NHIF.

basic_salary = float(input("Enter your basic salary: "))
benefits = float(input("Enter your benefits: "))

gross_salary = basic_salary + benefits

nhif = 0

if gross_salary > 0:
    if gross_salary <= 5999:
        nhif = 150
    elif (gross_salary >= 6000) and (gross_salary <= 7999):
        nhif = 300
    elif (gross_salary >= 8000) and (gross_salary <= 11999):
        nhif = 400
    elif (gross_salary >= 12000) and (gross_salary <= 14999):
        nhif = 500    
    elif (gross_salary >= 15000) and (gross_salary <= 19999):
        nhif = 600
    elif (gross_salary >= 20000) and (gross_salary <= 24999):
        nhif = 750
    elif (gross_salary >= 25000) and (gross_salary <= 29999):
        nhif = 850
    elif (gross_salary >= 30000) and (gross_salary <= 34999):
        nhif = 900
    elif (gross_salary >= 35000) and (gross_salary <= 39999):
        nhif = 950
    elif (gross_salary >= 40000) and (gross_salary <= 44999):
        nhif = 1000
    elif (gross_salary >= 45000) and (gross_salary <= 49999):
        nhif = 1100
    elif (gross_salary >= 50000) and (gross_salary <= 59999):
        nhif = 1200
    elif (gross_salary >= 60000) and (gross_salary <= 69999):
        nhif = 1300
    elif (gross_salary >= 70000) and (gross_salary <= 79999):
        nhif = 1400
    elif (gross_salary >= 80000) and (gross_salary <= 89999):
        nhif = 1500
    elif (gross_salary >= 90000) and (gross_salary <= 99999):   
        nhif = 1600
    else:
        nhif = 1700
else:
    print("Gross salary cannot be 0 or less")
    
print("NHIF amount: " + str(nhif))