import json
import os
import yaml


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
