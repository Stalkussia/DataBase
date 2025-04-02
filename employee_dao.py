import sqlite3
from employee import Employee


class EmployeeDAO():
    def __init__(self,database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

        sql = 'SELECT * FROM Employee'
        self.cursor.execute(sql)

        rows = self.cursor.fetchall()
        employees = []

        for row in rows:
            employee = Employee(row[0],row[1], row[2], row[3], row[4])
            employees.append(employee)

    def insert(self,employee:Employee):
        self.cursor.execute('INSERT INTO Employee (name,position,salary,hire_date) VALUES (?,?,?,?)', (employee.name, employee.position, employee.salary, employee.hire_date))
        self.conn.commit()

    def get_all(self):
        self.cursor.execute("SELECT * FROM employee")
        rows = self.cursor.fetchall()
        return print(rows)

    def get_by_id(self,id):
        self.cursor.execute('SELECT id, name, position, salary, hire_date FROM Employee WHERE id = ?', (id,))
        row = self.cursor.fetchone()

        if row:
            return print(Employee(row[0], row[1], row[2], row[3], row[4]))
        else:
            return print('No employee found. . .')

    def update(self, id:int, new_position:str, new_salary:int):
        self.cursor.execute('UPDATE Employee '
                            'SET position = ?, salary = ?' 'WHERE id = ?', (new_position,new_salary, id))
        self.conn.commit()

    def delete_(self,id:int):
        self.cursor.execute('DELETE FROM Employee '
                            'WHERE id = ?', (id,))
        self.conn.commit()




