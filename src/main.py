from src.read_excel import get_worksheets, get_centre_number
from src.user_prompts import get_excel_filepath, get_csv_filepath
from src.xml.results_dict import get_results_dict
from src.save_to_xml import export_dict_to_xml, write_xml_to_file


def main(exam_board: str, message_id: str) -> None:
    """Takes exam board and message_id, connects to excel & csv data and
    exports mock A2C file for Cambridge International components.
    
    Prompts user for Excel file with Cambridge component results and csv file
    with candidate information. Saves to xml file in data folder.
    
    Args:
        exam_board(str): ID for exam board "02" for Cambridge International
        message_id(str): 36 character string used to ensure file is valid.
    """

    # get csv & excel filenames from user
    excel_filepath = get_excel_filepath()
    csv_filepath = get_csv_filepath()
    print("Saving results to data folder")

    # get excel data
    sheets = get_worksheets(excel_filepath)
    centre = get_centre_number(sheets)

    # save results data to python dictionary
    results_dict = get_results_dict(
        centre, exam_board, message_id, sheets, csv_filepath
    )

    # save results data to xml file
    a2c = f"data/a2c.{str(centre)}.{exam_board}.EDIResults.{message_id}.xml"
    xml = export_dict_to_xml(results_dict)
    write_xml_to_file(xml, a2c)
    print("Results saved to : cambridge-a2c/" + a2c)


if __name__ == "__main__":
    EXAM_BOARD = "02"
    MESSAGE_ID = "00000000-0000-0000-0000-000000000000"
    main(EXAM_BOARD, MESSAGE_ID)
