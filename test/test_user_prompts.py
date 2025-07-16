import pytest
from unittest.mock import patch
from src.user_prompts import (
    get_excel_filepath,
    get_csv_filepath,
    valid_headings
)


@pytest.mark.it("Testing get_excel_filepath function")
class TestGetExcelFilepath:
    @pytest.mark.it('Returns string')
    @patch("src.user_prompts.input", return_value="test_results.xlsx")
    def test_returns_str(self, mock_input):
        """using patching to provide mock user input: test_results.xlsx"""

        filepath = get_excel_filepath()
        assert isinstance(filepath, str)

    @pytest.mark.it('Returns expected path.')
    @patch("src.user_prompts.input", return_value="test_results.xlsx")
    def test_returns_expected_path(self, mock_input):
        """using patching to provide mock user input: test_results.xlsx"""

        filepath = get_excel_filepath()
        assert filepath == "data/test_results.xlsx"

    @pytest.mark.it('Adds file extension when not provided')
    @patch("src.user_prompts.input", return_value="test_results")
    def test_adds_file_extension(self, mock_input):
        """using patching to provide mock user input: test_results"""

        filepath = get_excel_filepath()
        assert filepath == "data/test_results.xlsx"

    @pytest.mark.it('Doesn\'t accept non-existent file')
    @patch("src.user_prompts.input")
    def test_non_existent_file(self, mock_input):
        """using patching to provide a list of mock user inputs"""

        mock_input.side_effect = [
            "Missing", "Testing.doc", "test_results.xlsx"
        ]
        filepath = get_excel_filepath()
        assert filepath == "data/test_results.xlsx"


class TestValidHeadings:
    @pytest.mark.it("Returns true if correct headings")
    def test_returns_true(self):
        temp_file = "data/test_headings.csv"
        with open(temp_file, "w") as f:
            f.write("Candidate Number,UCI,Date of Birth\n")
            f.write("new line")
        assert valid_headings(temp_file)

    @pytest.mark.it("Returns True if additional headings")
    def test_returns_true_with_additional_headings(self):
        temp_file = "data/test_headings.csv"
        with open(temp_file, "w") as f:
            f.write("Heading3,Candidate Number,UCI,Heading,Date of Birth\n")
            f.write("new line")
        assert valid_headings(temp_file)

    @pytest.mark.it("Returns False if no UCI")
    def test_returns_false_with_no_uci(self):
        temp_file = "data/test_headings.csv"
        with open(temp_file, "w") as f:
            f.write("Heading3,Candidate Number,Heading,Date of Birth\n")
            f.write("new line")
        assert not valid_headings(temp_file)

    @pytest.mark.it("Returns False if different capitalisation")
    def test_returns_false_with_no_different_capitalisation(self):
        temp_file = "data/test_headings.csv"
        with open(temp_file, "w") as f:
            f.write("candidate number,UCI,Date of Birth\n")
            f.write("new line")
        assert not valid_headings(temp_file)

    @pytest.mark.it("Returns False if different white space")
    def test_returns_false_if_different_white_space(self):
        temp_file = "data/test_headings.csv"
        with open(temp_file, "w") as f:
            f.write("Candidate Number,UCI, Date of Birth\n")
            f.write("new line")
        assert not valid_headings(temp_file)


@pytest.mark.it("Testing get_excel_filepath function")
class TestGetCSVFilepath:
    @pytest.mark.it('Returns string')
    @patch("src.user_prompts.input", return_value="test_candidates.csv")
    def test_returns_str(self, mock_input):
        """using patching to provide mock user input: test_candidates.csv"""

        filepath = get_csv_filepath()
        assert isinstance(filepath, str)

    @pytest.mark.it('Returns expected path.')
    @patch("src.user_prompts.input", return_value="test_candidates.csv")
    def test_returns_expected_path(self, mock_input):
        """using patching to provide mock user input: test_candidates.csv"""

        filepath = get_csv_filepath()
        assert filepath == "data/test_candidates.csv"

    @pytest.mark.it('Adds file extension when not provided')
    @patch("src.user_prompts.input", return_value="test_candidates")
    def test_adds_file_extension(self, mock_input):
        """using patching to provide mock user input: test_candidates"""

        filepath = get_csv_filepath()
        assert filepath == "data/test_candidates.csv"

    @pytest.mark.it('Doesn\'t accept non-existent file')
    @patch("src.user_prompts.input")
    def test_non_existent_file(self, mock_input):
        """using patching to provide a list of mock user inputs"""

        mock_input.side_effect = [
            "Missing", "Testing.xlsx", "test_candidates.csv"
        ]
        filepath = get_csv_filepath()
        assert filepath == "data/test_candidates.csv"

    @pytest.mark.it("Doesn't accept file with different headings")
    @patch("src.user_prompts.input")
    def test_invalid_headings(self, mock_input):
        """using patching to provide a list of mock user inputs"""

        temp_file = "headings_test.csv"

        with open("data/" + temp_file, "w") as f:
            f.write("candidate number,uci,dat of birth")
        mock_input.side_effect = [temp_file, "test_candidates.csv"]
        filepath = get_csv_filepath()
        assert filepath == "data/test_candidates.csv"
