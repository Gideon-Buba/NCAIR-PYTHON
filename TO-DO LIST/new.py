# Initialize an empty list to store tasks
tasks = []

while True:
    # Display the main menu
    print("\nSimple To-Do List Manager:")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as complete")
    print("4. Remove a task")
    print("5. Exit")

    # Take user input for choice
    option = input("Enter your choice (1-5): ")

    # Perform actions based on user choice
    if option == '1':
        task = input("Enter the new task: ")
        tasks.append(task)  # Add task to the list
        print("Task added:", task)
    elif option == '2':
        print("Viewing all tasks:")
        if tasks:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks added yet.")
    elif option == '3':
        task_number = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            print("Task marked as complete:", tasks[task_number - 1])
            # Implement task completion logic here if needed
        else:
            print("Invalid task number.")
    elif option == '4':
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print("Task removed:", removed_task)
        else:
            print("Invalid task number.")
    elif option == '5':
        print("Exiting the to-do list manager.")
        break
    else:
        print("Invalid choice.")

    # Ask user if they want to continue
    continue_choice = input("Do you want to continue (yes/no)? ")
    if continue_choice.lower() != 'yes':
        print("Exiting the to-do list manager.")
        break
