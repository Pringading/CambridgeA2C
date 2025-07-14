import pytest
from src.read_csv import (
    get_data,
    dict_from_candidates,
    results_and_candidates
)


@pytest.mark.it("Testing get_data function")
class TestGetData:
    @pytest.mark.it("Returns list")
    def test_returns_list(self):
        test_file = "data/candidates.csv"
        candidates = get_data(test_file)
        assert isinstance(candidates, list)

    @pytest.mark.it("Each item in list is dictionary")
    def test_list_of_dicts(self):
        test_file = "data/candidates.csv"
        candidates = get_data(test_file)
        for candidate in candidates:
            assert isinstance(candidate, dict)
    
    @pytest.mark.it("List is expected length")
    def test_list_is_expected_length(self):
        test_file = "data/candidates.csv"
        candidates = get_data(test_file)
        assert len(candidates) == 155

    @pytest.mark.it("Dictionaries have expected keys")
    def test_dictionaries_have_expected_keys(self):
        test_file = "data/candidates.csv"
        candidates = get_data(test_file)
        for candidate in candidates:
            assert "Date of Birth" in candidate
            assert "UCI" in candidate
            assert "Candidate Number" in candidate


@pytest.mark.skip
@pytest.mark.it("Testing dict_from_candidates_function")
class TestDictFromCandidates:
    @pytest.mark.it("Returns dictionary")
    def test_returns_dict(self):
        pass


@pytest.mark.skip
@pytest.mark.it("Testing results_and_candidates function")
class TestResultsAndCandidates:
    @pytest.mark.it("Returns list")
    def test_returns_list(self):
        pass
