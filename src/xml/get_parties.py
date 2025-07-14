def get_pupils(pupils: list) -> list:

    parties = []
    candidates = []
    for pupil in pupils:
        if pupil["UCI"] in candidates:
            continue
        candidates.append(pupil["UCI"])
        parties.append(
            {
                "Party_ID": {"Party_Id": pupil["UCI"]},
                "Party_Type": "Person",

                "Person": {
                    "Date_Of_Birth": pupil["DOB"],
                    # "Legal_Sex_Type": "Female"
                }
            }
        )
    return parties


def get_organisations(orgs: list):
    org_parties = [{
            "Party_ID": {"Party_Id": org},
            "Party_Type": "Organisation",
            "Organisation": None
        } for org in orgs]
    return org_parties
