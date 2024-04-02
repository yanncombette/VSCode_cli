from utils import json, select_project_root, remove_messages as get_message


def remove_projects_root(projects_root, db_path):
    selected_project_root = select_project_root(projects_root)
    execute_project(selected_project_root, db_path)


def execute_project(selected_project_root, db_path):
    confirmation = (
        input(get_message("input_confirmation_message", selected_project_root.name))
        .strip()
        .lower()
    )

    if confirmation == "y" or confirmation == "":
        with open(db_path, "r") as f:
            projects_data = json.load(f)

        index_to_remove = None
        for index, project in enumerate(projects_data):
            if project["id"] == selected_project_root.id:
                index_to_remove = index
                break

        if index_to_remove is not None:
            del projects_data[index_to_remove]
            print(get_message("Project_removed_message", selected_project_root.name))
        else:
            print(get_message("project_not_found_message", selected_project_root.name))

        with open(db_path, "w") as f:
            json.dump(projects_data, f, indent=4)
    else:
        print(get_message("canel_remove_message"))


if __name__ == "__main__":
    remove_projects_root()
