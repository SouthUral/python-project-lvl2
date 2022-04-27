

# 3 сценария
# 1) - was removed
# 2) -+ was updated. From old_value to new_value
# 3) + was added with value: new_value


def plain(data): # noqa
    # в этот список ведется запись
    output_list = []

    def rec_in_output(txt, node):
        if node != '':
            output_txt = "Property '" + node + "." + txt
        else:
            output_txt = "Property '" + txt
        output_list.append(output_txt)

    def recusive_func(data, parent_node=''):
        crutch = []
        repeat_check = lambda item: False if item in crutch else True # noqa
        # проверка ключей на изменения
        key_sort = sorted(data.keys(), key=sorted_key)
        for key in key_sort:
            if key[0] in ['+', '-'] and repeat_check(key[2:]):
                crutch.append(key[2:])
                message = message_construct(key, data)
                rec_in_output(message, parent_node)
            else:
                key_data = data[key]
                if isinstance(key_data, dict):
                    if parent_node == '':
                        all_node = key
                    else:
                        all_node = parent_node + '.' + key
                    recusive_func(key_data, all_node)
    recusive_func(data)
    return fix_bug_readfile('\n'.join(output_list))


# Функция находит ключ, определяет есть ли второй ключ и запускает 1 из 3-х сценариев # noqa
def message_construct(key, data):
    prefix = (lambda simb: '-' if simb == '+' else '+')(key[0])
    new_key = prefix + key[1:]
    if new_key in data:
        # запуск 2 сценария
        new_value = verif_value(data['+' + key[1:]])
        old_value = verif_value(data['-' + key[1:]])
        return f"{key[2:]}' was updated. From {old_value} to {new_value}"
    else:
        if key[0] == '-':
            # запуск 1 сценария
            return f"{key[2:]}' was removed"
        else:
            # запуск 3 сценария
            new_value = verif_value(data[key])
            return f"{key[2:]}' was added with value: {new_value}"


# заменяет данные на строку [complex value]
def verif_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return value


def sorted_key(value):
    return value if value[0] not in ['+', '-'] else value[2:]


# надо переставить функцию в место где происходит парсинг
def fix_bug_readfile(text_data):
    res = text_data.replace('True', 'true').replace('False', 'false')
    return res.replace('None', 'null')
