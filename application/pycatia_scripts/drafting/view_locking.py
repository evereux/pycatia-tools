from pycatia.exception_handling import CATIAApplicationException

from application.pycatia_scripts.the_document import PTDrawingDocument


def view_locker(lock: bool, lock_main: bool, lock_background: bool) -> dict:
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

    if output['errors']:
        return output

    sheets = pt_drawing_document.drawing_document.sheets

    for sheet in sheets:
        output['data'][sheet.name] = []
        views = sheet.views
        if not sheet.is_detail():
            for view in views:
                if view.name == "Main View" and not lock_main:
                    continue
                if view.name == "Background View" and not lock_background:
                    continue
                # print(f"\tProcessing view: {view.name}")
                view.lock_status = lock

                output['data'][sheet.name].append(f'{view.name} {'Locked' if lock else 'Unlocked'}')

    return output