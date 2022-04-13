import argparse
import json
from gendiff.app_functionality import gendiff_logic

parser = argparse.ArgumentParser()
parser.add_argument('first_file')
parser.add_argument('second_file')
args = parser.parse_args()


def main():
    first_file = json.load(open(args.first_file))
    second_file = json.load(open(args.second_file))
    print(gendiff_logic.generate_diff(first_file, second_file))


if __name__ == '__main__':
    main()
