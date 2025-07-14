import pytest
from src.read_excel import get_worksheets, get_results
from src.read_csv import (
    get_csv_data,
    dict_from_candidates,
    results_and_candidates
)

@pytest.fixture(scope="session")
def test_results():
    filepath = "data/Testing.xlsx"
    sheets = get_worksheets(filepath)
    results = get_results(sheets)
    csv_data = get_csv_data("data/candidates.csv")
    candidates = dict_from_candidates(csv_data)
    all_data = results_and_candidates(candidates, results)
    return all_data

@pytest.fixture(scope="session")
def test_orgs():
    return ["JCQ", 10000, "02"]