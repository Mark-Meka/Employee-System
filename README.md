|# Employee Management System

This Python program is an employee management system that allows for the management of employee records within an organization. It offers functionalities to add new employees, view all employee details, update employee salaries, and delete employees based on age criteria.

## Features

- **Add New Employee**: Input the name, age, position, and salary to add a new employee to the system.
- **Print All Employees**: Lists the details of all employees currently in the system.
- **Delete Employee by Age**: Removes employees from the system within a specified age range.
- **Update Salary by Name**: Update the salary for a specific employee by entering their name and the new salary amount.

## Classes and Methods

- `Employee`: Represents an employee with attributes for name, age, position, and salary. It includes methods to get and set these attributes.
- `add_employee()`: Static method to add a new employee to the system.
- `print_employees()`: Static method to print all employee details.
- `update_salary()`: Static method to update the salary of an employee based on their name.
- `delete_by_age()`: Static method to delete employees within a specified age range.

## Usage

1. **Run the Program**: Start the program in a Python environment.
2. **Menu Options**: The program will display a menu with options:
   - `1`: Add a new employee.
   - `2`: Print all employees.
   - `3`: Delete employees by age range.
   - `4`: Update an employee's salary by name.
   - `5`: Exit the program.
3. **Select an Option**: Input your choice and follow the prompts to manage employee records.

## Example

```python
# Add a new employee
1 -> Enter the name, age, position, and salary as prompted.

# Print all employees
2 -> Displays a list of all employees with their details.

# Delete employees by age
3 -> Enter the start and end age. Employees within this range will be deleted.

# Update an employee's salary
4 -> Enter the employee's name and the new salary.

# Exit the program
5 -> Ends the program execution.
