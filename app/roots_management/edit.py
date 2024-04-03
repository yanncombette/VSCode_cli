from utils import (
    select_project_root,
    validate_projects_root_path,
    validate_projects_root_name,
    load_data,
    save_data,
    edit_messages as get_message,
)


def edit_projects_root(projects_roots_list, db_path, projects_root=None):
    if projects_root:
        print(f"the path for this projects root is: {projects_root.path}")
        projects_root.path = validate_projects_root_path(get_message("input_new_path_message"), projects_roots_list)
        print(get_message("success_modif_path_message", projects_root.name))
        execute_edit(projects_root, db_path)
        return

    selected_projects_root = select_project_root(projects_roots_list)

    while True:
        print(get_message("make_a_choice_message"))
        choice = input().strip().lower()

        if choice == "n":
            selected_projects_root.name = validate_projects_root_name(
                get_message("input_new_name_message"), projects_roots_list
            )
            print(
                get_message("success_modif_name_message", selected_projects_root.name)
            )
            break
        elif choice == "p":
            selected_projects_root.path = validate_projects_root_path(
                get_message("input_new_path_message"), projects_roots_list
            )
            print(
                get_message("success_modif_path_message", selected_projects_root.name)
            )
            break
        else:
            print(get_message("invalid_choice_message"))

    execute_edit(selected_projects_root, db_path)


def execute_edit(selected_projects_root, db_path):
    data = load_data(db_path)

    for projects_root in data:
        if projects_root["id"] == selected_projects_root.id:
            projects_root["name"] = selected_projects_root.name
            projects_root["path"] = selected_projects_root.path
            break

    save_data(data, db_path)


if __name__ == "__main__":
    edit_projects_root()
