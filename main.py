employees = []

def main():
  while True:
    print("\nEmployee management system")
    print("1: Show all employees")
    print("2: Add employee")
    print("3: Edit employee")
    print("4: Delete employee")
    print("5: Exit")

    choice = input("Pick 1-5: ")

    if choice == '1':
      view_employees()
    elif choice == '2':
      add_employee()
    elif choice == '3':
      update_employee()
    elif choice == '4':
      delete_employee()
    elif choice == '5':
      break
    else:
      print("Try again")

def view_employees():
  if not employees:
    print("No employees available")
    return

  print("\nAll employees:")
  for employee in employees:
    print("-", employee['name'], "(id", employee['id'] + ")", "dept", employee['department'], "sal", employee['salary'])


def add_employee():
  name = input("Name: ")

  while True:
    employee_id = input("id (number): ")
    if employee_id.isdigit():
      break
    print("Id must be a number")

  department = input("Department: ")

  while True:
    salary = input("Salary (number): ")
    if salary.count('.') <= 1:
      formatted = salary.replace('.', '', 1)
      is_valid = formatted.isdigit()
    else:
      is_valid = False

    if is_valid:
      break
    print("Salary must be a number")

  employees.append({
    "name": name,
    "id": employee_id,
    "department": department,
    "salary": salary
  })

  print("Employee added")

def find_employee_by_id(employee_id):
  for employee in employees:
    if employee['id'] == employee_id:
      return employee
  return None

def update_employee():
  employee_id = input("Enter employee id to edit: ")
  employee = find_employee_by_id(employee_id)
  if not employee:
    print("Employee not found")
    return

  print(employee)
  new_name = input("Enter new name (Press enter to keep current): ")
  if new_name:
    employee['name'] = new_name

  new_department = input("Enter new department name (Press enter to keep current): ")
  if new_department:
    employee['department'] = new_department

  new_salary = input("Enter new salary (Press enter to keep current): ")
  if new_salary:
    if new_salary.count('.') <= 1:
      formatted = new_salary.replace('.', '', 1)
      is_valid = formatted.isdigit()
    else:
      is_valid = False

    if is_valid:
      employee['salary'] = new_salary
    else:
      print("Salary must be a number, change ignored")

  print("Employee updated")

def delete_employee():
  employee_id = input("Enter id to remove: ")
  employee = find_employee_by_id(employee_id)
  if not employee:
    print("Employee not found")
    return

  employees.remove(employee)
  print("Employee removed")

main()
