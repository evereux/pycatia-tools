from pycatia.exception_handling.exceptions import CATIAApplicationException

from application.pycatia_scripts.the_document import PTDrawingDocument


def view_framer(display: bool) -> dict:
    """

    """

    output = {
        'errors': [],
        'data': {},
    }

    try:
        pt_drawing_document = PTDrawingDocument()
        if not pt_drawing_document.is_drafting_document():
            output['errors'].append('Active document is not a CATDrawing.')
    except CATIAApplicationException:
        output['errors'].append('No active document.')
    except AttributeError:
        output['errors'].append('No active document or active document is not a CATDrawing.')

    sheets = pt_drawing_document.drawing_document.sheets

    for sheet in sheets:
        output['data'][sheet.name] = []
        views = sheet.views
        for view in views:
            view.frame_visualization = display
            output['data'][sheet.name].append(f'{view.name} {'Frame on' if display else 'Frame off'}')

    return output
