#! /usr/bin/python3.8

from pycatia.drafting_interfaces.drawing_sheet import DrawingSheet
from pycatia.enumeration.enumeration_types import cat_text_anchor_position

from application.pycatia_scripts.settings import drawing_template
from .background_view import get_background_view_and_factory
from .text_properties import set_text_properties


def create_template_name(sheet: DrawingSheet, size_info: dict):
    """
    The drawing template name is added to the bottom right hand corner of the
    drawing inside the border itself.
    :param DrawingSheet sheet:
    :param dict size_info:
    :return:
    """

    sheet_x = size_info['sheet_x']

    position_offset = 3

    bottom_right_x = sheet_x - drawing_template['border_offset']
    bottom_right_y = position_offset

    background_view, factory_2d, _ = get_background_view_and_factory(sheet)
    texts = background_view.texts
    new_text = texts.add(drawing_template['template_name'], bottom_right_x, bottom_right_y)
    anchor_position = cat_text_anchor_position.index('catBottomRight')
    new_text.anchor_position = anchor_position
    set_text_properties(new_text, size=2.5)
