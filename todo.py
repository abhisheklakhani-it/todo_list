# todo.py

import os

# File to store the tasks
TASK_FILE = 'tasks.txt'

def load_tasks():
    """Load tasks from a file."""
    if not os.path.exists(TASK_FILE):
        return []
    
    with open(TASK_FILE, 'r') as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

def save_tasks(tasks):
    """Save tasks to a file."""
    with open(TASK_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task(task):
    """Add a new task."""
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task "{task}" added.')

def view_tasks():
    """View all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f'{idx}. {task}')

def update_task(task_number, new_task):
    """Update an existing task."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1] = new_task
        save_tasks(tasks)
        print(f'Task {task_number} updated to "{new_task}".')
    else:
        print("Invalid task number.")

def delete_task(task_number):
    """Delete a task."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f'Task "{deleted_task}" deleted.')
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            view_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '3':
            view_tasks()
            task_number = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task: ")
            update_task(task_number, new_task)
        elif choice == '4':
            view_tasks()
            task_number = int(input("Enter the task number to delete: "))
            delete_task(task_number)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()