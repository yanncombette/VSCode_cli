import pytest
from app import create_project
from tests import set_keyboard_input, get_display_output, delete_test_project_folder, db_test


def test_create():
    print("create in process...")
    set_keyboard_input(["1", "test_project"])

    create_project(db_test)

    output = get_display_output()

    assert output == [
        "\nSelect a project:",
        "1. test",
        "\nEnter your choice from (1): ",
        "\nEnter a new project name: ",
        "\nNew project 'test_project' created successfully.",
    ]

def test_fail_create_wrong_directory_input():
    print("create in process...")
    set_keyboard_input(["2"])
    with pytest.raises(IndexError):
        create_project(db_test)

    output = get_display_output()

    assert output == [
        "\nSelect a project:",
        "1. test",
        "\nEnter your choice from (1): ",
        "Invalid choice. Please enter a valid option.",
        "\nSelect a project:",
        "1. test",
        "\nEnter your choice from (1): "
    ]


def test_fail_create_existing_project_name():
    print("create in process...")
    set_keyboard_input(["1", "test_project"])
    with pytest.raises(IndexError):
        create_project(db_test)

    output = get_display_output()

    assert output == [
        "\nSelect a project:",
        "1. test",
        "\nEnter your choice from (1): ",
        "\nEnter a new project name: ",
        "\nThe project 'test_project' already exists in the root directory.",
        "Please enter a different project name: "
    ]

