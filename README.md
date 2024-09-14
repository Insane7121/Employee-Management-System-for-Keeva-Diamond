# Employee Management System for Keeva Diamond

This is a command-line Python project for managing employee information at Keeva Diamond. It allows you to add, view, search, update, and delete employee records using an SQLite database.

## Features

- **Add Employee**: Add new employees with details like name, age, department, position, and salary.
- **View Employees**: View a list of all employees.
- **Search Employee**: Search for an employee by name.
- **Update Employee**: Update the details of an employee.
- **Delete Employee**: Delete an employee record by their ID.

## Requirements

This project uses **Python 3** and **SQLite3**.

## How to Run the Project

1. **Clone the repository or download the project files**.

2. **Install Python 3**: If you don't have Python installed, download and install it from [python.org](https://www.python.org/downloads/).

3. **Run the program**:
   - Navigate to the project directory where `employee_management.py` is located.
   - Open a terminal/command prompt and run:
     ```bash
     python employee_management.py
     ```

4. **Follow the instructions** in the terminal to manage employee data.

## Program Flow

- The system presents a menu with options to:
  1. Add Employee
  2. View Employees
  3. Search Employee
  4. Update Employee
  5. Delete Employee
  6. Exit

- Choose an option by typing the number corresponding to the action you want to perform.

## Database Details

The system uses **SQLite** to store employee information in a file called `employee.db`. The database is automatically created the first time the program runs, and it will store the following details for each employee:

- **ID**: Auto-incremented unique identifier.
- **Name**: The employee's full name.
- **Age**: The employee's age.
- **Department**: The department where the employee works.
- **Position**: The employee's job title.
- **Salary**: The employee's salary.

## Sample Commands

- Add a new employee with the required details.
- View the list of employees currently stored in the database.
- Search for an employee by their name to get more information.
- Update the employee information using their unique employee ID.
- Delete an employee from the system by ID.

## License

This project is open-source and available under the [MIT License](LICENSE).

