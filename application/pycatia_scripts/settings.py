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

border_offset = json_data['drawing_template']['border_offset']
company_details = json_data['drawing_template']['company_details']
logo = Path(path_prefix, json_data['drawing_template']['logo'])
parameters = json_data['drawing_template']['parameters']
sheet_names = json_data['drawing_template']['sheet_names']
sheet_sizes = json_data['drawing_template']['sheet_sizes']
template_name = json_data['drawing_template']['template_name']
tolerances = json_data['drawing_template']['tolerances']
units = json_data['drawing_template']['units']
geometric_sets = json_data['part_template']['geometric_sets']
