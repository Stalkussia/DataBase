from datetime import datetime

class Employee:
    def __init__(self, id:int,name:str,position:str,salary:int,hire_date:datetime):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary
        self.hire_date = hire_date


    def set_name(self,name):
        self.name = name

    def set_position(self,position:str):
        self.position = position

    def set_salary(self,salary:int):
        self.salary = salary

    def set_hire_date(self,hire_date:datetime):
        self.hire_date = hire_date

    def get_name(self):
        return print(f"Name and Surname: {self.name}")

    def get_position(self):
        return print(f"Position: {self.position}")

    def get_hire_date(self):
        return print(f"Hire date: {self.hire_date}")



    def __str__(self):
        return f"Id: {self.id}, Name and Surname: {self.name}, Position: {self.position}, Hire date: {self.hire_date}."



