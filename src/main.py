from dotenv import load_dotenv
from os import environ

load_dotenv()

# Variables
YEAR = 2024
EXAM_BOARD = "02"
CENTRE_NUMBER = environ.get("CENTRE_NUMBER")
MESSAGE_ID = "00000000-0000-0000-0000-000000000000"

# calculated variables
DATE = str(YEAR) + "-08-13"
organisations = [
    "JCQ",
    CENTRE_NUMBER,
    EXAM_BOARD,
]
FILENAME = f"a2c.{str(CENTRE_NUMBER)}.{EXAM_BOARD}.EDIResults.{MESSAGE_ID}.xml"


