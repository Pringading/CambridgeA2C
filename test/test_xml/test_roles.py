import pytest
from src.xml.roles import get_role, get_pupil_roles, get_all_roles
from unittest.mock import Mock, patch

@pytest.mark.it('Tesing get_role function')
class TestGetRole:
    @pytest.fixture
    def test_args(self):
        return {
            "party_1": 10000,
            "party_2": "100000251000A",
            "role_type": "Learner",
            "date": "2025-07-07",
            "ref": 1000,
            "ref_type": "Candidate Number"
        }

    @pytest.mark.it("Returns dictionary")
    def test_returns_dict(self, test_args):
        role = get_role(test_args)
        assert isinstance(role, dict)

    @pytest.mark.it("Dictionary has expected key-value pairs")
    def test_has_expected_key_values(self, test_args):
        role = get_role(test_args)
        assert isinstance(role["PartyRelationshipRole_ID"], dict)
        assert role["Relationship_Reference"] == 1000
        assert role["Party_RR_Reference_Type"] == "Candidate Number"

    @pytest.mark.it("Dictionary has expected key-value pairs on " +
        "PartyRelationshipRole_ID")
    def test_has_expected_key_values(self, test_args):
        role = get_role(test_args)
        role_id = role["PartyRelationshipRole_ID"]
        assert role_id["Party_Id_1st"] == 10000
        assert role_id["Party_Id_2nd"] == "100000251000A"
        assert role_id["Party_Role_Type"] == "Learner"
        assert role_id["Party_Role_Effective_Date"] == "2025-07-07"


@pytest.mark.it('Testing get_pupil_roles function')
class TestGetPupilRoles:
    @pytest.fixture(scope="class")
    def test_args(self, test_results):
        return {
            "pupils": test_results,
            "centre_number": 10000,
            "date": "2025-07-07",
            "exam_board": "02"
        }

    @pytest.mark.it("Returns list")
    def test_returns_list(self, test_args):
        roles = get_pupil_roles(**test_args)
        assert isinstance(roles, list)

    @pytest.mark.it("Returns list of dictionaries")
    def test_returns_list_of_dicts(self, test_args):
        roles = get_pupil_roles(**test_args)
        for role in roles:
            assert isinstance(role, dict)

    @pytest.mark.it("No duplicates in list")
    def test_no_duplicates(self, test_args):
        roles = get_pupil_roles(**test_args)
        for i, role in enumerate(roles):
            assert role not in roles[i+ 1:]

    @pytest.mark.it("Assert get_role is called expected number of times")
    def test_get_role_called(self, test_args):
        mock_get = Mock(return_value={})
        candidates = []
        for pupil in test_args["pupils"]:
            if pupil["CandidateNumber"] not in candidates:
                candidates.append(pupil["CandidateNumber"])
        expected_calls = len(candidates) * 3
        with patch('src.xml.roles.get_role') as mock_get:
            mock_response = Mock()
            mock_get.return_value = mock_response
            get_pupil_roles(**test_args)
            assert mock_get.call_count == expected_calls


@pytest.mark.it('Testing get_all_roles_function')
class TestGetOtherRoles:
    pass

@pytest.mark.it('Testing get_all_roles_function')
class TestGetAllRoles:
    pass
