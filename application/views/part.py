from application import app
from application.support.template import render_template
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
    return render_template(
        'part_new.html',
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
