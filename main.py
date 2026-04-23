import os
import pandas
from datetime import date

from crud.add import add_employee
from crud.view import view_employees
from crud.update import update_employee
from crud.delete import delete_employee
from crud.filter import filter_employees
from crud.export_to_csv import export_to_csv

terminal_width = os.get_terminal_size().columns
employees = []
csv_file = "employees.csv"


def load_data():
    global employees
    if os.path.exists(csv_file):
        data = pandas.read_csv(csv_file)
        employees.clear()

        for i in range(len(data)):
            row = data.iloc[i]
            salary = str(row["Salary"]).replace("$", "").replace(",", "")
            employees.append(
                {
                    "date": row["Date"],
                    "id": row["ID"],
                    "name": row["Name"],
                    "department": row["Department"],
                    "role": row["Role"],
                    "salary": float(salary) if salary != "" else 0,
                }
            )
        if len(employees) == 1:
            print("Loaded 1 employee".center(terminal_width))
        else:
            print(
                ("Loaded " + str(len(employees)) + " employees").center(terminal_width)
            )
    else:
        print("No existing CSV file found".center(terminal_width))


def main():
    load_data()

    while True:
        print("─" * terminal_width)
        print(
            "1. Show all employees  2. Add employee  3. Edit employee  4. Delete employee  5. Filter employees  6. Export to CSV  7. Exit".center(
                terminal_width
            )
        )
        print("─" * terminal_width)

        prompt = "Pick 1-7: "
        padding = " " * ((terminal_width - len(prompt)) // 2)
        choice = input(padding + prompt)

        print("─" * terminal_width)

        if choice == "1":
            view_employees(employees)
        elif choice == "2":
            add_employee(employees, date.today())
        elif choice == "3":
            update_employee(employees)
        elif choice == "4":
            delete_employee(employees)
        elif choice == "5":
            filter_employees(employees)
        elif choice == "6":
            export_to_csv(employees)
        elif choice == "7":
            break
        else:
            print("Try again".center(terminal_width))


main()
