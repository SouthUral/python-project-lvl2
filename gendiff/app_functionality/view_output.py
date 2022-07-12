from . import recursive_parsing
from . import read_file
from . import parsing_data
from .views.formater import stylish
from .views.format_plain import plain
from .views.format_json import json_format


def generate_diff(file1, file2, view='stylish'):
    content_1 = read_file.reading_file(file1)
    format1 = read_file.get_file_format(file1)
    content_2 = read_file.reading_file(file2)
    format2 = read_file.get_file_format(file2)
    dict_1 = parsing_data.parsing(content_1, format1)
    dict_2 = parsing_data.parsing(content_2, format2)
    data_analyzed = recursive_parsing.parsing(dict_1, dict_2)
    if view == 'stylish':
        stylized_output = stylish(data_analyzed)
    elif view == 'plain':
        stylized_output = plain(data_analyzed)
    else:
        stylized_output = json_format(data_analyzed)
    return stylized_output
