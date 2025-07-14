import pytest
from src.xml.relationships import get_relationships, get_other_relationships


@pytest.mark.it('Testing get_relationships function')
class TestGetRelationships:
    @pytest.fixture(scope="class")
    def test_args(self, test_orgs, test_results):
        return {
            "pupils": test_results,
            "organisations": test_orgs,
            "date": "2025-07-07"
        }

    @pytest.mark.it("Returns list")
    def test_returns_list(self, test_args):
        relationships = get_relationships(**test_args)
        assert isinstance(relationships, list)

    @pytest.mark.it("Returns list of dictionaries")
    def test_returns_list_of_dicts(self, test_args):
        relationships = get_relationships(**test_args)
        for relationship in relationships:
            assert isinstance(relationship, dict)

    @pytest.mark.it("Returns list of expected length")
    def test_returns_list_of_expected_length(self, test_args):
        expected_length = len(test_args["pupils"])
        expected_length *= len(test_args["organisations"])
        relationships = get_relationships(**test_args)
        assert len(relationships) == expected_length

    @pytest.mark.it("Expected data on expected keys of dictioary")
    def test_expected_data_on_expected_keys(self, test_args):
        relationships = get_relationships(**test_args)
        for r in relationships:
            assert r["Party_Relationship_Eff_Date"] == "2025-07-07"
            assert isinstance(r["PartyRelationship_ID"], dict)

    @pytest.mark.it("Points to valid UCI number and organisation ID")
    def test_valid_uci_and_org(self, test_args):
        orgs = test_args["organisations"]
        ucis = [p["UCI"] for p in test_args["pupils"]]
        relationships = get_relationships(**test_args)
        for r in relationships:
            parties = r["PartyRelationship_ID"]
            assert parties["Party_Id_1st"] in orgs
            assert parties["Party_Id_2nd"] in ucis


@pytest.mark.it('Testing get_other_relationships function')
class TestGetOtherRelationships:
    @pytest.fixture
    def test_args(self):
        return {
            "centre": 10000,
            "exam_board": "02",
            "date": "2025-07-07"
        }

    @pytest.mark.it("Returns list")
    def test_returns_list(self, test_args):
        relationships = get_other_relationships(**test_args)
        assert isinstance(relationships, list)

    @pytest.mark.it("Returns list with 2 dictinoaries")
    def test_returns_list_of_two_dicts(self, test_args):
        relationships = get_other_relationships(**test_args)
        assert len(relationships) == 2
        for r in relationships:
            assert isinstance(r, dict)

    @pytest.mark.it("Expected data on expected keys of dictioary")
    def test_expected_data_on_expected_keys(self, test_args):
        relationships = get_other_relationships(**test_args)
        for r in relationships:
            assert r["Party_Relationship_Eff_Date"] == "2025-07-07"
            assert isinstance(r["PartyRelationship_ID"], dict)

    @pytest.mark.it("Points to valid organisation ID")
    def test_valid_org(self, test_args):
        orgs = [10000, "02"]
        relationships = get_other_relationships(**test_args)
        for i, r in enumerate(relationships):
            parties = r["PartyRelationship_ID"]
            assert parties["Party_Id_1st"] == "JCQ"
            assert parties["Party_Id_2nd"] == orgs[i]
