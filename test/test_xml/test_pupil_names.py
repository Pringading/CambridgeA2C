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
    pass
