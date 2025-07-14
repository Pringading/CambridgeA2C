import pytest
from src.read_excel import get_worksheets, get_results
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
            c_num = int(c["Candidate Number"])
            assert c_num in c_dict

    @pytest.mark.it("All UCIs in dict on candidate key")
    def test_all_ucis_in_dict_on_key(self, c_list):
        c_dict = dict_from_candidates(c_list)
        for c in c_list:
            c_num = int(c["Candidate Number"])
            expected_uci = c["UCI"]
            assert c_dict[c_num]["UCI"] == expected_uci

    @pytest.mark.it("All date of births in dict on candidate key")
    def test_all_dob_in_dict_on_key(self, c_list):
        c_dict = dict_from_candidates(c_list)
        for c in c_list:
            c_num = int(c["Candidate Number"])
            expected_dob = c["Date of Birth"]
            returned_dob = c_dict[c_num]["DOB"]
            expected_dob[6:10] == returned_dob[0:4]
            expected_dob[3:5] == returned_dob[5:7]
            expected_dob[0:2] == returned_dob[8:10]


@pytest.mark.it("Testing results_and_candidates function")
class TestResultsAndCandidates:
    @pytest.fixture
    def test_args(self):
        c_list = get_csv_data("data/candidates.csv")
        c_dict = dict_from_candidates(c_list)
        sheets = get_worksheets("data/Testing.xlsx")
        results = get_results(sheets)
        return {
            "candidates": c_dict,
            "results": results

        }

    @pytest.mark.it("Returns list")
    def test_returns_list(self, test_args):
        results = results_and_candidates(**test_args)
        assert isinstance(results, list)

    @pytest.mark.it("Returns list of dicts")
    def test_returns_list_of_dicts(self, test_args):
        results = results_and_candidates(**test_args)
        for result in results:
            assert isinstance(result, dict)

    @pytest.mark.it("Returns new list")
    def test_returns_new_list(self, test_args):
        input_list = test_args["results"]
        output_list = results_and_candidates(**test_args)
        assert input_list is not output_list

    @pytest.mark.it("New list has dicts with UCI and DOB keys")
    def test_adds_uci_and_dob_keys(self, test_args):
        output_list = results_and_candidates(**test_args)
        for result in output_list:
            assert "UCI" in result
            assert "DOB" in result

    @pytest.mark.it("Input list is not mutated")
    def test_input_list_not_mutated(self, test_args):
        sheets = get_worksheets("data/Testing.xlsx")
        original_input = get_results(sheets)
        results_and_candidates(**test_args)
        assert test_args["results"] == original_input

    @pytest.mark.it("Correct data on existing keys")
    def test_correct_data_on_existing_keys(self, test_args):
        input_list = test_args["results"]
        output_list = results_and_candidates(**test_args)
        for i, result in enumerate(input_list):
            result["Results"] == output_list[i]["Results"]
            result["CandidateNumber"] == output_list[i]["CandidateNumber"]
            result["CandidateName"] == output_list[i]["CandidateName"]

    @pytest.mark.it("Correct data on new keys")
    def test_correct_data_on_new_keys(self, test_args):
        output_list = results_and_candidates(**test_args)
        c_dict = test_args["candidates"]
        for result in output_list:
            candidate = result["CandidateNumber"]
            assert result["UCI"] == c_dict[candidate]["UCI"]
            assert result["DOB"] == c_dict[candidate]["DOB"]
