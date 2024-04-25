from pycatia.mec_mod_interfaces.part_document import PartDocument

from application.pycatia_scripts.com_objects import get_app_object


def create_new_part(part_number: str, revision: str, definition: str, nomenclature: str):
    """

    :param part_number:
    :param revision:
    :param definition:
    :param nomenclature:
    :return:
    """

    application = get_app_object()
    documents = application.documents

    part_document = PartDocument(documents.add('Part').com_object)
    product = part_document.product
    product.part_number = part_number
    product.revision = revision
    product.definition = definition
    product.nomenclature = nomenclature

    return True
