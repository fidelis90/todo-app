# The goal of this app is to create a TODO app
# users can add item to todo list
# show items in the list
# mark items as completed
# edit items in the list
#from functions import get_todo_list, write_todo_to_list
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)


while True:
    prompt = input("Type add, show, edit, complete or exit: ")
    prompt.strip()

    if prompt.startswith("add"):
        todo = prompt[4:]

        todo_list = functions.get_todo_list()  # initialize a list

        todo_list.append(todo + "\n")

        functions.write_todo_to_list(todo_list)

    elif prompt.startswith("show"):
        todo_list = functions.get_todo_list()
        # list comprehension
        new_todo_list = [item.strip("\n") for item in todo_list]

        for i, item in enumerate(new_todo_list):
            row = f"{i+1}-{item}"
            print(row)

    elif prompt.startswith("edit"):
        try:  # This is used to handle error bug
            num = int(prompt[5:])
            with open('todo.txt', 'r') as file:
                for count, line in enumerate(file):
                    pass
            num_of_lines_in_database = int(count + 1)
            num_to_edit = num - 1
            if num_to_edit <= num_of_lines_in_database:
                new_todo = input("Enter the new todo item: ") + "\n"
                todo_list = functions.get_todo_list()
                todo_list[num_to_edit] = new_todo

                functions.write_todo_to_list(todo_list)
            else:
                print("The item is not in list")
        except ValueError:  # specify the error
            print("Your command is not valid")
            continue
        except IndexError:
            print("The command is out of range")

    elif prompt.startswith("complete"):
        num = int(prompt[9:]) - 1
        todo_list = functions.get_todo_list()
        todo_to_remove = todo_list[num].strip("\n")
        message = f'"{todo_to_remove}" was removed from the list.'
        todo_list.pop(num)
        functions.write_todo_to_list(todo_list)
        print(message)

    elif prompt.startswith("exit"):
        break

    else:
        print("Command is not valid")

print("bye")
