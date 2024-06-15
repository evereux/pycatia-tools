import csv
import os
import tempfile
from pathlib import Path

from pycatia.exception_handling.exceptions import CATIAApplicationException
from werkzeug.datastructures import ImmutableMultiDict
from werkzeug.utils import secure_filename

from application.pycatia_scripts.common import get_output
from application.pycatia_scripts.the_document import PTPartDocument
from application.support.documents import get_part_document
from application.support.files import allowed_file


def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def are_numbers(x, y, z):
    if is_number(x) and is_number(y) and is_number(z):
        return True
    return False


def import_points(geometric_set: str, files: ImmutableMultiDict):
    """

    """

    output = get_output()

    if 'file' not in files:
        output['errors'].append('Missing file input.')

    try:
        file = files['file']
    except KeyError:
        output['errors'].append('No file has been uploaded.')

    if output['errors']:
        return output

    if file.filename == '':
        output['errors'].append('Missing file input')
    if file and allowed_file(file.filename):
        file_name = secure_filename(file.filename)
        temp_dir = tempfile.mkdtemp()
        target_file = Path(temp_dir, file_name)
        file.save(target_file)
    else:
        output['errors'].append('There was a problem with the file.')

    pt_part_document, errors = get_part_document()
    output['errors'] = output['errors'] + errors

    if not geometric_set:
        output['errors'].append('Please provide name of Geometric Set containing points.')

    if output['errors']:
        return output

    part_document = pt_part_document.part_document
    application = part_document.application
    application.refresh_display = False
    part = part_document.part
    hsf = part.hybrid_shape_factory
    hbs = part.hybrid_bodies
    try:
        target_set = hbs.item(geometric_set)
    except CATIAApplicationException:
        # the geometric set doesn't exist so create it.
        target_set = hbs.add()
        target_set.name = geometric_set

    # create_points(part, file_name, 'mm', geometric_set, )
    point_data = []
    data = dict
    # read the csv file into memory.
    with open(target_file) as file:
        csv_file = csv.reader(file, delimiter=",")
        for line in csv_file:
            point_data.append((line[0], line[1], line[2], line[3]))

    # clean up the temp file and directory
    target_file.unlink()
    os.rmdir(temp_dir)

    i = 1
    for point in point_data:
        name = point[0]
        x = point[1]
        y = point[2]
        z = point[3]
        if are_numbers(x, y, z):
            x_int = float(x)
            y_int = float(y)
            z_int = float(z)
            new_point = hsf.add_new_point_coord(x_int, y_int, z_int)
            new_point.name = name
            target_set.append_hybrid_shape(new_point)
            if i < 100:
                output['data'][name] = (x, y, z)
            i += 1

    application.refresh_display = False
    part.update()
    return output
