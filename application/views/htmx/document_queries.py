from pathlib import Path

from flask import render_template
from pycatia.in_interfaces.document import Document
from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.drafting_interfaces.drawing_document import DrawingDocument
from pycatia.product_structure_interfaces.product_document import ProductDocument
from pycatia.exception_handling.exceptions import CATIAApplicationException

from application import app
from application.pycatia_scripts.the_document import PTActiveDocument
from application.views.url_prefixes import htmx

@app.route(f'{htmx}/document/object', methods=['GET'])
def htmx_document_object():
    document_type: str = None
    document_object: Document = None
    try:
        pt_active_document = PTActiveDocument()
        document: Document = pt_active_document.active_document
        cls = type(document)
        module = cls.__module__
        name = cls.__qualname__
        if name == ProductDocument.__name__:
            document_type = "document"
            product_document = ProductDocument(document.com_object)
            document_object = product_document.product
        elif name == PartDocument.__name__:
            document_type = "document"
            part_document = PartDocument(document.com_object)
            document_object = part_document.product
        elif name == DrawingDocument.__name__:
            document_type = "drawing"
            document_object = DrawingDocument(document.com_object)
        else:
            document_type = "document"
            document_object = document
        return render_template('partials/document_object.html', document_type=document_type, document_object=document_object)
    except CATIAApplicationException:
        return render_template('partials/document_object.html', document_type=document_type)
    
    return render_template('partials/document_object.html', document_type=document_type)


@app.route(f'{htmx}/document/path', methods=['GET'])
def htmx_document_path():
    """
    returns the directory path of current active document as a form input.
    """

    try:
        pt_active_document = PTActiveDocument()
        pt_document = pt_active_document.active_document
        target_path = Path(pt_document.full_name).parent
        if str(target_path) == ".":
            target_path = ""
        return render_template(
            'partials/form_input_path.html',
            target_path=target_path
            )
    except CATIAApplicationException:
        return render_template(
            'partials/form_input_path.html',
            target_path=""
        )
     
    return render_template(
        'partials/form_input_path.html',
        target_path=""
    )

