from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.product_structure_interfaces.product_document import ProductDocument
from werkzeug.datastructures import ImmutableMultiDict

from application.pycatia_scripts.common import check_part_number_exists
from application.pycatia_scripts.common import get_output
from application.pycatia_scripts.com_objects import get_app_object
from application.pycatia_scripts.settings import part_template
from application.support.properties import update_properties


def create_new_part(form: ImmutableMultiDict):
    """

    :param form:
    :return:
    """

    output = get_output()

    application = get_app_object()
    documents = application.documents

    output = check_part_number_exists(documents, output, form.get('part_number'))

    if output['errors']:
        return output

    part_document = PartDocument(documents.add('Part').com_object)
    update_properties(part_document.product, form)

    part = part_document.part

    if part_template['geometric_sets']:
        hybrid_bodies = part.hybrid_bodies
        for gs_name in part_template['geometric_sets']:
            new_gs = hybrid_bodies.add()
            new_gs.name = gs_name

    if part_template['parameters']:
        parameters = part.parameters
        for parm in part_template['parameters']:
            name = parm
            type_ = part_template['parameters'][parm]['type'].upper()
            value = part_template['parameters'][parm]['value']
            allowed_dimensions = ['LENGTH']
            if type_ in allowed_dimensions:
                parameters.create_dimension(name, type_, value)

    part.update()

    output['data'] = f'New Part "{form.get("part_number")}" created.'

    return output
