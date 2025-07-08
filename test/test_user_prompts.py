import pytest
from unittest.mock import patch
from src.user_prompts import get_filepath


@pytest.mark.it('Returns string')
@patch("src.user_prompts.input", return_value="Testing.xlsx")
def test_returns_str(mock_input):
    """using patching to provide mock user input: Testing.xlsx"""

    filepath = get_filepath()
    assert isinstance(filepath, str)


@pytest.mark.it('Returns expected path.')
@patch("src.user_prompts.input", return_value="Testing.xlsx")
def test_returns_expected_path(mock_input):
    """using patching to provide mock user input: Testing.xlsx"""

    filepath = get_filepath()
    assert filepath == "data/Testing.xlsx"


@pytest.mark.it('Adds file extension when not provided')
@patch("src.user_prompts.input", return_value="Testing")
def test_adds_file_extension(mock_input):
    """using patching to provide mock user input: Testing"""

    filepath = get_filepath()
    assert filepath == "data/Testing.xlsx"


@pytest.mark.it('Doesn\'t accept non-existent file')
@patch("src.user_prompts.input")
def test_non_existent_file(mock_input):
    """using patching to provide a list of mock user inputs defined below"""

    mock_input.side_effect = ["Missing", "Testing.doc", "Testing.xlsx"]
    filepath = get_filepath()
    assert filepath == "data/Testing.xlsx"
