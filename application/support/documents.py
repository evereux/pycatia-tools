from typing import List, Tuple

from pycatia.exception_handling import CATIAApplicationException

from application.pycatia_scripts.the_document import PTDrawingDocument
from application.pycatia_scripts.the_document import PTPartDocument

from application.pycatia_scripts.the_document import PTProductDocument


def get_part_document() -> Tuple[PTPartDocument | None, List]:
    errors = []
    pt_part_document = None
    try:
        pt_part_document = PTPartDocument()
        if not pt_part_document.is_part_document():
            errors.append('The active document is not a CATPart')
    except CATIAApplicationException:
        errors.append('No active document.')
    except AttributeError:
        errors.append('No active document or active document is not a CATPart.')

    return pt_part_document, errors


def get_drawing_document() -> Tuple[PTDrawingDocument | None, List]:
    errors = []
    pt_drawing_document = None
    try:
        pt_drawing_document = PTDrawingDocument()
        if not pt_drawing_document.is_drafting_document():
            errors.append('The active document is not a CATDrawing')
    except CATIAApplicationException:
        errors.append('No active document.')
    except AttributeError:
        errors.append('No active document or active document is not a CATDrawing.')

    return pt_drawing_document, errors


def get_product_document(product_only: bool = True) -> Tuple[PTProductDocument | None, List]:
    """

    :param product_only:
    :return:
    """
    errors = []
    pt_product_document = None
    try:
        pt_product_document = PTProductDocument()
        if product_only:
            if not pt_product_document.is_product_document():
                errors.append('The active document is not a CATProduct')
    except CATIAApplicationException:
        errors.append('No active document.')
    except AttributeError:
        errors.append('No active document.')

    return pt_product_document, errors
