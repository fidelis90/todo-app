import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_todos = sg.Listbox(values=functions.get_todo_list(),
                        key="todos", enable_events=True, size=[45, 10],
                        background_color="blue")
edit_button = sg.Button("Edit")


layout = [[label], [input_box, add_button], [list_todos, edit_button]]

window = sg.Window("My to do App", layout, font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values["todos"])

    match event:
        case "Add":
            todos = functions.get_todo_list()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todo_to_list(todos)
            window['todos'].Update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + '\n'
            todos = functions.get_todo_list()
            index_of_todo_to_edit = todos.index(todo_to_edit)
            todos[index_of_todo_to_edit] = new_todo
            functions.write_todo_to_list(todos)
            window['todos'].Update(values=todos)

        case 'todos':
            window['todo'].Update(value=values['todos'][0])

    if event in (None, sg.WIN_CLOSED):
        break

window.close()
