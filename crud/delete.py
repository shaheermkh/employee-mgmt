import os

terminal_width = os.get_terminal_size().columns


def delete_employee(employees):
    prompt = "Enter id to remove: "
    padding = " " * ((terminal_width - len(prompt)) // 2)
    employee_id = input(padding + prompt)

    print("─" * terminal_width)

    employee = find_employee_by_id(employees, employee_id)
    if not employee:
        print("Employee not found".center(terminal_width))
        return

    employees.remove(employee)
    print("Employee removed".center(terminal_width))


def find_employee_by_id(employees, employee_id):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    return None
