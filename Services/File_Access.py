import json
from typing import  Optional
from Models.Employee import Employee

def save_employees_to_file(filename:str,employees:list[Employee]):
    employee_list = []

    for employee in employees:
        employee_dict_format = employee.to_dictionary()
        employee_list.append(employee_dict_format)

    with open(filename,"w") as file:
        json.dump(employee_list,file)

    file.close()

def load_employees_from_file(filename:str)->Optional[list[Employee]]:
    try:
        with open(filename,"r") as file:
            file_data = json.load(file)
        employee_list = []
        for employee in file_data:
            new_employee = Employee(**employee) # Create Employee using dictionary unzipping
            employee_list.append(new_employee)
        return employee_list
    except FileNotFoundError as e:
        print(f"{e} {filename} not found")
        return None