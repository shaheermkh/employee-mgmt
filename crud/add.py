import os
terminal_width = os.get_terminal_size().columns

from crud.export_to_csv import export_to_csv

def add_employee(employees, date_added):
  while True:
    prompt = "Enter employee id (number): "
    padding = " " * ((terminal_width - len(prompt)) // 2)
    employee_id = input(padding + prompt)

    if not employee_id.isdigit():
      print("Id must be a number".center(terminal_width))
      continue
    
    prompt = "Enter employee name: "
    padding = " " * ((terminal_width - len(prompt)) // 2)
    name = input(padding + prompt)
   
    prompt = "Enter employee department: "
    padding = " " * ((terminal_width - len(prompt)) // 2)
    department = input(padding + prompt)

    prompt = "Enter employee role: "
    padding = " " * ((terminal_width - len(prompt)) // 2)
    role = input(padding + prompt)

    prompt = "Enter employee salary (number): "
    padding = " " * ((terminal_width - len(prompt)) // 2)
    salary = input(padding + prompt)

    if salary.count('.') <= 1:
      formatted = salary.replace('.', '', 1)
      is_valid = formatted.isdigit()
    else:
      is_valid = False

    if not is_valid:
      print("Salary must be a number".center(terminal_width))
      continue

    break

  employees.append({
    "date": date_added,
    "name": name,
    "id": employee_id,
    "department": department,
    "role": role,
    "salary": salary
  })

  print("Employee added".center(terminal_width))
  print("─" * terminal_width)
  
  prompt = "Export to CSV? Y/N: "
  padding = " " * ((terminal_width - len(prompt)) // 2)
  choice = input(padding + prompt)

  if choice in ('y', 'yes', 'Y', 'YES'):
    export_to_csv(employees, date_added=date_added)