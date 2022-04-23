

def stylish(data_structure):
    format_list = []
    def recursive(data, indent='  '):
        key_sort = sorted(data.keys(), key=lambda value: value if value[0] not in ['+', '-'] else value[2:])
        for key in key_sort:
            # добавление общего отступа, первый отступ 2 все последующие +4
            format_list.append(indent)
            format_list.append(check_indent(key))
            if isinstance(data[key], dict):
                format_list.append('{')
                format_list.append('\n')
                recursive(data[key], indent + (' ' * 4))
                # закрывающая скобка всегда общий отступ + выравнивание + 2
                format_list.append(indent + '  ' + '}\n')
            else:
                format_list.append(check_str(data[key]))
                format_list.append('\n')
    recursive(data_structure)
    return fix_bug_readfile('{\n' + ''.join(format_list) + '}')


# выравнивание всегда на 2 отступа
def check_indent(item):
    if item[0] in ['+', '-']:
        return item + ': '
    return '  ' + item + ': '


def check_str(item):
    if isinstance(item, str):
        return item
    return str(item)

# убираем баг с чтением null, true, false
def fix_bug_readfile(text_data):
    return text_data.replace('True', 'true').replace('False', 'false').replace('None', 'null')
