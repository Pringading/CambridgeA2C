import pytest
from src.xml.get_pupils import get_pupils
from src.read_excel import get_worksheets, get_results


@pytest.fixture
def test_pupils():
    filepath = "data/Testing.xlsx"
    sheets = get_worksheets(filepath)
    results = get_results(sheets)
    return results


@pytest.mark.it('Returns list')
def test_get_pupils_returns_list():
    parties = get_pupils([])
    assert isinstance(parties, list)


@pytest.mark.it('Returned list length same as input list length')
def test_list_length(test_pupils):
    expected_length = len(test_pupils)
    parties = get_pupils(test_pupils)
    assert len(parties) == expected_length


@pytest.mark.it('Returns list of dictionaries')
def test_list_of_dicts(test_pupils):
    parties = get_pupils(test_pupils)
    for party in parties:
        assert isinstance(party, dict)


@pytest.mark.it('Each dictionary has expected key value pairs')
def test_expected_keys_(test_pupils):
    parties = get_pupils(test_pupils)
    for party in parties:
        assert "Party_ID" in party
        assert party["Party_Type"] == "Person"
        assert party["Person"] == None


@pytest.mark.it('Dictionary with Party ID on Candidate')
def test_party_id_contains_expected(test_pupils):
    parties = get_pupils(test_pupils)
    for party in parties:
        party_id = party["Party_ID"]
        assert isinstance(party_id, dict)
        assert "Party_Id" in party_id
