import json
from .read_data import defined_by_format
from .recursive_parsing import parsing_rec


file_path_1 = '/home/vova/python_learn/projects/python-project-lvl2/tests/fixtures/file_rec1.json'
file_path_2 = '/home/vova/python_learn/projects/python-project-lvl2/tests/fixtures/file_rec2.json'
file_write = '/home/vova/python_learn/projects/python-project-lvl2/tests/fixtures/file_gendiff_json.json'
file1_dict = defined_by_format(file_path_1)
file2_dict = defined_by_format(file_path_2)
processed_data = parsing_rec(file1_dict, file2_dict)

with open(file_write, 'w') as file:
    json.dump(processed_data, file, indent=2, sort_keys=True)