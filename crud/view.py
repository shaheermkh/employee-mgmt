import os

terminal_width = os.get_terminal_size().columns


def view_employees(employees):
    if not employees:
        print("No employees available".center(terminal_width))
        return

    print("All employees:".center(terminal_width))
    for employee in employees:
        date_added = employee.get("date", "N/A")
        print(
            f"Date {date_added}- Name: {employee['name']} ID: {employee['id']} Dept: {employee['department']} Role: {employee.get('role', '')} Salary: {employee['salary']}".center(
                terminal_width
            )
        )
