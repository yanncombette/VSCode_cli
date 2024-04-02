from utils import json, select_project_root, remove_messages as get_message


def remove_projects_root(projects_roots_list, db_path):
    selected_projects_root = select_project_root(projects_roots_list)
    execute_project(selected_projects_root, db_path)


def execute_project(selected_projects_root, db_path):
    confirmation = (
        input(get_message("input_confirmation_message", selected_projects_root.name))
        .strip()
        .lower()
    )

    if confirmation == "y" or confirmation == "":
        with open(db_path, "r") as f:
            data = json.load(f)

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

        with open(db_path, "w") as f:
            json.dump(data, f, indent=4)
    else:
        print(get_message("canel_remove_message"))


if __name__ == "__main__":
    remove_projects_root()
