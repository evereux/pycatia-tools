from flask import request

from application import app
from application.pycatia_scripts.part.points_import import import_points
from application.support.template import render_template
from application.views.url_prefixes import htmx


@app.route(f'{htmx}/part/import_points', methods=['POST'])
def htmx_import_points():

    geometric_set = request.form.get('geometric_set_import', type=str) or None

    files = request.files

    output = import_points(geometric_set, files)
    data = output['data']
    errors = output['errors']

    if errors:
        return render_template('partials/errors.html', errors=errors)

    if data:
        return render_template('partials/point_table.html', data=data)

    return '<p class="alert alert-danger mt-3">There was a problem</p>'
