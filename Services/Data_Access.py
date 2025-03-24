# Importing Employee Object from Models Package
# Importing Structures For Storage
from Models import Employee
from Data_Structures import Structures

def categorize_employees(employees:list[Employee])-> dict[str,list[Employee]]:
    #Categorize Employees to Low, Mid and High based on salary
    return {
    "Low":[employee for employee in employees if employee.salary <  1000],
    "Mid":[employee for employee in employees if 1000 <= employee.salary <=  5000],
    "High":[employee for employee in employees if employee.salary >  5000]
    }


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
    employee_hash = {}
    for employee in employees:
        employee_hash[employee.name] = employee

    #Return as a Dictionary For Using
    return {
        "Stack_Storage":employee_stack,
        "Queue_Storage":employee_queue,
        "Hash_Storage":employee_hash
    }




