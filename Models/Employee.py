#There is a model of employee base class and subclasses with store a data as a dict format
#Type hints and annotations to ensure the data types



class Employee:
    def __init__(self, name: str, age: int, salary: float, department: str):
        self.name = name
        self.age = age
        self.salary = salary
        self.department = department

    def to_dictionary(self):
        return {
            "name" : self.name,
            "age" : self.age,
            "salary" : self.salary,
            "department" : self.department
        }
    #Define Properties
    #name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value:str):
        self.__name = value
    #age
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        self.__age = value

    #salary
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,salary:float):
        self.__salary = salary

    #Department
    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self,department):
        self.__department = department

    def give_raise(self,raise_amount):
        self.salary += raise_amount

    def __repr__(self):
        return (f"Employee(name='{self.name}', age={self.age}, "
                f"salary={self.salary}, department='{self.department}')")



class Developer(Employee):
    def __init__(self,name:str,age:int,salary:float,department:str,language:str):
        super().__init__(name,age,salary,department)
        self.language = language

    def to_dictionary(self):
        data = super().to_dictionary()
        data["language"] = self.language
        return data
    #Add Properties
    #Language
    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self,language):
        self.__language = language

    def __repr__(self):
        return (f"Developer(name='{self.name}', age={self.age}, "
                f"salary={self.salary}, department='{self.department}', "
                f"language='{self.language}')")


class Manager(Employee):
    def __init__(self,name:str,age:int,salary:float,department:str,team_members_number:int):
        super().__init__(name,age,salary,department)
        self.team_members_number = team_members_number

    def to_dictionary(self):
        data = super().to_dictionary()
        data["Team_Size"] = self.team_members_number
        return data
    #Add Properties
    #Team_Size
    @property
    def team_size(self):
        return self.__team_members_number

    @team_size.setter
    def team_size(self,team_members_number):
        self.__team_members_number = team_members_number

    def __repr__(self):
        return (f"Manager(name='{self.name}', age={self.age}, "
                f"salary={self.salary}, department='{self.department}', "
                f"team_size={self.team_members_number})")
