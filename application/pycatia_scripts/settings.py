#! /usr/bin/python3.8

import json
from pathlib import Path
import os


def read_json(f: Path):
    """
    Reads the contents of json file `f` and returns the data.
    """
    with open(f, encoding='utf-8') as file:
        data = json.load(file)

    return data


# you probably wouldn't have to do this out of a development environment.
path_prefix = Path(os.getcwd())

json_settings = Path(path_prefix, 'settings.json')
json_data = read_json(json_settings)

drawing_template = json_data['drawing_template']
part_template = json_data['part_template']
