

def parsing_rec(data_1, data_2): # noqa
    data_structure = dict()

    def write_data(data):
        for key, value in data.items():
            data_structure[key] = value

    def new_dict(keys, data_dict):
        res_dict = {}
        for key in keys:
            res_dict[key] = data_dict[key]
        return res_dict

    def rename_keys(data1, data2):
        rename_data1 = {f'- {key}': value for key, value in data1.items()}
        rename_data2 = {f'+ {key}': value for key, value in data2.items()}
        return rename_data1, rename_data2

    def define_keys(key_data1, key_data2):
        keys1, keys2 = list(map(set, [key_data1, key_data2]))
        gen_keys = keys1 & keys2
        keys_1 = keys1 - keys2
        keys_2 = keys2 - keys1
        return gen_keys, keys_1, keys_2

    def recursive_func(data1, data2, key_dict=''):

        def recursion_logic(dict_write):
            for key in general_keys:
                if all([isinstance(data1[key], dict), isinstance(data2[key], dict)]): # noqa
                    dict_write[key] = recursive_func(data1[key], data2[key], key_dict=key) # noqa
                else:
                    if data1[key] == data2[key]:
                        dict_write[key] = data1[key]
                    else:
                        dict_write[f'- {key}'] = data1[key]
                        dict_write[f'+ {key}'] = data2[key]

        general_keys, keys_1, keys_2 = define_keys(data1.keys(), data2.keys())
        gen_dict1 = new_dict(keys_1, data1)
        gen_dict2 = new_dict(keys_2, data2)
        new_data_1, new_data_2 = rename_keys(gen_dict1, gen_dict2)
        if key_dict == '':
            write_data(new_data_1)
            write_data(new_data_2)
            recursion_logic(data_structure)
        else:
            merge_dict = {**new_data_1, **new_data_2}
            recursion_logic(merge_dict)
            return merge_dict
    recursive_func(data_1, data_2)
    return data_structure
