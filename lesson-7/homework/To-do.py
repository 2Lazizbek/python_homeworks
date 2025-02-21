filename1 = "ToDo.txt"
class Task:
    def __init__(self, task_id, title, description, status, due_date = "Not set"):
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
        # Try to read existing tasks from the file
        try:
            with open(filename, "r") as file:
                self.tasks = [Task(*row.strip().split(",")) for row in file if row.strip()]
                self.filename = filename
        except FileNotFoundError:
            # If file does not exist, initialize with an empty list
            self.tasks = []
            self.filename = filename

    # Function to save tasks to file
    def save_to_file(self):
        with open(self.filename, "w", newline="") as file:
            file.writelines((",".join([task.task_id, task.title, task.description, task.status, task.due_date]) + "\n") for task in self.tasks)

    # Function to output menu
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
        
    def add_task(self):
        while True:
            try:
                new_id = int(input("Enter Task ID: "))
                if new_id == 0:
                    return -1
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
        while new_status not in ("Pending","In Progress","Completed"):
            new_status = input("Enter Status (Pending/In Progress/Completed): ").strip()
        new_task = Task(new_id, new_title, new_descrip, new_status)
        if new_due:
            new_task.set_due_date(new_due)
        self.tasks.append(new_task)
        self.save_to_file()
        print("Task added successfully!")
    
    def display_all(self):
        print("Tasks:")
        for task in self.tasks:
            print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")
    
    def search_with_id(self):
        while True:
            task_id = input("Enter Task ID (100-999, 0 to quit): ")
            if task_id == '0':
                return -1  # Return -1 if the user wants to exit
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
        while new_status not in ("Pending","In Progress","Completed"):
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
    
    def delete_task(self):
        id_in_tasks = self.search_with_id()
        if id_in_tasks == -1:
            return -1
        del self.tasks[id_in_tasks]
        print("Task has been deleted successfully.")
    
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
                    raise ValueError("Input 1, 2 or 3.")
                break
            except ValueError as e:
                print("ERROR:", e)
        if choice == 1:
            filter = "Completed"
        elif choice == 2:
            filter = "In Progress"
        else:
            filter = "Pending"
        for task in self.tasks:
            if task.status == filter:
                print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")
        return -1
mylist = ToDo(filename1)
while True:
    while True:
        try:
            mylist.output_options()
            choice = int(input("---> "))
            if not (1 <= choice <=8):
                raise ValueError("Invalid input. Enter number from 1 to 8.")
            break
        except ValueError as e:
            print(e)
    print("")
    if choice == 1:
        mylist.add_task()
    elif choice == 2:
        mylist.display_all()
    elif choice == 3:
        mylist.update_task()
    elif choice == 4:
        mylist.delete_task()
    elif choice == 5:
        mylist.filter_by_status()
    elif choice == 6:
        mylist.save_to_file()
    elif choice == 7:
        pass
    else:
        print("<<< Program terminated >>>")
        break