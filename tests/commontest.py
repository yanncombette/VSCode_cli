from app import open_project
from tests import set_keyboard_input, get_display_output
import os
import json
import sys
import subprocess

# cloning database...
data = []
dbtest_path = os.path.join(os.path.dirname(__file__), "dbtest.json")
test_project = os.path.join(os.path.dirname(__file__), "test_folder/test_project")


class Project:
    def __init__(self, id, name, path):
        self.id = id
        self.name = name
        self.path = path


def load_db():
    if not os.path.exists(dbtest_path):
        print(
            f"\nError: The database file 'utils/db.json' does not exist. Please run 'install.py' to set up the database.\n"
        )
        sys.exit(1)

    with open(dbtest_path) as f:
        data = json.load(f)
    return [Project(item["id"], item["name"], item["path"]) for item in data]


db_test = load_db()


def reset_db():
    with open(dbtest_path, "w") as f:
        json.dump(data, f, indent=4)


def delete_test_project_folder():
    # print(
    #     f"Deleting directory '{test_project}' for test purposes make sure the directory is corecte and empthy..."
    # )
    try:
        subprocess.run(["sudo", "rm", "-rf", test_project], check=True)
        # print(f"Directory '{test_project}' has been deleted successfully.")
    except subprocess.CalledProcessError:
        print(f"Error: Permission denied or directory not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
