import os
import pytest
from app import add_project
from tests import set_keyboard_input, get_display_output, db_test, dbtest_path, reset_db

test_folder = os.path.join(os.path.dirname(__file__), "test_folder")


def test_add():

    print("add in process...")
    set_keyboard_input(["test", test_folder])

    add_project(db_test, dbtest_path)
    output = get_display_output()

    assert output == [
        "Enter project name: ",
        "Enter project path: ",
        "Project successfully added!",
    ]


def test_fail_add_existing_name():
    print("fail add name in process...")
    set_keyboard_input(["test"])

    with pytest.raises(IndexError):
        add_project(db_test, dbtest_path)

    output = get_display_output()

    assert output == [
        "Enter project name: ",
        "Error: The specified project name already exists in the database. Please enter a unique name.",
        "enter a different name: ",
    ]


def test_fail_add_incorect_route():
    print("fail add name in process...")
    set_keyboard_input(["test2", "test/path"])

    with pytest.raises(IndexError):
        add_project(db_test, dbtest_path)

    output = get_display_output()

    assert output == [
        "Enter project name: ",
        "Enter project path: ",
        "Error: The specified directory does not exist. Please enter a valid directory path.",
        "Enter project path: ",
    ]


def test_fail_add_existing_path():
    print("fail add name in process...")
    set_keyboard_input(["test2", test_folder])

    with pytest.raises(IndexError):
        add_project(db_test, dbtest_path)

    output = get_display_output()

    assert output == [
        "Enter project name: ",
        "Enter project path: ",
        "Error: The specified directory path already exists in the database.",
        "Enter project path: ",
    ]


def test_fail_add_all():
    print("fail add name in process...")
    set_keyboard_input(["test", "test2", "test/path", test_folder])

    with pytest.raises(IndexError):
        add_project(db_test, dbtest_path)

    output = get_display_output()

    assert output == [
        "Enter project name: ",
        "Error: The specified project name already exists in the database. Please enter a unique name.",
        "enter a different name: ",
        "Enter project path: ",
        "Error: The specified directory does not exist. Please enter a valid directory path.",
        "Enter project path: ",
        "Error: The specified directory path already exists in the database.",
        "Enter project path: ",
    ]
