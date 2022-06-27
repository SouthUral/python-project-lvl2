import json
import yaml
from yaml.loader import SafeLoader


def parsing(data, format):
    if format == 'json':
        return json.loads(data)
    else:
        return yaml.load(data, Loader=SafeLoader)
