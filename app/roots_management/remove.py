import sys
from utils import (
    select_project_root,
    load_data,
    save_data,
    remove_messages as get_message,
)


def remove_projects_root(projects_roots_list, db_path, projects_root=None):
    if projects_root:
        execute_remove(projects_root, db_path)
            

    selected_projects_root = select_project_root(projects_roots_list)
    execute_remove(selected_projects_root, db_path)


def execute_remove(selected_projects_root, db_path):
    confirmation = (
        input(get_message("input_confirmation_message", selected_projects_root.name))
        .strip()
        .lower()
    )

    if confirmation == "y" or confirmation == "":
        data = load_data(db_path)

        index_to_remove = None
        for index, projects_root in enumerate(data):
            if projects_root["id"] == selected_projects_root.id:
                index_to_remove = index
                break

        if index_to_remove is not None:
            del data[index_to_remove]
            print(get_message("Project_removed_message", selected_projects_root.name))
        else:
            print(get_message("project_not_found_message", selected_projects_root.name))

        save_data(data, db_path)
        sys.exit()
    else:
        print(get_message("canel_remove_message"))


if __name__ == "__main__":
    remove_projects_root()
