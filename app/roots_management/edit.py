from utils import os, json, select_project_root, edit_messages as get_message


def edit_project(projects_root, db_path):
    selected_project_root = select_project_root(projects_root)

    while True:
        print(get_message("make_a_choice_message"))
        choice = input().strip().lower()

        if choice == "n":
            selected_project_root.name = validate_projects_root_name(projects_root)
            print(get_message("success_modif_name_message", selected_project_root.name))
            break
        elif choice == "p":
            selected_project_root.path = validate_projects_root_path(projects_root)
            print(get_message("success_modif_path_message", selected_project_root.name))
            break
        else:
            print(get_message("invalid_choice_message"))

    update_project_db(projects_root, db_path, selected_project_root)


def validate_projects_root_name(projects):
    while True:
        new_name = input(get_message("input_new_name_message")).strip()
        if new_name not in [project.name for project in projects]:
            return new_name
        else:
            print(get_message("error_project_exists_message"))


def validate_projects_root_path(projects):
    while True:
        new_root = input(get_message("input_new_path_message")).strip()
        if os.path.isdir(new_root):
            if new_root not in [project.path for project in projects]:
                return new_root
            else:
                print(get_message("error_path_exists_message"))
        else:
            print(get_message("error_invalid_path_message"))


def update_project_db(projects_root, db_path, selected_project_root):
    with open(db_path, "r") as f:
        projects_data = json.load(f)

    for project in projects_data:
        if project["id"] == selected_project_root.id:
            project["name"] = selected_project_root.name
            project["path"] = selected_project_root.path
            break

    with open(db_path, "w") as f:
        json.dump(projects_data, f, indent=4)


if __name__ == "__main__":
    edit_project()
