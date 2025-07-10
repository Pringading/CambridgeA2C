def get_party_name_comp(order: int, type: str, name: str):
    name_comp = {
        "PartyNameComponent_ID": {
            "Party_Name_Component_Order": order
        },
        "Party_Name_Component_Type": type,
        "Party_Name_Component": name
    }
    return name_comp
    


def get_names():
    pass


# CandidateName Surname: Forenames