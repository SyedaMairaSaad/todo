def read_todos():
    with open('todo.txt', 'r') as file:
        todos = file.readlines()
        return todos

def write_todos(todos):
    with open('todo.txt', 'w') as file:
        file.writelines(todos)