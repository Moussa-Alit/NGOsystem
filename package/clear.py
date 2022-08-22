from functions import get_script_path

def clear_navbar():
    x = get_script_path()
    with open(f"{get_script_path()}/templates/navbar.html") as file:
        lines = file.readlines()
    for i in lines:
        if i == '\n':
            lines.remove(i)
    print(lines)
