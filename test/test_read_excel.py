import pytest
from openpyxl.worksheet.worksheet import Worksheet
from src.read_excel import get_worksheets, get_date


@pytest.mark.it('get_worksheets function tests')
class TestGetWorksheets:
    @pytest.mark.it('test returns list')
    def test_get_worksheets_returns_list(self):
        test_file = "data/Testing.xlsx"
        assert isinstance(get_worksheets(test_file), list)

    @pytest.mark.it('test returns list of worksheets')
    def test_get_worksheets_returns_worksheets(self):
        test_file = "data/Testing.xlsx"
        sheets = get_worksheets(test_file)
        for sheet in sheets:
            assert isinstance(sheet, Worksheet)
    
    @pytest.mark.it('only returns sheets with component numbers')
    def test_filters_sheets(self):
        test_file = "data/Testing.xlsx"
        sheets = get_worksheets(test_file)
        assert [sheet.title for sheet in sheets] == ["0100", "0101", "0102"]


@pytest.mark.it('get_date function tests')
class TestGetDate:
    @pytest.mark.it('Returns string')
    def test_get_date_returns_string(self):
        assert isinstance(get_date([]), str)
