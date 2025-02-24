import json

filename1 = "ToDo.txt"

class Task:
    def __init__(self, task_id, title, description, status, due_date="Not set"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def set_due_date(self, date):
        self.due_date = date

    def __str__(self):
        return f"Task ID: {self.task_id}\nTitle: {self.title}\nDescription: {self.description}\nStatus: {self.status}\nDue Date: {self.due_date}"

class ToDo:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = []
        self.load()

    # Function to load tasks from a text file
    def txt_load(self):
        try:
            with open(self.filename, "r") as file:
                self.tasks = [Task(*row.strip().split(",")) for row in file if row.strip()]
        except FileNotFoundError:
            print(f"File '{self.filename}' not found. Starting with an empty task list.")
            self.tasks = []

    # Function to save tasks to a text file
    def txt_save(self):
        with open(self.filename, "w", newline="") as file:
            file.writelines((",".join([task.task_id, task.title, task.description, task.status, task.due_date]) + "\n") for task in self.tasks)

    # Function to save tasks to a JSON file
    def json_save(self):
        with open(self.filename, "w") as file:
            json.dump([task.__dict__ for task in self.tasks], file, indent=4)

    # Function to load tasks from a JSON file
    def json_load(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.tasks = [Task(**task) for task in data]
        except FileNotFoundError:
            print(f"File '{self.filename}' not found. Starting with an empty task list.")
            self.tasks = []
        except json.JSONDecodeError:
            print(f"File '{self.filename}' is corrupted or not a valid JSON file. Starting with an empty task list.")
            self.tasks = []

    # Function to load tasks based on file format
    def load(self):
        if self.filename.endswith(".json"):
            self.json_load()
        elif self.filename.endswith(".txt"):
            self.txt_load()
        else:
            print("Unsupported file format. Starting with an empty task list.")
            self.tasks = []

    # Function to save tasks based on user choice
    def save(self):
        print("""1. Save as .txt file
2. Save as .json file""")
        while True:
            try:
                choice = int(input("---> "))
                if choice not in (1, 2):
                    raise ValueError("Invalid choice. Enter 1 or 2.")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                filename = input("Enter file name (without extension): ")
                if len(filename) > 20:
                    raise ValueError("File name is too long.")
                break
            except ValueError as e:
                print(e)

        if choice == 1:
            self.filename = filename + ".txt"
            self.txt_save()
        elif choice == 2:
            self.filename = filename + ".json"
            self.json_save()
        print(f"Tasks saved to {self.filename}")

    # Function to display the menu
    def output_options(self):
        print("""---------------------------------
Welcome to the To-Do Application!
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Filter tasks by status
6. Save tasks
7. Load tasks
8. Exit
---------------------------------""")

    # Function to add a new task
    def add_task(self):
        while True:
            try:
                new_id = int(input("Enter Task ID: "))
                if new_id == 0:
                    return
                if not (100 <= new_id <= 999):
                    raise ValueError("ID should be an integer between 100 and 999.")
                if any(str(new_id) == task.task_id for task in self.tasks):
                    raise ValueError("Task ID already exists.")
                break
            except ValueError as e:
                print(e)

        new_title = input("Enter title: ")
        while len(new_title) > 20:
            new_title = input("Enter title[max 20 characters]: ").strip()
        new_descrip = input("Enter Description: ")
        while len(new_descrip) > 100:
            new_descrip = input("Enter Description[max 100 characters]: ").strip()
        new_due = input("Enter Due Date (YYYY-MM-DD): ")
        new_status = input("Enter Status (Pending/In Progress/Completed): ").strip()
        while new_status not in ("Pending", "In Progress", "Completed"):
            new_status = input("Enter Status (Pending/In Progress/Completed): ").strip()
        new_task = Task(str(new_id), new_title, new_descrip, new_status)
        if new_due:
            new_task.set_due_date(new_due)
        self.tasks.append(new_task)
        print("Task added successfully!")

    # Function to display all tasks
    def display_all(self):
        print("Tasks:")
        for task in self.tasks:
            print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")

    # Function to search for a task by ID
    def search_with_id(self):
        while True:
            task_id = input("Enter Task ID (100-999, 0 to quit): ")
            if task_id == '0':
                return -1
            if task_id.isdigit() and 100 <= int(task_id) <= 999:
                break
            print("Invalid ID! Please enter a number between 100 and 999.")
        for i, task in enumerate(self.tasks):
            if task.task_id == task_id:
                print(task)
                return i
        else:
            print("Task not found.")
            return -1

    # Function to update a task
    def update_task(self):
        id_in_tasks = self.search_with_id()
        if id_in_tasks == -1:
            return
        print("Leave blank to keep the data unchanged.")
        new_title = input("Enter title: ")
        while len(new_title) > 20:
            new_title = input("Enter title[max 20 characters]: ").strip()
        new_descrip = input("Enter Description: ")
        while len(new_descrip) > 100:
            new_descrip = input("Enter Description[max 100 characters]: ").strip()
        new_due = input("Enter Due Date (YYYY-MM-DD): ")
        new_status = input("Enter Status (Pending/In Progress/Completed): ").strip()
        while new_status not in ("Pending", "In Progress", "Completed"):
            new_status = input("Enter Status (Pending/In Progress/Completed): ").strip()
        if new_due:
            self.tasks[id_in_tasks].set_due_date(new_due)
        if new_title:
            self.tasks[id_in_tasks].title = new_title
        if new_descrip:
            self.tasks[id_in_tasks].description = new_descrip
        if new_status:
            self.tasks[id_in_tasks].status = new_status
        print("Task updated successfully!")

    # Function to delete a task
    def delete_task(self):
        id_in_tasks = self.search_with_id()
        if id_in_tasks == -1:
            return
        del self.tasks[id_in_tasks]
        print("Task has been deleted successfully.")

    # Function to filter tasks by status
    def filter_by_status(self):
        print("""Show only
1. Completed
2. In Progress
3. Pending
""")
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if not (1 <= choice <= 3):
                    raise ValueError("Input 1, 2, or 3.")
                break
            except ValueError as e:
                print("ERROR:", e)
        status_map = {1: "Completed", 2: "In Progress", 3: "Pending"}
        filter_status = status_map[choice]
        for task in self.tasks:
            if task.status == filter_status:
                print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")

# Main program
mylist = ToDo(filename1)
while True:
    mylist.output_options()
    choice = input("---> ").strip()
    if choice == "1":
        mylist.add_task()
    elif choice == "2":
        mylist.display_all()
    elif choice == "3":
        mylist.update_task()
    elif choice == "4":
        mylist.delete_task()
    elif choice == "5":
        mylist.filter_by_status()
    elif choice == "6":
        mylist.save()
    elif choice == "7":
        mylist.load()
    elif choice == "8":
        print("<<< Program terminated >>>")
        break
    else:
        print("Invalid choice. Please try again.")