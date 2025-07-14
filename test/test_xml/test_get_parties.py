import pytest
from src.xml.get_parties import get_pupils, get_organisations


@pytest.mark.it('Testing get_pupils function')
class TestGetPupils:
    """tests use test_results fixture from conftest."""
    
    @pytest.mark.it('Returns list')
    def test_get_pupils_returns_list(self):
        parties = get_pupils([])
        assert isinstance(parties, list)

    @pytest.mark.it('Returned list length same as input list length')
    def test_list_length(self, test_results):
        candidates = []
        for c in test_results:
            if c["UCI"] not in candidates:
                candidates.append(c["UCI"])
        parties = get_pupils(test_results)
        assert len(parties) == len(candidates)

    @pytest.mark.it('Returns list of dictionaries')
    def test_list_of_dicts(self, test_results):
        parties = get_pupils(test_results)
        for party in parties:
            assert isinstance(party, dict)

    @pytest.mark.it('Each dictionary has expected key value pairs')
    def test_expected_keys_(self, test_results):
        parties = get_pupils(test_results)
        for party in parties:
            assert "Party_ID" in party
            assert party["Party_Type"] == "Person"
            assert isinstance(party["Person"], dict)

    @pytest.mark.it('Dictionary with Party ID on Candidate')
    def test_party_id_contains_expected(self, test_results):
        parties = get_pupils(test_results)
        for party in parties:
            party_id = party["Party_ID"]
            assert isinstance(party_id, dict)
            assert "Party_Id" in party_id
        
    @pytest.mark.it("No duplicates in returned list")
    def test_no_duplicates_in_list(self, test_results):
        parties = get_pupils(test_results)
        for i, party in enumerate(parties):
            assert party not in parties[i + 1: ]


@pytest.mark.it('Testing get organisations function')
class TestGetOrganisations:
    @pytest.fixture
    def test_orgs(self):
        return ["a", "b", "c"]

    @pytest.mark.it('Returns list')
    def test_returns_list(self):
        org_parties = get_organisations([])
        assert isinstance(org_parties, list)

    @pytest.mark.it('List of dictionaries')
    def test_returns_list_of_dictionaries(self, test_orgs):
        org_parties = get_organisations(test_orgs)
        for org in org_parties:
            assert isinstance(org, dict)

    @pytest.mark.it('Dictionary contains expected key value pairs')
    def test_dictionary_contains_expected_key_value_pairs(self, test_orgs):
        org_parties = get_organisations(test_orgs)
        for org in org_parties:
            assert "Party_ID" in org
            assert org["Party_Type"] == "Organisation"
            assert org["Organisation"] is None

    @pytest.mark.it('Organisation on Party_Id key')
    def test_organisation_on_party_id_key(self, test_orgs):
        org_parties = get_organisations(test_orgs)
        for i, org in enumerate(org_parties):
            party_id = org["Party_ID"]["Party_Id"]
            assert party_id == test_orgs[i]
