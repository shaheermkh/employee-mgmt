import os
terminal_width = os.get_terminal_size().columns

def filter_employees(employees):
  if not employees:
    print("No employees available".center(terminal_width))
    return

  print("Filter by:".center(terminal_width))
  print("1: Department  2. Role  3. Salary >=  4. Salary <=  5. Exact salary  6. Back".center(terminal_width))
  print("─" * terminal_width)

  prompt = "Pick 1-6: "
  padding = " " * ((terminal_width - len(prompt)) // 2)
  choice = input(padding + prompt)
  
  if choice == '1':
    dept = input("Department to filter: ".center(terminal_width))
    filtered = [e for e in employees if e['department'].lower() == dept.lower()]
  elif choice == '2':
    role = input("Role to filter: ".center(terminal_width))
    filtered = [e for e in employees if e.get('role', '').lower() == role.lower()]
  elif choice == '3':
    val = input("Minimum salary: ".center(terminal_width))
    try:
      min_salary = float(val)
      filtered = [e for e in employees if float(e['salary']) >= min_salary]
    except ValueError:
      print("Invalid number".center(terminal_width))
      return
  elif choice == '4':
    val = input("Maximum salary: ".center(terminal_width))
    try:
      max_salary = float(val)
      filtered = [e for e in employees if float(e['salary']) <= max_salary]
    except ValueError:
      print("Invalid number".center(terminal_width))
      return
  elif choice == '5':
    val = input("Exact salary: ".center(terminal_width))
    try:
      exact_salary = float(val)
      filtered = [e for e in employees if float(e['salary']) == exact_salary]
    except ValueError:
      print("Invalid number".center(terminal_width))
      return
  else:
    return

  if not filtered:
    print("No employees match filter".center(terminal_width))
    return

  print("\nFiltered employees:".center(terminal_width))
  for employee in filtered:
    print(f"- {employee['name']} (id {employee['id']}) dept {employee['department']} role {employee.get('role', '')} sal {employee['salary']}".center(terminal_width))
