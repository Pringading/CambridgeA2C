def get_outcome_cn(
    exam_board: str, 
    component: str,
    timestamp: str,
    mark: int,
    date: str
) -> dict:
    outcome_cn = {
            "QualificationElementOutcome_ID": {
                "Awarding_Organisation_Party_Id": exam_board,
                "AO_Qualification_Element_Id": component,
                "Qualification_Element_Type": "Assessable",
                "QEA_Effective_Start_Date_Time": timestamp,
                "QE_Outcome_Type": "Result",
                "QE_Outcome_Value_Type": "Scaled/Weighted Mark",
                "QE_Outcome_Date_Time": timestamp
            },
            "QE_Outcome_Value": mark,
            "QE_Outcome_Date": date,
            "QE_Outcome_Status_Type": "Issued"
        }
    return outcome_cn

def get_outcomes(pupils: list, exam_board: str, timestamp: str, date: str):
    
    outcomes = []
    for pupil in pupils:
        outcome_cns = []
        for result in pupil["Results"]:
            args = {
                "exam_board": exam_board,
                "component": result[0],
                "timestamp": timestamp,
                "mark": result[1],
                "date": date
            }
            outcome_cns.append(get_outcome_cn(**args))
        outcome = {
            "PartyRelationship_ID": {
                    "Party_Id_Originator": exam_board,
                    "Learner_Party_Id" : pupil["UCI"]
                },
            "QEOutcome_CN": outcome_cns
        }
        outcomes.append(outcome)
    return outcomes
