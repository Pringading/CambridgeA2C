def get_role(inp: dict) -> dict:
    """Returns one role as used by get_pupil_roles and get_other_roles
    functions"""

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


def get_pupil_roles(pupils: list, centre: int, date: str, board: str) -> list:
    """Returns role information linking pupils to JCQ, exam board and centre
    returns a list."""

    roles = []
    candidates = []
    for pupil in pupils:
        if pupil["UCI"] in candidates:
            continue
        candidates.append(pupil["UCI"])
        candidate = {
            "party_1": centre,
            "ref": pupil["CandidateNumber"],
            "ref_type": "Candidate Number"
        }

        uci = {
            "party_1": "JCQ",
            "ref": pupil["UCI"],
            "ref_type": "UCI"
        }

        ao = {
            "party_1": board,
            "ref": pupil["UCI"],
            "ref_type": "AO Assigned Learner Identifier"
        }

        for role in (candidate, uci, ao):
            role["date"] = date
            role["party_2"] = pupil["UCI"]
            role["role_type"] = "Learner"
            roles.append(get_role(role))

    return roles


def get_other_roles(centre: int, board: str, date: str) -> list:
    """Gets list of roles linking JCQ to centre and exam board."""

    roles = []
    c_role = {
        "party_2": centre,
        "role_type": "Centre",
        "ref": centre,
        "ref_type": "NCN"
    }
    e_role = {
        "party_2": board,
        "role_type": "Awarding Organisation",
        "ref": board,
        "ref_type": "JCQ Awarding Organisation ID"
    }
    for role in (c_role, e_role):
        role["party_1"] = "JCQ"
        role["date"] = date
        roles.append(get_role(role))
    return roles


def get_all_roles(centre: int, board: str, pupils: list, date: int) -> list:
    """calls get_other_roles and get_pupil roles function returning a list of
    all roles."""

    roles = get_other_roles(centre, board, date)
    roles += get_pupil_roles(pupils, centre, date, board)
    return roles
