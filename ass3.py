emp_id = input("Enter Employee ID: ")
name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))


employee = {
    "ID": emp_id,
    "Name": name,
    "Basic": basic_salary
}

hra = 0.20 * basic_salary
da = 0.10 * basic_salary
total_salary = basic_salary + hra + da

employee["HRA"] = hra
employee["DA"] = da
employee["Total"] = total_salary

print(employee["Total"])
print(employee)