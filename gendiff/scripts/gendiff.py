import argparse
from gendiff.app_functionality.read_data import general

parser = argparse.ArgumentParser()
parser.add_argument('first_file')
parser.add_argument('second_file')
args = parser.parse_args()


def main():
    first_file = args.first_file
    second_file = args.second_file
    print(general(first_file, second_file))


if __name__ == '__main__':
    main()
