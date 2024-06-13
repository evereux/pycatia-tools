from pathlib import Path

from flask import render_template
from pycatia.exception_handling.exceptions import CATIAApplicationException

from application import app
from application.pycatia_scripts.the_document import PTActiveDocument
from application.views.url_prefixes import htmx

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

