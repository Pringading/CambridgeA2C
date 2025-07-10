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