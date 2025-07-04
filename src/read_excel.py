from openpyxl import load_workbook
from warnings import filterwarnings


def get_worksheets(filename: str) -> list:
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
    return ""


def get_candidates(sheets: list) -> list:
    # get candidate number, mark, component code
    pass
