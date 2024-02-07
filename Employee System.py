class Employee:
    def __init__(self, name, age, salary, position):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

    def get_position(self):
        return self.position

    def get_salary(self):
        return self.salary

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_position(self, position):
        self.position = position

    def set_salary(self, salary):
        self.salary = salary

    def add_employee(employees):
        name=str(input("Enter the name of Employee: "))
        age=int(input("Enter the age of Employee: "))
        position=str(input("Enter the position of Employee: "))
        salary=int(input("Enter the salary of Employee: "))
        employee=Employee(name,age,position,salary)
        employees.append(employee)

    def __str__(self):
        return f'Name: {self.name},Age: {self.age},Position: {self.position},Salary: {self.salary}'

    def print_employees(employees):
        for employee in employees:
            print(employee)

    def update_salary(employees):
        name=input("Enter the name of Employee to update the salary: ")
        salary=int(input("Enter to update his salary: "))
        employee_found=False
        for employee in employees:
            if employee.get_name() == name:
                employee.set_salary(salary)
                employee_found=True
                break
            if not employee_found:
                print("No Employee found with this name")

    def delete_by_age(employees):
        Agefrom=int(input("Enter Age from: "))
        Ageto=int(input("Enter Age to: "))
        employee_copy=employees.copy()
        employees=[i for i in employees if not Agefrom <= i.get_age() <= Ageto]
        if employees == employee_copy:
            print("No employees found within the specified age range.")
        return employees

if __name__ == "__main__":
    employees = []
    while True:
        print("\n1. Add new employee")
        print("2. Print all employees")
        print("3. Delete employee by age")
        print("4. Update salary by name")
        print("5. End the program")
        choice = int(input("\nEnter your choice (1 to 5): "))

        if choice == 1:
            Employee.add_employee(employees)

        elif choice == 2:
            Employee.print_employees(employees)

        elif choice == 3:
            employees = Employee.delete_by_age(employees)

        elif choice == 4:
            Employee.update_salary(employees)

        elif choice == 5:
            break

        else:
            print("Invalid choice. Please enter a valid choice.")
