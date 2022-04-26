import argparse
from gendiff.app_functionality.read_data import general

parser = argparse.ArgumentParser()
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format' , dest='format', metavar='\b',  help='output format (default: "stylish")') # noqa
args = parser.parse_args()


def main():
    generate_diff()


if __name__ == '__main__':
    main()


def generate_diff():
    first_file = args.first_file
    second_file = args.second_file
    format_view = args.format
    if format_view is None:
        print(general(first_file, second_file))
    else:
        print(general(first_file, second_file, format_view))
