import streamlit as st
import functions

todos = functions.read_todos()
def add_todos():
    new_todo = st.session_state['new_todo']
    todos.append(new_todo+'\n')
    functions.write_todos(todos)

st.title('My Todo App')
st.subheader('This is my todo app')
st.write('This App is to increase your productivity')

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='', placeholder='Enter a todo' ,key='new_todo', on_change=add_todos)