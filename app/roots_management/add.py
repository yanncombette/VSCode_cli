from utils import Project, json, os, add_messages as get_message


def add_projects_root(projects_roots_list, db_path):
    projects_root_id = get_next_projects_root_id(projects_roots_list)
    projects_root_name = prompt_for_name(
        get_message("input_name_message"), projects_roots_list
    )
    projects_root_path = prompt_for_directory(
        get_message("input_path_message"), projects_roots_list
    )
    execute_add(
        projects_root_id,
        projects_root_name,
        projects_root_path,
        projects_roots_list,
        db_path,
    )
    if projects_root_id in [projects_root.id for projects_root in projects_roots_list]:
        print(get_message("project_added_message"))
    else:
        print(get_message("error_adding_path_message"))


def get_next_projects_root_id(projects_roots_list):
    projects_roots_list_id = [projects_root.id for projects_root in projects_roots_list]
    return max(projects_roots_list_id) + 1 if projects_roots_list_id else 1


def prompt_for_name(message, projects_roots_list):
    while True:
        directory_name = input(message)
        if directory_name not in [
            projects_root.name for projects_root in projects_roots_list
        ]:
            return directory_name
        else:
            print(get_message("error_project_exists_message"))
            message = get_message("input_name2_message")


def prompt_for_directory(message, projects_roots_list):
    while True:
        directory_path = input(message)
        if os.path.isdir(directory_path):
            if directory_path not in [
                projects_root.path for projects_root in projects_roots_list
            ]:
                return directory_path
            else:
                print(get_message("error_path_exists_message"))
        else:
            print(get_message("error_invalid_path_message"))


def execute_add(
    projects_root_id,
    projects_root_name,
    projects_root_path,
    projects_roots_list,
    db_path,
):
    projects_roots_list.append(
        Project(projects_root_id, projects_root_name, projects_root_path)
    )
    data = [
        {"id": projects_root.id, "name": projects_root.name, "path": projects_root.path}
        for projects_root in projects_roots_list
    ]
    with open(db_path, "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    add_projects_root()
