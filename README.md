Employee Database

Description:

This is a Python application that manages employee data using a SQLite database. It performs basic CRUD operations (Create, Read, Update, Delete) on an `employee` table.
The project uses an `Employee` class to represent employee data and an `EmployeeDAO` class to handle database operations.

- Create and connect to a SQLite database (`employee_db`)
- Create an `employee` table with the following columns:
  - id (integer, primary key, auto-increment)
  - name (text)
  - position (text)
  - salary (real)
  - hire_date (text)
- Add new employees
- Retrieve employees by ID or list all
- Update existing employee details
- Delete employees by ID


1. Employee

This class represents an individual employee.

Fields:

id:ID (set by the database)

name: Employee’s name

position: Job

salary: Employee salary

hire_date: Hiring date (format: YYYY-MM-DD)

Example:

emp = Employee(None, "John Smith", "Manager", 75000, "2023-01-01")
print(emp)

Output:

Employee(id=None, name='John Smith', position='Manager', salary=75000, hire_date='2023-01-01')

2. EmployeeDAO

This class handles all interactions with the database.

def insert(employee: Employee)

Adds a new employee to the database.

Example:

dao.insert(emp)

Output:
Employee inserted successfully.

def get_by_id(id: int)

Fetches a single employee by ID.

Example:

dao.get_by_id(1)

Output:

Employee(id=1, name='John Smith', position='Manager', salary=75000, hire_date='2023-01-01')


def get_all()

Fetches all employees from the database.

Example:


dao.get_all()

Output:

Employee(id=1, name='John Smith', position='Manager', salary=75000, hire_date='2023-01-01')
Employee(id=2, name='Jane Doe', position='Developer', salary=65000, hire_date='2023-02-01')


update(employee: Employee)
Updates an employee’s information.

Example:

emp.salary = 80000
dao.update(emp)

Output:
Employee updated successfully.


def delete(id: int)

Deletes an employee by ID.

Example:
dao.delete(1)
Output:
Employee deleted successfully.


Employee.py: Defines the Employee class.

EmployeeDAO.py: Handles the database logic.

main.py: Example tests for CRUD operations.
