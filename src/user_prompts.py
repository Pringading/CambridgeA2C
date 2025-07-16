from os.path import isfile


def get_excel_filepath() -> str:
    """Prompts the user for input and provides relative path to xlsx file.

    The function prompts the user to save file into cambridge-a2c/data folder
    Then asks for the filename. If the file is not found in the folder or the
    user provides a different file extension it will ask the user again for
    the file name. Adds .xlsx when extension not provided.

    Returns (str):
        "data/<filename>.xlsx"
    Examples:
        >>> get_filepath()
        >>> Cambridge spreadsheet filename: Testing
        >>> data/Testing.xlsx

        >>> get_filepath()
        >>> Cambridge spreadsheet filename: Testing.xlsx
        >>> data/Testing.xlsx

        >>> get_filepath()
        >>> Cambridge spreadsheet filename: Testing.doc
        >>> File testing.doc.xlsx not found...

    """

    filepath = "data/"

    # prompting user
    print(
        "Please save cambridge components result spreadsheet into the " +
        "cambridge-a2c/data folder."
    )
    filename = input("Cambridge spreadsheet filename: ")

    # adds file extension if none provided
    if len(filename) > 5 and filename[-5:] != ".xlsx":
        filename += ".xlsx"

    # ask for input again if file doesn't exist in cambridge-a2c/data folder
    while not isfile(filepath + filename):
        print(
            f"File {filename} not found in cambridge-a2c/data folder," +
            " (only accepts .xlsx files)"
        )
        filename = input("Please enter filename again: ")

        # add file extension
        if len(filename) > 5 and filename[-5:] != ".xlsx":
            filename += ".xlsx"
    return filepath + filename


def valid_headings(filepath: str) -> bool:
    """Takes csv file and returns True if contains "UCI", "Candidate Number"
    and "Date of Birth" headings, False if not.

    Args:
        filepath(str): path to csv file to be checked
    """
    with open(filepath, "r", encoding="utf-8") as f:
        headings = f.readline().rstrip().split(",")

        if "Candidate Number" not in headings:
            print(f"\nCandidate Number column not found in {headings}")
            print("Please check spaces and capitalisation and retry.")
            return False

        elif "UCI" not in headings:
            print(f"\nUCI column not found in {headings}")
            print("Please check spaces and capitalisation and retry.")
            return False

        elif "Date of Birth" not in headings:
            print(f"\nDate of Birth column not found in {headings}")
            print("Please check spaces and capitalisation and retry.")
            return False
        return True


def get_csv_filepath() -> str:
    filepath = "data/"
    print(
        "Please save csv file with 'Candidate Number', 'UCI' and 'Date of " +
        "Birth' headings to the cambridge-a2c/data folder.\nThis can include"
        " data for all candidates or just those with Cambridge International "
        "entries. Date of Birth column should be in dd/mm/yyyy format.\n" +
        "Please ensure headings are exactly as above including " +
        "capitalisation and spaces. If saving csv from Excel save to " +
        "CSV UTF-8 (Comma Delimited) format"
    )
    filename = input("candidate csv filename: ")

    # adds file extension if none provided
    if len(filename) > 4 and filename[-4:] != ".csv":
        filename += ".csv"

    # ask for input again if file doesn't exist in cambridge-a2c/data folder
    while (
        not isfile(filepath + filename)
        or not valid_headings(filepath + filename)
    ):
        if not isfile(filepath + filename):
            print(
                f"File {filename} not found in cambridge-a2c/data folder," +
                " (only accepts .csv files)"
            )
        else:
            print(
                "Please save csv file with correct headings to " +
                "cambridge-a2c/data folder"
            )
        filename = input("Please enter filename again: ")

        # add file extension
        if len(filename) > 4 and filename[-4:] != ".csv":
            filename += ".csv"

    return filepath + filename
