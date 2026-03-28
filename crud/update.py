import os
terminal_width = os.get_terminal_size().columns

def update_employee(employees):
  prompt = "Enter employee id to edit: "
  padding = " " * ((terminal_width - len(prompt)) // 2)
  employee_id = input(padding + prompt)

  print("─" * terminal_width)

  employee = find_employee_by_id(employees, employee_id)
  if not employee:
    print("Employee not found".center(terminal_width))
    return

  print(employee.center(terminal_width))
  prompt = "Enter new name (Press enter to keep current): "
  padding = " " * ((terminal_width - len(prompt)) // 2)
  new_name = input(padding + prompt)

  if new_name:
    employee['name'] = new_name

  prompt = "Enter new department (Press enter to keep current): "
  padding = " " * ((terminal_width - len(prompt)) // 2)
  new_department = input(padding + prompt)
  if new_department:
    employee['department'] = new_department

  prompt = "Enter new role (Press enter to keep current): "
  padding = " " * ((terminal_width - len(prompt)) // 2)
  new_role = input(padding + prompt)
  if new_role:
    employee['role'] = new_role

  prompt = "Enter new salary (Press enter to keep current): "
  padding = " " * ((terminal_width - len(prompt)) // 2)
  new_salary = input(padding + prompt)
  if new_salary:
    if new_salary.count('.') <= 1:
      formatted = new_salary.replace('.', '', 1)
      is_valid = formatted.isdigit()
    else:
      is_valid = False

    if is_valid:
      employee['salary'] = new_salary
    else:
      print("Salary must be a number, change ignored".center(terminal_width))

  print("Employee updated".center(terminal_width))


def find_employee_by_id(employees, employee_id):
  for employee in employees:
    if employee['id'] == employee_id:
      return employee
  return None
