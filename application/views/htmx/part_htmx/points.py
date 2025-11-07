from flask import request, render_template

from application import app
from application.pycatia_scripts.part.points_export import export_points
from application.pycatia_scripts.part.points_import import import_points
from application.views.url_prefixes import htmx


@app.route(f'{htmx}/part/export_points', methods=['POST'])
def htmx_export_points():
    geometric_set = request.form.get('geometric_set', type=str) or None
    file_name = request.form.get('file_name', type=str) or None
    directory = request.form.get('directory', type=str) or None

    output = export_points(geometric_set, file_name, directory)
    data = output['data']
    errors = output['errors']
    file_name = output['output_file']

    if errors:
        return render_template('partials/errors.html', errors=errors)

    if data:
        return render_template('partials/point_table.html', data=data, file_name=file_name)

    return render_template('partials/error.html')


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

    return render_template('partials/error.html')
