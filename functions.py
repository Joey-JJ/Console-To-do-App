def init():
    print('-------- Welcome to To-do --------\nType \'help\' for a list of commands')

def print_commands():
    commands = '\n--- Commands ---\n\
add - add a todo to the list\n\
remove - remove a todo from the list\n\
list - get an overview of your todos\n\
completed - mark/unmark a todo as completed\n\
remove completed - remove all completed todos\n\
quit - Quit the program\n'
    print(commands)

def reset_id(todos: list):
    """Reassigning the index to todos"""
    for todo in range(len(todos)):
        todos[todo]['id'] = todo + 1

def add_todo(todos: list):
    """Function to add todos to the todo list"""
    todo_name = input('Enter todo name: ').title()
    todo_task = input('Enter the todo: ').title()
    todo_dict = {'name': todo_name, 'task': todo_task, 'completed': False}
    print('Invalid input') if len(todo_name) < 1 else todos.append(todo_dict)
    reset_id(todos)
    print('Todo added')

def remove_todo(todos: list, all_completed: bool = False):
    """Function to remove todos from the todo list"""
    if not all_completed:
        name_remove = input('Enter the name of the todo you want to remove: ').title()
        todos[:] = [todo for todo in todos if todo['name'] != name_remove]
        print('Todo removed')
    else:
        todos[:] = [todo for todo in todos if todo['completed'] != True]
        print('Deleted completed todos')
    reset_id(todos)

def list_todos(todos: list):
    """Function to display all todos to the user"""
    if len(todos) > 0:
        print(f'\n{len(todos)} todo(s) left\n')
        for todo in todos:
            completed_str = '[x]' if todo['completed'] else '[ ]'
            print(f"ID: {todo['id']}\nName: {todo['name']}\nTask: {todo['task']}\nCompleted: {completed_str}\n")
    else:
        print('Todo list empty')

def edit_completed(todos: list):
    """Function to mark a todo as 'completed'"""
    name_todo = input('Enter the name of todo: ').title()
    for todo in todos:
        if todo['name'] == name_todo:
            todo['completed'] = True if todo['completed'] == False else False
    print('Done')
