class Employee:
    def __init__(self, name, department, position):
        self.name = name
        self.department = department
        self.position = position

    
class Department:
    def __init__(self,name):
        self.name = name
        self.employees = []

    def add_employees(self, other):
        if(other.department == self.name):
            self.employees.append(other)
    
    def display_employees(self):
        if not self.employees:
            return f"No employees in {self.name} department"
        else:
            employee_list = '\n'.join(str(emp) for emp in self.employees)
            return f"Employees in {self.name} department:\n{employee_list}"