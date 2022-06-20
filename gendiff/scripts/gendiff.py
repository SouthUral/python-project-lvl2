import argparse
from gendiff import generate_diff

parser = argparse.ArgumentParser()
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format' , dest='format', metavar='\b',  help='output format (default: "stylish")') # noqa
args = parser.parse_args()


def main():
    first_file = args.first_file
    second_file = args.second_file
    format_view = args.format
    if format_view is None:
        print(generate_diff(first_file, second_file))
    else:
        print(generate_diff(first_file, second_file, format_view))


if __name__ == '__main__':
    main()
