import pytest
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.cell.cell import Cell
from src.read_excel import (
    get_worksheets,
    get_date,
    get_titles,
    get_sheet_results,
    get_results,
    get_centre_number
)
from datetime import datetime


@pytest.mark.it('get_worksheets function tests')
class TestGetWorksheets:
    @pytest.fixture
    def test_file(self):
        return "data/test_results.xlsx"
    
    @pytest.mark.it('test returns list')
    def test_get_worksheets_returns_list(self, test_file):
        assert isinstance(get_worksheets(test_file), list)

    @pytest.mark.it('test returns list of worksheets')
    def test_get_worksheets_returns_worksheets(self, test_file):
        sheets = get_worksheets(test_file)
        for sheet in sheets:
            assert isinstance(sheet, Worksheet)

    @pytest.mark.it('only returns sheets with component numbers')
    def test_filters_sheets(self, test_file):
        sheets = get_worksheets(test_file)
        assert [sheet.title for sheet in sheets] == ["0100", "0101", "0102"]


@pytest.mark.it('get_date function tests')
class TestGetDate:
    @pytest.mark.it('Returns string')
    def test_get_date_returns_string(self):
        assert isinstance(get_date([]), str)

    @pytest.mark.it('Returns date value')
    def test_get_date_returns_date(self):
        test_file = "data/test_results.xlsx"
        sheets = get_worksheets(test_file)
        assert get_date(sheets) == "2024-08-13"

    @pytest.mark.it("Returns date if no date found")
    def test_get_date_returns_date_format(self):
        date = get_date([])
        for digit in date[0:4] + date[5:7] + date[8:]:
            assert digit.isdigit()
        assert date[4] == "-"
        assert date[7] == "-"

    @pytest.mark.it("Returns today's date if no date found")
    def test_get_date_returns_todays_date(self):
        date = get_date([])
        parsed_date = datetime.strptime(date, r"%Y-%m-%d").date()
        assert parsed_date == datetime.now().date()


@pytest.mark.it("get_titles function tests")
class TestGetTitles:
    @pytest.fixture
    def test_row(self):
        syllabus = Cell(worksheet=None, row=1, column=1, value="Syllabus")
        cand = Cell(worksheet=None, row=1, column=3, value="Candidate number")
        name = Cell(worksheet=None, row=1, column=8, value="Candidate name")
        comp_01 = Cell(worksheet=None, row=1, column=3, value="Component 01")
        comp_20 = Cell(worksheet=None, row=1, column=5, value="Component 20")
        return (syllabus, cand, name, comp_01, comp_20)

    @pytest.mark.it("Returns dictionary")
    def test_get_titles_returns_dict(self, test_row):
        titles = get_titles("0000", test_row)
        assert isinstance(titles, dict)

    @pytest.mark.it("Returns dictionary with expected keys")
    def test_get_titles_returns_expected_keys(self, test_row):
        titles = get_titles("0000", test_row)
        assert "CandidateNumber" in titles
        assert "CandidateName" in titles
        assert "Components" in titles

    @pytest.mark.it("Returns expected component values")
    def test_get_titles_returns_components(self, test_row):
        titles = get_titles("0000", test_row)
        expected = [(3, "0000/01"), (5, "0000/20")]
        assert titles["Components"] == expected


@pytest.mark.it('get_sheet_results funciton tests')
class TestGetSheetResults:
    @pytest.fixture
    def test_file(self):
        return "data/test_results.xlsx"

    @pytest.mark.it("Returns list")
    def test_get_results_returns_list(self):
        test_worksheet = Worksheet(parent=None, title="test")
        candidates = get_sheet_results(test_worksheet)
        assert isinstance(candidates, list)

    @pytest.mark.it("Returns list of dictionaries")
    def test_get_results_returns_list_of_dicts(self, test_file):
        sheets = get_worksheets(test_file)
        results = get_sheet_results(sheets[0])
        assert isinstance(results[0], dict)
        for result in results:
            assert isinstance(result, dict)

    @pytest.mark.it("Dictionaries contain candidate number and candidate name")
    def test_get_results_has_candidate_no_and_name(self, test_file):
        sheets = get_worksheets(test_file)
        results = get_sheet_results(sheets[0])
        for result in results:
            assert isinstance(result["CandidateNumber"], int)
            assert isinstance(result["CandidateName"], str)

    @pytest.mark.it("Dictionaries contain expected keys")
    def test_get_results_dict_keys(self, test_file):
        sheets = get_worksheets(test_file)
        results = get_sheet_results(sheets[0])
        for result in results:
            assert "Results" in result
            for mark in result["Results"]:
                assert mark[0] in ("0100/01",  "0100/02", "0100/03")
                assert isinstance(mark[1], int)


@pytest.mark.it('get_results function tests')
class TestGetResults:
    @pytest.fixture
    def test_sheets(self):
        test_file = "data/test_results.xlsx"
        return get_worksheets(test_file)

    @pytest.mark.it("Returns list")
    def test_get_results_returns_list(self, test_sheets):
        candidates = get_results(test_sheets)
        assert isinstance(candidates, list)

    @pytest.mark.it("Returns list of dictionaries")
    def test_get_results_returns_list_of_dicts(self, test_sheets):
        results = get_results(test_sheets)
        assert isinstance(results[0], dict)
        for result in results:
            assert isinstance(result, dict)

    @pytest.mark.it("Dictionaries contain expected keys")
    def test_get_results_dict_keys(self, test_sheets):
        candidates = get_results(test_sheets)
        for candidate in candidates:
            assert "CandidateNumber" in candidate
            assert "Results" in candidate

    @pytest.mark.it("Returns expected number of results")
    def test_get_results_returns_expected_number(self, test_sheets):
        candidates = get_results(test_sheets)
        assert len(candidates) == 105


@pytest.mark.it('Testing get_centre_number function')
class TestGetCentreNumber:
    @pytest.fixture
    def test_sheets(self):
        test_file = "data/test_results.xlsx"
        return get_worksheets(test_file)

    @pytest.mark.it('returns integer')
    def test_get_centre_number_returns_int(self, test_sheets):
        centre_number = get_centre_number(test_sheets)
        assert isinstance(centre_number, int)

    @pytest.mark.it('returns expected number')
    def test_get_centre_number_returns_expected_cn(self, test_sheets):
        centre_number = get_centre_number(test_sheets)
        assert centre_number == 10000
