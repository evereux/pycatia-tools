from pycatia.exception_handling.exceptions import CATIAApplicationException

from application.pycatia_scripts.common import output
from application.pycatia_scripts.the_document import PTDrawingDocument
from application.support.documents import get_drawing_document


def view_framer(display: bool) -> dict:
    """

    """
    pt_drawing_document, errors = get_drawing_document()

    sheets = pt_drawing_document.drawing_document.sheets

    for sheet in sheets:
        output['data'][sheet.name] = []
        views = sheet.views
        for view in views:
            view.frame_visualization = display
            state = 'Frame on' if view.frame_visualization else 'Frame off'
            output['data'][sheet.name].append(f'{view.name} {state}')

    return output
