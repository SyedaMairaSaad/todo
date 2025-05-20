import FreeSimpleGUI as sg
import functions
import time

sg.theme('DarkBrown1')
time_label= sg.Text(key='time_label')
label =sg.Text('Type in TODO')
input_box=sg.InputText(tooltip="Enter TODO", key='todo')
add_btn = sg.Button('Add')
todos_list = sg.Listbox(values=functions.read_todos() , key='todos',enable_events=True, size =[45 , 10])
edit_btn = sg.Button('Edit')
complete_btn = sg.Button('Complete')
exit_btn = sg.Button('Exit')

window = sg.Window('My TODO App',
                   layout=[[time_label],
                       [label],
                           [input_box,add_btn],
                           [todos_list,edit_btn, complete_btn],
                           [exit_btn]],
                   font=('Helevica',20))
while True:
    event, values = window.read(timeout=200)
    window['time_label'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.read_todos()
            todos.append(values['todo']+"\n")
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                todo = values['todos'][0]
                new_todo = values['todo']+'\n'
                todos = functions.read_todos()
                todo_index = todos.index(todo)
                todos[todo_index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('Please select item first',font=('Helevica',20))
        case 'Complete':
            try:
                todo = values['todos'][0]
                todos = functions.read_todos()
                todos.remove(todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Please select item first',font=('Helevica',20))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break
window.close()
