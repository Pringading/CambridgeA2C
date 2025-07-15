from src.xml.get_parties import get_pupils, get_organisations
from src.xml.pupil_names import get_names

def get_party_ds(results: list, organisations: list) -> dict:
    """returns dictionary with party information"""

    pupil_parties = get_pupils(results)
    org_parties = get_organisations(organisations)
    party_ds = {
        "DataBlockName": "Party_DS",
        "Party_DS": {
            "Party": org_parties + pupil_parties
        }
    }
    return party_ds

def get_party_name_ds(results: list, date: str):
    """Returns dictionary with party name information"""

    party_name_ds = {
        "DataBlockName": "PartyName_DS",
        "PartyName_DS": {
            "PartyName": get_names(results, date)
        }
    }
    return party_name_ds

def get_party_relationship_ds():
    pass

def get_party_relationship_role_ds():
    pass

def get_qe_outcome_ds():
    pass

def get_data_block():
    # args: centre number, exam board
    pass