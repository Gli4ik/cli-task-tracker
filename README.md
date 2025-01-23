# Simple CLI Task Tracker

A Python-based Command-Line Interface (CLI) application for managing tasks efficiently. 
This tool allows users to add, update, delete, and list tasks with different statuses.

## Features

Add Tasks: Create a new task with a description and an optional status.
Update Tasks: Modify the description of an existing task.
Delete Tasks: Remove tasks by their ID.
List Tasks: Display all tasks or filter by specific statuses.
Mark Tasks: Update the status of a task.

## Usage

Run the program using the command:

`python task-tracker.py <command> [options]`

### Commands

#### 1. Add a New Task

`python task-tracker.py add <description> [-s STATUS]`

description: Description of the task (required).

-s, --status: Initial status of the task. Options: done, in-progress, todo (default: todo).

Example:

`python task-tracker.py add "Buy groceries" -s todo`

#### 2. Update a Task

`python task-tracker.py update <id> <new_description>`

id: ID of the task to update (required).

new_description: New description for the task (required).

Example:

`python task-tracker.py update 1 "Buy groceries and cook dinner"`

#### 3. Delete a Task

`python task-tracker.py delete <id>`

id: ID of the task to delete (required).

Example:

`python task-tracker.py delete 1`

#### 4. Mark a Task

`python task-tracker.py mark <id> <status>`

id: ID of the task to mark (required).

status: New status for the task. Options: done, in-progress, todo.

Example:

`python task-tracker.py mark 1 done`

#### 5. List Tasks

python task-tracker.py list [options]

--done, -d: Show tasks with status done.

--in-progress, -i: Show tasks with status in-progress.

--todo, -t: Show tasks with status todo.

Example:

`python task-tracker.py list --todo`
