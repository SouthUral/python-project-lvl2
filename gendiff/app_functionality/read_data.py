import json
import os
import yaml
from . import recursive_parsing
from .views.formater import stylish
from .views.format_plain import plain
from .views.format_json import json_format


def reading_file_data(name_file):
    format = name_file.split('.')[1]
    if format == 'json':
        return open_json(name_file)
    else:
        return open_yaml(name_file)


def open_yaml(name_file):
    yaml_open = yaml.safe_load(open(os.path.abspath(name_file)))
    return yaml_open


def open_json(name_file):
    json_open = json.load(open(os.path.abspath(name_file)))
    return json_open


def generate_diff(file1, file2, view='stylish'):
    file_data_1 = reading_file_data(file1)
    file_data_2 = reading_file_data(file2)
    data_analyzed = recursive_parsing.parsing(file_data_1, file_data_2)
    if view == 'stylish':
        stylized_output = stylish(data_analyzed)
    elif view == 'plain':
        stylized_output = plain(data_analyzed)
    else:
        stylized_output = json_format(data_analyzed)
    return stylized_output
