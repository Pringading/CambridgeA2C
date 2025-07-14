import pytest
from src.xml.get_outcome import get_outcome_cn, get_outcomes
from src.read_excel import get_worksheets, get_results
from src.read_csv import (
    get_csv_data,
    dict_from_candidates,
    results_and_candidates
)


@pytest.mark.it('Test get_outcome_cn function')
class TestGetOutcomeCN:
    @pytest.fixture
    def test_args(self):
        args = {
            "exam_board": "02",
            "component": "0001/01",
            "timestamp": "timestamp",
            "mark": 25,
            "date": "2025-07-07"
        }
        return args
    
    @pytest.mark.it('Retuns dictionary')
    def test_returns_dictionary(self,test_args):
        outcome_cn = get_outcome_cn(**test_args)
        assert isinstance(outcome_cn, dict)

    @pytest.mark.it('Returned dictionary has expected key value pairs')
    def test_returns_dictionary_with_expected_keys(self, test_args):
        outcome_cn = get_outcome_cn(**test_args)
        assert "QualificationElementOutcome_ID" in outcome_cn
        assert outcome_cn["QE_Outcome_Value"] == 25
        assert outcome_cn["QE_Outcome_Date"] == "2025-07-07"
        assert outcome_cn["QE_Outcome_Status_Type"] == "Issued"

    @pytest.mark.it('dictionary with expected keys on QualificationElementOutcome_ID key')
    def test_nested_dictionary(self, test_args):
        outcome_cn = get_outcome_cn(**test_args)
        qual_elems = outcome_cn["QualificationElementOutcome_ID"]
        assert qual_elems["Awarding_Organisation_Party_Id"] == "02"
        assert qual_elems["AO_Qualification_Element_Id"] == "0001/01"
        assert qual_elems["Qualification_Element_Type"] == "Assessable"
        assert qual_elems["QEA_Effective_Start_Date_Time"] == "timestamp"
        assert qual_elems["QE_Outcome_Type"] == "Result"
        assert qual_elems["QE_Outcome_Value_Type"] == "Scaled/Weighted Mark"
        assert qual_elems["QE_Outcome_Date_Time"] == "timestamp"


@pytest.mark.it('Test get_outcomes function')
class TestGetOutcomes:
    @pytest.fixture(scope="class")
    def outcome_args(self):
        filepath = "data/Testing.xlsx"
        sheets = get_worksheets(filepath)
        results = get_results(sheets)
        csv_data = get_csv_data("data/candidates.csv")
        candidates = dict_from_candidates(csv_data)
        all_data = results_and_candidates(candidates, results)
        args = {
            "pupils": all_data,
            "exam_board": "02",
            "timestamp": "timestamp",
            "date": "2025-07-07"
        }
        return args

    @pytest.mark.it('Returns list')
    def test_returns_list(self, outcome_args):
        outcomes = get_outcomes(**outcome_args)
        assert isinstance(outcomes, list)
    
    @pytest.mark.it('Returns list')
    def test_returns_list(self, outcome_args):
        outcomes = get_outcomes(**outcome_args)
        assert isinstance(outcomes, list)
    
    @pytest.mark.it('List is expected length')
    def test_returns_list_of_expected_length(self, outcome_args):
        expected_length = len(outcome_args["pupils"])
        outcomes = get_outcomes(**outcome_args)
        assert len(outcomes) == expected_length
    
    @pytest.mark.it('Returns list of dictionaries')
    def test_returns_list_of_dicts(self, outcome_args):
        outcomes = get_outcomes(**outcome_args)
        for outcome in outcomes:
            assert isinstance(outcome, dict)
    
    @pytest.mark.it('Each dictionary has expected keys')
    def test_dictionaries_have_expected_keys(self, outcome_args):
        outcomes = get_outcomes(**outcome_args)
        for outcome in outcomes:
            assert "PartyRelationship_ID" in outcome
            assert "QEOutcome_CN" in outcome

    @pytest.mark.it('Dictionary with expected key value pairs on ' +
        'PartyRelationship_ID key')
    def test_dictionaries_have_expected_keys(self, outcome_args):
        pupils = outcome_args["pupils"]
        candidates = [pupil["CandidateNumber"] for pupil in pupils]
        outcomes = get_outcomes(**outcome_args)
        for outcome in outcomes:
            party = outcome["PartyRelationship_ID"]
            assert party["Party_Id_Originator"] == "02"
            assert party["Learner_Party_Id"] in candidates
    
    @pytest.mark.it('List on QEOutcome_CN key')
    def test_dictionaries_have_expected_keys(self, outcome_args):
        outcomes = get_outcomes(**outcome_args)
        for outcome in outcomes:
            assert isinstance(outcome["QEOutcome_CN"], list)
    

    @pytest.mark.it('Returns expected Results')
    def test_expected_results(self):
        pupils = []
        for num in range(3):
            pupil = {}
            pupil["CandidateNumber"] = num
            pupil["Results"] = [("000/01", 10), ("000/02", 20)]
        outcomes = get_outcomes(pupils, "", "", "")
        for outcome in outcomes:
            outcome_cns = outcome["QEOutcome_CN"]
            for cn in outcome_cns:
                mark = cn["QE_Outcome_Value"]
                qual = cn["QualificationElementOutcome_ID"]
                component = qual["AO_Qualification_Element_Id"]

                assert isinstance(mark, int)
                assert mark in (10, 20)
                assert isinstance(component, str)
                assert component in ("000/01", "000/02")