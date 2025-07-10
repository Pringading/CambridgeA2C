from os.path import isfile


def get_filepath():
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
