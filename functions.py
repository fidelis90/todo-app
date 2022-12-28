FILEPATH = "todo.txt"


def get_todo_list(filepath=FILEPATH):
    """ Read a text file and return the 
    list of todo items. 
    """
    with open(filepath, "r") as file_local:
        todo_list_local = file_local.readlines()
    return todo_list_local


def write_todo_to_list(todos_arg, filepath=FILEPATH):
    """ Write the todo items list in the text file. """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todo_list())
