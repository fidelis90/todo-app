import functions
import PySimpleGUI as sg
import time

sg.theme('Black')

clock = sg.Text('', key='clock')
label = sg.Text("Type in a todo", justification='center')
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(key="Add", image_source="add.png",
                       size=3, mouseover_colors="lightgreen", tooltip="Add Item")
list_todos = sg.Listbox(values=functions.get_todo_list(),
                        key="todos", enable_events=True, size=[45, 10],
                        background_color="blue")
edit_button = sg.Button(key="Edit", image_source="edit.png",
                        size=1, mouseover_colors="Purple", tooltip="Edit Item")
remove_button = sg.Button(key="Remove", image_source="complete.png",
                          size=5, mouseover_colors="Red", tooltip="Remove Item")
exit_button = sg.Button("Exit")


layout = [[clock], [label], [input_box, add_button], [
    list_todos, edit_button, remove_button], [exit_button]]

window = sg.Window("My to do App", layout, font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=100)
    window['clock'].Update(value=time.strftime("%Y-%m-%d %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.get_todo_list()
            new_todo = values["todo"] + '\n'
            todos.append(new_todo)
            index_of_new_todo = todos.index(new_todo)
            functions.write_todo_to_list(todos)
            window['todos'].Update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'
                todos = functions.get_todo_list()
                index_of_todo_to_edit = todos.index(todo_to_edit)
                todos[index_of_todo_to_edit] = new_todo
                functions.write_todo_to_list(todos)
                window['todos'].Update(values=todos)
            except IndexError:
                sg.popup("Please select an item to edit",
                         font=('Helvetica', 20))

        case "Remove":
            try:
                todo_to_remove = values["todos"][0]
                todos = functions.get_todo_list()
                todos.remove(todo_to_remove)
                functions.write_todo_to_list(todos)
                window['todos'].Update(values=todos)
                window['todo'].Update(value='')
            except IndexError:
                sg.popup("Please select an item to remove",
                         font=('Helvetica', 20))

        case 'todos':
            window['todo'].Update(value=values['todos'][0])

        case 'Exit':
            break

    if event in (None, sg.WIN_CLOSED):
        break

window.close()
