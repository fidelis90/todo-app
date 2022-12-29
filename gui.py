import functions
import PySimpleGUI as sg

label = sg.Text("Enter a to-do item")
input_box = sg.InputText(tooltip="Enter to-do")
add_button = sg.Button("Add")


# create a window
window = sg.Window("Swags Todo App", layout=[
                   [label], [input_box, add_button]])
window.read()
window.close()
