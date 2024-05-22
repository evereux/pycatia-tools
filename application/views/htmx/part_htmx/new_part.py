from flask import request

from application import app
from application.pycatia_scripts.part.new_part import create_new_part
from application.support.template import render_template
from application.views.url_prefixes import htmx


@app.route(f'{htmx}/part/create_new', methods=['POST'])
def htmx_create_new_part():

    part_number = request.form.get('part_number', type=str) or ""
    revision = request.form.get('revision', type=str) or ""
    definition = request.form.get('definition', type=str) or ""
    nomenclature = request.form.get('nomenclature', type=str) or ""

    output = create_new_part(part_number, revision, definition, nomenclature)
    data = output['data']
    errors = output['errors']

    if errors:
        return render_template('partials/errors.html', errors=errors)

    if data:
        return render_template('partials/success.html', data=data)
    
    return render_template('partials/error.html')
