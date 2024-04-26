from pathlib import Path

from pycatia.drafting_interfaces.drawing_document import DrawingDocument
from pycatia.in_interfaces.application import Application
from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.product_structure_interfaces.product_document import ProductDocument

from application.pycatia_scripts.com_objects import get_app_object


def is_type_document(type_: str, application: Application):
    active_document = application.active_document
    file_name = Path(active_document.path())
    if file_name.suffix == type_:
        return True
    return False


class PTActiveDocument:

    def __init__(self):
        self.application = get_app_object()
        self.active_document = self.application.active_document

    def is_drafting_document(self):
        return is_type_document('.CATDrawing', self.application)

    def is_part_document(self):
        return is_type_document('.CATPart', self.application)

    def is_product_document(self):
        return is_type_document('.CATProduct', self.application)

class PTProductDocument(PTActiveDocument):

    def __init__(self):
        super().__init__()
        self.product_document = ProductDocument(self.active_document.com_object)
        self.product = self.product_document.product

    @property
    def details(self) -> {}:

        if not self.is_product_document():
            return {}

        revision = self.product.revision
        part_number = self.product.part_number
        definition = self.product.definition
        nomenclature = self.product.nomenclature

        details = {
            'definition': definition,
            'nomenclature': nomenclature,
            'part_number': part_number,
            'revision': revision
        }

        return details


class PTPartDocument(PTActiveDocument):

    def __init__(self):
        super().__init__()
        self.part_document = PartDocument(self.active_document.com_object)
        self.part = self.part_document.part
        self.product = self.part_document.product

    @property
    def details(self) -> {}:

        if not self.is_part_document():
            return {}

        revision = self.product.revision
        part_number = self.product.part_number
        definition = self.product.definition
        nomenclature = self.product.nomenclature

        details = {
            'definition': definition,
            'nomenclature': nomenclature,
            'part_number': part_number,
            'revision': revision
        }

        return details


class PTDrawingDocument(PTActiveDocument):

    def __init__(self):
        super().__init__()
        self.drawing_document = DrawingDocument(self.active_document.com_object)

    @property
    def details(self) -> {}:

        if not self.is_drafting_document():
            return {}

        sheets = self.drawing_document.sheets

        details = {'file_name': self.active_document.path(), 'sheets': {}}

        for sheet in sheets:
            details['sheets'][sheet.name] = []
            for view in sheet.views:
                details['sheets'][sheet.name].append(view.name)

        return details
