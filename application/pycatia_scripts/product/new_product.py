from pycatia.product_structure_interfaces.product_document import ProductDocument

from application.pycatia_scripts.com_objects import get_app_object


def create_new_product(part_number: str, revision: str, definition: str, nomenclature: str):
    """

    :param part_number:
    :param revision:
    :param definition:
    :param nomenclature:
    :return:
    """

    application = get_app_object()
    documents = application.documents

    product_document = ProductDocument(documents.add('Product').com_object)
    product = product_document.product
    product.part_number = part_number
    product.revision = revision
    product.definition = definition
    product.nomenclature = nomenclature

    return True
