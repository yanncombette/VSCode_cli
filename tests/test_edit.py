import os
import pytest
from app import edit_projects_root
from tests import (
    set_keyboard_input,
    get_display_output,
    db_test,
    dbtest_path,
)

test_folder = os.path.join(os.path.dirname(__file__), "")


# @pytest.mark.skip(reason="testing db")
def test_edit_name():

    set_keyboard_input(["1", "n", "test_modifies"])

    edit_projects_root(db_test, dbtest_path)

    output = get_display_output()

    assert output == [
        "\nSelect a project:",
        "1. test",
        "\nEnter your choice from (1): ",
        "Do you want to edit project's name 'n' or path 'p' ?",
        "",
        "Enter the new name: ",
        "Name 'test_modifies' modified successfully!",
    ]


# @pytest.mark.skip(reason="testing db")
def test_edit_root():

    set_keyboard_input(["1", "p", test_folder])

    edit_projects_root(db_test, dbtest_path)

    output = get_display_output()

    assert output == [
        "\nSelect a project:",
        "1. test_modifies",
        "\nEnter your choice from (1): ",
        "Do you want to edit project's name 'n' or path 'p' ?",
        "",
        "Enter the new path: ",
        "Path 'test_modifies' modified successfully!",
    ]
