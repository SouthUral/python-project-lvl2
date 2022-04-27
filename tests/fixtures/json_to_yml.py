# предназначен для перезаписи json фикстур в yml фикстуры

import json
import yaml


def open_json(name_file):
    json_open = json.load(open(name_file))
    return json_open


def converter(path_json):
    data_dict = open_json(path_json)
    name_newfile = path_json.split('.')[0] + '.yml'
    with open(name_newfile, 'w') as file:
        yaml.dump(data_dict, file, default_flow_style=False)


converter('/home/vova/python_learn/projects/python-project-lvl2/tests/fixtures/file_rec1.json')
converter('/home/vova/python_learn/projects/python-project-lvl2/tests/fixtures/file_rec2.json')
