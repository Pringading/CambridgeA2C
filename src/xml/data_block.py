from src.xml.get_parties import get_pupils, get_organisations
from src.xml.pupil_names import get_names
from src.xml.relationships import get_relationships, get_other_relationships
from src.xml.roles import get_all_roles
from src.xml.get_outcome import get_outcomes

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

def get_party_name_ds(results: list, date: str) -> dict:
    """Returns dictionary with party name information"""

    party_name_ds = {
        "DataBlockName": "PartyName_DS",
        "PartyName_DS": {
            "PartyName": get_names(results, date)
        }
    }
    return party_name_ds

def get_party_relationship_ds(
    results: list, organisations: list, date: str, centre: int, board: str
) -> dict:
    """Returns dictionary with party relationship information"""

    pupil_relationships = get_relationships(results, organisations, date)
    other_relationships = get_other_relationships(centre, board, date)
    party_relationship_ds = {
        "DataBlockName": "PartyRelationship_DS",
        "PartyRelationship_DS": {
            "PartyRelationship": other_relationships + pupil_relationships
        }
    }
    return party_relationship_ds

def get_party_relationship_role_ds(centre: int, board: str, results: list, date: str):
    """returns dictionary with role information"""

    roles = get_all_roles(centre, board, results, date)
    party_relationship_role_ds = {
        "DataBlockName": "PartyRelationshipRole_DS",
        "PartyRelationshipRole_DS": {
            "PartyRelationshipRole": roles
        }
    }
    return party_relationship_role_ds

def get_qe_outcome_ds():
    pass
    

def get_data_block(results: list, organisations: list, date: str, centre: int, board: str):
    data_block = [
        get_party_ds(results, organisations),
        get_party_name_ds(results, date),
        get_party_relationship_ds(results, organisations, date, centre, board),
        get_party_relationship_role_ds(centre, board, results, date),
        get_qe_outcome_ds()
    ]
    return data_block