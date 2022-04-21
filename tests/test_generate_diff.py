from gendiff.app_functionality import read_data
from gendiff.app_functionality import parsing_data


def open_file(name_file):
    file_on = open(name_file, 'r')
    return ''.join([i for i in file_on])


file3 = open_file('tests/fixtures/file_test_gendiff.txt')


def test_gendiff_json():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    assert read_data.general(file1, file2) == file3


def test_gendiff_yaml():
    file1 = 'tests/fixtures/file1.yml'
    file2 = 'tests/fixtures/file2.yml'
    assert read_data.general(file1, file2) == file3

    