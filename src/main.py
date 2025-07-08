from read_excel import (
    get_worksheets,
    get_date,
    get_results,
    get_centre_number
)

# User prompts
filepath = ""

# Get Data
sheets = get_worksheets(filepath)
date = get_date(sheets)
results = get_results(sheets)
centre_number = get_centre_number(sheets)
year = int(date[:4])

print(results)
# Variables
EXAM_BOARD = "02"
MESSAGE_ID = "00000000-0000-0000-0000-000000000000"

# Calculated Variables
organisations = [
    "JCQ",
    centre_number,
    EXAM_BOARD,
]
FILENAME = f"a2c.{str(centre_number)}.{EXAM_BOARD}.EDIResults.{MESSAGE_ID}.xml"
