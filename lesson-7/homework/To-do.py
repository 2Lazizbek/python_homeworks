class Task:
    def __init__(self, task_id, title, description, due_date, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
    def __str__(self):
        return f"Task ID: {self.task_id}\nTitle: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {self.status}"

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
            file.writelines((",".join([task.task_id, task.title, task.description, task.due_date, task.status]) + "\n") for task in self.tasks)

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