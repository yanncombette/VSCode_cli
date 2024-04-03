from utils import os, json, select_project_root, edit_messages as get_message


def edit_projects_root(projects_roots_list, db_path, projects_root=None):
    if projects_root:
        print(f"the path for this projects root is: {projects_root.path}")
        projects_root.path = validate_projects_root_path(projects_roots_list)
        print(get_message("success_modif_path_message", projects_root.name))
        execute_edit(projects_root, db_path)
        return

    selected_projects_root = select_project_root(projects_roots_list)

    while True:
        print(get_message("make_a_choice_message"))
        choice = input().strip().lower()

        if choice == "n":
            selected_projects_root.name = validate_projects_root_name(
                projects_roots_list
            )
            print(
                get_message("success_modif_name_message", selected_projects_root.name)
            )
            break
        elif choice == "p":
            selected_projects_root.path = validate_projects_root_path(
                projects_roots_list
            )
            print(
                get_message("success_modif_path_message", selected_projects_root.name)
            )
            break
        else:
            print(get_message("invalid_choice_message"))

    execute_edit(selected_projects_root, db_path)


def validate_projects_root_name(projects_roots_list):
    while True:
        new_name = input(get_message("input_new_name_message")).strip()
        if new_name not in [
            projects_root.name for projects_root in projects_roots_list
        ]:
            return new_name
        else:
            print(get_message("error_project_exists_message"))


def validate_projects_root_path(projects_roots_list):
    while True:
        new_path = input(get_message("input_new_path_message")).strip()
        if os.path.isdir(new_path):
            if new_path not in [
                projects_root.path for projects_root in projects_roots_list
            ]:
                return new_path
            else:
                print(get_message("error_path_exists_message"))
        else:
            print(get_message("error_invalid_path_message"))


def execute_edit(selected_projects_root, db_path):
    with open(db_path, "r") as f:
        data = json.load(f)

    for projects_root in data:
        if projects_root["id"] == selected_projects_root.id:
            projects_root["name"] = selected_projects_root.name
            projects_root["path"] = selected_projects_root.path
            break

    with open(db_path, "w") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    edit_projects_root()
