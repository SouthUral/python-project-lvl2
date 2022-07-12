import json
import yaml
from yaml.loader import SafeLoader


def parsing(data, format):
    if format == 'json':
        return json.loads(data)
    elif format in ('yml', 'yaml'):
        return yaml.load(data, Loader=SafeLoader)
    else:
        raise ValueError
