# r - only read
# r+ - read and write
# w - only write
# a - append
table_employee = []

employee_file = open("employees.txt", "r")
#print(employee_file.readable()) # can read?
for employee  in employee_file.readlines():
    employee_data = employee.split(",")
    table_employee.append(employee_data)
   
#print(employee_file.readlines()) # read the whole file and create a new list
# print(employee_file.read()) # read the whole file
print(table_employee) 
employee_file.close()