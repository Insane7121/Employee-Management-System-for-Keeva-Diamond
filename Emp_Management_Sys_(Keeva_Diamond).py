import sqlite3
from sqlite3 import Error


# Database connection
def create_connection():
    """Create a database connection to SQLite."""
    conn = None
    try:
        conn = sqlite3.connect('employee.db')
        return conn
    except Error as e:
        print(e)
    return conn

# Create employee table
def create_table(conn):
    """Create the employee table."""
    try:
        sql = '''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            department TEXT NOT NULL,
            position TEXT NOT NULL,
            salary REAL
        );
        '''
        conn.execute(sql)
    except Error as e:
        print(e)

# Add a new employee
def add_employee(conn, employee):
    """Insert a new employee into the employees table."""
    sql = ''' INSERT INTO employees(name, age, department, position, salary)
              VALUES(?, ?, ?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, employee)
    conn.commit()
    return cur.lastrowid

# View all employees
def view_employees(conn):
    """Query all rows in the employees table."""
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")

    rows = cur.fetchall()
    print("\nEmployee List:")
    for row in rows:
        print(row)

# Search employee by name
def search_employee(conn, name):
    """Search employee by name."""
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees WHERE name=?", (name,))
    rows = cur.fetchall()

    if rows:
        print("\nSearch Results:")
        for row in rows:
            print(row)
    else:
        print("No employee found with that name.")

# Update employee details
def update_employee(conn, employee):
    """Update an employee's details."""
    sql = ''' UPDATE employees
              SET name = ?,
                  age = ?,
                  department = ?,
                  position = ?,
                  salary = ?
              WHERE id = ? '''
    cur = conn.cursor()
    cur.execute(sql, employee)
    conn.commit()

# Delete employee by ID
def delete_employee(conn, emp_id):
    """Delete an employee by ID."""
    sql = 'DELETE FROM employees WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (emp_id,))
    conn.commit()

# Main program logic
def main():
    conn = create_connection()
    if conn is not None:
        create_table(conn)

        while True:
            print("\nEmployee Management System - Keeva Diamond")
            print("1. Add Employee")
            print("2. View Employees")
            print("3. Search Employee")
            print("4. Update Employee")
            print("5. Delete Employee")
            print("6. Exit")

            choice = input("\nEnter your choice (1-6): ")

            if choice == '1':
                name = input("Enter employee name: ")
                age = int(input("Enter employee age: "))
                department = input("Enter employee department: ")
                position = input("Enter employee position: ")
                salary = float(input("Enter employee salary: "))

                employee = (name, age, department, position, salary)
                add_employee(conn, employee)
                print(f"\nEmployee '{name}' added successfully!")

            elif choice == '2':
                view_employees(conn)

            elif choice == '3':
                name = input("Enter employee name to search: ")
                search_employee(conn, name)

            elif choice == '4':
                emp_id = int(input("Enter employee ID to update: "))
                name = input("Enter new name: ")
                age = int(input("Enter new age: "))
                department = input("Enter new department: ")
                position = input("Enter new position: ")
                salary = float(input("Enter new salary: "))

                employee = (name, age, department, position, salary, emp_id)
                update_employee(conn, employee)
                print(f"\nEmployee ID {emp_id} updated successfully!")

            elif choice == '5':
                emp_id = int(input("Enter employee ID to delete: "))
                delete_employee(conn, emp_id)
                print(f"\nEmployee ID {emp_id} deleted successfully!")

            elif choice == '6':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")

        conn.close()
    else:
        print("Error! Cannot connect to the database.")

if __name__ == '__main__':
    main()
