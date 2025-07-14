from csv import DictReader

def get_data(filepath: str) -> list:
    """Gets data from csv file and returns list of dictionaries"""
    
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        data = DictReader(f)
        return list(data)


def dict_from_candidates(candidates: list) -> dict:
    pass


def results_and_candidates(candidates: dict, results: list) -> list:
    pass
