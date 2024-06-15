from pycatia.product_structure_interfaces.product_document import ProductDocument

from application.pycatia_scripts.common import get_output
from application.pycatia_scripts.common import check_part_number_exists
from application.pycatia_scripts.com_objects import get_app_object


def create_new_product(part_number: str, revision: str, definition: str, nomenclature: str) -> bool:
    """

    :param part_number:
    :param revision:
    :param definition:
    :param nomenclature:
    :return:
    """
    
    output = get_output()

    application = get_app_object()
    documents = application.documents

    output = check_part_number_exists(documents, output, part_number)

    if output['errors']:
        return output
    
    try:

        product_document = ProductDocument(documents.add('Product').com_object)
        product = product_document.product
        product.part_number = part_number
        product.revision = revision
        product.definition = definition
        product.nomenclature = nomenclature

        output['data'] = f'New Product "{part_number}" created.'

        return output

    except:

        output['errors'].append('There was a problem.')

        return output
