from src.xml.get_parties import get_pupils, get_organisations
from src.xml.pupil_names import get_names
from src.xml.relationships import get_relationships, get_other_relationships
from src.xml.roles import get_all_roles
from src.xml.get_outcome import get_outcomes
from src.read_csv import get_all_data
from src.read_excel import get_date


def get_party_ds(results: list, organisations: list) -> dict:
    """returns dictionary with party information.

    pupil info from get_pupils function from src/xml/get_parties.py
    organisation info from get_organisations function from
        src/xml/get_parties.py

    Args:
        results(list): list of candidates, with one dictionary per candidates,
            duplicates will be filtered.
        organisations(list): list of organisation ids [JCQ, centre, exam_board]

    Returns:
        dictionary with party information to be written to xml in mock A2C
        file.
    """

    pupil_parties = get_pupils(results)
    org_parties = get_organisations(organisations)
    party_ds = {
        "DataBlockName": "Party_DS",
        "Party_DS": {
            "Party": org_parties + pupil_parties
        }
    }
    return party_ds


def get_party_name_ds(results: list, date: str) -> dict:
    """Returns dictionary with party name information

    names info from get_names function from src/xml/pupil_names.py

    Args:
        results(list): list of candidates, with one dictionary per candidates,
            duplicates will be filtered.
        date(str): date results are valid from in "yyyy-mm-dd" format.

    Returns:
        dictionary with party name information to be written to xml in mock A2C
        file.
    """

    party_name_ds = {
        "DataBlockName": "PartyName_DS",
        "PartyName_DS": {
            "PartyName": get_names(results, date)
        }
    }
    return party_name_ds


def get_party_relationship_ds(
    results: list, organisations: list, date: str, centre: int, board: str
) -> dict:
    """Returns dictionary with party relationship information

    pupil info from get_relationships function from src/xml/relationships.py
    organisation info from get_other_relationships function from
        src/xml/relationships.py

    Args:
        results(list): list of candidates, with one dictionary per candidates,
            duplicates will be filtered.
        organisations(list): list of organisation ids [JCQ, centre, exam_board]
        date(str): date results are valid from in "yyyy-mm-dd" format.
        centre(int): centre number
        board(str): exam board identifier "02" for Cambridge International

    Returns:
        dictionary with relationship information to be written to xml in mock
        A2C file.
    """

    pupil_relationships = get_relationships(results, organisations, date)
    other_relationships = get_other_relationships(centre, board, date)
    party_relationship_ds = {
        "DataBlockName": "PartyRelationship_DS",
        "PartyRelationship_DS": {
            "PartyRelationship": other_relationships + pupil_relationships
        }
    }
    return party_relationship_ds


def get_party_relationship_role_ds(
    centre: int, board: str, results: list, date: str
) -> dict:
    """returns dictionary with role information.

    Args:
        centre(int): centre number
        board(str): exam board identifier "02" for Cambridge International
        results(list): list of candidates, with one dictionary per candidates,
            duplicates will be filtered.
        date(str): date results are valid from in "yyyy-mm-dd" format.

    Returns:
        dictionary with role information to be written to xml in mock A2C
        file.
    """

    roles = get_all_roles(centre, board, results, date)
    party_relationship_role_ds = {
        "DataBlockName": "PartyRelationshipRole_DS",
        "PartyRelationshipRole_DS": {
            "PartyRelationshipRole": roles
        }
    }
    return party_relationship_role_ds


def get_qe_outcome_ds(
    results: list, board: str, timestamp: str, date: str
) -> dict:
    """Returns dictionary with outcome information.

    Args:
        results(list): list of candidate results with dictionary for each
            candidate/syllabus.
        board(str): exam board id "02" for Cambridge International
        timestamp(str): timestamp in isoformat with timezone
        date(str): date results are valid from in yyyy-mm-dd format.

    Returns:
        dictionary with outcome information to be written to xml in mock A2C
        file.
    """

    outcomes = get_outcomes(results, board, timestamp, date)
    qe_outcome_ds = {
        "DataBlockName": "QEOutcome_DS",
        "QEOutcome_DS": {
            "QEOutcome": outcomes
        }
    }
    return qe_outcome_ds


def get_data_block(
    sheets: list, centre: int, board: str, timestamp: str, csv_filepath: str
) -> list:
    """returns list with all information contained in data block.

    Args:
        sheets(list): List of excel sheets data with cambridge results info
        centre(int): centre number
        board(int): exam board identifier ("02" for cambridge)
        timestamp(str): timestamp in isoformat with timezone
        csv_filepath(str): relative path to csv file with candidate info:
            "UCI", "Candidate Number" & "Date of Birth"

    Returns:
        list of information in data block to be written to mock A2C file.
    """

    organisations = ["JCQ", centre, board]
    date = get_date(sheets)
    results = get_all_data(sheets, csv_filepath)

    data_block = [
        get_party_ds(results, organisations),
        get_party_name_ds(results, date),
        get_party_relationship_ds(results, organisations, date, centre, board),
        get_party_relationship_role_ds(centre, board, results, date),
        get_qe_outcome_ds(results, board, timestamp, date)
    ]

    return data_block
