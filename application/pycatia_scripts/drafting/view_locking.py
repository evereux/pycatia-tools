from application.pycatia_scripts.common import output
from application.support.documents import get_drawing_document


def view_locker(lock: bool, lock_main: bool, lock_background: bool) -> dict:
    """

    """

    pt_drawing_document, errors = get_drawing_document()

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
                state = 'Locked' if lock else 'Unlocked'
                output['data'][sheet.name].append(f'{view.name} {state}')

    return output