import re


# Parent Class
class Employee:
    total_employees = 0

    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
        Employee.total_employees += 1

    def calculate_salary(self):
        #This method will be override
        pass


# Child Class: Manager
class Manager(Employee):
    total_managers = 0
    fixed_salary = 4000

    def __init__(self, name, employee_id):
        if not Manager.validate_id(employee_id):
            raise ValueError("Invalid Manager ID!")

        super().__init__(name, employee_id)
        Manager.total_managers += 1

    def calculate_salary(self):
        return Manager.fixed_salary

    @staticmethod
    def validate_id(employee_id):
        pattern = r"^M\d{3}$"
        if re.match(pattern, employee_id):
           return True
        else:
           return False


# Child Class: Developer
class Developer(Employee):
    total_developers = 0
    hourly_rate = 25
    working_hours = 160

    def __init__(self, name, employee_id):
        if not Developer.validate_id(employee_id):
            raise ValueError("Invalid Developer ID!")

        super().__init__(name, employee_id)
        Developer.total_developers += 1

    def calculate_salary(self):
        return Developer.hourly_rate * Developer.working_hours

    @staticmethod
    def validate_id(employee_id):
        pattern = r"^D\d{3}$"
        if re.match(pattern, employee_id):
           return True
        else:
           return False


# test section
# Create valid employee
manager1 = Manager("mahsa", "M123")
developer1 = Developer("hashemi", "D456")

# Try to create employee with invalid ID
try:
    manager2 = Manager("blah", "X999")
except ValueError as error:
    print("Error:", error)


employees = [manager1, developer1]

for emp in employees:
    print(f"Name: {emp.name}")
    print(f"ID: {emp.emp_id}")
    print(f"Monthly Salary:{emp.calculate_salary()}")

print(f"Total Employees: {Employee.total_employees}")
print(f"Total Managers: {Manager.total_managers}")
print(f"Total Developers: {Developer.total_developers}")

