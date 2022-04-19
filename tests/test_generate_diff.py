from gendiff.app_functionality import gendiff_logic


def test_gendiff():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    file3 = open_file('tests/fixtures/file_test_gendiff.txt')
    assert gendiff_logic.generate_diff(file1, file2) == file3


def open_file(name_file):
    file_on = open(name_file, 'r')
    return ''.join([i for i in file_on])
    