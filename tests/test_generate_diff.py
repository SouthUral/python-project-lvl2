from gendiff import generate_diff


def open_file(name_file):
    file_on = open(name_file, 'r')
    return ''.join([i for i in file_on])


file3 = open_file('tests/fixtures/file_test_gendiff.txt')
file_rec = open_file('tests/fixtures/file_test_gendiff_rec.txt')
file_plain_views = open_file('tests/fixtures/file_test_gendif_plain.txt')
file_json_views = open_file('tests/fixtures/file_gendiff_json.json')
file_plain_hexlet = open_file('tests/fixtures/hexlet_test.txt')


def test_gendiff_json():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    assert generate_diff(file1, file2) == file3


def test_gendiff_yaml():
    file1 = 'tests/fixtures/file1.yml'
    file2 = 'tests/fixtures/file2.yml'
    assert generate_diff(file1, file2) == file3


def test_gendiff_rec_json():
    file1 = 'tests/fixtures/file_rec1.json'
    file2 = 'tests/fixtures/file_rec2.json'
    assert generate_diff(file1, file2) == file_rec


def test_gendiff_rec_yaml():
    file1 = 'tests/fixtures/file_rec1.yml'
    file2 = 'tests/fixtures/file_rec2.yml'
    assert generate_diff(file1, file2) == file_rec


def test_plain_views():
    file1 = 'tests/fixtures/file_rec1.json'
    file2 = 'tests/fixtures/file_rec2.json'
    assert generate_diff(file1, file2, 'plain') == file_plain_views


def test_json_view():
    file1 = 'tests/fixtures/file_rec1.json'
    file2 = 'tests/fixtures/file_rec2.json'
    assert generate_diff(file1, file2, 'json') == file_json_views


def test_hexlet_views_yml():
    file1 = 'tests/fixtures/hexlet_test1.yml'
    file2 = 'tests/fixtures/hexlet_test2.yml'
    assert generate_diff(file1, file2, 'plain') == file_plain_hexlet
