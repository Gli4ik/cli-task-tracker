from Classes.task import Task
from Classes.task_manager import TaskManager
import argparse

JSON = "data.json"
manager = TaskManager(JSON)


def add_task(args):
    manager.add_task(args.description)


def update_task(args):
    manager.update_task(args.id, args.description)


def delete_task(args):
    manager.delete_task(args.id)


def list_tasks(args):
    if not args.status:
        manager.print_tasks()


def mark_task(args):
    manager.change_status(args.id, args.status)


def main():
    parser = argparse.ArgumentParser(description='Simple CLI Task Tracker')
    subparsers = parser.add_subparsers(dest='command', help='Commands available')

    parser_add = subparsers.add_parser('add', help='Add a new task')
    parser_add.add_argument('description', help='Task\'s description', type=str)
    parser_add.set_defaults(func=add_task)

    parser_update = subparsers.add_parser('update', help='Update a task')
    parser_update.add_argument('id',
                               help='Task\'s id',
                               type=int)
    parser_update.add_argument('description', help='New task\'s description', type=str)
    parser_update.set_defaults(func=update_task)

    parser_delete = subparsers.add_parser('delete', help='Delete a task')
    parser_delete.add_argument('id',
                               help='Task\'s id',
                               type=int)
    parser_delete.set_defaults(func=delete_task)

    parser_mark = subparsers.add_parser('mark', help='Mark a task')
    parser_mark.add_argument('id', help='Task\'s id', type=int)
    parser_mark.add_argument('status',
                             help='New task\'s status',
                             choices=['done', 'in-progress', 'todo'])
    parser_mark.set_defaults(func=mark_task)

    parser_list = subparsers.add_parser('list', help='List tasks')
    group_list = parser_list.add_mutually_exclusive_group()
    group_list.add_argument('-d', '--done',
                            dest='status',
                            help='Display tasks with status "done"',
                            action='store_const',
                            const='done')
    group_list.add_argument('-i', '--in-progress',
                            dest='status',
                            help='Display tasks with status "in-progress"',
                            action='store_const',
                            const='in-progress')
    group_list.add_argument('-t', '--todo',
                            dest='status',
                            help='Display tasks with status "todo"',
                            action='store_const',
                            const='todo')
    parser_list.set_defaults(func=list_tasks)

    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
