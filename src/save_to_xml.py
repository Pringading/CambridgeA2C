from dict2xml import dict2xml, DataSorter


def export_dict_to_xml(dict_to_convert: dict) -> str:
    """Takes python dictinoary and exports to xml string.

    None values in the dictionary will create self closing xml tags.
    """

    data_sorter = DataSorter.never()
    return dict2xml(
        dict_to_convert,
        data_sorter=data_sorter,
        closed_tags_for=[None]
    )


def write_xml_to_file(xml: str, filepath: str) -> None:
    """Writes xml string to xml file.

    Adds opening and closing tags from A2C file.
    Args:
        xml(str): xml string to be written to file.
        filepath(str): relative path where file will be saved.
    """

    with open(filepath, "w") as f:
        f.write('<A2CMessage xmlns:xs="http://www.w3.org/2001/XMLSchema" ')
        f.write('xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ')
        f.write('xmlns="http://jcq.org.uk/a2c">\n')
        f.write(xml)
        f.write('\n</A2CMessage>')
