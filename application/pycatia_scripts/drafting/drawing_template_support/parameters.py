#! /usr/bin/python3.8

from pywintypes import com_error

from pycatia.drafting_interfaces.drawing_document import DrawingDocument
from pycatia.knowledge_interfaces.parameters import Parameters

from application.pycatia_scripts.settings import drawing_template


def create_parameters(drawing: DrawingDocument, form_parameters: dict) -> Parameters:
    """

    :param drawing:
    :return:
    """

    drawing_parameters = drawing.parameters

    existing_parameters = drawing_parameters.all_parameters()

    for param in drawing_template['parameters']:
        # if the method get_item fails, capture the exception and add the parameter.
        try:
            # see if the parameter already exists
            dp = drawing_parameters.get_item(f'Drawing\{param}')
            if dp:
                drawing_parameters.remove(f'Drawing\{param}')
        except com_error:
            # the parameter doesn't exist so we can continue with creation.
            pass
        if param in form_parameters:
            if form_parameters[param]:
                drawing_template['parameters'][param] = form_parameters[param]
        drawing_parameters.create_string(param, drawing_template['parameters'][param])

    return drawing.parameters
