from app import open_project, create_project, add_project, remove_project, edit_project
from utils import load_db, db_path
import sys


def show_help():
    print(
        """
Usage: project1 <command>

Commands:
  -c, --create    Create a new project
  -o, --open      Open an existing project
  -a, --add       Add new projects directory
  -e, --edit      edit projects directory
  -r, --remove    remove projects directory
  -h, --help      Show this help message
"""
    )


def main():
    try:
        if len(sys.argv) < 2:
            print("Invalid command. Use '-h' or '--help' for usage instructions.")
            return

        command = sys.argv[1]
        if command in ["-h", "--help"]:
            show_help()
        elif command in ["-c", "--create"]:
            create_project(load_db())
        elif command in ["-o", "--open"]:
            open_project(load_db())
        elif command in ["-a", "--add"]:
            add_project(load_db(), db_path)
        elif command in ["-e", "--edit"]:
            edit_project(load_db(), db_path)
        elif command in ["-r", "--remove"]:
            remove_project(load_db(), db_path)
        else:
            print("Invalid command. Use '-h' or '--help' for usage instructions.")
            show_help()
    except KeyboardInterrupt:
        print("\nQuitting application...")
        exit()


if __name__ == "__main__":
    main()
