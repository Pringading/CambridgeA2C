from os.path import isfile

def get_filepath():
    print("Please save cambridge components result spreadsheet into the cambridge-a2c/data folder.")
    filepath = "data/"
    filename = input("Cambridge spreadsheet filename:")
    if len(filename) > 5 and filename[-5:] != ".xlsx":
        filename += ".xlsx"
    while not isfile(filepath + filename):
        print(f"File {filename} not found in cambridge-a2c/data folder, (only accepts .xlsx files)")
        filename = input("Please enter filename again")
        if len(filename) > 5 and filename[-5:] != ".xlsx":
            filename += ".xlsx"
    return filepath + filename