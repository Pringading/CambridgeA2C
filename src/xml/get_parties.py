def get_pupils(pupils: list) -> list:

    parties = []
    for pupil in pupils:
        parties.append(
            {
                # change from uci to candidate number
                "Party_ID": {"Party_Id": pupil["CandidateNumber"]},
                "Party_Type": "Person",

                # dict including dob and gender
                "Person": None
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
