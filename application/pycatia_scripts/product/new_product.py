from pycatia.product_structure_interfaces.product_document import ProductDocument
from werkzeug.datastructures import ImmutableMultiDict

from application.pycatia_scripts.common import get_output
from application.pycatia_scripts.common import check_part_number_exists
from application.pycatia_scripts.com_objects import get_app_object
from application.support.properties import update_properties


def create_new_product(form: ImmutableMultiDict) -> bool:
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

    try:
        product_document = ProductDocument(documents.add('Product').com_object)
        update_properties(product_document.product, form)

        output['data'] = f'New Product "{form.get("part_number")}" created.'

        return output

    except:
        output['errors'].append('There was a problem.')
        return output
