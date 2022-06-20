def new_dict(keys, data, prefix):
    new_data = {}
    for key in keys:
        rename_key = f'{prefix} {key}'
        new_data[rename_key] = data[key]
    return new_data


def define_keys(data1, data2):
    keys1, keys2 = list(map(set, [data1.keys(), data2.keys()]))
    keys_general = keys1 & keys2
    keys_data1 = keys1 - keys2
    keys_data2 = keys2 - keys1
    return keys_general, keys_data1, keys_data2


def parsing(data1, data2):
    merge_data = {}
    keys_general, keys_data1, keys_data2 = define_keys(data1, data2)
    merge_data.update(new_dict(keys_data1, data1, '-'))
    merge_data.update(new_dict(keys_data2, data2, '+'))
    for key in keys_general:
        if all([isinstance(data1[key], dict), isinstance(data2[key], dict)]):
            merge_data[key] = parsing(data1[key], data2[key])
        else:
            if data1[key] == data2[key]:
                merge_data[key] = data1[key]
            else:
                merge_data[f'- {key}'] = data1[key]
                merge_data[f'+ {key}'] = data2[key]
    return merge_data
