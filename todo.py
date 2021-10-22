# Creating the todo list
todos = []

# Functionality
def reset_id():
    '''Reassigning the index to todos'''
    for todo in range(len(todos)):
        todos[todo]['id'] = todo + 1

def add_todo():
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
    reset_id()

def remove_todo():
    '''Function to remove todos from the todo list'''
    name_remove = input('Enter the name of the todo you want to remove: ').title()
    # redefining list without the todo which needs to be removed
    todos[:] = [todo for todo in todos if todo.get('name') != name_remove]
    reset_id()

def list_todos():
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

def mark_completed():
    '''Function to mark a todo as "completed"'''
    name_todo = input('Enter the name of completed todo: ').title()
    for i in todos:
        if i['name'] == name_todo:
            i['completed'] = True

def mark_uncompleted():
    '''Function to mark a todo as "uncompleted"'''
    name_todo = input('Enter the name of uncompleted todo: ').title()
    for i in todos:
        if i['name'] == name_todo:
            i['completed'] = False

def remove_completed():
    '''Function to remove all completed todos from the list'''
    todos[:] = [todo for todo in todos if todo.get('completed') != True]
    reset_id()

def init():
    '''Logic of the program'''
    # Welcome message
    print('-------- Welcome to To-do --------')
    print('Type \'help\' for a list of commands')

    # Program logic
    running = True
    while running:
        user_input = input('What would you like to do? ').lower()
        if user_input == 'help':
            print('\n--- Commands ---\nadd - add a todo to the list\nremove - remove a todo from the list\nlist - get an overview of your todos\ncomplete - mark a todo as completed\nuncomplete - mark a todo as uncompleted\nremove completed - remove all completed todos\nquit - Quit the program\n')
        elif user_input == 'add':
            add_todo()
            print('Todo added')
        elif user_input == 'remove':
            remove_todo()
            print('Todo removed')
        elif user_input == 'list':
            list_todos()
        elif user_input == 'quit':
            running = False
            print('Program ended')
        elif user_input == 'complete':
            mark_completed()
            print('Done')
        elif user_input == 'uncomplete':
            mark_uncompleted()
            print('Done')
        elif user_input == 'remove completed':
            remove_completed()
            print('Deleted completed todos')
        else:
            print('Invalid input. Type \'help\' for a list of commands')


init()
