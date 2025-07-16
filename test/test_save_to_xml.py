import pytest
from src.save_to_xml import export_dict_to_xml, write_xml_to_file
from os.path import isfile


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
    @pytest.mark.it("Adds file to location")
    def test_saves_file(self, tmp_path):
        d = tmp_path / "sub"
        d.mkdir()
        p = d / "file.xml"
        write_xml_to_file("", p)
        assert isfile(p)

    @pytest.mark.it("Adds opening and closing tags.")
    def test_adds_opening_and_closing_tags(self, tmp_path):
        expected_line_1 = (
            '<A2CMessage xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns' +
            ':xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http' +
            '://jcq.org.uk/a2c">\n'
        )
        d = tmp_path / "sub"
        d.mkdir()
        p = d / "file.xml"
        write_xml_to_file("", p)
        with open(p, "r") as f:
            assert f.readline() == expected_line_1
            assert f.readline() == "\n"
            assert f.readline() == '</A2CMessage>'

    @pytest.mark.it("Writes expected content to the file")
    def test_writes_expected_content_to_file(self, tmp_path):
        test_xml = "<test>1</test>"
        d = tmp_path / "sub"
        d.mkdir()
        p = d / "file.xml"
        write_xml_to_file(test_xml, p)
        with open(p, "r") as f:
            assert test_xml in f.read()
