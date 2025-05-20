import functions

user_prompt = 'Type add, show, Edit, complete or exit:'
todo_prompt = 'Type todo:'
while True:
    user_input = input(user_prompt)
    user_input = user_input.strip()

    match user_input:
        case 'add':
            todo_input = input(todo_prompt)+ '\n'
            todos=functions.read_todos()
            todos.append(todo_input)
            functions.write_todos(todos)
        case 'show':
            todos = functions.read_todos()
            for index, item in enumerate(todos):
                item.replace('\n','')
                print(f"{index}-{item}")
        case 'edit':
            todos = functions.read_todos()
            edit_input = int(input('input index:'))
            new_input = input('input new value:')+'\n'
            todos[edit_input] = new_input
            functions.write_todos(todos)
        case 'complete':
            todos = functions.read_todos()
            remove_input = int(input('input todo value to remove:'))
            todos.remove(remove_input)
            functions.write_todos(todos)
        case 'exit':
            break
        case _:
            print('Hey! you input invalid value')
print('bye')