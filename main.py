from task import Task
from task_manager import TaskManager
import sys

JSON = "data.json"

def main():
    manager = TaskManager(JSON)
    args = sys.argv
    n = len(args)
    if n == 0:
        print("No arguments provided")
        sys.exit()
    else:
        command = args[1]
        if command == "add":
            description = args[2]
            manager.add_task(description)
        elif command == "delete":
            try:
                identifier = int(args[2])
            except ValueError:
                print("Invalid argument")
                sys.exit()
            else:
                manager.delete_task(identifier)
        elif command == "list":
            status = args[2]
            if status:
                manager.print_tasks(status)
            else:
                manager.print_tasks()


