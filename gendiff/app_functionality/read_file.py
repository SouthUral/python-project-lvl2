

def reading_file(name_file):
    with open(name_file) as file:
        file_data = file.read()
    return file_data


def get_file_format(name_file):
    return name_file.split('.')[1]
