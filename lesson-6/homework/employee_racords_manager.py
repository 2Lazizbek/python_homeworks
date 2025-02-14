import csv
filename = "employees.txt"

def add_record():
    with open(filename, "r") as file:
        records = [row for row in csv.reader(file) if row]
        if records:
            last_id = int(records[-1][0])
        else:
            last_id = 99
    print("Enter 0 to quit to menu.")
    new_name = input("Enter a new name: ")
    if new_name == '0':
        return -1
    while len(new_name) >50:
        if new_name == '0':
            return -1
        print("Invalid input.")
        new_name = input("Enter a new name: ")
    new_role = input("Enter new role: ")
    while len(new_role) > 50:
        if new_role == '0':
            return -1
        print("Invalid input.")
        new_role = input("Enter a new role: ")
    new_salary = input("Enter new salary: ")
    while not new_salary.isnumeric() or int(new_salary) < 0:
        if new_salary == '0':
            return -1
        print("Invalid input.")
        new_salary = input("Enter new salary: ")
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([str(last_id+1), " "+new_name, " "+new_role, " "+new_salary])
    print("New record added successfully.")

def display_all():
    print()
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())

def output_options():
    print("""\n--------------------------------------------
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit
--------------------------------------------""")

def search_with_id():
    while True:
        employee_id = input("Enter Employee ID (100-999, 0 to quit): ")
        if employee_id == '0':
            return -1  # Return special value to indicate exit
        if employee_id.isdigit() and 100 <= int(employee_id) <= 999:
            break
        print("Invalid ID! Please enter a number between 100 and 999.")
    with open(filename, "r") as file:
        records = [row for row in csv.reader(file) if row]
    for i, row in enumerate(records):
        if row[0] == employee_id:
            print("\nEmployee id: "+ row[0])
            print("Name:"+ row[1])
            print("Role:"+ row[2])
            print("Salary($):"+ row[3])
            return i
    else:
        print("Employee not found.")
        return -1

def update():
    record_id = search_with_id()
    while record_id == -1:
        record_id = search_with_id()
    with open(filename, "r") as file:
        records = [row for row in csv.reader(file) if row]
        print(records)
    print("Leave blank to keep the data unchanged.")
    new_name = input("Enter a new name: ")
    while len(new_name) >50:
        print("Invalid input.")
        new_name = input("Enter a new name: ")
    new_role = input("Enter new role: ")
    while len(new_role) > 50:
        print("Invalid input.")
        new_role = input("Enter a new role: ")
    new_salary = input("Enter new salary: ")
    while not new_salary.isnumeric() or int(new_salary) < 0:
        if not new_salary:
            break
        print("Invalid input.")
        new_salary = input("Enter new salary: ")
    if new_name:
        records[record_id][1] = " " + new_name
    if new_role:
        records[record_id][2] = " " + new_role
    if new_salary:  
        records[record_id][3] = " " + new_salary
    print(records)
    if not new_salary and not new_name and not new_role:
        print("\n--->Employee data hasn't changed.")
    else:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(records)
        print("\n--->Employee data changed successfully.")
        
def delete():
    record_id = search_with_id()
    while record_id == -1:
        record_id = search_with_id()
    with open(filename, "r") as file:
        records = [row for row in csv.reader(file) if row]
    del records[record_id]
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(records)
    print("Employee data has beed deleted successfully.")


def main():
    while True:
        output_options()
        while True:
            try:
                choice = int(input("---> "))
                while 1 > choice or choice > 6:
                    output_options()
                    print("Invalid input. Enter number from 1 to 6.")
                    choice = int(input("---> "))
                break
            except Exception:
                output_options()
                print("Invalid input. Enter number from 1 to 6.")
        print("")
        if choice == 1:
            add_record()
        elif choice == 2:
            display_all()
        elif choice == 3:
            search_with_id()
        elif choice == 4:
            update()
        elif choice == 5:
            delete()
        else:
            print("<<<Program terminated>>>")
            break
main()