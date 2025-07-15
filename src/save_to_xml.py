from dict2xml import dict2xml, DataSorter

def export_dict_to_xml(dict_to_convert: dict):
    data_sorter = DataSorter.never()
    return dict2xml(
        dict_to_convert,
        data_sorter = data_sorter,
        closed_tags_for = [None]
    )

def write_xml_to_file():
    pass
