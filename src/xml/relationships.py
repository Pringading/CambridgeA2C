def get_relationships(pupils: list, organisations: list, date: str) -> list:
    """Returns list of dictionaries linking UCI numbers to JCQ, exam board id
    and centre number.

    Args: pupils(list): list of dictionaries each representing a pupil each
            has a UCI key.
        organisations (list): list of organisations
            ie. ["JCQ", centre number (int), exam board id (str)]
            eg. ["JCQ", 10000, "02"]
        date: date results are valid from in yyyy-mm-dd format
    """

    relationships = []
    for pupil in pupils:
        for org in organisations:
            relationships.append({
                "PartyRelationship_ID": {
                    "Party_Id_1st": org,
                    "Party_Id_2nd": pupil["UCI"]
                },
                "Party_Relationship_Eff_Date": date
            })
    return relationships


def get_other_relationships(centre: int, exam_board: str, date: str) -> list:
    """Returns list of dictionaries linking exam board and centre number to JCQ

    Args:
        centre (int): centre number
        exam_board (str): exam_board id "02" for cambridge
        date (str): date results are valid from in yyyy-mm-dd format
    """
    relationships = []
    orgs = [centre, exam_board]
    for org in orgs:
        relationships.append({
                "PartyRelationship_ID": {
                    "Party_Id_1st": "JCQ",
                    "Party_Id_2nd": org
                },
                "Party_Relationship_Eff_Date": date
            })
    return relationships
