import streamlit as st
import functions as fc

todos = fc.get_todo_list()

st.title('My Todo App')
st.subheader("This is my todo app.")
st.write('This is to increase my productivity daily')

for todo in todos:
    st.checkbox(todo)

st.text_input(label='', placeholder="Add an item")
