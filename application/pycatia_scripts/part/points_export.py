import csv
import os
from pathlib import Path

from pycatia.enumeration.enumeration_types import geometrical_feature_type
from pycatia.exception_handling.exceptions import CATIAApplicationException

from application.pycatia_scripts.common import output
from application.support.documents import get_part_document


def export_points(geometric_set: str, file_name: str, target_directory: str) -> {}:
    """

    """

    if not geometric_set:
        output['errors'].append('Please provide name of Geometric Set containing points.')

    if not target_directory:
        target_directory = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    if not Path(target_directory).is_dir():
        output['errors'].append(f'"{target_directory}" is not a directory.')

    pt_part_document, errors = get_part_document()

    output['errors'] = output['errors'] + errors

    if output['errors']:
        return output

    part_document = pt_part_document.part_document
    product = part_document.product
    spa_workbench = part_document.spa_workbench()
    part = part_document.part
    part_number = product.part_number
    hsf = part.hybrid_shape_factory
    hbs = part.hybrid_bodies

    if not file_name:
        file_name = f'{part_number}.csv'

    target_file = Path(target_directory, file_name)
    output['output_file'] = target_file

    set_exists = False
    set_with_points = None
    try:
        set_with_points = hbs.item(geometric_set)
        set_exists = True
    except CATIAApplicationException:
        output['errors'].append(f'Could not find- Geometric Set "{geometric_set}".')

    if set_exists and set_with_points:

        hybrid_shapes = set_with_points.hybrid_shapes

        data = {}

        try:
            with open(f'{target_file}', 'w', newline='') as file:
                writer = csv.writer(file)
                field = ['name', 'x', 'y', 'z']
                writer.writerow(field)

                i = 1
                for hybrid_shape in hybrid_shapes:
                    hs_reference = part.create_reference_from_object(hybrid_shape)
                    gft = hsf.get_geometrical_feature_type(hs_reference)
                    gft_text = geometrical_feature_type[gft]
                    if gft_text == 'Point':
                        measurable = spa_workbench.get_measurable(hs_reference)
                        coordinates = measurable.get_point()
                        print(hybrid_shape.name, coordinates)
                        if i < 100:
                            data[hybrid_shape.name] = coordinates
                        writer.writerow([hybrid_shape.name, coordinates[0], coordinates[1], coordinates[2]])
                    i += 1

            output['data'] = data
        except PermissionError:
            output['errors'].append(f'Could not write to {target_file}. If the file open?')

    return output
