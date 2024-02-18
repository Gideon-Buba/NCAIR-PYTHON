# Define a class for the to-do list
class ToDoList:
    def __init__(self):
        self.tasks = []

    # function to add new task to the list
    def add_task(self, task):
        self.tasks.append({"task": task, "complete": False})

    # function
    # to view all tasks in the list
    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Your Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                status = "Complete" if task["complete"] else "Incomplete"
                print(f"{index}. {task['task']} - {status}")

    # Method to mark a task as complete
    def mark_complete(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["complete"] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")

    # Method to remove a task from the list
    def remove_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            print("Task removed.")
        else:
            print("Invalid task number.")

# Main function to run the program
def main():
    # Create a new instance of the to-do list
    todo_list = ToDoList()

    # Loop to keep the program running until the user decides to exit
    while True:
        # Display menu options
        print("\nTodo List Manager")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as complete")
        print("4. Remove a task")
        print("5. Exit")

        # Get user input for their choice
        choice = input("Enter your choice: ")

        # Perform actions based on user's choice
        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter the task number to mark as complete: "))
            todo_list.mark_complete(task_number)
        elif choice == "4":
            task_number = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_number)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Call the main function to start the program
if __name__ == "__main__":
    main()
