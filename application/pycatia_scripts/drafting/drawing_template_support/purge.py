from pycatia.drafting_interfaces.drawing_document import DrawingDocument
from pycatia.drafting_interfaces.drawing_sheet import DrawingSheet
from pycatia.drafting_interfaces.drawing_view import DrawingView


def delete_all(drawing: DrawingDocument, sheet: DrawingSheet, query: str, type_: str):
    """

    :param drawing:
    :param sheet:
    :param query:
    :param type_:
    :return:
    """

    views = sheet.views
    background_view = DrawingView(views.get_item_by_name('Background View').com_object)

    sel = drawing.selection
    sel.clear()
    sel.add(background_view)
    query = f'{query},sel'
    sel.search(query)
    if sel.count > 0:
        print(f'Deleting {sel.count} {type_} elements.')
        sel.delete()
    else:
        print('Could not find anything to delete.')
    sel.clear()


def purge_background_view(drawing: DrawingDocument, sheet: DrawingSheet):
    queries = [
        'Drafting.Line',
        'Drafting.Text',
        'Drafting.Picture',
    ]

    for query in queries:
        delete_all(drawing, sheet, query, query[9:])
