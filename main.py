import os
import json
import csv

from crud.add import add_employee
from crud.view import view_employees
from crud.update import update_employee
from crud.delete import delete_employee
from crud.filter import filter_employees

terminal_width = os.get_terminal_size().columns
employees = []
json_file = "data/employees.json"

def load_data():
    global employees
    if os.path.exists(json_file):
        with open(json_file, "r") as f:
            employees = json.load(f)

def save_data():
    os.makedirs("data", exist_ok=True)
    with open(json_file, "w") as f:
        json.dump(employees, f, indent=4)
  
def export_to_csv(employees, filename="data/employees.csv"):
    if not employees:
        print("No employees to export.".center(terminal_width))
        return

    def get_emp_value(emp, key):
        if isinstance(emp, dict):
            return emp.get(key, "")
        else:
            return getattr(emp, key, "")

    def format_salary(salary):
        if isinstance(salary, (int, float)):
            return f"${salary:,.2f}"
        return salary

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(["ID", "Name", "Department", "Role", "Salary"])
        for emp in employees:
            emp_id = get_emp_value(emp, "id")
            name = get_emp_value(emp, "name")
            department = get_emp_value(emp, "department")
            role = get_emp_value(emp, "role")
            salary = format_salary(get_emp_value(emp, "salary"))
            writer.writerow([emp_id, name, department, role, salary])

    print(f"Saved to {filename}")

def main():
    load_data()
    print("Employee Management System".center(terminal_width))

    while True:
        print("─" * terminal_width)
        print("1. Show all employees  2. Add employee  3. Edit employee  4. Delete employee  5. Filter employees  6. Export to CSV  7. Exit".center(terminal_width))
        print("─" * terminal_width)
        
        prompt = "Pick 1-7: "
        padding = " " * ((terminal_width - len(prompt)) // 2)
        choice = input(padding + prompt)

        print("─" * terminal_width)

        if choice == '1':
            view_employees(employees)
        elif choice == '2':
            add_employee(employees)
            save_data()
        elif choice == '3':
            update_employee(employees)
            save_data()
        elif choice == '4':
            delete_employee(employees)
            save_data()
        elif choice == '5':
            filter_employees(employees)
        elif choice == '6':
            export_to_csv(employees)
        elif choice == '7':
            break
        else:
            print("Try again".center(terminal_width))

main()
