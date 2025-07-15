from src.xml.get_parties import get_pupils, get_organisations
from src.xml.pupil_names import get_names

def get_party_ds(pupils: list, organisations: list) -> dict:
    pupil_parties = get_pupils(pupils)
    org_parties = get_organisations(organisations)
    party_ds = {
        "DataBlockName": "Party_DS",
        "Party_DS": {
            "Party": org_parties + pupil_parties
        }
    }
    return party_ds

def get_party_name_ds():
    pass

def get_party_relationship_ds():
    pass

def get_party_relationship_role_ds():
    pass

def get_qe_outcome_ds():
    pass

def get_data_block():
    # args: centre number, exam board
    pass