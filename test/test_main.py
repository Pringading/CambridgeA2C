import pytest
from unittest.mock import patch, Mock, call
from src.main import main


@pytest.fixture
def test_args():
    return {
        "exam_board": "02",
        "message_id": "00000000-0000-0000-0000-000000000000"
    }

@pytest.fixture
def mock_inputs():
    with patch("src.user_prompts.input") as mock_input:
        mock_input.side_effect = ["test_results.xlsx", "test_candidates.csv"]
        yield mock_input


@patch("src.user_prompts.input", return_value="test_candidates.csv")
@patch("src.main.get_excel_filepath")
@pytest.mark.it("Calls get_excel_filepath function")
def test_get_excel_filepath_called(mock_excel, mock_input, test_args):
    mock_func = Mock(return_value="data/test_results.xlsx")
    mock_excel.side_effect = mock_func
    main(**test_args)
    assert mock_func.call_count == 1


@patch("src.user_prompts.input", return_value="test_results.xlsx")
@patch("src.main.get_csv_filepath")
@pytest.mark.it("Calls get_csv_filepath function")
def test_get_csv_filepath_called(mock_csv, mock_input, test_args):
    mock_func = Mock(return_value="data/test_candidates.csv")
    mock_csv.side_effect = mock_func
    main(**test_args)
    assert mock_func.call_count == 1


@patch("src.main.get_worksheets")
@pytest.mark.it("Calls get_worksheets function with expected args")
def test_get_worksheets_called(mock_sheets, mock_inputs, test_args):
    mock_func = Mock(return_value=[])
    mock_sheets.side_effect = mock_func
    main(**test_args)
    assert mock_func.call_count == 1
    assert call("data/test_results.xlsx") == mock_func.call_args 


@patch("src.main.get_centre_number")
@pytest.mark.it("Calls get_centre_number function")
def test_get_centre_number_called(mock_cn, mock_inputs, test_args):
    mock_func = Mock(return_value=10000)
    mock_cn.side_effect = mock_func
    main(**test_args)
    assert mock_func.call_count == 1


@patch("src.main.get_results_dict")
@pytest.mark.it("Calls get_results_dict function")
def test_get_results_dict_called(mock_res, mock_inputs, test_args):
    mock_func = Mock(return_value=[])
    mock_res.side_effect = mock_func
    main(**test_args)
    assert mock_func.call_count == 1


@patch("src.main.export_dict_to_xml")
@pytest.mark.it("Calls export_dict_to_xml function")
def test_export_dict_to_xml_called(mock_xml, mock_inputs, test_args):
    mock_func = Mock(return_value="")
    mock_xml.side_effect = mock_func
    main(**test_args)
    assert mock_func.call_count == 1


@patch("src.main.write_xml_to_file")
@pytest.mark.it("Calls write_xml_to_file function")
def test_write_xml_to_file_called(mock_write, mock_inputs, test_args):
    mock_func = Mock()
    mock_write.side_effect = mock_func
    main(**test_args)
    assert mock_func.call_count == 1


