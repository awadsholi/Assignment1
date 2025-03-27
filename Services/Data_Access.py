# Importing Employee Object from Models Package
# Importing Structures For Storage

from functools import reduce
import time
from Models.Employee import Employee
from typing import Dict, List, Union, Optional
from Data_Structures import Structures
from Exceptions.exceptions import EmployeeNotFound
from Services.decorator import log_time
def categorize_employees(employees:list[Employee])-> dict[str,list[Employee]]:
    #Categorize Employees to Low, Mid and High based on salary
    categorize_dictionary: dict[str, list[Employee]] = {
        "Low": [],
        "Mid": [],
        "High": []
    }

    for employee in employees:
        if employee.salary < 1000:
            categorize_dictionary["Low"].append(employee)
        elif 1000 <= employee.salary <=  5000:
            categorize_dictionary["Mid"].append(employee)

        else:
            categorize_dictionary["High"].append(employee)

    return categorize_dictionary


#Storage Employees Data
def storage_employees(employees:list[Employee]):
    # Implementing Stack Storage
    employee_stack = Structures.Stack()
    for emp in employees:
        employee_stack.push(emp)
    # Implementing Queue Storage
    employee_queue = Structures.Queue()
    for emp in employees:
        employee_queue.enqueue(emp)

    # Hash Map Simple
    employee_hash: Dict[str, Employee] = reduce(
        lambda temp_dict, emp: {**temp_dict, emp.name: emp},
        employees,
        {}
    )
    #temp_dict as short dictionary
    #{**temp_dict, emp.name: emp} ---> new dictionary created in each iteration
    #this is the same code
    #employee_hash = {}
    #for emp in employees:
    #    employee_hash[emp.name] = emp
    #Return as a Dictionary For Using
    return {
        "Stack_Storage":employee_stack,
        "Queue_Storage":employee_queue,
        "Hash_Storage":employee_hash
    }


#Find Employee Function
def find_employee(name:str,employees:list[Employee])->list[Employee]:
    filtered = list(filter(lambda e : e.name == name , employees))
    #code equivalent:
    #for employee in employees:
    #    if employee.name == name:
    #        return employee
    if not filtered:
        raise EmployeeNotFound(f"Employee with name {name} Not Found")
    return  filtered



def calculate_bonus(*args: Union[Employee, dict], **kwargs: float) -> dict[str, float]:
    rate = kwargs.get("rate", 0.1)
    return dict(
        map(
            lambda emp: (
                emp.name if isinstance(emp, Employee) else emp['name'],
                (emp.salary if isinstance(emp, Employee) else emp['salary']) * rate
            ),
            args
        )
    )

@log_time
def total_salary(employees: list[Employee]) -> float:
    time.sleep(2)
    return reduce(lambda temp_salary, emp:temp_salary + emp.salary , employees,0.0)

