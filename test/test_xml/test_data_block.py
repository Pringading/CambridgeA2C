import pytest
from unittest.mock import patch, Mock
from src.xml.data_block import (
    get_party_ds,
    get_party_name_ds,
    get_party_relationship_ds,
    get_party_relationship_role_ds,
    get_qe_outcome_ds,
    get_data_block
)


@pytest.mark.it('Testing get_party_ds function')
class TestGetPartyDS:
    @pytest.fixture(scope="class")
    def test_args(self, test_results, test_orgs):        
        return {
            "pupils": test_results,
            "organisations": test_orgs
        }

    @pytest.mark.it("Returns dict")
    def test_returns_dict(self, test_args):
        party_ds = get_party_ds(**test_args)
        assert isinstance(party_ds, dict)
    
    @pytest.mark.it("Dictionary has expected key-value pairs")
    def test_dictionary_has_expected_key_values(self, test_args):
        party_ds = get_party_ds(**test_args)
        assert party_ds["DataBlockName"] == "Party_DS"
        assert isinstance(party_ds["Party_DS"]["Party"], list)
    
    @patch("src.xml.data_block.get_pupils")
    @pytest.mark.it("Calls get_pupils function")
    def test_calls_get_pupils(self, mock_pupils, test_args):
        mock_pupils = Mock(return_value=[])
        get_party_ds(**test_args)
        mock_pupils.assert_called_once
    
    @patch("src.xml.data_block.get_pupils")
    @pytest.mark.it("Calls get_organisations function")
    def test_calls_get_organisations(self, mock_orgs, test_args):
        mock_orgs = Mock(return_value=[])
        get_party_ds(**test_args)
        mock_orgs.assert_called_once


@pytest.mark.it('Testing get_party_name_ds function')
class TestGetPartyNameDS:
    pass


@pytest.mark.it('Testing get_party_relationship_ds function')
class TestGetPartyRelationshipDS:
    pass


@pytest.mark.it('Testing get_party_relationship_role_ds function')
class TestPartyRelationshipRoleDS:
    pass


@pytest.mark.it('Testing get_qe_outcome_ds function')
class TestGetQEOutcomeDS:
    pass


@pytest.mark.it('Testing get_data_block function')
class TestDataBlockDS:
    pass
