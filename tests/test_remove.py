import pytest
from app import remove_projects_root
from tests import set_keyboard_input, get_display_output, db_test, dbtest_path

# @pytest.mark.skip(reason="testing db")
def test_remove():

    set_keyboard_input(["1", "y"])
    with pytest.raises(SystemExit):
        remove_projects_root(db_test, dbtest_path)

    output = get_display_output()

    assert output == [
        "\nSelect a project:",
        "1. test_modifies",
        "\nEnter your choice from (1): ",
        "Are you sure you want to remove 'test_modifies' from the database? [Y/n] ",
        "Project test_modifies removed from db.",
    ]

# @pytest.mark.skip(reason="testing db")
def test_remove_cancel():

    set_keyboard_input(["1", "n"])
    remove_projects_root(db_test, dbtest_path)

    output = get_display_output()

    assert output == [
        "\nSelect a project:",
        "1. test_modifies",
        "\nEnter your choice from (1): ",
        "Are you sure you want to remove 'test_modifies' from the database? [Y/n] ",
        "Removal canceled.",
    ]
