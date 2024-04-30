from pycatia.drafting_interfaces.drawing_document import DrawingDocument
from pycatia.drafting_interfaces.drawing_view import DrawingView

from application.pycatia_scripts.common import output
from application.support.documents import get_drawing_document

from application.pycatia_scripts.drafting.drawing_template_support.border import create_border
from application.pycatia_scripts.drafting.drawing_template_support.copyright_box import create_copyright_box
from application.pycatia_scripts.drafting.drawing_template_support.paper_size import get_sheet_size_info
from application.pycatia_scripts.drafting.drawing_template_support.parameters import create_parameters
from application.pycatia_scripts.drafting.drawing_template_support.purge import purge_background_view
from application.pycatia_scripts.drafting.drawing_template_support.template_name import create_template_name
from application.pycatia_scripts.drafting.drawing_template_support.title_block import create_title_block


def insert_drawing_template(form_parameters):

    pt_drawing_document, errors = get_drawing_document()

    output['errors'] = output['errors'] + errors

    if output['errors']:
        return output

    drawing: DrawingDocument = pt_drawing_document.drawing_document
    application = drawing.application
    sheets = drawing.sheets
    parameters = create_parameters(drawing, form_parameters)
    sheet_number = 1
    for sheet in sheets:
        statement = f'Processing sheet: {sheet.name}'
        print('='*len(statement) + '\n' + statement + '\n' + '='*len(statement))
        size_info = get_sheet_size_info(sheet)

        # !! delete everything in the background view!!
        purge_background_view(drawing, sheet)

        create_border(sheet, size_info)
        create_copyright_box(sheet, parameters)
        create_title_block(sheet, size_info, parameters, sheet_number)
        create_template_name(sheet, size_info)
        # required as colour changes are not otherwise visible.
        sheet.force_update()
        sheet_number += 1

    # activate the first sheet and main view.
    # on border creation the main view is activated after work in the
    # background view is completed yet it seems to have no effect on sheet 1.
    # I even tried looping through the sheets to activate the main view but
    # then this didn't work for sheet.2.
    for sheet in sheets:
        sheet.activate()
        main_view = DrawingView(sheet.views.get_item_by_name('Main View').com_object)
        main_view.activate()
        viewer = application.active_window
        # fit all in.
        viewer.active_viewer.reframe()
    sheets[0].activate()

    output['data'] = 'Drawing template inserted.'

    return output
