from . import recursive_parsing
from . import read_data
from .views.formater import stylish
from .views.format_plain import plain
from .views.format_json import json_format


def output_diff(file1, file2, view='stylish'):
    file_data_1 = read_data.reading_file_data(file1)
    file_data_2 = read_data.reading_file_data(file2)
    data_analyzed = recursive_parsing.parsing(file_data_1, file_data_2)
    if view == 'stylish':
        stylized_output = stylish(data_analyzed)
    elif view == 'plain':
        stylized_output = plain(data_analyzed)
    else:
        stylized_output = json_format(data_analyzed)
    return stylized_output