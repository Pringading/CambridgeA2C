def get_relationships(pupils: list, organisations: list, date: str) -> list:
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


def get_other_relationships():
    pass
