import pytest
from unittest.mock import patch, Mock
from src.xml.results_dict import (
    get_msg_info,
    get_results_dict
)


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


@pytest.mark.it('Testing get_results_dict function')
class TestGetResultsDict:
    @pytest.fixture(scope="class")
    def test_args(self, test_sheets):
        return {
            "message_id": "00000",
            "board": "02",
            "centre": 100000,
            "sheets": test_sheets,
            "csv_filepath": "data/test_candidates.csv"
        }

    @pytest.mark.it("Returns dict")
    def test_returns_dict(self, test_args):
        results = get_results_dict(**test_args)
        assert isinstance(results, dict)

    @pytest.mark.it("Returns dict with expected keys")
    def test_dict_keys(self, test_args):
        results = get_results_dict(**test_args)
        assert "MsgHeader" in results
        assert "DataBlock" in results

    @pytest.mark.it("Returns expected transation info")
    def test_expected_transaction_info(self, test_args):
        expected = {"TransactionName": "ProcessResults"}
        results = get_results_dict(**test_args)
        assert results["MsgHeader"]["TransactionInfo"] == expected

    @patch("src.xml.results_dict.get_msg_info")
    @pytest.mark.it("Calls get_msg_info function")
    def test_get_msg_info_called(self, mock_msg, test_args):
        value = Mock(return_value={"test": "msg"})
        mock_msg.side_effect = value
        result = get_results_dict(**test_args)
        assert value.call_count == 1
        assert result["MsgHeader"]["MsgInfo"] == {"test": "msg"}

    @patch("src.xml.results_dict.get_data_block")
    @pytest.mark.it("Calls get_data_block function")
    def test_get_data_block_called(self, mock_block, test_args):
        value = Mock(return_value={"test": "block"})
        mock_block.side_effect = value
        result = get_results_dict(**test_args)
        assert value.call_count == 1
        assert result["DataBlock"] == {"test": "block"}
