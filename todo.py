import os  # Importing os module for system operations
from tabulate import tabulate  # Importing tabulate for formatted table display
from cs50 import SQL  # Importing SQL module from CS50 library for database operations
from datetime import date  # Importing date class for handling dates

# Clear the console screen
os.system("cls")  
# Create an empty tasks database file if it doesn't exist
open("tasks.db", "a+").close()  
# Initialize a connection to the SQLite database
db = SQL("sqlite:///tasks.db")  
# Create tasks table if it doesn't already exist
db.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, priority TEXT, task_date DATE, status TEXT)")

def main():
    while True:
        try:
            # Display the main menu options
            print("1. Add Task")
            print("2. Delete Task")
            print("3. Update Task Status")
            print("4. Show Tasks")
            print("5. Exit")

            operation = input().strip()  # Get user input

            # Call the corresponding function based on user choice
            if operation == '1':
                add_task()
            elif operation == '2':
                delete_task()
            elif operation == '3':
                update_status()
            elif operation == '4':
                display_tasks()
            elif operation == '5':
                exit("Good Bye ^_^")  # Exit the program with a goodbye message
            else:
                raise ValueError  # Raise error if input is invalid
        except ValueError:
            # Handle invalid input and prompt user to try again
            print("Please enter a valid number of operation", end="\n\n")
            return main()  # Restart the main menu

def add_task():
    while True:
        task_name = input("Task: ").strip()  # Get task name
        if task_name:
            break  # Exit loop if task name is valid
    while True:
        # Get task priority and validate input
        task_priority = input("Priority [high, medium, low]: ").strip().lower()
        if task_priority in ["high", "medium", "low"]:
            break
        else:
            print("Please enter high or medium or low", end="\n\n")
    while True:
        # Get task status and validate input
        task_status = input("Status [pending, completed]: ").strip().lower()
        if task_status in ["pending", "completed"]:
            break
        else:
            print("Please enter pending or completed", end="\n\n")
    
    # Insert the new task into the database
    db.execute("INSERT INTO tasks(task, priority, task_date, status) VALUES(?, ?, ?, ?)", task_name.title(), task_priority.title(), date.today(), task_status.title())
    print("Task Added Successfully", end="\n\n")  # Confirmation message

def display_tasks():
    # Retrieve all tasks from the database
    tasks = db.execute("SELECT * FROM tasks ORDER BY id")
    if len(tasks) == 0:
        print("There are no tasks to display it", end="\n\n")
        return  # Exit if no tasks are found
    # Display the tasks in a formatted table
    print(tabulate(tasks, headers="keys", tablefmt="grid"), end="\n\n")

def delete_task():
    # Check if there are any tasks to delete
    search_for_tasks = db.execute("SELECT * FROM tasks")
    if len(search_for_tasks) == 0:
        print("There are no tasks to delete it", end="\n\n")
        return 
    try:
        # Provide options for deleting tasks
        delete = input("1. Delete Specific Task\n2. Delete All Tasks\n3. Back to main\n").strip()
        if delete == '1':
            task_name  = input("Task: ").strip().title()  # Get the name of the task to delete
            search_for_task = db.execute("SELECT * FROM tasks WHERE task LIKE (?)", task_name)  # Search for the task
            if len(search_for_task) == 0:
                print("No task with this name to delete it", end="\n\n")
                return delete_task()  # Prompt again if task not found
            else:
                # Delete the specific task
                db.execute("DELETE FROM tasks WHERE task LIKE (?)", task_name)
                print(f"{task_name} Deleted Successfully", end="\n\n'")
        elif delete == '2':
            # Delete all tasks from the database
            db.execute("DELETE FROM tasks")
            print("All Tasks Deleted Successfully", end="\n\n")
        elif delete == '3':
            return main()  # Return to main menu
        else:
            raise ValueError  # Raise error if input is invalid
    except ValueError:
        # Handle invalid input and prompt user to try again
        print("Please select 1 or 2 or 3")
        return delete_task()

def update_status():
    # Check if there are any tasks to update
    search_for_tasks = db.execute("SELECT * FROM tasks")
    if len(search_for_tasks) == 0:
        print("There are no tasks to update it", end="\n\n")
        return
    while True:
        task_name = input("Task: ").strip().title()  # Get the name of the task to update
        if task_name:
            break
    search_for_task = db.execute("SELECT * FROM tasks WHERE task LIKE (?)", task_name)  # Search for the task
    if len(search_for_task) == 0:
        print("There are no task with this name to update it", end="\n\n")
        return
    while True:
        # Get new status and validate input
        new_status = input("New Status [pending, completed]: ").strip().lower()
        if new_status in ["pending", "completed"]:
            break
        else:
            print("Please enter pending or completed", end="\n\n")

    # Update the status of the task in the database
    db.execute("UPDATE tasks SET status = (?) WHERE task = (?)", new_status.title(), task_name)
    print(f"{task_name} Status Updated Successfully", end="\n\n")  # Confirmation message


if __name__ == "__main__":  # Check if the script is being run directly
    main()  # Start the main function
