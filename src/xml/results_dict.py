from datetime import datetime
from src.xml.data_block import get_data_block


def get_msg_info(
    msg_id: str, board: str, centre: int, timestamp: str
) -> dict:
    """Returns dictionary with message info.

    Args:
        msg_id(str): 36 character long string.
        board(str): board ID "02" for Cambridge International
        centre(int): centre number
        timestamp(str): timestamp in isoformat with timezone

    Returns:
        dictionary with message info for mock A2C results file
    """

    msg_info = {
        "MessageID": msg_id,
        "TimeStamp": timestamp,
        "Sequence": 0,
        "Initiator_Data": {
            "Initiator_Party_Id": board
        },
        "Receiver_Data": {
            "Receiver_Party_Id": centre
        },
        "SchemaVersion": "10.7",
        "Exchange_Name": "JCQ-A2C",
        "ExchangeSpec_Version": "2020"
    }
    return msg_info


def get_results_dict(
        centre: int,
        board: str,
        message_id: str,
        sheets: list,
        csv_filepath: str
) -> dict:
    """Gets dictionary with component results info contained in A2C file.

    Args:
        centre(int): centre number
        board(str): board ID "02" for Cambridge International
        message_id(str): 36 character long string.
        sheets(list): list of Excel worksheet data from Cambridge component
            results Excel workbook.
        filepath(str): relative path to csv file with candidate info:
            "UCI", "Candidate Number" & "Date of Birth"

    Returns:
        Dictionary with all results info for mock A2C component results file
    """

    timestamp = datetime.now().astimezone().replace(microsecond=0).isoformat()
    msg_info = get_msg_info(message_id, board, centre, timestamp)
    data_block = get_data_block(sheets, centre, board, timestamp, csv_filepath)
    results_dict = {
        "MsgHeader": {
            "MsgInfo": msg_info,
            "TransactionInfo": {"TransactionName": "ProcessResults"}
        },
        "DataBlock": data_block
    }
    return results_dict
