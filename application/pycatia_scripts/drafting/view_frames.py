from pycatia.exception_handling.exceptions import CATIAApplicationException

from application.pycatia_scripts.the_document import PTDrawingDocument


def view_framer(display: bool) -> bool:
    """

    """
    try:
        pt_drawing_document = PTDrawingDocument()
    except CATIAApplicationException:
        return False

    if not pt_drawing_document.is_drafting_document():
        return False

    sheets = pt_drawing_document.drawing_document.sheets

    for sheet in sheets:
        views = sheet.views
        for view in views:
            view.frame_visualization = display

    return True
