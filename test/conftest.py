import pytest
from src.read_excel import get_worksheets, get_results
from src.read_csv import (
    get_csv_data,
    dict_from_candidates,
    results_and_candidates
)


@pytest.fixture(scope="session")
def test_sheets():
    filepath = "data/test_results.xlsx"
    return get_worksheets(filepath)


@pytest.fixture(scope="session")
def test_results(test_sheets):
    results = get_results(test_sheets)
    csv_data = get_csv_data("data/test_candidates.csv")
    candidates = dict_from_candidates(csv_data)
    all_data = results_and_candidates(candidates, results)
    return all_data


@pytest.fixture(scope="session")
def test_orgs():
    return ["JCQ", 10000, "02"]
