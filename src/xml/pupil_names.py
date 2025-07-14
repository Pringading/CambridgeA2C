def get_party_name_comp(order: int, type: str, name: str):
    name_comp = {
        "PartyNameComponent_ID": {
            "Party_Name_Component_Order": order
        },
        "Party_Name_Component_Type": type,
        "Party_Name_Component": name
    }
    return name_comp
    

def get_names(pupils: list, date: str):
    name_list = []
    candidates = []
    for pupil in pupils:
        if pupil["UCI"] in candidates:
            continue
        candidates.append(pupil["UCI"])
        surname, forename = pupil["CandidateName"].split(": ")
        forename_comp = get_party_name_comp(1, "Given", forename)
        surname_comp = get_party_name_comp(2, "Family", surname)
        name_list.append({
            "Party_ID": {"Party_Id": pupil["UCI"]},
            "PartyName_CN": {
                "PartyName_ID": {
                    "Party_Name_Type": "Full",
                    "Party_Name_Effective_Date": date
                },
                
                "PartyNameComponent": [forename_comp, surname_comp]
            }
        })
    return name_list
