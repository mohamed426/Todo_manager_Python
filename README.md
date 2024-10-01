
## Task Manager

This is a simple command-line task management application that allows users to add, delete, update, and display tasks with priorities and statuses. The application uses SQLite to store tasks and the `tabulate` library to display tasks in a table format.

### Features:
- **Add Task**: Create a new task with a name, priority (high, medium, low), and status (pending, completed).
- **Delete Task**: Remove tasks by name or delete all tasks at once.
- **Update Task**: Change the status of existing tasks (pending or completed).
- **Show Tasks**: Display all tasks in a formatted table.

### Dependencies:
- **Python 3.x**
- **CS50 Library for Python** (`pip install cs50`)
- **Tabulate Library** (`pip install tabulate`)

### Setup:
1. Clone or download the repository.
2. Ensure the necessary Python libraries are installed:
   ```bash
   pip install cs50 tabulate
   ```
3. Run the application:
   ```bash
   python todo.py
   ```

### Database:
- The tasks are stored in an SQLite database named `tasks.db`.
- The table schema includes:
  - `id`: Task ID (Primary Key, auto-incremented).
  - `task`: Task description.
  - `priority`: Task priority (high, medium, low).
  - `task_date`: The date the task was added.
  - `status`: Task status (pending, completed).

### Usage:
- After running the script, you will be prompted to select an operation from the menu:
  1. Add Task
  2. Delete Task
  3. Update Task Status
  4. Show Tasks
  5. Exit

Follow the prompts to manage your tasks.

### Author:
- Mohammed Khaled Abdalla
