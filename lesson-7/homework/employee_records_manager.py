filename1 = "employees.txt"

# Employee class to store employee details
class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"Employee ID: {self.employee_id}\nEmployee name: {self.name}\nEmployee position: {self.position}\nEmployee salary: {self.salary}"

# EmployeeManager class to handle employee records
class EmployeeManager:
    def __init__(self, filename):
        # Try to read existing records from the file
        try:
            with open(filename, "r") as file:
                self.records = [Employee(*row.strip().split(", ")) for row in file if row.strip()]
                self.filename = filename
        except FileNotFoundError:
            # If file does not exist, initialize with an empty list
            self.records = []
            self.filename = filename

    # Function to save records to file
    def save_to_file(self):
        with open(self.filename, "w", newline="") as file:
            file.writelines((", ".join([record.employee_id, record.name, record.position, record.salary]) + "\n") for record in self.records)

    # Function to append a record to file
    def append_to_file(self, record):
        with open(self.filename, "a", newline="") as file:
            file.write(", ".join([record.employee_id, record.name, record.position, record.salary]) + "\n")

    # Function to add a new employee record
    def add_record(self):
        print("Enter 0 to quit to menu.")
        while True:
            try:
                new_id = int(input("Enter new employee id: "))
                if new_id == 0:
                    return -1
                if not (100 <= new_id <= 999):
                    raise ValueError("ID should be an integer between 100 and 999.")
                if any(str(new_id) == record.employee_id for record in self.records):
                    raise ValueError("Employee ID already exists.")
                break
            except ValueError as e:
                print(e)
        new_name = input("Enter a new name: ")
        if new_name == '0':
            return -1
        while len(new_name) > 50:
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
        new_employee = Employee(str(new_id), new_name, new_role, new_salary)
        self.append_to_file(new_employee)  # Save immediately after adding a record
        print("\nNew record added successfully:")
        print(new_employee)

    # Function to display all employee records with sorting options
    def display_all(self):
        while True:
            try:
                print("""\n--------------------------------------------
1. Do not sort
2. Sort by ID
3. Sort by Name
4. Sort by Salary
--------------------------------------------""")
                choice = int(input("--->"))
                if 0 < choice < 5:
                    break
            except Exception:
                print("Invalid input.")
        if choice == 1:
            sorted_records = self.records.copy()
        elif choice == 2:
            sorted_records = sorted(self.records, key=lambda x: int(x.employee_id))
        elif choice == 3:
            sorted_records = sorted(self.records, key=lambda x: x.name)
        else:
            sorted_records = sorted(self.records, key=lambda x: int(x.salary))
        for record in sorted_records:
            print(f"{record.employee_id}, {record.name}, {record.position}, {record.salary}")

    # Function to display menu options
    def output_options(self):
        print("""\n--------------------------------------------
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit
--------------------------------------------""")

    # Function to search for an employee by ID
    def search_with_id(self):
        while True:
            employee_id = input("Enter Employee ID (100-999, 0 to quit): ")
            if employee_id == '0':
                return -1  # Return -1 if the user wants to exit
            if employee_id.isdigit() and 100 <= int(employee_id) <= 999:
                break
            print("Invalid ID! Please enter a number between 100 and 999.")
        for i, record in enumerate(self.records):
            if record.employee_id == employee_id:
                print(record)
                return i
        else:
            print("Employee not found.")
            return -1

    # Function to update an existing employee record
    def update(self):
        record_id = self.search_with_id()
        if record_id == -1:
            return -1
        print("Leave blank to keep the data unchanged.")
        new_name = input("Enter a new name: ").strip()
        while len(new_name) > 50:
            print("Invalid input.")
            new_name = input("Enter a new name: ").strip()
        new_role = input("Enter new role: ").strip()
        while len(new_role) > 50:
            print("Invalid input.")
            new_role = input("Enter a new role: ").strip()
        new_salary = input("Enter new salary: ").strip()
        while not new_salary.isnumeric() or int(new_salary) < 0:
            if not new_salary:
                break
            print("Invalid input.")
            new_salary = input("Enter new salary: ").strip()

        # Update only the fields that were changed
        if not new_salary and not new_name and not new_role:
            print("\n--->Employee data hasn't changed.")
        else:
            if new_name:
                self.records[record_id].name = new_name
            if new_role:
                self.records[record_id].position = new_role
            if new_salary:
                self.records[record_id].salary = new_salary
            self.save_to_file()  # Save immediately after updating a record
            print("\n--->Employee data changed successfully.")

    # Function to delete an employee record
    def delete(self):
        record_id = self.search_with_id()
        if record_id == -1:
            return -1
        del self.records[record_id]
        self.save_to_file()  # Save immediately after deleting a record
        print("Employee data has been deleted successfully.")

    # Function to exit the program and save data
    def exit(self):
        self.save_to_file()
        print("Records saved successfully.")

# Main function to run the program
def main():
    Records = EmployeeManager(filename1)
    while True:
        while True:
            try:
                Records.output_options()
                choice = int(input("---> "))
                while 1 > choice or choice > 6:
                    Records.output_options()
                    print("Invalid input. Enter number from 1 to 6.")
                    choice = int(input("---> "))
                break
            except Exception:
                Records.output_options()
                print("Invalid input. Enter number from 1 to 6.")
        print("")
        if choice == 1:
            Records.add_record()
        elif choice == 2:
            Records.display_all()
        elif choice == 3:
            Records.search_with_id()
        elif choice == 4:
            Records.update()
        elif choice == 5:
            Records.delete()
        else:
            Records.exit()
            print("<<< Program terminated >>>")
            break

# Run the main function
main()