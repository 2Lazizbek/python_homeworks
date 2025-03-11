import json
import csv
from statistics import mean

# Step 1: Create initial tasks.json
def create_initial_json():
    tasks = [
        {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
        {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
        {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
    ]
    
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

# Task Management Class
class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = []
    
    def load_tasks(self):
        """Load tasks from JSON file"""
        try:
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            print(f"Error: {self.filename} not found")
            self.tasks = []
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in {self.filename}")
            self.tasks = []
    
    def save_tasks(self):
        """Save tasks back to JSON file"""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.tasks, file, indent=4)
            print("Tasks saved successfully")
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def display_tasks(self):
        """Display all tasks in a formatted way"""
        print("\nTasks List:")
        print("-" * 50)
        print(f"{'ID':<5} {'Task Name':<20} {'Completed':<12} {'Priority':<8}")
        print("-" * 50)
        for task in self.tasks:
            print(f"{task['id']:<5} {task['task']:<20} {str(task['completed']):<12} {task['priority']:<8}")
        print("-" * 50)
    
    def calculate_stats(self):
        """Calculate and display task statistics"""
        if not self.tasks:
            return {
                'total': 0,
                'completed': 0,
                'pending': 0,
                'avg_priority': 0
            }
        
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task['completed'])
        pending = total - completed
        avg_priority = mean(task['priority'] for task in self.tasks)
        
        stats = {
            'total': total,
            'completed': completed,
            'pending': pending,
            'avg_priority': avg_priority
        }
        
        print("\nTask Statistics:")
        print(f"Total Tasks: {total}")
        print(f"Completed Tasks: {completed}")
        print(f"Pending Tasks: {pending}")
        print(f"Average Priority: {avg_priority:.2f}")
        
        return stats
    
    def convert_to_csv(self, csv_filename='tasks.csv'):
        """Convert tasks to CSV format"""
        try:
            with open(csv_filename, 'w', newline='') as file:
                writer = csv.writer(file)
                # Write header
                writer.writerow(['ID', 'Task', 'Completed', 'Priority'])
                # Write task data
                for task in self.tasks:
                    writer.writerow([
                        task['id'],
                        task['task'],
                        task['completed'],
                        task['priority']
                    ])
            print(f"Tasks successfully converted to {csv_filename}")
        except Exception as e:
            print(f"Error converting to CSV: {e}")

# Main execution
def main():
    # Create initial JSON file
    create_initial_json()
    print("Created tasks.json")
    
    # Initialize task manager
    tm = TaskManager()
    
    # Load and display tasks
    tm.load_tasks()
    tm.display_tasks()
    
    # Calculate and display statistics
    tm.calculate_stats()
    
    # Example modification: mark "Do laundry" as completed
    for task in tm.tasks:
        if task['id'] == 1:
            task['completed'] = True
            print("\nModified task 'Do laundry' to completed")
    
    # Display updated tasks
    tm.display_tasks()
    
    # Save changes
    tm.save_tasks()
    
    # Convert to CSV
    tm.convert_to_csv()
    
    # Display final statistics
    tm.calculate_stats()

if __name__ == "__main__":
    main()