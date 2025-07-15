from datetime import datetime
from src.xml.data_block import get_data_block

def get_msg_info(
    msg_id: str, board: str, centre: int, timestamp: str
) -> dict:
    """Returns dictionary with message info."""

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

def get_transation_info():
    return {
        "TransactionName": "ProcessResults"
    }

def get_results_dict(centre: int, board: str, message_id: str, sheets: list):
    timestamp = datetime.now().astimezone().replace(microsecond=0).isoformat()
    msg_info = get_msg_info(message_id, board, centre, timestamp)
    results_dict = {}
    return results_dict