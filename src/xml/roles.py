def get_role(inp: dict):
    role = {
        "PartyRelationshipRole_ID": {
            "Party_Id_1st": inp["party_1"],
            "Party_Id_2nd": inp["party_2"],
            "Party_Role_Type": inp["role_type"],
            "Party_Role_Effective_Date": inp["date"],
        },
        "Relationship_Reference": inp["ref"],
        "Party_RR_Reference_Type": inp["ref_type"]
    }
    return role


def get_pupil_roles():
    pass


def get_other_roles():
    pass


def get_all_roles():
    pass
