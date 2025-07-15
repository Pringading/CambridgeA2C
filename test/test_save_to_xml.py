import pytest
from src.save_to_xml import export_dict_to_xml, write_xml_to_file

@pytest.mark.it("Test export_dict_to_xml function")
class TestExportDictToXML:
    @pytest.mark.it("Returns string")
    def test_returns_string(self):
        xml = export_dict_to_xml({})
        assert isinstance(xml, str)
    
    @pytest.mark.it("Returns expected value")
    def test_returns_expected_value(self):
        test_dict = {
            "First": 1,
            "Outer": {
                "Inner": "Value"
            },
        }
        expected_value = "<First>1</First>\n"
        expected_value += "<Outer>\n"
        expected_value += "  <Inner>Value</Inner>\n"
        expected_value += "</Outer>"
        result = export_dict_to_xml(test_dict)
        assert result == expected_value

    @pytest.mark.it("Doesn't change the order of dictinoary")
    def test_doesnt_change_order(self):
        test_dict = {
            "c": 1,
            "b": 2,
            "a": 3
        }
        expected_value = "<c>1</c>\n<b>2</b>\n<a>3</a>"
        result = export_dict_to_xml(test_dict)
        assert result == expected_value

    @pytest.mark.it("Returns self closing tag if value is none")
    def test_returns_self_closing_tag_for_None(self):
        test_dict = {
            "a": None
        }
        expected_value = "<a/>"
        result = export_dict_to_xml(test_dict)
        assert result == expected_value

@pytest.mark.it("Test write_xml_to_file function")
class TestWriteXMLToFile:
    pass