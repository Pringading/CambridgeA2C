from openpyxl import load_workbook
from openpyxl.worksheet.worksheet import Worksheet
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

    If date not found returns today's date.
    """

    if not sheets:
        parsed_date = datetime.now()
    else:
        sheet = sheets[0]
        for cell in sheet['A']:
            if isinstance(cell.value, str) and "Report generated" in cell.value:
                date = cell.value[20:]
                break
        parsed_date = datetime.strptime(date, r"%d%b%Y")
    formatted_date = datetime.strftime(parsed_date, r"%Y-%m-%d")
    return formatted_date


def get_titles(option: str, row: tuple) -> dict:
    titles = {
        "Components": []
    }
    option += "/"
    for cell in row:
        if cell.value == "Candidate number":
            titles["CandidateNumber"] = cell.column
        if isinstance(cell.value, str) and "component" in cell.value.lower():
            component = option + cell.value[-2:]
            titles["Components"].append((cell.column, component))
    return titles


def get_sheet_results(sheet: Worksheet) -> list:
    """Get title locations from specified row."""
    option = sheet.title
    mark_rows = []
    #     if row[0] == "Syllabus":
    #         start = cell.row
    #         break
    # for cell in sheet[start]:
    #     if cell.value.lower() == "candidate number":
    #         candidate_col = cell.col

    #     if isinstance(cell.value, str) and "Component" in cell.value:
    #         component = cell.value[-2:]
    #         mark_rows.append((cell.col, component))
    
    # start += 1
    # for row in sheet[start]:
    #     if row[0] == None:
    #         break
    #     candidate = row[candidate_col]


def get_results(sheets: list) -> list:
    """Get results data."""
    results = []
    for sheet in sheets:
        results += get_sheet_results(sheet)
        
    return results

# get centre number
