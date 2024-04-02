from utils import Project, json, os, add_messages as get_message


def add_projects_root(projects_root, db_path):
    project_id = get_next_project_id(projects_root)
    project_name = prompt_for_name(get_message("input_name_message"), projects_root)
    project_path = prompt_for_directory(
        get_message("input_path_message"), projects_root
    )
    execute_add(project_id, project_name, project_path, projects_root, db_path)
    if project_id in [project.id for project in projects_root]:
        print(get_message("project_added_message"))
    else:
        print(get_message("error_adding_path_message"))


def get_next_project_id(projects):
    project_ids = [project.id for project in projects]
    return max(project_ids) + 1 if project_ids else 1


def prompt_for_name(message, projects):
    while True:
        directory_name = input(message)
        if directory_name not in [project.name for project in projects]:
            return directory_name
        else:
            print(get_message("error_project_exists_message"))
            message = get_message("input_name2_message")


def prompt_for_directory(message, projects):
    while True:
        directory_path = input(message)
        if os.path.isdir(directory_path):
            if directory_path not in [project.path for project in projects]:
                return directory_path
            else:
                print(get_message("error_path_exists_message"))
        else:
            print(get_message("error_invalid_path_message"))


def execute_add(project_id, project_name, project_path, projects, db_path):
    projects.append(Project(project_id, project_name, project_path))
    data = [
        {"id": project.id, "name": project.name, "path": project.path}
        for project in projects
    ]
    with open(db_path, "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    add_projects_root()
