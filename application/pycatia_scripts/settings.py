from pathlib import Path
import os

import yaml


def read_yaml(f: Path):
    """
    Reads the contents of the yaml file `f` and returns the data.
    """
    data = None
    with open(f) as file:
        try:
            data = yaml.safe_load(file)
        except yaml.YAMLError as e:
            print(e)

    return data


path_prefix = Path(os.path.dirname(__file__)).parent.parent

yaml_file = Path(path_prefix, 'settings.yaml')
yaml_data = read_yaml(yaml_file)

drawing_template = yaml_data['drawing_template']
part_template = yaml_data['part_template']
product_template = yaml_data['product_template']
