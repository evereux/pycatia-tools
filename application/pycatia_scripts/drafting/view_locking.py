from application.pycatia_scripts.the_document import PTDrawingDocument


def view_locker(lock: bool, lock_main: bool, lock_background: bool) -> bool:
    """

    :param bool lock:
    :param bool lock_main:
    :param bool lock_background:
    :return:
    """

    pt_drawing_document = PTDrawingDocument()

    if not pt_drawing_document.is_drafting_document():
        return False

    sheets = pt_drawing_document.drawing_document.sheets

    for sheet in sheets:
        views = sheet.views
        if not sheet.is_detail():
            for view in views:
                if view.name == "Main View" and not lock_main:
                    continue
                if view.name == "Background View" and not lock_background:
                    continue
                # print(f"\tProcessing view: {view.name}")
                view.lock_status = lock

    return True
