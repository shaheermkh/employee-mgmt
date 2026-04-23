import os
import csv

terminal_width = os.get_terminal_size().columns


def export_to_csv(employees, filename="employees.csv", date_added=None):
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
        writer.writerow(["Date", "ID", "Name", "Department", "Role", "Salary"])
        for emp in employees:
            emp_date_added = get_emp_value(emp, "date")
            emp_id = get_emp_value(emp, "id")
            name = get_emp_value(emp, "name")
            department = get_emp_value(emp, "department")
            role = get_emp_value(emp, "role")
            salary = format_salary(get_emp_value(emp, "salary"))
            writer.writerow([emp_date_added, emp_id, name, department, role, salary])

    print(f"Saved to {filename}".center(terminal_width))
