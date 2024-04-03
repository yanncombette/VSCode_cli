from utils import (
    Project,
    validate_projects_root_path,
    validate_projects_root_name,
    save_data,
    add_messages as get_message,
)


def add_projects_root(projects_roots_list, db_path):
    projects_root_id = get_next_projects_root_id(projects_roots_list)
    projects_root_name = validate_projects_root_name(
        get_message("input_name_message"), projects_roots_list
    )
    projects_root_path = validate_projects_root_path(
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
    save_data(data, db_path)


if __name__ == "__main__":
    add_projects_root()
