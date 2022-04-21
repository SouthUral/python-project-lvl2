import json
import os
import yaml
from .parsing_data import parsing


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


def general(file1, file2):
    file1_dict = defined_by_format(file1)
    file2_dict = defined_by_format(file2)
    return parsing(file1_dict, file2_dict)
