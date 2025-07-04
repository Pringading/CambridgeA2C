import pytest
from src.read_excel import get_date


@pytest.fixture
def test_file():
    return "data/Testing.xlsx"


@pytest.mark.it('get_date function tests')
class TestGetDate:
    @pytest.mark.it('Returns string')
    def test_get_date_returns_string(self):
        assert isinstance(get_date([]), str)
