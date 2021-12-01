import functions as fn


def todo_app():
    fn.init()
    running = True
    todos = []
    while running:
        user_input = input('What would you like to do? ').lower()
        if user_input == 'help':
            fn.print_commands()
        elif user_input == 'add':
            fn.add_todo(todos)
        elif user_input == 'remove':
            fn.remove_todo(todos)
        elif user_input == 'remove completed':
            fn.remove_todo(todos, all_completed = True)
        elif user_input == 'list':
            fn.list_todos(todos)
        elif user_input == 'complete':
            fn.edit_completed(todos)
        elif user_input == 'quit':
            running = False
        else:
            print('Invalid input. Type \'help\' for a list of commands')


if __name__ == '__main__':
    todo_app()
