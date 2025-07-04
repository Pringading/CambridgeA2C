from openpyxl import load_workbook
from warnings import filterwarnings
from datetime import datetime

def get_worksheets(filename: str) -> list:
    """"Get list of worksheets objects from filename.

    Args: filename
    Returns list of worksheets
    
    Will filter out worksheets that are not 4 characters starting with a
    digit. This means only worksheets with results data will be retained
    from Cambridge International component marks sheet.
    """

    filterwarnings(
        "ignore",
        message="Cannot parse header or footer so it will be ignored"
    )
    wb = load_workbook(filename=filename)
    sheets = []
    for sheet in wb.worksheets:
        if len(sheet.title) == 4 and sheet.title[0].isdigit():
            sheets.append(sheet)
    return sheets


def get_date(sheets: list) -> str:
    """Finds date from Cambridge International component results file

    Args: list of worksheets
    Returns date as a string formatted as yyyy-mm-dd
    """

    if not sheets:
        return ""
    sheet = sheets[0]
    for cell in sheet['A']:
        if isinstance(cell.value, str) and "Report generated" in cell.value:
            date = cell.value[20:]
    parsed_date = datetime.strptime(date, r"%d%b%Y")
    formatted_date = datetime.strftime(parsed_date, r"%Y-%m-%d")
    return formatted_date


def get_candidates(sheets: list) -> list:
    # get candidate number, mark, component code
    pass
