from . import parsing_data


def reading_file(name_file):
    format = name_file.split('.')[1]
    file_on = open(name_file, "r")
    file_data = "".join([i for i in file_on])
    file_on.close()
    return file_data, format


def decryption_data(name_file):
    file_data, format = reading_file(name_file)
    return parsing_data.parsing(file_data, format)
