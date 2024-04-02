from utils import (
    os,
    select_project_root,
    open_project_in_vscode,
    open_messages as get_message,
    check_directories,
)


def open_project(projects_root):
    false_path, project_name = check_directories(projects_root)
    if false_path:
        input(
            f"\n[WARNING]: Project root '{project_name}' has been moved or erased. Do you want to continue? [y/N]: "
        )

    selected_project_root = select_project_root(projects_root)
    project_name = input(get_message("input_project_name_message"))
    execute_project(selected_project_root, project_name)


def execute_project(selected_project_root, project_name):
    project_root = selected_project_root.path
    project_path = os.path.join(project_root, project_name)

    if os.path.exists(project_path):
        print(
            get_message("opening_project_message", project_name, selected_project_root)
        )
        open_project_in_vscode(project_path)

    else:
        if project_name == "?":
            print(
                get_message(
                    "project_in_directory_message",
                    selected_project_root=selected_project_root,
                )
            )
            print("\n".join(os.listdir(project_root)))
            new_project_name = input(get_message("input_project_name2_message"))
            execute_project(selected_project_root, new_project_name)
        else:
            print(get_message("project_selection_error_message", project_name))
            new_project_name = input(get_message("input_project_name_message"))
            execute_project(selected_project_root, new_project_name)


if __name__ == "__main__":
    open_project()
