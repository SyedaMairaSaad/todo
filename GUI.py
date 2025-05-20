import FreeSimpleGUI as sg
import functions
label =sg.Text('Type in TODO')
input_box=sg.InputText(tooltip="Enter TODO", key='todo')
add_btn = sg.Button('Add')
todos_list = sg.Listbox(values=functions.read_todos() , key='todos',enable_events=True, size =[45 , 10])
edit_btn = sg.Button('Edit')

window = sg.Window('My TODO App',
                   layout=[[label],[input_box,add_btn],[todos_list,edit_btn]],
                   font=('Helevica',20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.read_todos()
            todos.append(values['todo']+"\n")
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todo = values['todos'][0]
            new_todo = values['todo']+'\n'
            todos = functions.read_todos()
            todo_index = todos.index(todo)
            todos[todo_index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
window.close()
