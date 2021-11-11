import functions as fn


def init():
    fn.welcome_msg()
    running = True
    todos = []
    commands = '\n--- Commands ---\n\
                add - add a todo to the list\n\
                remove - remove a todo from the list\n\
                list - get an overview of your todos\n\
                complete - mark a todo as completed\n\
                uncomplete - mark a todo as uncompleted\n\
                remove completed - remove all completed todos\n\
                quit - Quit the program\n'
    while running:
        user_input = input('What would you like to do? ').lower()
        if user_input == 'help':
            print(commands)
        elif user_input == 'add':
            fn.add_todo(todos)
        elif user_input == 'remove':
            fn.remove_todo(todos)
        elif user_input == 'list':
            fn.list_todos(todos)
        elif user_input == 'quit':
            running = False
        elif user_input == 'complete':
            fn.mark_completed(todos)
        elif user_input == 'uncomplete':
            fn.mark_uncompleted(todos)
        elif user_input == 'remove completed':
            fn.remove_completed(todos)
        else:
            print('Invalid input. Type \'help\' for a list of commands')


if __name__ == '__main__':
    init()
