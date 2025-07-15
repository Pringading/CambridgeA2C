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
            "results": test_results,
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
    @pytest.fixture(scope="class")
    def test_args(self, test_results, test_orgs):        
        return {
            "results": test_results,
            "date": "2025-07-07"
        }

    @pytest.mark.it("Returns dict")
    def test_returns_dict(self, test_args):
        party_names = get_party_name_ds(**test_args)
        assert isinstance(party_names, dict)
    
    @pytest.mark.it("Dictionary has expected key-value pairs")
    def test_dictionary_has_expected_key_values(self, test_args):
        party_names = get_party_name_ds(**test_args)
        assert party_names["DataBlockName"] == "PartyName_DS"
        assert isinstance(party_names["PartyName_DS"]["PartyName"], list)

    @patch("src.xml.data_block.get_names")
    @pytest.mark.it("Calls get_names function")
    def test_calls_get_names_func(self, mock_names, test_args):
        mock_names = Mock(return_value=[])
        get_party_name_ds(**test_args)
        mock_names.assert_called_once


@pytest.mark.it('Testing get_party_relationship_ds function')
class TestGetPartyRelationshipDS:
    @pytest.fixture(scope="class")
    def test_args(self, test_results, test_orgs):        
        return {
            "results": test_results,
            "organisations": test_orgs,
            "date": "2025-07-07",
            "centre": 10000,
            "board": "02"
        }

    @pytest.mark.it("Returns dict")
    def test_returns_dict(self, test_args):
        relationships = get_party_relationship_ds(**test_args)
        assert isinstance(relationships, dict)
    
    @pytest.mark.it("Dictionary has expected key-value pairs")
    def test_dictionary_has_expected_key_values(self, test_args):
        relationships = get_party_relationship_ds(**test_args)
        r_list = relationships["PartyRelationship_DS"]["PartyRelationship"]
        assert relationships["DataBlockName"] == "PartyRelationship_DS"
        assert isinstance(r_list, list)

    @patch("src.xml.data_block.get_relationships")
    @pytest.mark.it("Calls get_relationships function")
    def test_calls_get_relationsihps(self, mock_re, test_args):
        mock_re = Mock(return_value=[])
        get_party_relationship_ds(**test_args)
        mock_re.assert_called_once

    @patch("src.xml.data_block.get_other_relationships")
    @pytest.mark.it("Calls get_other_relationships function")
    def test_calls_get_other_relationships(self, mock_other, test_args):
        mock_other = Mock(return_value=[])
        get_party_relationship_ds(**test_args)
        mock_other.assert_called_once


@pytest.mark.it('Testing get_party_relationship_role_ds function')
class TestPartyRelationshipRoleDS:
    pass


@pytest.mark.it('Testing get_qe_outcome_ds function')
class TestGetQEOutcomeDS:
    pass


@pytest.mark.it('Testing get_data_block function')
class TestDataBlockDS:
    pass
