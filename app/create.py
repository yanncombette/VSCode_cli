from utils import (
    os,
    select_project_root,
    open_project_in_vscode,
    create_messages as get_message,
)


def create_project(projects_root):
    selected_project_root = select_project_root(projects_root)
    project_name = input(get_message("input_new_name_message"))
    path = selected_project_root.path
    create_and_open_project(path, project_name)


def create_and_open_project(path, project_name):
    new_project_path = os.path.join(path, project_name)

    if not os.path.exists(new_project_path):
        os.makedirs(new_project_path)
        print(get_message("new_project_created_message", project_name))
        open_project_in_vscode(new_project_path)
    else:
        print(get_message("Project_name_exist_message", project_name))
        project_name = input(get_message("input_different_name_message"))
        create_and_open_project(path, project_name)


if __name__ == "__main__":
    create_project()
