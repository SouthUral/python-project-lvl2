import json
import os
import yaml
from .recursive_parsing import parsing_rec
from .views.formater import stylish
from .views.format_plain import plain


def defined_by_format(name_file):
    format = name_file.split('.')[1]
    if format == 'json':
        return open_json(name_file)
    else:
        return open_yaml(name_file)


def open_yaml(name_file):
    yaml_open = yaml.safe_load(open(abc_path(name_file)))
    return yaml_open


def open_json(name_file):
    json_open = json.load(open(abc_path(name_file)))
    return json_open


def abc_path(name_file):
    return os.path.abspath(name_file)


def general(file1, file2, view='stylish'):
    file1_dict = defined_by_format(file1)
    file2_dict = defined_by_format(file2)
    ready_internal_structure = parsing_rec(file1_dict, file2_dict)
    if view == 'stylish':
        stylized_output = stylish(ready_internal_structure)
    else:
        stylized_output = plain(ready_internal_structure)
    return stylized_output
