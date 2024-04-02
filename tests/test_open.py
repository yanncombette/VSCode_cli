import os
import pytest
from app import open_project
from tests import (
    set_keyboard_input,
    get_display_output,
    reset_db,
    delete_test_project_folder,
    db_test,
)


def test_open():

    set_keyboard_input(["1", "test_project"])

    open_project(db_test)

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
        open_project(db_test)

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
        open_project(db_test)

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

    set_keyboard_input(["1", "incorect_project"])

    with pytest.raises(IndexError):
        open_project(db_test)

    output = get_display_output()

    assert output == [
        "\nSelect a project:",
        "1. test",
        "\nEnter your choice from (1): ",
        "Enter a project name (or '?' to see the list of projects): ",
        "The project 'incorect_project' does not exist in the root directory. \n",
        "Enter a project name (or '?' to see the list of projects): ",
    ]

# TODO : this test wont work and i dont know how, folder is deleted so i dont see why it doesnt give me the error.
def test_fail_open_moved_or_erased_Project_root():
    set_keyboard_input([])

    delete_test_project_folder()

    with pytest.raises(IndexError):
        open_project(db_test)

    output = get_display_output()

    warning_message = "\n[WARNING]: Project root 'tes2' has been moved or erased. Do you want to continue? [y/N]: "
    assert (
        warning_message in output
    ), f"Expected warning message not found in output:\n{output}"


@pytest.fixture(scope="session", autouse=True)
def final_teardown():
    reset_db()
