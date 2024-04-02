def add_messages(message_type):
    messages = {
        "input_name_message": "Enter project name: ",
        "input_name2_message": "enter a different name: ",
        "input_path_message": "Enter project path: ",
        "project_added_message": "Project successfully added!",
        "error_project_exists_message": "Error: The specified project name already exists in the database. Please enter a unique name.",
        "error_path_exists_message": "Error: The specified directory path already exists in the database.",
        "error_invalid_path_message": "Error: The specified directory does not exist. Please enter a valid directory path.",
        "error_adding_path_message": "Error: Project was not added.",
    }

    if message_type in messages:
        return messages[message_type]
    else:
        return "Invalid message type"


def create_messages(message_type, project_name=None):
    messages = {
        "input_new_name_message": "\nEnter a new project name: ",
        "new_project_created_message": "\nNew project '{project_name}' created successfully.",
        "Project_name_exist_message": "\nThe project '{project_name}' already exists in the root directory.",
        "input_different_name_message": "Please enter a different project name: ",
    }

    if message_type in messages:
        if (
            message_type == "new_project_created_message"
            or message_type == "Project_name_exist_message"
        ):
            return messages[message_type].format(project_name=project_name)
        else:
            return messages[message_type]
    else:
        return "Invalid message type"


def open_messages(message_type, project_name=None, selected_project_root=None):
    messages = {
        "input_project_name_message": "Enter a project name (or '?' to see the list of projects): ",
        "input_project_name2_message": "\nEnter a project name: ",
        "opening_project_message": "Opening {project_name} from {selected_project_root.name}...",
        "project_in_directory_message": "\nProjects in the {selected_project_root.name} directory:",
        "project_selection_error_message": "The project '{project_name}' does not exist in the root directory. \n",
    }

    if message_type in messages:
        if message_type == "opening_project_message":
            return messages[message_type].format(
                project_name=project_name, selected_project_root=selected_project_root
            )
        elif message_type == "project_in_directory_message":
            return messages[message_type].format(
                selected_project_root=selected_project_root
            )
        elif message_type == "project_selection_error_message":
            return messages[message_type].format(project_name=project_name)
        else:
            return messages[message_type]
    else:
        return "Invalid message type"


def remove_messages(message_type, project_root_name=None):
    messages = {
        "input_confirmation_message": "Are you sure you want to remove '{project_root_name}' from the database? [Y/n] ",
        "Project_removed_message": "Project {project_root_name} removed from db.",
        "project_not_found_message": "Project {project_root_name} not found.",
        "canel_remove_message": "Removal canceled.",
    }

    if message_type in messages:
        if (
            message_type == "input_confirmation_message"
            or message_type == "Project_removed_message"
            or message_type == "project_not_found_message"
        ):
            return messages[message_type].format(project_root_name=project_root_name)
        else:
            return messages[message_type]
    else:
        return "Invalid message type"


def edit_messages(message_type, project_root_name=None):
    messages = {
        "make_a_choice_message": "Do you want to edit project's name 'n' or path 'p' ?",
        "invalid_choice_message": "Invalid choice. Please enter 'n' to edit name or 'r' to edit root.",
        "input_new_name_message": "Enter the new name: ",
        "error_project_exists_message": "Error: The specified project name already exists in the database. Please enter a unique name.",
        "input_new_path_message": "Enter the new path: ",
        "error_path_exists_message": "Error: The specified directory path already exists in the database.",
        "error_invalid_path_message": "Error: The specified directory does not exist. Please enter a valid directory path.",
        "success_modif_name_message": "Name '{project_root_name}' modified successfully!",
        "success_modif_path_message": "Path '{project_root_name}' modified successfully!",
    }

    if message_type in messages:
        if (
            message_type == "success_modif_name_message"
            or message_type == "success_modif_path_message"
        ):
            return messages[message_type].format(project_root_name=project_root_name)
        else:
            return messages[message_type]
    else:
        return "Invalid message type"
