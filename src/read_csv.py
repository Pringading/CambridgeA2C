from csv import DictReader
from copy import deepcopy

def get_csv_data(filepath: str) -> list:
    """Gets data from csv file and returns list of dictionaries"""
    
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
            "Date of Birth": "01/01/2020"}, {}...]
        >>> dict_from_candidates(c_list)
        >>> {
            1000: {"UCI": 100000251000A, "DOB": "2020-01-01"},
            1001: {}...
        }
    """
    c_dict = {}
    for c in c_list:
        c_num = int(c["Candidate Number"])
        c_dict[c_num] = {
            "UCI": c["UCI"],
            "DOB": c["Date of Birth"]
        }
    return c_dict


def results_and_candidates(candidates: dict, results: list) -> list:
    data = []
    for result in results:
        candidate = result["CandidateNumber"]
        new_result = deepcopy(result)
        new_result["DOB"] = candidates[candidate]["DOB"]
        new_result["UCI"] = candidates[candidate]["UCI"]
        data.append(new_result)
    return data
