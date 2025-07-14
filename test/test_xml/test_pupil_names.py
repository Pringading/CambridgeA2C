import pytest
from src.xml.pupil_names import get_party_name_comp, get_names

@pytest.mark.it('Testing get_party_name_comp function')
class TestGetPartyNameComp:
    @pytest.fixture
    def comp_args(self):
        args = {
            "order": 3,
            "type": "Custom",
            "name": "candidate-name"
        }
        return args
    
    @pytest.mark.it('Returns dictionary')
    def test_returns_dict(self, comp_args):
        name_comp = get_party_name_comp(**comp_args)
        assert isinstance(name_comp, dict)
    
    @pytest.mark.it('Dictionary contains expected key-value pairs')
    def test_dict_has_expected_keys(self, comp_args):
        name_comp = get_party_name_comp(**comp_args)
        assert "PartyNameComponent_ID" in name_comp
        assert name_comp["Party_Name_Component_Type"] == "Custom"
        assert name_comp["Party_Name_Component"] == "candidate-name"

    @pytest.mark.it('Dictionary contains expected name component order')
    def test_expected_name_component_order(self, comp_args):
        name_comp = get_party_name_comp(**comp_args)
        name_comp_id = name_comp["PartyNameComponent_ID"]
        assert name_comp_id["Party_Name_Component_Order"] == 3


@pytest.mark.it('Testing get_names function')
class TestGetNames:
    @pytest.fixture(scope="class")
    def names_args(self, test_results):
        args = {
            "pupils": test_results,
            "date": "2025-07-07"
        }
        return args

    @pytest.mark.it('Returns list')
    def test_returns_list(self):
        names = get_names([], "")
        assert isinstance(names, list)

    @pytest.mark.it('Returns list of dictionaries')
    def test_returns_list_of_dicts(self, names_args):
        names = get_names(**names_args)
        for name in names:
            assert isinstance(name, dict)

    @pytest.mark.it('List is expected length')
    def test_list_is_expected_length(self, names_args):
        candidates = []
        for c in names_args["pupils"]:
            if c["UCI"] not in candidates:
                candidates.append(c["UCI"])
        names = get_names(**names_args)
        assert len(names) == len(candidates)

    @pytest.mark.it('Each dictionary has expected keys')
    def test_dictionary_has_expected_keys(self, names_args):
        expected_length = len(names_args["pupils"])
        names = get_names(**names_args)
        assert len(names) == expected_length

    @pytest.mark.it('Each dictionary has expected keys')
    def test_dictionary_has_expected_keys(self, names_args):
        names = get_names(**names_args)
        for name in names:
            assert "Party_ID" in name
            assert "PartyName_CN" in name

    @pytest.mark.it('Each dictionary correct party id')
    def test_dictionary_has_correct_party_id(self, names_args):
        pupils = names_args["pupils"]
        names = get_names(**names_args)
        for i, name in enumerate(names):
            party_id = name["Party_ID"]["Party_Id"]
            assert party_id == pupils[i]["UCI"]

    @pytest.mark.it('Each dictionary correct partyname_cn')
    def test_dictionary_has_correct_party_name_cn(self, names_args):
        names = get_names(**names_args)
        for name in names:
            partyname_id = name["PartyName_CN"]["PartyName_ID"]
            assert partyname_id["Party_Name_Type"] == "Full"
            assert partyname_id["Party_Name_Effective_Date"] == "2025-07-07"
        
    @pytest.mark.it("Each dictionary contains expected names")
    def test_dictionary_containd_expected_names(self, names_args):
        input_names = names_args["pupils"]
        names = get_names(**names_args)
        for i, name in enumerate(names):
            input_name = input_names[i]["CandidateName"]
            components = name["PartyName_CN"]["PartyNameComponent"]
            for comp in components:
                assert comp["Party_Name_Component"] in input_name
    
    @pytest.mark.it("Test no duplicates in returned list")
    def test_no_duplicates_in_list(self, names_args):
        names = get_names(**names_args)
        for i, name in enumerate(names):
            assert name not in names[i + 1: ]