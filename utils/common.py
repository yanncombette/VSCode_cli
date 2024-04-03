import os
import subprocess
import json
import sys


def open_project_in_vscode(project_path):
    subprocess.run(["code", project_path])


# -- db ---------------------------------------------------------
db_path = os.path.join(os.path.dirname(__file__), "db.json")


class Project:
    def __init__(self, id, name, path):
        self.id = id
        self.name = name
        self.path = path


def load_db():
    if not os.path.exists(db_path):
        print(
            f"\nError: The database file 'utils/db.json' does not exist. Please run 'install.py' to set up the database.\n"
        )
        sys.exit(1)

    data = load_data(db_path)
    return [Project(item["id"], item["name"], item["path"]) for item in data]


def load_data(db_path):
    with open(db_path, "r") as f:
        return json.load(f)


def save_data(data, db_path):
    with open(db_path, "w") as f:
        json.dump(data, f, indent=4)


# -- end of db --------------------------------------------------


# -- validation ---------------------------------------------------------
def check_projects_root_path_os(directory_path):
    if os.path.isdir(directory_path):
        return directory_path
    else:
        return None


def check_projects_root_db(new_projects_root, projects_roots_list, attribute):
    attribute_list = [
        getattr(projects_root, attribute) for projects_root in projects_roots_list
    ]
    if new_projects_root not in attribute_list:
        return new_projects_root
    else:
        return None


def validate_projects_root_path(message, projects_roots_list):
    while True:
        new_projects_root_path = input(message)
        if check_projects_root_path_os(new_projects_root_path):
            if check_projects_root_db(
                new_projects_root_path, projects_roots_list, "path"
            ):
                return new_projects_root_path
            else:
                print("error_path_exists_message")
        else:
            print("error_invalid_path_message")


def validate_projects_root_name(message, projects_roots_list):
    while True:
        new_projects_root_name = input(message)
        if check_projects_root_db(new_projects_root_name, projects_roots_list, "name"):
            return new_projects_root_name
        else:
            print("error_project_exists_message")
            message = "input_name2_message"


def validate_projects_root_id(message, projects_roots_list):
    while True:
        selected_projects_root_id = input(message)
        if check_projects_root_db(selected_projects_root_id, projects_roots_list, "id"):
            return selected_projects_root_id
        else:
            print("error_project_exists_message")
            message = "input_name2_message"


# -- end of validation --------------------------------------------------


# -- need work ---------------------------------------------------------
def select_project_root(projects_roots_list):
    if not projects_roots_list:
        print(
            f"\nThere are no project roots in your database. Please run the script using '-a' or '-h' for help.\n"
        )
        sys.exit(1)

    print("\nSelect a project:")
    for projects_root in projects_roots_list:
        print(f"{projects_root.id}. {projects_root.name}")

    valid_ids = [str(root.id) for root in projects_roots_list]
    choice = input(f"\nEnter the id of your choice: ")

    # todo implementing validate_projects_root_id()
    if choice in valid_ids:
        for projects_root in projects_roots_list:
            if str(projects_root.id) == choice:
                return projects_root
    else:
        print("Invalid choice. Please enter a valid id.")
        return select_project_root(projects_roots_list)


def check_directories(projects_roots_list):
    for projects_root in projects_roots_list:
        if not os.path.exists(projects_root.path):
            # todo if there are more than one incorect path, i should be able to colecte a aray pf names
            return projects_root
    return None


# -- end of need work --------------------------------------------------
