import pytest
from src.xml.roles import get_role, get_pupil_roles, get_all_roles


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
    pass


@pytest.mark.it('Testing get_all_roles_function')
class TestGetAllRoles:
    pass
