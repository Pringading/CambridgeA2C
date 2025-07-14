from csv import DictReader

def get_csv_data(filepath: str) -> list:
    """Gets data from csv file and returns list of dictionaries"""
    
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        data = DictReader(f)
        return list(data)


def dict_from_candidates(c_list: list) -> dict:
    c_dict = {}
    for c in c_list:
        c_num = c["Candidate Number"]
        c_dict[c_num] = {
            "UCI": c["UCI"],
            "DOB": c["Date of Birth"]
        }
    return c_dict


def results_and_candidates(candidates: dict, results: list) -> list:
    pass
