def welcome_msg():
    print('-------- Welcome to To-do --------')
    print('Type \'help\' for a list of commands')

def reset_id(todos:list):
    '''Reassigning the index to todos'''
    for todo in range(len(todos)):
        todos[todo]['id'] = todo + 1

def add_todo(todos:list):
    '''Function to add todos to the todo list'''
    todo_name = input('Enter todo name: ').title()
    todo_task = input('Enter the todo: ').title()

    # Creating a dictionary for the todo item
    todo_dict = {'name': todo_name, 'task': todo_task, 'completed': False}

    # Checking if input is valid, if so, appending the item 
    if len(todo_name) < 1:
        print('Invalid input')
    else:
        todos.append(todo_dict)
    reset_id(todos)
    print('Todo added')


def remove_todo(todos:list):
    '''Function to remove todos from the todo list'''
    name_remove = input('Enter the name of the todo you want to remove: ').title()
    # redefining list without the todo which needs to be removed
    todos[:] = [todo for todo in todos if todo.get('name') != name_remove]
    reset_id(todos)
    print('Todo removed')


def list_todos(todos:list):
    '''Function to display all todos to the user'''
    if len(todos) > 0:
        print(f'\n{len(todos)} todo(s) left\n')
        for todo in todos:
            name_str = todo['name']
            task_str = todo['task']
            completed_str = ''
            # Making a string to show cross when a todo has been completed
            if todo['completed']:
                completed_str = '[x]'
            else:
                completed_str = '[ ]'
            print(f"ID: {todo['id']}\nName: {name_str}\nTask: {task_str}\nCompleted: {completed_str}\n")
    else:
        print('Todo list empty')

def mark_completed(todos:list):
    '''Function to mark a todo as "completed"'''
    name_todo = input('Enter the name of completed todo: ').title()
    for i in todos:
        if i['name'] == name_todo:
            i['completed'] = True
    print('Done')

def mark_uncompleted(todos:list):
    '''Function to mark a todo as "uncompleted"'''
    name_todo = input('Enter the name of uncompleted todo: ').title()
    for i in todos:
        if i['name'] == name_todo:
            i['completed'] = False
    print('Done')

def remove_completed(todos:list):
    '''Function to remove all completed todos from the list'''
    todos[:] = [todo for todo in todos if todo.get('completed') != True]
    reset_id(todos)
    print('Deleted completed todos')

