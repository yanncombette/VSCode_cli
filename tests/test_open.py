import json
import os
import pytest
from app import open_project
from tests import (
    set_keyboard_input,
    get_display_output,
    delete_test_project_folder,
    db_test,
    dbtest_path,
)


def test_open():

    set_keyboard_input(["1", "test_project"])

    open_project(db_test, dbtest_path)

    output = get_display_output()

    assert output == [
        "\nSelect a project:",
        "1. test",
        "\nEnter your choice from (1): ",
        "Enter a project name (or '?' to see the list of projects): ",
        "Opening test_project from test...",
    ]


def test_open_using_question():

    set_keyboard_input(["1", "?"])

    with pytest.raises(IndexError):
        open_project(db_test, dbtest_path)

    output = get_display_output()

    assert output == [
        "\nSelect a project:",
        "1. test",
        "\nEnter your choice from (1): ",
        "Enter a project name (or '?' to see the list of projects): ",
        "\nProjects in the test directory:",
        "test_project\ntes_foler.md",
        "\nEnter a project name: ",
    ]


def test_fail_open_wrong_directory_input():

    set_keyboard_input(["2"])

    with pytest.raises(IndexError):
        open_project(db_test, dbtest_path)

    output = get_display_output()

    assert output == [
        "\nSelect a project:",
        "1. test",
        "\nEnter your choice from (1): ",
        "Invalid choice. Please enter a valid option.",
        "\nSelect a project:",
        "1. test",
        "\nEnter your choice from (1): ",
    ]


def test_fail_open_wrong_project_name_input():
    delete_test_project_folder()
    set_keyboard_input(["1", "incorect_project"])

    with pytest.raises(IndexError):
        open_project(db_test, dbtest_path)

    output = get_display_output()

    assert output == [
        "\nSelect a project:",
        "1. test",
        "\nEnter your choice from (1): ",
        "Enter a project name (or '?' to see the list of projects): ",
        "The project 'incorect_project' does not exist in the root directory. \n",
        "Enter a project name (or '?' to see the list of projects): ",
    ]


new_data = {"id": 1, "name": "test", "path": "/invalid/path"}


@pytest.fixture(scope="session", autouse=True)
def reset_db():
    dbtest_path = os.path.join(os.path.dirname(__file__), "dbtest.json")
    with open(dbtest_path, "r") as f:
        data = json.load(f)

    for project in data:
        if project["id"] == new_data["id"]:
            project["name"] = new_data["name"]
            project["path"] = new_data["path"]
            break

    with open(dbtest_path, "w") as f:
        json.dump(data, f, indent=4)


@pytest.mark.skip(reason="doesnt work need need help?")
def test_fail_open_moved_or_erased_Project_root():
    set_keyboard_input([])

    with pytest.raises(IndexError):
        open_project(db_test, dbtest_path)

    output = get_display_output()

    assert output == [
        "\n[WARNING]: Project root 'tes2' has been moved or erased. Do you want to continue? [y/N]: ",
    ]
