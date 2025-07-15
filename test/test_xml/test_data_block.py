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
    @pytest.fixture(scope="class")
    def test_args(self, test_results):        
        return {
            "results": test_results,
            "date": "2025-07-07",
            "centre": 10000,
            "board": "02"
        }

    @pytest.mark.it("Returns dict")
    def test_returns_dict(self, test_args):
        roles = get_party_relationship_role_ds(**test_args)
        assert isinstance(roles, dict)

    @pytest.mark.it("Dictionary has expected key-value pairs")
    def test_dictionary_has_expected_key_values(self, test_args):
        roles = get_party_relationship_role_ds(**test_args)
        r_list = roles["PartyRelationshipRole_DS"]["PartyRelationshipRole"]
        assert roles["DataBlockName"] == "PartyRelationshipRole_DS"
        assert isinstance(r_list, list)

    @patch("src.xml.data_block.get_all_roles")
    @pytest.mark.it("Calls get_all_roles function")
    def test_calls_get_all_roles(self, mock_roles, test_args):
        mock_roles = Mock(return_value=[])
        get_party_relationship_role_ds(**test_args)
        mock_roles.assert_called_once


@pytest.mark.it('Testing get_qe_outcome_ds function')
class TestGetQEOutcomeDS:
    @pytest.fixture(scope="class")
    def test_args(self, test_results):        
        return {
            "results": test_results,
            "date": "2025-07-07",
            "board": "02",
            "timestamp": "timestamp"
        }

    @pytest.mark.it("Returns dict")
    def test_returns_dict(self, test_args):
        roles = get_qe_outcome_ds(**test_args)
        assert isinstance(roles, dict)

    @pytest.mark.it("Dictionary has expected key-value pairs")
    def test_dictionary_has_expected_key_values(self, test_args):
        outcomes = get_qe_outcome_ds(**test_args)
        o_list = outcomes["QEOutcome_DS"]["QEOutcome"]
        assert outcomes["DataBlockName"] == "QEOutcome_DS"
        assert isinstance(o_list, list)

    @patch("src.xml.data_block.get_outcomes")
    @pytest.mark.it("Calls get_outcomes function")
    def test_calls_get_outcomes(self, mock_outcomes, test_args):
        mock_outcomes = Mock(return_value=[])
        get_qe_outcome_ds(**test_args)
        mock_outcomes.assert_called_once


@pytest.mark.it('Testing get_data_block function')
class TestDataBlockDS:
    @pytest.fixture(scope="class")
    def test_args(self, test_sheets):        
        return {
            "sheets": test_sheets,
            "centre": 10000,
            "board": "02",
            "timestamp": "timestamp",
            "csv_filepath": "data/candidates.csv"
        }

    @pytest.mark.it("Returns list")
    def test_returns_list(self, test_args):
        blocks = get_data_block(**test_args)
        assert isinstance(blocks, list)

    @pytest.mark.it("List length is 5")
    def test_list_length_is_5(self, test_args):
        blocks = get_data_block(**test_args)
        assert len(blocks) == 5

    @patch("src.xml.data_block.get_party_ds")
    @pytest.mark.it("Calls get_party_ds function")
    def test_calls_get_party_ds(self, mock_party, test_args):
        mock_party = Mock(return_value=[])
        get_data_block(**test_args)
        mock_party.assert_called_once
    
    @patch("src.xml.data_block.get_party_name_ds")
    @pytest.mark.it("Calls get_party_name_ds function")
    def test_calls_get_party_name_ds(self, mock_names, test_args):
        mock_names = Mock(return_value=[])
        get_data_block(**test_args)
        mock_names.assert_called_once
    
    @patch("src.xml.data_block.get_outcomes")
    @pytest.mark.it("Calls get_outcomes function")
    def test_calls_get_outcomes(self, mock_outcomes, test_args):
        mock_outcomes = Mock(return_value=[])
        get_data_block(**test_args)
        mock_outcomes.assert_called_once
    
    @patch("src.xml.data_block.get_party_relationship_ds")
    @pytest.mark.it("Calls get_party_relationship_ds function")
    def test_calls_get_party_relationship_ds(self, mock_relationships, test_args):
        mock_relationships = Mock(return_value=[])
        get_data_block(**test_args)
        mock_relationships.assert_called_once
    
    @patch("src.xml.data_block.get_party_relationship_role_ds")
    @pytest.mark.it("Calls get_party_relationship_role_ds function")
    def test_calls_get_party_relationship_role_ds(self, mock_roles, test_args):
        mock_roles = Mock(return_value=[])
        get_data_block(**test_args)
        mock_roles.assert_called_once
    
    @patch("src.xml.data_block.get_qe_outcome_ds")
    @pytest.mark.it("Calls get_qe_outcome_ds function")
    def test_calls_get_qe_outcome_ds(self, mock_outcomes, test_args):
        mock_outcomes = Mock(return_value=[])
        get_data_block(**test_args)
        mock_outcomes.assert_called_once

    @patch("src.xml.data_block.get_date")
    @pytest.mark.it("Calls get_date function")
    def test_calls_get_date_function(self, mock_date, test_args):
        mock_date = Mock(return_value="2025-07-07")
        get_data_block(**test_args)
        mock_date.assert_called_once
    
    @patch("src.xml.data_block.get_all_data")
    @pytest.mark.it("Calls get_all_data function")
    def test_calls_get_all_data_function(self, mock_data, test_args):
        mock_data = Mock(return_value=[])
        get_data_block(**test_args)
        mock_data.assert_called_once
