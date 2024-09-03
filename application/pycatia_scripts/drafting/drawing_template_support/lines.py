from typing import List

from pycatia.in_interfaces.selection import Selection
from pycatia.sketcher_interfaces.line_2D import Line2D


def update_line_properties(
        lines: List[Line2D],
        selection: Selection,
        line_width: int = 0,
        inheritance: int = 0
) -> None:
    """

    :param lines:
    :param selection:
    :param line_width:
    :param inheritance:
    :return:
    """
    selection.clear()
    for line in lines:
        selection.add(line)
    vp = selection.vis_properties
    vp.set_real_width(line_width, inheritance)
