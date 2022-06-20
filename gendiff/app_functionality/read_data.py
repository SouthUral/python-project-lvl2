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
    file1_dict = reading_file_data(file1)
    file2_dict = reading_file_data(file2)
    ready_internal_structure = recursive_parsing.parsing(file1_dict, file2_dict)
    if view == 'stylish':
        stylized_output = stylish(ready_internal_structure)
    elif view == 'plain':
        stylized_output = plain(ready_internal_structure)
    else:
        stylized_output = json_format(ready_internal_structure)
    return stylized_output
