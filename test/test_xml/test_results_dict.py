import pytest
from src.xml.results_dict import (
    get_msg_info,
    get_transation_info,
    get_results_dict
)
from src.read_excel import get_worksheets


@pytest.mark.it('Testing get_msg_info function')
class TestGetMessageInfo:
    @pytest.fixture(scope="class")
    def test_args(self):
        return {
            "msg_id": "00000",
            "board": "02",
            "centre": 100000,
            "timestamp": "timestamp"
        }
    
    @pytest.mark.it("returns dict")
    def test_returns_dict(self, test_args):
        msg_info = get_msg_info(**test_args)
        assert isinstance(msg_info, dict)

    @pytest.mark.it("returns dict")
    def test_returns_expected_value(self, test_args):
        expected_msg = {
            "MessageID": "00000",
            "TimeStamp": "timestamp",
            "Sequence": 0,
            "Initiator_Data": {
                "Initiator_Party_Id": "02"
            },
            "Receiver_Data": {
                "Receiver_Party_Id": 100000
            },
            "SchemaVersion": "10.7",
            "Exchange_Name": "JCQ-A2C",
            "ExchangeSpec_Version": "2020"
        }
        returned_msg = get_msg_info(**test_args)
        assert returned_msg == expected_msg


@pytest.mark.it('Testing get_transaction_info function')
class TestGetTransactionInfo:
    pass


@pytest.mark.it('Testing get_results_dict function')
class TestGetResultsDict:
    @pytest.fixture(scope="class")
    def test_args(self, test_sheets):
        return {
            "message_id": "00000",
            "board": "02",
            "centre": 100000,
            "sheets": test_sheets
        }
