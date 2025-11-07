from flask import render_template

from application import app
from application.support.properties import get_properties
from application.views.view_wrappers import catia_v5_required


@app.route('/part')
@catia_v5_required
def part():
    return render_template(
        'part.html',
    )


@app.route('/part/new')
@catia_v5_required
def part_new():
    default_properties = get_properties(None, 'default')
    user_defined_properties = get_properties(None, 'user')

    return render_template(
        'part_new.html',
        default_properties=default_properties,
        user_defined_properties=user_defined_properties
    )


@app.route('/part/points')
@catia_v5_required
def part_points():
    return render_template(
        'part_points.html',
    )


@app.route('/part/bounding_box')
@catia_v5_required
def part_bounding_box():
    return render_template(
        'part_bounding_box.html',
    )
