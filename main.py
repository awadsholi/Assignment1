from Services import File_Access as File_Services
from Services import Data_Access as Data_Processing


def main():
    filename = "Employees.json"
    employees = File_Services.load_employees_from_file(filename)

    if not employees:
        print("No Employees found, Exit")
        return

    print("\nEMPLOYEES:")
    for employee in employees:
        print(f"- {employee.name}: {employee.department} | Salary: {employee.salary}$ | Age: {employee.age}")

    # Categorize employees
    categories = Data_Processing.categorize_employees(employees)
    print("\nSALARY CATEGORIES:")
    for category, emps in categories.items():
        print(f"{category} salary: {len(emps)} employees")

    # Store employees in different data structures
    storage = Data_Processing.storage_employees(employees)

    # Print storage structures
    print("\nSTACK STORAGE :")
    storage['Stack_Storage'].print_stack()

    print("\nQUEUE STORAGE :")
    storage['Queue_Storage'].print_queue()

    print("\nHASH MAP STORAGE:")
    for name, emp in storage['Hash_Storage'].items():
        print(f"{name} | {emp}")

    print(Data_Processing.total_salary(employees))

    File_Services.save_employees_to_file("Employees.json", employees)

if __name__ == "__main__":
    main()