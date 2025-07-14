import pytest
from src.read_csv import (
    get_csv_data,
    dict_from_candidates,
    results_and_candidates
)


@pytest.mark.it("Testing get_data function")
class TestGetData:
    @pytest.mark.it("Returns list")
    def test_returns_list(self):
        test_file = "data/candidates.csv"
        candidates = get_csv_data(test_file)
        assert isinstance(candidates, list)

    @pytest.mark.it("Each item in list is dictionary")
    def test_list_of_dicts(self):
        test_file = "data/candidates.csv"
        candidates = get_csv_data(test_file)
        for candidate in candidates:
            assert isinstance(candidate, dict)
    
    @pytest.mark.it("List is expected length")
    def test_list_is_expected_length(self):
        test_file = "data/candidates.csv"
        candidates = get_csv_data(test_file)
        assert len(candidates) == 148

    @pytest.mark.it("Dictionaries have expected keys")
    def test_dictionaries_have_expected_keys(self):
        test_file = "data/candidates.csv"
        candidates = get_csv_data(test_file)
        for candidate in candidates:
            assert "Date of Birth" in candidate
            assert "UCI" in candidate
            assert "Candidate Number" in candidate


@pytest.mark.it("Testing dict_from_candidates_function")
class TestDictFromCandidates:
    @pytest.fixture
    def c_list(self):
        test_file = "data/candidates.csv"
        candidates = get_csv_data(test_file)
        return candidates
    
    @pytest.mark.it("Returns dictionary")
    def test_returns_dict(self, c_list):
        c_dict = dict_from_candidates(c_list)
        assert isinstance(c_dict, dict)
    
    @pytest.mark.it("All candidates in input list are keys in dict")
    def test_all_candidates_keys_in_dict(self, c_list):
        c_dict = dict_from_candidates(c_list)
        for c in c_list:
            assert c["Candidate Number"] in c_dict
    
    @pytest.mark.it("All UCIs in dict on candidate key")
    def test_all_ucis_in_dict_on_key(self, c_list):
        c_dict = dict_from_candidates(c_list)
        for c in c_list:
            c_num = c["Candidate Number"]
            expected_uci = c["UCI"]
            assert c_dict[c_num]["UCI"] == expected_uci
        
    @pytest.mark.it("All date of births in dict on candidate key")
    def test_all_dob_in_dict_on_key(self, c_list):
        c_dict = dict_from_candidates(c_list)
        for c in c_list:
            c_num = c["Candidate Number"]
            expected_dob = c["Date of Birth"]
            assert c_dict[c_num]["DOB"] == expected_dob


@pytest.mark.it("Testing results_and_candidates function")
class TestResultsAndCandidates:
    @pytest.mark.it("Returns list")
    def test_returns_list(self):
        pass
