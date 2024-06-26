#! /usr/bin/python3.8

from pycatia.drafting_interfaces.drawing_sheet import DrawingSheet
from pycatia.enumeration.enumeration_types import cat_text_anchor_position

from application.pycatia_scripts.settings import drawing_template

from .background_view import get_background_view_and_factory
from .lines import update_line_properties
from .text_properties import set_text_properties


def create_border(sheet: DrawingSheet, size_info: dict):
    legible_paper_size = size_info['legible_paper_size']
    sheet_x = size_info['sheet_x']
    sheet_y = size_info['sheet_y']

    sheet_x_splits = drawing_template['sheet_sizes'][legible_paper_size][1][0]
    sheet_y_splits = drawing_template['sheet_sizes'][legible_paper_size][1][1]

    background_view, factory_2d, main_view = get_background_view_and_factory(sheet)
    selection = sheet.application.active_document.selection

    # lines is a collector that will collect lines to change vis_properties
    lines = []
    # create the outside border at page limits.
    line_outer_bottom = factory_2d.create_line(0, 0, sheet_x, 0)
    line_outer_right = factory_2d.create_line(sheet_x, 0, sheet_x, sheet_y)
    line_outer_top = factory_2d.create_line(sheet_x, sheet_y, 0, sheet_y)
    line_outer_left = factory_2d.create_line(0, sheet_y, 0, 0)

    lines.extend([line_outer_bottom, line_outer_right, line_outer_top, line_outer_left])

    # create inner border offset by 10mm
    offset = drawing_template['border_offset']
    line_inner_bottom = factory_2d.create_line(offset, offset, sheet_x - offset, offset)
    line_inner_right = factory_2d.create_line(sheet_x - offset, offset, sheet_x - offset, sheet_y - offset)
    line_inner_top = factory_2d.create_line(sheet_x - offset, sheet_y - offset, offset, sheet_y - offset)
    line_inner_left = factory_2d.create_line(offset, sheet_y - offset, offset, offset)

    lines.extend([line_inner_bottom, line_inner_right, line_inner_top, line_inner_left])

    x_offset = sheet_x / sheet_x_splits
    y_offset = sheet_y / sheet_y_splits

    # create the vertical grid reference lines
    for n in range(sheet_x_splits):
        i = n + 1
        # bottom
        bottom_vertical_line = factory_2d.create_line(x_offset * i, 0, x_offset * i, offset)
        # top
        top_vertical_line = factory_2d.create_line(x_offset * i, sheet_y - offset, x_offset * i, sheet_y)
        lines.extend([bottom_vertical_line, top_vertical_line])

    # create the horizontal grid reference lines
    for n in range(sheet_y_splits):
        i = n + 1
        # left
        left_vertical_line = factory_2d.create_line(0, y_offset * i, offset, y_offset * i)
        # right
        right_vertical_line = factory_2d.create_line(sheet_x, y_offset * i, sheet_x - offset, y_offset * i)
        lines.extend([left_vertical_line, right_vertical_line])

    update_line_properties(lines, selection)

    # add text for grid references
    anchor_position = cat_text_anchor_position.index('catMiddleCenter')
    texts = background_view.texts

    # horizontal numerical texts
    for i in range(sheet_x_splits):
        x = i + 1
        if i == 0:
            x_position = x_offset / 2
        else:
            x_position = (x_offset / 2) + (x_offset * x)

        # break out of the loop if the text is outside border
        if x_position > sheet_x:
            break

        # bottom
        text_bottom = texts.add(str(x), x_position, offset / 2)
        text_bottom.anchor_position = anchor_position
        set_text_properties(text_bottom)
        # top
        text_top = texts.add(str(x), x_position, sheet_y - (offset / 2))
        text_top.anchor_position = anchor_position
        set_text_properties(text_top)

    # vertical character texts
    start_char = 'A'
    for i in range(sheet_y_splits):
        if i == 0:
            char = start_char
            y_position = y_offset / 2
        else:
            char = chr(ord(start_char) + i)
            y_position = (y_offset / 2) + (y_offset * i)

        # break out of the loop if the text is outside border
        if y_position > sheet_y:
            break

        # left
        text_left = texts.add(char, offset / 2, y_position)
        text_left.anchor_position = anchor_position
        set_text_properties(text_left)
        # right
        text_right = texts.add(char, sheet_x - (offset / 2), y_position)
        text_right.anchor_position = anchor_position
        set_text_properties(text_right)
