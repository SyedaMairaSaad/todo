import FreeSimpleGUI as sg
import functions
label =sg.Text("Type in TODO")
input_box=sg.InputText(tooltip="Enter TODO", key="todo")
add_btn = sg.Button("Add")
window = sg.Window("My TODO App",
                   layout=[[label],[input_box,add_btn]],
                   font=('Helevica',20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.read_todos()
            todos.append("/n"+values['todo'])
            functions.write_todos(todos)
window.close()
