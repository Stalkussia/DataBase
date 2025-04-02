from datetime import datetime
from employee import Employee
from employee_dao import EmployeeDAO

if __name__ == '__main__':
    test1 = Employee(26,'Said Amanov', 'Biter', 20000,datetime.now()) #New Employee class object

    dao = EmployeeDAO('Employee') #dao is an EmployeeDAO object that is connected to the dataBase.

    dao.insert(test1) #Inserting an Employee object into the database

    dao.get_by_id(24) #prints Info about an employee using his id.

    dao.get_all() #Prints out all the table of the database

    dao.update(24,'Tester', 20000) #Updates info (position and salary only) about an employee using his ID.

    dao.delete_(24)





