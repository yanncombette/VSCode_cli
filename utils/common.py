import os
import subprocess
import json
import sys

db_path = os.path.join(os.path.dirname(__file__), "db.json")


class Project:
    def __init__(self, id, name, path):
        self.id = id
        self.name = name
        self.path = path


def open_project_in_vscode(project_path):
    vscode_command = ["code", project_path]
    subprocess.run(vscode_command)


def select_project_root(projects):
    if not projects:
        print(
            f"\nThere are no project roots in your database. Please run the script using '-a' or '-h' for help.\n"
        )
        sys.exit(1)

    print("\nSelect a project:")
    for idx, project in enumerate(projects, start=1):
        print(f"{project.id}. {project.name}")

    options = "/".join(str(i) for i in range(1, len(projects) + 1))
    choice = input(f"\nEnter your choice from ({options}): ")

    if choice.isdigit() and 1 <= int(choice) <= len(projects):
        return projects[int(choice) - 1]
    else:
        print("Invalid choice. Please enter a valid option.")
        return select_project_root(projects)


def load_db():
    if not os.path.exists(db_path):
        print(
            f"\nError: The database file 'utils/db.json' does not exist. Please run 'install.py' to set up the database.\n"
        )
        sys.exit(1)

    with open(db_path) as f:
        data = json.load(f)
    return [Project(item["id"], item["name"], item["path"]) for item in data]


def check_directories(projects):
    false_path = False
    project_name = None
    for project in projects:
        if not os.path.exists(project.path):
            false_path = True
            project_name = project.name
            break #todo if there are more than one incorect path, i should be able to colecte a aray pf names
    return false_path, project_name

