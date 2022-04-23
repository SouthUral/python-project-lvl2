

def parsing_rec(data_1, data_2):
    structure = dict()


    def rec_data(data):
        for key, value in data.items():
            structure[key] = value


    def recursive_func(data1, data2, key_dict=''):
        general_keys = set(data1.keys()) & set(data2.keys())
        keys_1 = set(data1.keys()) - set(data2.keys())
        keys_2 = set(data2.keys()) - set(data1.keys())
        
        if key_dict == '':
            rec_data(rename_keys(new_dict(keys_1, data1), '-'))
            rec_data(rename_keys(new_dict(keys_2, data2), '+'))
            for key in general_keys:
                if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                    structure[key] = recursive_func(data1[key], data2[key], key_dict=key)
                else:
                    if data1[key] == data2[key]:
                        structure[key] = data_1[key]
                    else:
                        structure[f'- {key}'] = data1[key]
                        structure[f'+ {key}'] = data2[key]
        else:
            a = rename_keys(new_dict(keys_1, data1), '-')
            b = rename_keys(new_dict(keys_2, data2), '+')
            merge_dict = {**a, **b}
            for key in general_keys:
                if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                    merge_dict[key] = recursive_func(data1[key], data2[key], key_dict=key)
                else:
                    if data1[key] == data2[key]:
                        merge_dict[key] = data1[key]
                    else:
                        merge_dict[f'- {key}'] = data1[key]
                        merge_dict[f'+ {key}'] = data2[key]
            return merge_dict
    recursive_func(data_1, data_2)
    return structure


def new_dict(keys, data_dict):
    res_dict = {}
    for key in keys:
        res_dict[key] = data_dict[key]
    return res_dict


def rename_keys(data, symb):
    return {f'{symb} {key}' : value for key, value in data.items()}
