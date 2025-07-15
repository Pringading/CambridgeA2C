from csv import DictReader
from copy import deepcopy
from datetime import datetime
from src.read_excel import get_results


def get_csv_data(filepath: str) -> list:
    """Gets data from csv file and returns list of dictionaries

    Args:
        filepath(str): relative filepath to csv file.

    Returns: list of dictionaries, one dictionary for each row, with the column
        headings as the keys and the data as the values.
    """

    with open(filepath, 'r', encoding='utf-8-sig') as f:
        data = DictReader(f)
        return list(data)


def dict_from_candidates(c_list: list) -> dict:
    """Takes list of dictionaries with candidate numbers and returns dictionary
    with candidate numbers as keys and UCI and DOB on keys in nested
    dictionary.

    Args:
        c_list: list of dictionaries with candidate information on
            "Candidate Number", "UCI" and "Date of Birth" keys

    Returns:
        dictionary with candidate numbers as keys pointing to nested
        dictionary with "UCI" and "DOB" keys.

    Example:
        c_list = [{
            "Candidate Number": 1000,
            "UCI": 1000000251000A,
            "Date of Birth": "01/01/2020"}, {}...
        ]

        >>> dict_from_candidates(c_list)
        >>> {
            1000: {"UCI": 100000251000A, "DOB": "2020-01-01"},
            1001: {}...
        }
    """
    c_dict = {}
    for c in c_list:
        c_num = int(c["Candidate Number"])
        parsed_date = datetime.strptime(c["Date of Birth"], r"%d/%m/%Y")
        formatted_date = datetime.strftime(parsed_date, r"%Y-%m-%d")
        c_dict[c_num] = {
            "UCI": c["UCI"],
            "DOB": formatted_date
        }
    return c_dict


def results_and_candidates(candidates: dict, results: list) -> list:
    """Adds DOB and UCI to list of results using inputted candidates dictionary
    and outputs as new list.

    Args: candidates(dict): candidate numbers as keys pointing to dictionary
            with "DOB" key with candidate's Date of Birth
            and "UCI" key with candidate's UCI

        results(list): list of dictionaries each with "CandidateNumber" key

    Returns:
        New list with the same data as the input results list but with
            additional "DOB" and "UCI" keys
    """
    data = []
    for result in results:
        candidate = result["CandidateNumber"]
        if candidate not in candidates:
            print("UCI & DOB not found for Candidate: " + str(candidate))
            continue
        new_result = deepcopy(result)
        new_result["DOB"] = candidates[candidate]["DOB"]
        new_result["UCI"] = candidates[candidate]["UCI"]
        data.append(new_result)
    return data


def get_all_data(sheets: list, filepath: str) -> list:
    """Takes list of excel sheets and filepath to csv file and returns list of
    results data.
    
    Args:
        sheets(list): List of excel sheets data with cambridge results info
        filepath(str): relative path to csv file with candidate info:
            "UCI", "Candidate Number" & "Date of Birth"
    """
    
    results = get_results(sheets)
    csv_data = get_csv_data(filepath)
    candidates = dict_from_candidates(csv_data)
    all_data = results_and_candidates(candidates, results)
    return all_data
