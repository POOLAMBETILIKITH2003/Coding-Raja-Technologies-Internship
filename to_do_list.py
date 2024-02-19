import json
import os
from datetime import datetime

TODO_FILE = "todo.json"

def load_tasks():
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            tasks = json.load(file)
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task_name = input("Enter task name: ")
    priority = input("Enter priority (high/medium/low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    tasks.append({"name": task_name, "priority": priority, "due_date": due_date, "completed": False})
    save_tasks(tasks)
    print("Task added successfully.")

def remove_task(tasks):
    print_tasks(tasks)
    task_index = int(input("Enter task number to remove: ")) - 1

    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        save_tasks(tasks)
        print("Task removed successfully.")
    else:
        print("Invalid task number.")

def mark_completed(tasks):
    print_tasks(tasks)
    task_index = int(input("Enter task number to mark as completed: ")) - 1

    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def print_tasks(tasks):
    print("\nTODO LIST:")
    for i, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['name']} - Priority: {task['priority']}, Due Date: {task['due_date']}, Status: {status}")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            print_tasks(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()