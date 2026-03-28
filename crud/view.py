import os
terminal_width = os.get_terminal_size().columns

def view_employees(employees):
  if not employees:
    print("No employees available".center(terminal_width))
    return

  print("All employees:".center(terminal_width))
  for employee in employees:
    print(f"- {employee['name']} (id {employee['id']}) dept {employee['department']} role {employee.get('role', '')} sal {employee['salary']}".center(terminal_width))
