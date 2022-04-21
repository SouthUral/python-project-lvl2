

def parsing(data1, data2):
    line_indent = 2
    set_gen_data1 = gen_dict(data1)
    set_gen_data2 = gen_dict(data2)
    general_items = set_gen_data1 & set_gen_data2
    values_dif_file_1 = set_gen_data1 - set_gen_data2
    values_dif_file_2 = set_gen_data2 - set_gen_data1
    ready_data = sorted(
        [
            *data_indexing(general_items, line_indent),
            *data_indexing(values_dif_file_1, line_indent, '-'),
            *data_indexing(values_dif_file_2, line_indent, '+'),
        ], key=lambda value: value[line_indent + 2])
    str_data = '{\n' + '\n'.join(ready_data) + '\n}'
    return fix_json(str_data)


def data_indexing(data, line_indent, index=' '):
    indent = line_indent * ' '
    output_data = [f'{indent}{index} {value}' for value in data]
    return output_data


def fix_json(data_str):
    return data_str.replace('True', 'true').replace('False', 'false')


def gen_dict(data_dict):
    return {f'{key} : {values}' for key, values in data_dict.items()}
