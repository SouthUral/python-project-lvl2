from gendiff import generate_diff
import pytest


def open_file(name_file):
    file_on = open(name_file, "r")
    file_data = "".join([i for i in file_on])
    file_on.close()
    return file_data


result_flat_diff = open_file("tests/fixtures/result_flat_diff.txt")
result_recursive_diff = open_file("tests/fixtures/result_recursive_diff.txt")
result_diff_plain = open_file("tests/fixtures/result_diff_plain.txt")
result_json_views = open_file("tests/fixtures/result_diff_json.json")
result_hexlet_test = open_file("tests/fixtures/hexlet_result.txt")


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected, view",
    [
        ("flat_structure_1.json", "flat_structure_2.json", result_flat_diff, "stylish"),
        ("flat_structure_1.yml", "flat_structure_2.yml", result_flat_diff, "stylish"),
        (
            "tree_structure_1.json",
            "tree_structure_2.json",
            result_recursive_diff,
            "stylish",
        ),
        (
            "tree_structure_1.yml",
            "tree_structure_2.yml",
            result_recursive_diff,
            "stylish",
        ),
        (
            "tree_structure_1.json",
            "tree_structure_2.json",
            result_diff_plain,
            "plain",
        ),
        (
            "tree_structure_1.json",
            "tree_structure_2.json",
            result_json_views,
            "json",
        ),
        (
            "hexlet_1.yml",
            "hexlet_2.yml",
            result_hexlet_test,
            "plain",
        ),
    ],
)
def test_generate_diff(input_data_1, input_data_2, expected, view):
    path = "tests/fixtures/"
    file1 = path + input_data_1
    file2 = path + input_data_2
    assert generate_diff(file1, file2, view) == expected
