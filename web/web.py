import streamlit as st
import functions as fc

#: define function to add

session_state = st.session_state
todos = fc.get_todo_list()


def add_todo_item():
    todo = session_state["new_todo"] + '\n'
    todos.append(todo)
    fc.write_todo_to_list(todos)


title = st.title('My Todo App')
subheader = st.subheader("This is my todo app.")
app_desc = st.write('This is to increase my productivity daily')

for todo in todos:
    st.checkbox(todo)

user_input = st.text_input(label='Enter todo item', label_visibility="hidden", placeholder="Add an item",
                           key="new_todo", on_change=add_todo_item)

# session_state
