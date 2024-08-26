# To-Do List Application

## Overview

Welcome to the **To-Do List Application**! This simple command-line tool is designed to help you manage your daily tasks effectively. Whether you're looking to keep track of chores, work items, or personal goals, this application provides a straightforward way to add, view, update, and delete tasks.

## Features

- **View Tasks**: List all the tasks you have added.
- **Add a Task**: Insert new tasks into your list.
- **Update a Task**: Modify the description of an existing task.
- **Delete a Task**: Remove a task from your list.
- **Persistent Storage**: All tasks are saved in a text file (`tasks.txt`), ensuring that your tasks remain available even after you close the application.

## Installation

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Clone the Repository

To get started with the To-Do List Application, clone the repository using the following command:

```bash
git clone https://github.com/abhisheklakhani-it/todo_list.git
cd todo_list
```
## Running the Application

Once you’ve cloned the repository, run the application with:
```
python todo.py
```

## How to Use

### When you run the application, you’ll be greeted with a menu that offers the following options:

	1.	View tasks: Lists all tasks with their respective numbers.
	2.	Add a task: Prompts you to enter a new task to add to your list.
	3.	Update a task: Allows you to select a task by its number and update its description.
	4.	Delete a task: Enables you to remove a task by selecting its number.
	5.	Exit: Closes the application.

## Example Output

### Here’s a sample interaction with the application:
```bash
To-Do List Application
1. View tasks
2. Add a task
3. Update a task
4. Delete a task
5. Exit
Enter your choice (1-5): 2
Enter the task: Finish homework
Task "Finish homework" added.

To-Do List Application
1. View tasks
2. Add a task
3. Update a task
4. Delete a task
5. Exit
Enter your choice (1-5): 1
1. Finish homework

To-Do List Application
1. View tasks
2. Add a task
3. Update a task
4. Delete a task
5. Exit
Enter your choice (1-5): 3
1. Finish homework
Enter the task number to update: 1
Enter the new task: Finish math homework
Task 1 updated to "Finish math homework".

To-Do List Application
1. View tasks
2. Add a task
3. Update a task
4. Delete a task
5. Exit
Enter your choice (1-5): 4
1. Finish math homework
Enter the task number to delete: 1
Task "Finish math homework" deleted.
```

## Contributing

If you would like to contribute to the project, feel free to fork the repository, make your changes, and submit a pull request. Contributions are always welcome!

## Author 

This project is developed and maintained by Abhishek Lakhani.

### Thank you for checking out the To-Do List Application! Your feedback and contributions are highly appreciated.



