from .roots_management import edit_projects_root, remove_projects_root
from utils import (
    os,
    select_project_root,
    open_project_in_vscode,
    open_messages as get_message,
    check_directories,
)


def open_project(projects_roots_list, db_path):
    projects_root = check_directories(projects_roots_list)
    if projects_root:
        open_path_correction(
            projects_roots_list, db_path, projects_root, false_path=True
        )

    selected_projects_root = select_project_root(projects_roots_list)

    if selected_projects_root == projects_root:
        print(f"\n[ERROR]: you must edit path or remove '{projects_root.name}' .")
        open_path_correction(projects_roots_list, db_path, projects_root)

    project_name = input(get_message("input_project_name_message"))

    execute_project(selected_projects_root, project_name)


def open_path_correction(projects_roots_list, db_path, projects_root, false_path=None):
    message = "Enter 'e' to edit, 'r' to remove"
    if false_path:
        message += ", or press Enter to continue"
    message += ": "

    while True:
        user_input = input(message).lower()
        if user_input == "e":
            edit_projects_root(projects_roots_list, db_path, projects_root)
            return
        elif user_input == "r":
            remove_projects_root(projects_roots_list, db_path, projects_root)
            return
        elif user_input.strip() == "":
            if false_path:
                return
            else:
                print("Invalid input. Please enter 'e' or 'r'.")
        else:
            print("Invalid input. Please enter 'e' or 'r'.")


def execute_project(selected_projects_root, project_name):
    project_path = os.path.join(selected_projects_root.path, project_name)

    if os.path.exists(project_path):
        print(
            get_message("opening_project_message", project_name, selected_projects_root)
        )
        open_project_in_vscode(project_path)

    else:
        if project_name == "?":
            print(
                get_message(
                    "project_in_directory_message",
                    selected_project_root=selected_projects_root,
                )
            )
            print("\n".join(os.listdir(selected_projects_root.path)))
            diferent_project_name = input(get_message("input_project_name2_message"))
            execute_project(selected_projects_root, diferent_project_name)
        else:
            print(get_message("project_selection_error_message", project_name))
            diferent_project_name = input(get_message("input_project_name_message"))
            execute_project(selected_projects_root, diferent_project_name)


if __name__ == "__main__":
    open_project()
