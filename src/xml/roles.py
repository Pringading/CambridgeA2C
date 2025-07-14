from copy import deepcopy

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


def get_pupil_roles(pupils: list, centre_number: int, date: str, exam_board: str):
    roles = []
    candidates = []
    for pupil in pupils:
        if pupil["CandidateNumber"] in candidates:
            continue
        candidates.append(pupil["CandidateNumber"])
        candidate = {
            "party_1": centre_number,
            "ref": pupil["CandidateNumber"],
            "ref_type": "Candidate Number"
        }
        
        uci = {
            "party_1": "JCQ",
            "ref": pupil["UCI"],
            "ref_type": "UCI"
        }

        ao = {
            "party_1": centre_number,
            "ref": pupil["UCI"],
            "ref_type": "AO Assigned Learner Identifier"
        }

        for role in (candidate, uci, ao):
            role["date"] = date
            role["party_2"] = pupil["UCI"]
            role["role_type"] = "Learner"
            roles.append(get_role(role))

    return roles


def get_other_roles():
    pass


def get_all_roles():
    pass
